try:
    import socket
    import threading
    import time
    import csv
except:
    print('library not found ')


HOST = '192.168.0.69'  # The server's hostname or IP address
PORT = 65432        # The port used by the server


def process_data_from_server(x):        # Define function to split Incoming Data
    x1, y1, z1 = x.split(",")
    return x1, y1, z1


def my_client():

    # Define Threadding to run after every 11 seconds
    # dont send Request to often or you will crash server

    threading.Timer(11, my_client).start()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:        # define socket TCP
        s.connect((HOST, PORT))

        # my = input("Enter command ")
        my = 'Data'

        # encode the message
        my_inp = my.encode('utf-8')

        # send request ti server
        s.sendall(my_inp)

        # Get the Data from Server and process the Data
        data = s.recv(1024).decode('utf-8')

        # Process the data i mean split comma seperated value
        x, y, z = process_data_from_server(data)
        with open('socket_data.csv', mode='w') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"')
            writer.writerow([x, y, z])

        print("x: {}".format(x))
        print("y: {}".format(y))
        print("y: {}".format(y))

        s.close()
        time.sleep(5)


if __name__ == "__main__":
    while 1:
        my_client()
