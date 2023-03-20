import sys
import socket
import logging
from concurrent.futures import ThreadPoolExecutor


def kirim_data(nama="kosong"):
    logging.warning(f"nama {nama}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.warning("membuka socket")

    server_address = ('172.16.16.101', 45000)
    logging.warning(f"opening socket {server_address}")
    sock.connect(server_address)

    try:
        # Send data
        message = 'TIME\r\n'
        logging.warning(f"[CLIENT] sending: {message}")
        sock.sendall(message.encode())
        data = sock.recv(16)
        logging.warning(f"[DITERIMA DARI SERVER]: {data.decode()}")
    finally:
        logging.warning("closing")
        sock.close()
    return


if __name__=='__main__':
    executor = ThreadPoolExecutor()
    for i in range(10000):
        t = executor.map(kirim_data(i))