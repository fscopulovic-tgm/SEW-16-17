import socket
from enum import Enum

class TypeImportance(Enum):
    """
    Ranking which fields are important,
    bomb hast importance 0, which is the highest
    mountain has importance 1, which is the second on the ranking
    and so on
    Ranking can change due after considering the algorithm

    if bomb is found, then the enemy castle gets a 0 and bomb a 6, otherwise the enemy castle is 6
    """
    ENEMY_CASTLE = 6
    SELF_CASTLE = 5
    LAKE = 4
    FOREST = 3
    GRASS = 2
    MOUNTAIN = 1
    BOMB = 0

class scupi_client:

    def __init__(self, x_map_size, y_map_size):
        """
        Initializes everything that is needed for the client to work

        :param x_map_size: x-size of the map
        :param y_map_size: y-size of the map
        """
        self.importance = TypeImportance(Enum)
        self.xy = [0, 0]
        self.has_bomb = False
        self.map = []
        for x in range(x_map_size):
            self.map.append([])
            for y in range(y_map_size):
                self.map[x] += "0"
        self.print_map()

    def start_game(self):
        """
        Starts the game, server connection etc.

        :return None:
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientsocket:
            try:
                clientsocket.connect(('localhost', 5050))
                clientsocket.send("Scupi".encode())
                while True:
                    data = clientsocket.recv(1024).decode()
                    if not data or not data=="OK":
                        print("Connection is closed")
                        clientsocket.close()
                    else:
                        server_map = data
                        self.add_view(server_map)
                        self.print_map()
                        if self.has_bomb:
                            self.set_enum_after_bomb()
                            self.has_bomb = False
                        #TODO Implement algorithm


    def set_enum_after_bomb(self):
        """
        Changes the value of the BOMB and ENEMY_CASTLE

        :return None:
        """
        self.importance.BOMB = 6
        self.importance.ENEMY_CASTLE = 0

    def add_view(self, view):
        dist = (len(view) - 1) / 2
        print(dist)
        for y in range(0, len(view)):
            for x in range(0, len(view)):
                a = self.xy[0] + x - dist
                b = self.xy[1] + y - dist
                if a < 0:
                    a = len(self.map) + a
                if a >= len(self.map):
                    a = a - len(self.map)
                if b < 0:
                    b = len(self.map) + b
                if b >= len(self.map):
                    b = b - len(self.map)
                a = int(a)
                b = int(b)
                self.map[b][a] = view[y][x].upper()

    def print_map(self):
        """
        Prints out the map

        :return None:
        """
        for s in self.map:
            print(s)

test = scupi_client(10, 10)