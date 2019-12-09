import base64
from jarbas_hive_mind.bridges.facebook import platform, logger, JarbasFacebookBridge
from twisted.internet import reactor, ssl


def connect_to_facebook(mail, password, host="127.0.0.1", port=5678,
                        name="Jarbas Facebook Bridge", api="fb_key",
                        useragent=platform):
    authorization = bytes(name + ":" + api, encoding="utf-8")
    usernamePasswordDecoded = authorization
    api = base64.b64encode(usernamePasswordDecoded)
    headers = {'authorization': api}
    address = u"wss://" + host + u":" + str(port)
    logger.info("[INFO] connecting to hive mind at " + address)
    bridge = JarbasFacebookBridge(mail=mail,
                                  password=password,
                                  name=name, headers=headers,
                                  useragent=useragent)
    contextFactory = ssl.ClientContextFactory()
    reactor.connectSSL(host, port, bridge, contextFactory)
    reactor.run()


if __name__ == '__main__':
    # TODO arg parse
    mail = "xx@mail.com"
    pwd = "NotThis"
    connect_to_facebook(mail, pwd)