# coding: utf-8
import socket


# ====================== 请填充该请求头 =======================
# 要求向 localhost 发送一个 GET 请求，
# 请把你想到的有用的请求头填在里面，每个头字段之间用换行隔开
# 提示，你可以在浏览器中查看原始请求头作为参考来填充
GET_req_text = """{{request_type}}
{{request_head}}
"""

# ====================== 请填充该请求头 =======================


# ====================== 请填充该请求头 =======================
# 要求向 localhost 发送一个 POST 请求，
# 请把你想到的有用的请求头填在里面，每个头字段之间用换行隔开
# POST 内容为两个字段，字典形式为 { username: YuiCtwo, password: caicaizi }
# 请注意，HTTP 请求由请求类型，请求头，空行，请求体组成
# 提示，你可以使用 application/x-www-form-urlencoded 的数据类型
POST_req_text = """{{request_type}}
{{request_head}}

{{request_body}}
"""
# ====================== 请填充该请求头 =======================


class Client:

    def __init__(self):
        self.sock = None

    def do_get(self, url, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.connect((url, port))
            header = GET_req_text.split("\n")
            for i in header:
                self.sock.send((i + "\r\n").encode())
            self.sock.send("\r\n".encode())
            # print("Send finished")
            self.receive()
        except Exception:
            pass
        finally:
            self.sock.shutdown(1)
            self.sock.close()

    def do_post(self, url, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.connect((url, port))
            header = POST_req_text.split("\n")
            print(header)
            for i in header:
                self.sock.send((i + "\r\n").encode())
            self.sock.send("\r\n".encode())
            # print("Send finished")
            self.receive()
        except Exception:
            pass
        finally:
            self.sock.shutdown(1)
            self.sock.close()

    def receive(self):
        reply = ""
        while True:
            raw_reply = self.sock.recv(4096)
            if not raw_reply:
                break
            reply += raw_reply.decode("utf-8")
        print(reply)

