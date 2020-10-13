#  coding:utf-8
import socket

if __name__ == '__main__':
    # 1.创建tcp容户端套接字
    # AF_INET:ipv4地址类型
    # socK_STREAM : tcp传输协议类型
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 客户端不强制绑定端口号
    tcp_client_socket.bind(('', 8900))

    # 2.和服务端套接字建立连接
    tcp_client_socket.connect(('192.168.222.1', 9091))

    # 3．发送数据到服务端
    send_content = "我是客户端！"
    send_data = send_content.encode('gbk')  # 把字符串编码成二进制数据
    tcp_client_socket.send(send_data)

    # 4．接收服务端的数据
    recv_data = tcp_client_socket.recv(1024)  # 1024表示每次接收的最大字符数
    recv_content = recv_data.decode('gbk')
    print('接收服务端的数据为：', recv_content)
    print('接收数据长度为：', len(recv_data))

    # 5．关闭套接字
    tcp_client_socket.close()
