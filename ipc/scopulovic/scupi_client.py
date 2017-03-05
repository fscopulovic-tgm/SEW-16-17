import socket
import argparse
from enum import Enum


class Directions(Enum):
    """
    Enum for the directions
    """
    LEFT = [0, -1]
    RIGHT = [0, 1]
    UP = [-1, 0]
    DOWN = [1, 0]


class FilipClient:
    """
    The class that is a self playing client for the game ipc
    """

    def __init__(self, given_ip, given_port, square_size):
        """
        Initializes everything that is needed for the client to work

        :param given_ip: Ip address of the server
        :param given_port: Port number of the server socket
        :param square_size: It is set to 10, it is the map size as a square
        """
        self.xy = [0, 0]
        self.ip = given_ip
        self.port = given_port
        self.map_size = square_size
        self.has_bomb = False
        self.map = []
        self.turn = 0
        for y in range(self.map_size):
            self.map.append([])
            for x in range(self.map_size):
                self.map[y] += "0"
        self.start_game()

    def start_game(self):
        """
        Starts the game and also it starts the algorithm

        :return None:
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            try:
                client_socket.connect((self.ip, self.port))
                client_socket.send("Filip".encode())
                while True:
                    data = client_socket.recv(1024).decode()
                    if not data:
                        print("Connection is closed")
                        client_socket.close()
                        break
                    else:
                        self.add_view(data)
                        if not self.has_bomb:
                            goal_field = self.search_field('B')
                            if not (goal_field is None):
                                path = self.search_path(goal_field)
                                self.go_path(client_socket, path)
                                self.has_bomb = True
                            else:
                                self.go_through_map(client_socket)
                        else:
                            goal_field = self.search_field('C')
                            if not (goal_field is None):
                                    path = self.search_path(goal_field)
                                    self.go_path(client_socket, path)
                            else:
                                self.go_through_map(client_socket)
            except socket.error as server_error:
                print("Socket error: " + server_error.strerror)

    def go_through_map(self, client_socket):
        """
        Goes through the map

        :param client_socket: Is the client socket
        :return None:
        """
        while True:
            if self.turn == 1:
                help_var = self.get_pos_y(self.xy[0] + 1)
                if self.check_field([help_var, self.xy[1]]):
                    client_socket.send("right".encode())
                else:
                    client_socket.send("down".encode())
                self.turn = 0
            else:
                help_var = self.get_pos_x(self.xy[1] + 1)
                if self.check_field([self.xy[0], help_var]):
                    client_socket.send("down".encode())
                else:
                    client_socket.send("right".encode())
                self.turn = 1

    def check_field(self, field):
        """
        Checks if the field is not a mountain or a lake

        :return True or False:
        """
        help_field = self.map[self.get_pos_y(field[0])][self.get_pos_x(field[1])][0:1]
        if help_field == 'L':
            return True
        return False

    def search_path(self, goal_field):
        """
        Searches for a path to the goal field

        :param goal_field: The field that is the goal
        :return path_list: A list that contains the path to the goal field
        """
        path_list = []
        y_dist = self.xy[0] - goal_field[0]
        x_dist = self.xy[1] - goal_field[1]
        help_pos = self.xy
        while not self.xy[0] == goal_field[0]:
            if y_dist < 0:
                check = self.get_pos_y(help_pos[0] + 1)
                if self.check_field([check, help_pos[1]]):
                    help_pos[1] = self.get_pos_x(help_pos[1] + 1)
                    path_list.append(Directions.RIGHT)
                help_pos[0] = self.get_pos_y(help_pos[0] - 1)
                path_list.append(Directions.UP)
            else:
                check = self.get_pos_y(help_pos[0] + 1)
                if self.check_field([check, help_pos[1]]):
                    help_pos[1] = self.get_pos_x(help_pos[1] + 1)
                    path_list.append(Directions.RIGHT)
                else:
                    path_list.append(Directions.DOWN)
        while not self.xy[1] == goal_field[1]:
            if x_dist < 0:
                check = self.get_pos_x(help_pos[1] - 1)
                if self.check_field([help_pos[0], check]):
                    help_pos[0] = self.get_pos_y(help_pos[0] + 1)
                    path_list.append(Directions.DOWN)
                else:
                    path_list.append(Directions.LEFT)
            else:
                check = self.get_pos_x(help_pos[1] + 1)
                if self.check_field([help_pos[0], check]):
                    help_pos[0] = self.get_pos_y(help_pos[0] + 1)
                    path_list.append(Directions.DOWN)
                else:
                    path_list.append(Directions.RIGHT)
        return path_list

    def go_path(self, client_socket, path):
        """
        Gets the path and the client socket and it sends the direction in which the player needs to go

        :param client_socket: Is the client socket
        :param path: Is the path, that is given out by the algorithm
        :return: None
        """
        for direction in path:
            msg = ""
            if direction == Directions.UP:
                msg = "up"
                self.xy[0] = self.get_pos_y(self.xy[0] - 1)
            elif direction == Directions.DOWN:
                msg = "down"
                self.xy[0] = self.get_pos_y(self.xy[0] + 1)
            elif direction == Directions.RIGHT:
                msg = "right"
                self.xy[1] = self.get_pos_x(self.xy[1] + 1)
            elif direction == Directions.LEFT:
                msg = "left"
                self.xy[1] = self.get_pos_x(self.xy[1] - 1)
            client_socket.send(msg.encode())

    def search_field(self, field):
        """
        Iterates through the whole map and searches for field if field is found
        or B (the bomb) is found he return the y and x value

        :param field: The field that you want to search for
        :return return_list: Returns a list that contains all positions of the searched field as a list
        """
        return_list = []
        for y in self.map:
            for x in y:
                help_var = self.map[self.get_pos_y(y)][self.get_pos_x(x)]
                if help_var[1:2] == "B" \
                        or help_var[0:1] == field \
                        and not help_var == self.map[0][0] \
                        and not help_var == self.map[self.get_pos_y(self.xy[1])][self.get_pos_x(self.xy[0])]:
                    return return_list
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
                    if view[dx:dy][1:2] == "B":
                        self.map[self.get_pos_y(start_y)][self.get_pos_x(start_x)] = view[dx:dy][1:2]
                    else:
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
        new_y = sum(self.xy[0]) + y
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
        new_x = sum(self.xy[1]) + x
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

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    ip = parser.add_argument('-i', '--ip_address',
                             help='Address of the server (default=localhost)', default='localhost')
    port = parser.add_argument('-p', '--port',
                               help='Port of the server (default=5050)', default=5050, type=int)
    rows = parser.add_argument('-r', '--rows',
                               help='Rows of the server map (default=10)', default=10, type=int)

    args = parser.parse_args()
    client = FilipClient(args.ip_address, args.port, args.rows)
