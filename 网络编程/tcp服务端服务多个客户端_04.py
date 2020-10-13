#  coding:utf-8
import socket
import threading


# 处理客户端请求的任务
def handle_client_req(new_socket, ip_port):
    print('客户端的ip和端口号为：', ip_port)
    while True:
        # 5.循环接收容户端的数据
        recv_data = new_socket.recv(1024)
        if recv_data:
            recv_content = recv_data.decode('gbk')
            print('接收到的客户端数据为：', recv_content, ip_port)
            print('接收数据长度为：', len(recv_data))

            # 6.发送数据到客户端
            send_content = '问题正在处理中。。。'
            send_data = send_content.encode('gbk')
            new_socket.send(send_data)
        else:
            # 客户端关闭连接
            print('客户端下线了：', ip_port)
            break
    # 关闭服务端与客户端套接字，表示和客户端终止通信
    new_socket.close()


if __name__ == '__main__':
    # 1.创建tcp服务端套接字
    # AF_INET:ipv4，AF_INET6:ipv6
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 设置端口号复用，表示的意思︰服务端程序退出端口号则立即释放
    # 1.soL_SOCKET: 表示当前套接字
    # 2.so_REUSEADDR: 表示复用端口号的选项
    # 3.True: 确定复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    # 2.绑定端口号
    # 第一个参数表示ip地址，一般不用指定﹐表示本机的任何一个ip都可
    # 第二个参数表示端口号
    tcp_server_socket.bind(('', 9091))

    # 3.设置监听
    # 128:表示最大等待建立连接的个数
    tcp_server_socket.listen(128)

    while True:
        # 4.循环等待接受容户端的连接请求
        # 注意︰每次当客户端和服务端建立连接成功会返回一个新的套接字
        # tcp_server_socket只负责等待接收客户端的连接请求﹐收发消息不使用该套接字
        new_socket, ip_port = tcp_server_socket.accept()
        # 代码执行到此，说明客户端和服务端建立连接成功
        sub_thread = threading.Thread(target=handle_client_req, args=(new_socket, ip_port))
        # 设置守护主线程，主线程退出子线程直接销毁
        sub_thread.setDaemon(True)
        sub_thread.start()

    # 7.关闭套接字，表示服务端以后不再等待接受客户端的连接请求
    # tcp_server_socket.close() # 因为服务端的程序要一直运行，可以不用关闭
