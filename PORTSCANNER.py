import socket}
# PORTSCANNER04 project by kaleth
# Ultima modificacion 28 de Febrebro de 2025
# Script Modificado por (K4ledcb@gmail.com) 
# Dependencias : python

def scan_ports(host, start_port, end_port):
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port}: Open")
        else:
            print(f"Port {port}: Closed")
        sock.close()
#ingreso de parametros del usuario
if __name__ == "__main__":
    target_host = input("Enter the target host ('127.0.0.1'): ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    scan_ports(target_host, start_port, end_port)
