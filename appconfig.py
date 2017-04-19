# -*- coding:utf-8 -*-

LOCALHOST = 'www.xxx.com'


class appconfig:
    """
    支付宝——APP支付

    :param APP_ID: 开放平台APP id
    :param _INPUT_CHARSET: 字符格式
    :param PARTNER: 合作身份者ID，以2088开头的16位纯数字
    :param SELLER_EMAIL: 签约支付宝账号
    :param ALIPAY_PUBLIC_KEY: 支付宝官方的公钥
    :param SIGN_TYPE: 签名类型，目前APP支付仅支持RSA
    :param RETURN_URL: 付完款后跳转的页面（同步通知） 要用 http://格式的完整路径，不允许加?id=123这类自定义参数
    :param NOTIFY_URL: 交易完成返回给服务器处理异步通知的接口
    :param TRANSPORT: 访问模式,根据自己的服务器是否支持ssl访问，若支持请选择https；若不支持请选择http
    :param WEB_SERVICE: 使用的函数
    """

    APP_ID = 'xxxxxxxxxxxxxxxx'

    _INPUT_CHARSET = 'utf-8'

    PARTNER = 'xxxxxxxxxxxxx'

    SELLER_EMAIL = 'xxxxxxxxxxxxxxxx'

    ALIPAY_PUBLIC_KEY = """xxxxxxxxxxxxxxxxxxx"""

    SIGN_TYPE = 'RSA'

    RETURN_URL = LOCALHOST + "/xxx.html"

    NOTIFY_URL = LOCALHOST + '/xxxxxxxxxxxx/'

    TRANSPORT = 'https'

    SERVICE = 'alipay.trade.app.pay'