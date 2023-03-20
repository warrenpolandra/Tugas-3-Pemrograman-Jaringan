import sys
import socket
import logging
import threading


def kirim_data(nama="kosong"):
    logging.warning(f"nama {nama}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.warning("membuka socket")

    # Port 45000
    server_address = ('172.16.16.101', 45000)
    logging.warning(f"opening socket {server_address}")
    sock.connect(server_address)

    try:
        # Send data
        message = 'TIME\r\n'
        logging.warning(f"[CLIENT] sending: {message}")
        sock.sendall(message.encode())
        
        # Look for the response
        data = sock.recv(16)
        data = data.decode()
        logging.warning(f"[DITERIMA DARI SERVER]: {data}")
    
    finally:
        logging.warning("closing")
        # sock.close()
    return


if __name__=='__main__':
    threads = []
    for i in range(10000):
        t = threading.Thread(target=kirim_data, args=(i,))
        threads.append(t)

    for thr in threads:
        thr.start()
