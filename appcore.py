# -*- coding:utf-8 -*-

import base64
import urllib
import time
from appconfig import appconfig
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5


def params_filter_apppay(sign_parameters):
    """
    对数组排序并除去数组中的空值和签名参数,返回数组和链接串

    :param sign_parameters: 待组装的签名字符串
    """
    sign_array = []
    sign_encode_dict = {}
    sign_encode_array = []
    for key in sign_parameters:
        if key == "biz_content":
            s = '%s=%s' % (key, sign_parameters[key])
            sign_encode_dict[key] = sign_parameters[key]
            sign_encode_array.append('%s=%s' % (key, urllib.quote(sign_encode_dict[key]).replace("%20", "")))
        else:
            s = '%s=%s' % (key, sign_parameters[key])
            sign_encode_dict[key] = str(sign_parameters[key]).encode('utf-8')
            sign_encode_array.append('%s=%s' % (key, urllib.quote(sign_encode_dict[key])))

        sign_array.append(s.encode('utf-8'))

    sign_array.sort()
    sign_str = "&".join(sign_array)
    sign_encode_str = "&".join(sign_encode_array)
    return sign_encode_str, sign_str


def build_sign(prestr):
    """
    生成RSA签名

    :param prestr: 待签名字符串
    """
    private_key = RSA.importKey(open('rsa_private_key_pkcs8.pem', 'r'))
    value = SHA.new(prestr)
    signer = PKCS1_v1_5.new(private_key)
    signn = signer.sign(value)
    sign = base64.b64encode(signn)
    return sign



def trade_app_pay(order_number, subject, total_fee):
    """
    APP支付交易接口

    :param order_number: 订单号
    :param subject: 交易商品名字
    :param total_fee: 收取的金额
    """
    biz_content = '{' + '"timeout_express":"30m",' + '"seller_id":"",' + '"product_code":"QUICK_MSECURITY_PAY",' + \
                  ('"total_amount":"%s",' % total_fee) + ('"subject":"%s",' % subject.encode('utf-8')) + \
                  ('"body":"%s",' % subject.encode('utf-8')) + ('"out_trade_no":"%s"}' % str(order_number).encode('utf-8'))

    params = {"app_id": appconfig.APP_ID, "biz_content": biz_content, "sign_type": "RSA", "method": appconfig.SERVICE,
              "charset": "utf-8", "notify_url": appconfig.NOTIFY_URL, "version": "1.0",
              "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}
    sign_encode_str, sign_str = params_filter_apppay(params)
    r_sign = build_sign(sign_str.encode('utf-8'))
    sign_encode_str += "&" + urllib.urlencode({"sign": r_sign})
    return sign_encode_str