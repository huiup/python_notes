#  coding:utf-8
import socket

if __name__ == '__main__':
    # 1.创建tcp服务端套接字
    # AF_INET:ipv4，AF_INET6:ipv6
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.绑定端口号（服务端必须绑定端口号，否则客户端找不到该服务程序）
    # 第一个参数表示ip地址，一般不用指定﹐表示本机的任何一个ip都可
    # 第二个参数表示端口号
    tcp_server_socket.bind(('', 9090))

    # 3.设置监听
    # 128:表示最大等待建立连接的个数
    tcp_server_socket.listen(128)

    # 4.等待接受容户端的连接请求
    # 注意点︰每次当客户端和服务端建立连接成功会返回一个新的套接字
    # tcp_server_socket只负责等待接收客户端的连接请求﹐收发消息不使用该套接字
    new_socket, ip_port = tcp_server_socket.accept()
    # 代码执行到此，说明客户端和服务端建立连接成功
    print('客户端的ip和端口号为：', ip_port)

    # 5.接收容户端的数据
    recv_data = new_socket.recv(1024)
    recv_content = recv_data.decode('gbk')
    print('接收到的客户端数据为：', recv_content)

    # 6.发送数据到客户端
    send_content = '我是服务端！'
    send_data = send_content.encode('utf-8')
    new_socket.send(send_data)
    # 关闭服务端与客户端套接字，表示和客户端终止通信
    new_socket.close()

    # 7.关闭套接字，表示服务端以后不再等待接受客户端的连接请求
    tcp_server_socket.close()
