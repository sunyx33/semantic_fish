import fish_v2
import socket
import time
import os
import random

t = 0.5
host = "127.0.0.1"
port = 8888

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.bind((host, port))
print("Sever is working...")

listener.listen()
clientsocket, addr = listener.accept()
print("connected with %s" % str(addr))
InfoList = fish_v2.FishInfo()
os.system('pause')



InfoList.append('tuna', 0, [2, 4, 0], 3.3)
InfoList.append('tuna', 1, [4, 7, 0], 2)
InfoList.append('tuna', 2, [6, 10, 0], 3)
InfoList.append('gold', 3, [78, 43, 0], 2)
InfoList.append('gold', 4, [72, 39, 0], 2)
InfoList.send(clientsocket)
time.sleep(t)

InfoList.append('tuna', 0, [6, 4, 0], 3)
InfoList.append('tuna', 1, [8, 5, 0], 2)
InfoList.append('tuna', 2, [10, 10, 0], 3)
InfoList.append('gold', 3, [68, 40, 0], 2)
InfoList.append('gold', 4, [68, 36, 0], 2)
InfoList.send(clientsocket)
time.sleep(t)


InfoList.append('tuna', 0, [10, 4, 0], 2.3)
InfoList.append('tuna', 1, [12, 5, 0], 2)
InfoList.append('tuna', 2, [14, 10, 0], 3)
InfoList.append('gold', 3, [64, 39, 0], 2)
InfoList.append('gold', 4, [59, 37, 0], 2)
InfoList.send(clientsocket)
time.sleep(t)


InfoList.append('tuna', 0, [16, 4, 0], 3)
InfoList.append('tuna', 1, [18, 5, 0], 2)
InfoList.append('tuna', 2, [20, 10, 0], 3)
InfoList.append('gold', 3, [60, 35, 0], 2)
InfoList.append('gold', 4, [52, 32, 0], 2)
InfoList.append('rainbow', 5, [0, 43, 0], 4)
InfoList.append('rainbow', 6, [100, 100, 0], 1)
InfoList.send(clientsocket)
time.sleep(t)


InfoList.append('tuna', 0, [22, 4, 0], 3)
InfoList.append('tuna', 1, [24, 5, 0], 2)
InfoList.append('tuna', 2, [26, 10, 0], 3)
InfoList.append('gold', 3, [55, 30, 0], 2)
InfoList.append('gold', 4, [49, 29, 0], 2)
InfoList.append('rainbow', 5, [8, 38, 0], 3.7)
InfoList.append('rainbow', 6, [78, 43, 0], 4)
InfoList.send(clientsocket)
time.sleep(t)


InfoList.append('tuna', 0, [28, 4, 0], 3)
InfoList.append('tuna', 1, [30, 5, 0], 2)
InfoList.append('tuna', 2, [32, 10, 0], 3)
InfoList.append('gold', 3, [50, 26, 0], 2)
InfoList.append('gold', 4, [44, 23, 0], 2)
InfoList.append('rainbow', 5, [16, 30, 0], 3.2)
InfoList.append('rainbow', 6, [72, 39, 0], 3.5)
InfoList.send(clientsocket)
time.sleep(t)


InfoList.append('tuna', 0, [34, 4, 0], 3)
InfoList.append('tuna', 1, [36, 5, 0], 2)
InfoList.append('tuna', 2, [38, 10, 0], 3)
InfoList.append('gold', 3, [46, 20, 0], 2)
InfoList.append('gold', 4, [40, 17, 0], 2)
InfoList.append('rainbow', 5, [24, 23, 0], 2.8)
InfoList.append('rainbow', 6, [67, 35, 0], 3)
InfoList.send(clientsocket)
time.sleep(t)


InfoList.append('tuna', 0, [40, 4, 0], 3)
InfoList.append('tuna', 1, [42, 5, 0], 2)
InfoList.append('tuna', 2, [44, 10, 0], 3)
InfoList.append('gold', 3, [35, 18, 0], 2)
InfoList.append('gold', 4, [32, 14, 0], 2)
InfoList.append('rainbow', 5, [32, 18, 0], 2.5)
InfoList.append('rainbow', 6, [60, 32, 0], 2.5)
InfoList.send(clientsocket)
time.sleep(t)


InfoList.append('tuna', 0, [46, 4, 0], 3)
InfoList.append('tuna', 1, [48, 5, 0], 2)
InfoList.append('tuna', 2, [50, 10, 0], 3)
InfoList.append('gold', 3, [28, 14, 0], 2)
InfoList.append('gold', 4, [23, 11, 0], 2)
InfoList.append('rainbow', 5, [45, 15, 0], 2)
InfoList.append('rainbow', 6, [54, 30, 0], 2)
InfoList.send(clientsocket)
time.sleep(t)


InfoList.append('tuna', 0, [52, 4, 0], 2)
InfoList.append('tuna', 1, [54, 5, 0], 2)
InfoList.append('tuna', 2, [56, 10, 0], 3)
InfoList.append('gold', 3, [19, 10, 0], 2)
InfoList.append('gold', 4, [15, 6, 0], 2)
InfoList.append('rainbow', 5, [55, 10, 0], 1.7)
InfoList.append('rainbow', 6, [45, 26, 0], 1.5)
InfoList.send(clientsocket)
time.sleep(t)


InfoList.append('tuna', 0, [58, 4, 0], 2)
InfoList.append('tuna', 1, [60, 5, 0], 2)
InfoList.append('tuna', 2, [62, 10, 0], 3)
InfoList.append('gold', 3, [14, 6, 0], 2)
InfoList.append('gold', 4, [10, 3, 0], 2)
InfoList.append('rainbow', 5, [70, 5, 0], 2)
InfoList.append('rainbow', 6, [38, 22, 0], 1)
InfoList.send(clientsocket)
time.sleep(t)


InfoList.append('tuna', 0, [64, 4, 0], 2)
InfoList.append('tuna', 1, [66, 5, 0], 2)
InfoList.append('tuna', 2, [68, 10, 0], 3)
InfoList.append('gold', 3, [10, 3, 0], 2)
InfoList.append('gold', 4, [5, 2, 0], 2)
InfoList.append('rainbow', 6, [30, 33, 0], 1.5)

InfoList.send(clientsocket)
time.sleep(t)


InfoList.append('tuna', 0, [70, 4, 0], 2)
InfoList.append('tuna', 1, [72, 5, 0], 2)
InfoList.append('tuna', 2, [74, 10, 0], 3)
InfoList.append('gold', 3, [3, 1, 0], 2)
InfoList.append('rainbow', 6, [20, 39, 0], 2)

InfoList.send(clientsocket)
time.sleep(t)


InfoList.append('tuna', 0, [76, 4, 0], 2)
InfoList.append('tuna', 1, [78, 5, 0], 2)
InfoList.append('tuna', 2, [79, 10, 0], 3)
InfoList.append('rainbow', 6, [10, 43, 0], 2.5)
InfoList.send(clientsocket)
time.sleep(t)

InfoList.append('rainbow', 6, [4, 44, 0], 3)
InfoList.send(clientsocket)
time.sleep(t)

InfoList.send(clientsocket)
# InfoList.append('tuna', 0, [10, 4, 0], 1.3)
# InfoList.append('tuna', 1, [12, 5, 0], 2)
# InfoList.append('tuna', 2, [14, 10, 0], 3)
#
# InfoList.send(clientsocket)
# time.sleep(1)


os.system('pause')


