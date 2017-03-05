import socket
from enum import Enum
import random
import time


class WeissClient:
    """
    This class represents a client who can solve a game on it's own.
    """
    def __init__(self):
        """
        Initialization of the class "WeissClient"

        :param Data - String for saving locations on the map
        :param move_counter - Integer for saving the amount of moves made
        :param xyz - List for saving positions of player and nearby blocks
        :param direction - List for choosing next move
        :param msg - String for sending moves to server
        :param scroll - bool for checking if scroll is found
        :param wrong_c - bool for checking if the wrong castle is visited
        :param i_count - Integer that changes state only from 0 to 1, to change "msg"
        :param r_count - Integer for making sure if the wrong castle was visited, that the function "go_to_castle" is
                         called when the player is far away from wrong castle

        """
        self.Data = ''
        self.move_counter = 1
        self.xyz = {}
        self.direction = []
        self.msg = ""
        self.scroll = False
        self.wrong_c = False
        self.i_count = 0
        self.r_count = 0

    def rec_fields(self, clientsocket):
        """
        Gets messages from the server, checks them and print them to console

        :param clientsocket: Messages received from Server
        :return: True or False
        """
        self.Data = clientsocket.recv(1024).decode()

        if not self.Data:
            print("Connection closed")
            return True
        if len(self.Data) == 50:
            print(self.Data[0:10])
            print(self.Data[10:20])
            print(self.Data[20:30])
            print(self.Data[30:40])
            print(self.Data[40:50])
            print("Your position: " + self.Data[24:26])
            print("\n")
            yourPos = self.Data[24:26]
            leftBlock = self.Data[22:24]
            rightBlock = self.Data[26:28]
            upperBlock = self.Data[14:16]
            lowerBlock = self.Data[34:36]
            print("y " + yourPos + " le " + leftBlock + " ri " + rightBlock + " u " + upperBlock + " lo " + lowerBlock)

        elif len(self.Data) == 18:
            print(self.Data[0:6])
            print(self.Data[6:12])
            print(self.Data[12:18])
            print("Your position: " + self.Data[8:10])
            print("\n")
            yourPos = self.Data[8:10]
            leftBlock = self.Data[6:8]
            rightBlock = self.Data[10:12]
            upperBlock = self.Data[2:4]
            lowerBlock = self.Data[14:16]
            print("y " + yourPos + " le " + leftBlock + " ri " + rightBlock + " u " + upperBlock + " lo " + lowerBlock)

        elif len(self.Data) == 98:
            print(self.Data[0:14])
            print(self.Data[14:28])
            print(self.Data[28:42])
            print(self.Data[42:56])
            print(self.Data[56:70])
            print(self.Data[70:84])
            print(self.Data[84:98])
            print("Your position: " + self.Data[48:50])
            print("\n")
            yourPos = self.Data[48:50]
            leftBlock = self.Data[46:48]
            rightBlock = self.Data[50:52]
            upperBlock = self.Data[34:36]
            lowerBlock = self.Data[62:64]
            print("y " + yourPos + " le " + leftBlock + " ri " + rightBlock + " u " + upperBlock + " lo " + lowerBlock)

        else:
            # Lose / Win
            print(self.Data)
            return True
        return False

    def getAll(self, data):
        """
        Checks the data from server and saves some positions into a list
        :param data: Messages from server
        :return: List of positions
        """
        if len(data) == 50:
            yourPos = data[24:26]
            left = data[22:24]
            right = data[26:28]
            upper = data[14:16]
            lower = data[34:36]
            lower_right = data[36:38]
            lower_left = data[32:34]
            upper_right = data[16:18]
            upper_left = data[12:14]
            self.xyz = {'yourPos': yourPos, 'left': left, 'right': right, 'lower': lower, 'upper': upper,
                   'lower_right': lower_right, 'lower_left': lower_left, 'upper_right': upper_right,
                   'upper_left': upper_left}
            return self.xyz

        elif len(data) == 18:
            yourPos = data[8:10]
            left = data[6:8]
            right = data[10:12]
            upper = data[2:4]
            lower = data[14:16]
            lower_right = data[16:18]
            lower_left = data[12:14]
            upper_right = data[4:6]
            upper_left = data[0:2]
            self.xyz = {'yourPos': yourPos, 'left': left, 'right': right, 'lower': lower, 'upper': upper,
                   'lower_right': lower_right, 'lower_left': lower_left, 'upper_right': upper_right,
                   'upper_left': upper_left}
            return self.xyz

        elif len(data) == 98:
            yourPos = data[48:50]
            left = data[46:48]
            right = data[50:52]
            upper = data[34:36]
            lower = data[62:64]
            lower_right = data[78:80]
            lower_left = data[74:76]
            upper_right = data[36:38]
            upper_left = data[32:34]
            self.xyz = {'yourPos': yourPos, 'left': left, 'right': right, 'lower': lower, 'upper': upper,
                   'lower_right': lower_right, 'lower_left': lower_left, 'upper_right': upper_right,
                   'upper_left': upper_left}
            return self.xyz

    def check_lake(self):
        """
        Checks if there a lakes nearby to avoid them
        :return: variable "direction"
        """
        x = self.getAll(self.Data)
        if (self.xyz['right'] == 'L ' and self.xyz['left'] == 'L '):
            self.direction = ["down", "up"]
            return self.direction

        elif (self.xyz['left'] == 'L ' and self.xyz['right'] == 'L '):
            self.direction = ["down", "up"]
            return self.direction

        elif (self.xyz['upper'] == 'L ' and self.xyz['lower'] == 'L '):
            self.direction = ["left", "right"]
            return self.direction

        elif (self.xyz['lower'] == 'L ' and self.xyz['upper'] == 'L '):
            self.direction = ["left", "right"]
            return self.direction

        elif(self.xyz['left'] == 'L '):
            self.direction = ["right", "up", "down"]
            return self.direction

        elif(self.xyz['right'] == 'L '):
            self.direction = ["left", "up", "down"]
            return self.direction

        elif (self.xyz['upper'] == 'L '):
            self.direction = ["right", "left", "down"]
            return self.direction

        elif (self.xyz['lower'] == 'L '):
            self.direction = ["right", "up", "left"]
            return self.direction

    def check_bomb(self):
        """
        Checks if the bomb is nearby to get it as fast as possible
        :return: a move-direction
        """
        x = self.getAll(self.Data)

        if(self.xyz['upper_left'] == "GB" or self.xyz['upper_left'] == "FB" or self.xyz['upper_left'] == "MB"):
            if(self.xyz['left'] == 'L '):
                self.msg = "up"
                return self.msg
            elif(self.xyz['upper'] == 'L '):
                self.msg = "left"
                return self.msg
            else:
                self.msg = "up"
                return self.msg
        elif(self.xyz['upper'] == 'GB' or self.xyz['upper'] == "FB" or self.xyz['upper'] == "MB"):
            self.msg = "up"
            return self.msg
        elif(self.xyz['upper_right'] == 'GB' or self.xyz['upper_right'] == "FB" or self.xyz['upper_right'] == "MB"):
            if(self.xyz['upper'] == 'L '):
                self.msg = "right"
                return self.msg
            elif(self.xyz['right'] == 'L '):
                self.msg = "up"
                return self.msg
            else:
                self.msg = "up"
                return self.msg
        elif(self.xyz['left'] == 'GB' or self.xyz['left'] == "FB" or self.xyz['left'] == "MB"):
            self.msg = "left"
            return self.msg
        elif(self.xyz['right'] == 'GB' or self.xyz['right'] == "FB" or self.xyz['right'] == "MB"):
            self.msg = "right"
            return self.msg
        elif(self.xyz['lower_left'] == 'GB' or self.xyz['lower_left'] == "FB" or self.xyz['lower_left'] == "MB"):
            if(self.xyz['left'] == 'L '):
                self.msg = "down"
                return self.msg
            elif(self.xyz['lower'] == 'L '):
                self.msg = "left"
                return self.msg
            else:
                self.msg = "down"
                return self.msg
        elif(self.xyz['lower'] == 'GB' or self.xyz['lower'] == "FB" or self.xyz['lower'] == "MB"):
            self.msg = "down"
            return self.msg
        elif(self.xyz['lower_right'] == 'GB' or self.xyz['lower_right'] == "FB" or self.xyz['lower_right'] == "MB"):
            if(self.xyz['lower'] == 'L '):
                self.msg = "right"
                return self.msg
            elif(self.xyz['right'] == 'L '):
                self.msg = "down"
                return self.msg
            else:
                self.msg = "down"
                return self.msg

    def got_bomb(self):
        """
        Checks if the player got the bomb
        sets scroll to True

        :return: variable "scroll"
        """
        x = self.getAll(self.Data)

        if(self.xyz['yourPos'] == 'GB' or self.xyz['yourPos'] == 'FB' or self.xyz['yourPos'] == 'MB'):
            self.scroll = True
            return self.scroll

    def go_to_castle(self):
        """
        Checks if there is a castle nearby to go there as fast as possible
        :return: a move-direction
        """
        x = self.getAll(self.Data)

        if (self.xyz['upper_left'] == "C "):
            if (self.xyz['left'] == 'L '):
                self.msg = "up"
                return self.msg
            elif (self.xyz['upper'] == 'L '):
                self.msg = "left"
                return self.msg
            else:
                self.msg = "up"
                return self.msg
        elif (self.xyz['upper'] == 'C '):
            self.msg = "up"
            return self.msg
        elif (self.xyz['upper_right'] == 'C '):
            if (self.xyz['upper'] == 'L '):
                self.msg = "right"
                return self.msg
            elif (self.xyz['right'] == 'L '):
                self.msg = "up"
                return self.msg
            else:
                self.msg = "up"
                return self.msg
        elif (self.xyz['left'] == 'C '):
            self.msg = "left"
            return self.msg
        elif (self.xyz['right'] == 'C '):
            self.msg = "right"
            return self.msg
        elif (self.xyz['lower_left'] == 'C '):
            if (self.xyz['left'] == 'L '):
                self.msg = "down"
                return self.msg
            elif (self.xyz['lower'] == 'L '):
                self.msg = "left"
                return self.msg
            else:
                self.msg = "down"
                return self.msg
        elif (self.xyz['lower'] == 'C '):
            self.msg = "down"
            return self.msg
        elif (self.xyz['lower_right'] == 'C '):
            if (self.xyz['lower'] == 'L '):
                self.msg = "right"
                return self.msg
            elif (self.xyz['right'] == 'L '):
                self.msg = "down"
                return self.msg
            else:
                self.msg = "down"
                return self.msg

    def not_go_back(self):
        """
        Makes sure the player does not go back a step it has taken
        :return: list of directions
        """
        if (self.msg == "right"):
            self.direction = ["up", "down", "right"]
            return self.direction
        elif (self.msg == "up"):
            self.direction = ["right", "up", "left"]
            return self.direction
        elif (self.msg == "down"):
            self.direction = ["right", "down", "left"]
            return self.direction
        elif (self.msg == "left"):
            self.direction = ["left", "up", "down"]
            return self.direction

    def wrong_castle(self):
        """
        Checks if the wrong castle is visited
        :return: variable "wrong_c"
        """
        x = self.getAll(self.Data)

        if (self.xyz['yourPos'] == 'C ' and self.Data is not "You win"):
            if (self.wrong_c == False):
                self.r_count = 0
            self.wrong_c = True
        return self.wrong_c

    def find_other_castle(self):
        """
        If the wrong castle was visited this function tries to get away from that wrong castle to find the other one
        :return: a move-direction, variable "wrong_c"
        """
        x = self.getAll(self.Data)
        if (self.i_count == 0):
            if (self.xyz['right'] == "L "):
                self.check_lake()
            elif(self.xyz['right'] != "L "):
                self.msg = "right"
            self.i_count += 1
            self.r_count += 1
        elif (self.i_count == 1):
            if (self.xyz['lower'] == "L "):
                if (self.xyz['right'] != "L "):
                    self.msg = "right"
                elif (self.xyz['right'] == "L "):
                    self.msg = "up"
            elif (self.xyz['lower'] != "L "):
                self.msg = "down"
            self.i_count = 0
        if (self.r_count > 5):
            self.wrong_c = False
            self.go_to_castle()
        return self.msg, self.wrong_c

    def make_move(self, clientsocket):
        """
        Decides where the player is going, calls the other functions
        :param clientsocket: messages from the server
        :return:
        """
        self.direction = ["right", "up", "down", "left"]
        self.not_go_back()
        self.check_lake()
        self.msg = random.choice(self.direction)
        self.got_bomb()

        if (self.scroll == False):
            self.check_bomb()

        if (self.scroll == True):
            self.go_to_castle()
            self.wrong_castle()
            if (self.wrong_c):
                self.find_other_castle()
                self.wrong_castle()

        time.sleep(0.2)
        # Nachricht schicken

        x = self.getAll(self.Data)
        print("Moves made:  " + str(self.move_counter))

        if self.msg.lower() == "up":
            clientsocket.send(CommandType.UP.value.encode())
            self.move_counter += 1
        elif self.msg.lower() == "down":
            clientsocket.send(CommandType.DOWN.value.encode())
            self.move_counter += 1
        elif self.msg.lower() == "left":
            clientsocket.send(CommandType.LEFT.value.encode())
            self.move_counter += 1
        elif self.msg.lower() == "right":
            clientsocket.send(CommandType.RIGHT.value.encode())
            self.move_counter += 1

    def start(self):
        """
        Connects with the server and calls the "make_move" function
        :return:
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientsocket:
            try:
                # Verbindung herstellen (Gegenpart: accept() )
                clientsocket.connect(('localhost', 5050))
                # Nachricht schicken
                clientsocket.send("Weiss_Client".encode())
                # Antwort empfangen
                data = clientsocket.recv(1024).decode()
                if not data or not data=="OK":
                    # Schließen, falls Verbindung geschlossen wurde
                    clientsocket.close()
                else:
                    while True:
                        if self.rec_fields(clientsocket):
                            break
                        while True:
                            self.make_move(clientsocket)
                            break

            except socket.error as serr:
                print("Socket error: " + serr.strerror)


class CommandType(Enum):
    UP = "up"
    RIGHT = "right"
    DOWN = "down"
    LEFT = "left"

if __name__ == "__main__":
    c = WeissClient()
    c.start()
