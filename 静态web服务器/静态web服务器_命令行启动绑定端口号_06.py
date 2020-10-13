#  coding:utf-8
import socket
import os
import threading
import sys


# http协议的web服务器类
class HttpWebServer(object):
    def __init__(self, port):
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置端口号复用
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定端口号
        self.tcp_server_socket.bind(('', port))
        # 设置监听
        self.tcp_server_socket.listen(128)

    @staticmethod
    def handle_client_request(new_socket):
        # 接收客户端的请求信息
        recv_data = new_socket.recv(4096)
        if len(recv_data) == 0:
            new_socket.close()
            return

        # 对二进制数据进行解码
        recv_content = recv_data.decode('utf-8')
        # print(recv_content)

        # 对数据按照空格进行分割
        request_list = recv_content.split(' ', maxsplit=2)  # 分割两次
        # 获取请求的资源路径
        request_path = request_list[1]
        print(request_path)
        # 判断请求的是否是根目录，设置是根目录时的返回信息
        if request_path == '/':
            request_path = '/index.html'

        # 当访问的内容不存在
        # 1.os.path.exists('static' + request_path)
        # 2.try_except
        try:
            # 打开文件读取文件中的数据
            with open("static" + request_path, 'rb') as file:
                file_data = file.read()
        except Exception as e:
            # 代码执行到此﹔说明没有请求的该文件，返回404状态信息|
            # 响应行
            response_line = 'HTTP/1.1 404 NOT FOUND\r\n'
            # 响应头
            response_header = 'Server: PWS/1.0\r\n'

            with open('static/error.html', 'rb') as file:
                file_data = file.read()
            # 响应体
            response_body = file_data
            # 把数据封装成http响应报文格式的数据（二进制）
            response_data = (response_line + response_header + "\r\n").encode('utf-8') + response_body
            # 发送给浏览器的响应报文数据
            new_socket.send(response_data)
        else:  # 文件存在，返回200状态信息
            # 响应行
            response_line = 'HTTP/1.1 200 OK\r\n'
            # 响应头
            response_header = 'Server: PWS/1.0\r\n'
            # 空行
            # 响应体
            response_body = file_data
            # 把数据封装成http响应报文格式的数据（二进制）
            response_data = (response_line + response_header + "\r\n").encode('utf-8') + response_body
            # 发送给浏览器的响应报文数据
            new_socket.send(response_data)
        finally:
            new_socket.close()

    # 启动服务器
    def start(self):
        # 循环等待接受客户端的连接请求
        while True:
            # 等待接受客户端的连接请求
            new_socket, ip_port = self.tcp_server_socket.accept()
            # 代码执行到此，说明连接建立成功

            sub_thread = threading.Thread(target=self.handle_client_request, args=(new_socket,))
            # 设置成为守护主线程
            sub_thread.setDaemon(True)
            sub_thread.start()


def main():
    # 获取终端命令行参数
    params = sys.argv
    if len(params) != 2:
        print('执行命令行的格式如下：python xxx.py 端口号', )
        return
    # 判断第二个参数是否都是由数字组成的字符串
    if not params[1].isdigit():
        print('执行命令行的格式如下：python xxx.py 端口号', )
        return
    port = int(params[1])
    print('开启的端口号为:',port)
    web_server = HttpWebServer(port)
    web_server.start()


if __name__ == '__main__':
    main()
