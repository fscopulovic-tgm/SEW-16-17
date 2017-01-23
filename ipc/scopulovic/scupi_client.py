import socket


class FilipClient:
    """
    The class that is a self playing client for the game ipc
    """

    def __init__(self, square_size=10):
        """
        Initializes everything that is needed for the client to work

        :param square_size: It is set to 10, it is the map size as a square
        """
        self.xy = [0, 0]
        self.map_size = square_size
        self.has_bomb = False
        self.map = []
        for y in range(self.map_size):
            self.map.append([])
            for x in range(self.map_size):
                self.map[y] += "0"
        self.start_game()

    def start_game(self):
        """
        Dijkstra algorithm selected, but maybe I will do my own algorithm

        :return None:
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientsocket:
            try:
                clientsocket.connect(('localhost', 5050))
                clientsocket.send("Scupi".encode())
                while True:
                    data = clientsocket.recv(1024).decode()
                    if not data:
                        print("Connection is closed")
                        clientsocket.close()
                        break
                    else:
                        self.add_view(data)
                        # TODO implement algorithm
            except socket.error as server_error:
                print("Socket error: " + server_error.strerror)

    def search_field(self, field):
        """
        Iteraters through the whole map and searches for field if field is found
        or B (the bomb) is found he return the y and x value

        :param field: The field that you want to search for
        :return [y, x] or None: Returns None if the field is not found, else it returns a list with y and x
        """
        for y in self.map:
            for x in y:
                help_var = self.map[self.get_pos_y(y)][self.get_pos_x(x)]
                if help_var[1:2] == "B" \
                        or help_var[0:1] == field \
                        and not help_var == self.map[0][0] \
                        and not help_var == self.map[self.get_pos_y(self.xy[1])][self.get_pos_x(self.xy[0])]:
                    return [y, x]
        return None

    def add_view(self, view):
        """
        Adds the new map components from the server to the intern map

        :param view: Message from the server
        :return None:
        """
        dist = 0
        if len(view) == 50:
            dist = 5
        elif len(view) == 18:
            dist = 3
        elif len(view) == 98:
            dist = 7
        start_y = -int(dist / 2)
        dx = 0
        dy = 2
        for x in range(dist):
            start_x = -int(dist / 2)
            for y in range(dist):
                if self.map[self.get_pos_y(start_y)][self.get_pos_x(start_x)] == "0":
                    self.map[self.get_pos_y(start_y)][self.get_pos_x(start_x)] = view[dx:dy]
                start_x += 1
                dx += 2
                dy += 2
            start_y += 1
        print(view)
        self.print_map()

    def get_pos_y(self, y):
        """
        Returns the y-value of the parameter y and then it checks if it is bigger or smaller than the map size y
        and adds or takes it minus the map size y

        :param y: y-variable that needs to get checked
        :return None:
        """
        new_y = self.xy[1] + y
        if new_y < 0:
            return new_y + self.map_size
        elif new_y > self.map_size - 1:
            return new_y - self.map_size
        return new_y

    def get_pos_x(self, x):
        """
        Returns the x-value of the parameter x and then it checks if it is bigger or smaller than the map size x
        and adds or takes it minus the map size x

        :param x: x-variable that needs to get checked
        :return None:
        """
        new_x = self.xy[0] + x
        if new_x < 0:
            return new_x + self.map_size
        elif new_x > self.map_size - 1:
            return new_x - self.map_size
        return new_x

    def print_map(self):
        """
        Prints out the map

        :return None:
        """
        for s in self.map:
            print(s)

test = scupi_client(10)
