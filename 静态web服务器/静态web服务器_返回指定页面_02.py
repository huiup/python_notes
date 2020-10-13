#  coding:utf-8
import socket
import os

def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口号复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定端口号
    tcp_server_socket.bind(('', 8000))
    # 设置监听
    tcp_server_socket.listen(128)
    # 循环等待接受客户端的连接请求
    while True:
        # 等待接受客户端的连接请求
        new_socket, ip_port = tcp_server_socket.accept()
        # 代码执行到此，说明连接建立成功
        # 接收客户端的请求信息
        recv_data = new_socket.recv(4096)
        if len(recv_data) == 0:
            new_socket.close()
            return

        # 对二进制数据进行解码
        recv_content = recv_data.decode('utf-8')
        print(recv_content)

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
        else:  #  文件存在，返回200状态信息
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


if __name__ == '__main__':
    main()
