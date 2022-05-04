import json

class FishInfo():
    def __init__(self):
        self.Infolist = []

    def send(self, clientsocket):
        self.send_Infolist = json.dumps(self.Infolist)
        clientsocket.send(bytes(self.send_Infolist.encode('utf-8')))
        print('send:')
        for var in self.Infolist:
            print(var)
        print(' ')
        self.Infolist = []

    def append(self, type, idx, pos, scale):
        self.Info = {'type': type,'idx':idx, 'pos': pos, 'scale': scale}
        self.Infolist.append(self.Info)

