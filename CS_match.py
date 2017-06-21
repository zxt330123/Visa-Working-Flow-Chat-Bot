# coding=utf-8

__author__ = 'Austin'
import socket
from config import ChatScriptSercer, remoteServer



class CS_Match(object):
    def __init__(self, host, port, timeout):
        self.host = host
        self.port = port
        self.timeout = timeout

    def match(self, question):
        message = 'CSinput' + '\0' + 'xiaoanzi' + '\0' + " " + question + '\0'

        # Create a socket object
        self.sock = socket.socket()
        self.sock.settimeout(self.timeout)
        # Create a TCP/IP socket
        self.sock.connect((self.host, self.port))

        #  send message
        self.sock.send(message)  # , encoding='utf8'

        # receive from socket
        amount_received = 0
        max_amount_expected = 10000
        r_line = ''
        while amount_received < max_amount_expected:
            data = self.sock.recv(128)
            if len(data) == 0:
                break
            else:
                amount_received += len(data)
                r_line += data

        # Close the socket when done
        self.sock.close()

        return r_line


if __name__ == "__main__":

    m = CS_Match(ChatScriptSercer["host"], ChatScriptSercer["port"], ChatScriptSercer["timeout"])
    # m = CS_Match(remoteServer["host"], ChatScriptSercer["port"], ChatScriptSercer["timeout"])
    # m = CS_Match("10.139.104.57", ChatScriptSercer["port"], ChatScriptSercer["timeout"])

    # print m.match("your history")
    # print m.match(":build HARRY")
    # print m.match(":build XIAOANZI")
    # print m.match(":build VISA")
    # print m.match("stay home")
    # print m.match("cool")
    # print m.match("visa")
    # print m.match("what is your name")
    print m.match("你好")
