# -*- coding: utf-8 -*-

import hashlib
import urllib
from config import config


# 网关地址
_GATEWAY = 'https://mapi.alipay.com/gateway.do?'


def params_filter(sign_parameters):
    """
    对数组排序并除去数组中的空值和签名参数,返回数组和链接串

    :param sign_parameters: 待签名字符串
    """
    sign_array = []
    sign_encode_dict = {}
    for key in sign_parameters:
        s = "%s=%s" % (key, sign_parameters[key])
        sign_array.append(s.encode('utf-8'))
        sign_encode_dict[key] = str(sign_parameters[key]).encode('utf-8')
    sign_array.sort()
    sign_str = "&".join(sign_array)
    return sign_encode_dict, sign_str


def build_sign(prestr):
    """
    生成MD5签名

    :param prestr: 组装完成的字符串
    """
    return hashlib.md5(prestr + config.KEY).hexdigest()


def create_direct_pay_by_user(order_number, subject, body, total_fee, extra_common_param):
    """
    即时到账交易接口

    :param order_number: 订单号
    :param subject: 交易商品名字
    :param body: 交易内容——购买商品：xxxxx
    :param total_fee: 收取的金额
    :param extra_common_param: 额外信息
    """

    params = {"subject": subject, "body": body, "out_trade_no": "%s" % order_number,
              "payment_type": '1', "partner": config.PARTNER, "total_fee": total_fee, "service": config.WEB_SERVICE,
              "_input_charset": "utf-8", "seller_email": config.SELLER_EMAIL, "seller_id": config.PARTNER,
              "return_url": config.RETURN_URL, "notify_url": config.NOTIFY_URL}
    if extra_common_param:
        params["extra_common_param"] = extra_common_param

    encode_params, sign_str = params_filter(params)
    sign_encode_str = urllib.urlencode(encode_params)
    md5_sign = build_sign(sign_str)
    sign_encode_str += "&" + "sign=" + md5_sign + "&" + "sign_type=MD5"
    return _GATEWAY + sign_encode_str