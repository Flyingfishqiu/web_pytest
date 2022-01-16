from socket import *

# def tcp_connect():
#     tcp_socket = socket(AF_INET, SOCK_STREAM)
#     tcp_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
#     request_data = '这里是佳佳的回复'
#     # request_data = 'GET / HTTP/1.1\r\nhost: www.baidu.com\r\n\r\n'
#     tcp_socket.send(request_data.encode())
# tcp_recv = tcp_socket.recv(4096)
# print(tcp_recv.decode().find("\r\n\r\n"))
# with open('index.html', 'wb') as f:
#     f.write(tcp_recv[tcp_recv.decode().find("\r\n\r\n")+4:])
# tcp_socket.close()

