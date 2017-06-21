# coding:utf-8
import httplib,urllib #加载模块
import requests
from config import localServer,remoteServer


class serverTest(object):
    def __init__(self, t):
        self.t = t

    def send(self, query):
        for x in query:
            print "U:",x
            # print "B:",requests.get("http://" + remoteServer["host"] + ":" + str(remoteServer["port"]) + "/" + x).text
            print "B:",requests.get("http://" + localServer["host"] + ":" + str(localServer["port"]) + "/" + x).text
            print "---------------------------------"

        return 0


#everytime u change the RAWDATA, u need to rebuild it
if __name__ == "__main__":
    # query = [
    #     # "你好",
    #     ":build HARRY",
    #     ":build VISA",
    #     "visa",
    #     "stay home",
    #     "你好"
    # ]

    test = [
        "你好",
        "附近ATM",
        "menara ambank",
        "Cool",
        "你还能做什么",
        "常见问题",
        "更多常见问题",
        "什么是Visa卡检出",
        "显示优惠",
        "visa platinum",
        "美国",
        "什么是payWave",
        "安全吗",
        "ok",
        "卡片丢失",
        "我在国外",
        "美国",
    ]

    s = serverTest(True)
    # s.send(query)
    s.send(test)