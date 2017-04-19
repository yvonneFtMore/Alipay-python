# -*- coding:utf-8 -*-

LOCALHOST = 'www.xxx.com'


class config:
    """
    支付宝——即时支付

    :param KEY: 安全检验码，以数字和字母组成的32位字符
    :param _INPUT_CHARSET: 编码类型
    :param PARTNER: 支付宝合作者身份ID，以2088开头的16位纯数字
    :param SELLER_EMAIL: 签约支付宝账号
    :param SIGN_TYPE: 签名类型
    :param RETURN_URL: 付完款后跳转的页面（同步通知） 要用 http://格式的完整路径，不允许加?id=123这类自定义参数
    :param NOTIFY_URL: 交易完成返回给服务器处理异步通知的接口
    :param TRANSPORT: 访问模式,根据自己的服务器是否支持ssl访问，若支持请选择https；若不支持请选择http
    :param WEB_SERVICE: 使用的函数
    """

    KEY = 'xxxxxxxxx'

    _INPUT_CHARSET = 'utf-8'

    PARTNER = 'xxxxxxxxxxx'

    SELLER_EMAIL = 'xxxxxxxxxxxxxx'

    SIGN_TYPE = 'MD5'

    RETURN_URL = LOCALHOST + '/xxxxxxx.html'

    NOTIFY_URL = LOCALHOST + '/xxxxxxxxx/'

    TRANSPORT = 'https'

    WEB_SERVICE = 'create_direct_pay_by_user'