import socket
from mpu6050 import mpu6050

HOST = '192.168.0.69'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


def random_data():
    mpu = mpu6050(0x68)
    #run calibration after
    data = mpu.get_accel_data()
    data = list(data.values())
    return "{},{},{}".format(data[0], data[1], data[2])


def my_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("Server Started waiting for client to connect ")
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(5)
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024).decode('utf-8')

                if str(data) == "Data":

                    print("Ok Sending data ")

                    my_data = random_data()

                    x_encoded_data = my_data.encode('utf-8')

                    conn.sendall(x_encoded_data)

                elif str(data) == "Quit":
                    print("shutting down server ")
                    break

                if not data:
                    break
                else:
                    pass


if __name__ == '__main__':
    while 1:
        my_server()