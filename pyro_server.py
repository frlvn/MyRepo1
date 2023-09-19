import Pyro4
import pickle

class Server(object):
    @Pyro4.expose
    def welcomeMessage(self, num_ap):

            if num_ap == 101:
                return information1()
            elif num_ap == 102:
                return information2()
            elif num_ap == 103:
                return information3()




def startServer():
    server = Server()
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()
    uri = daemon.register(server)
    ns.register("server", uri)
    print("Object uri =", uri)
    daemon.requestLoop()

class House:
    def __init__(self, address):
        self.address = address
        self.apartments = []

    def add_apartment(self, apartment):
        self.apartments.append(apartment)

class Apartment(House):
    def __init__(self, number, area, num_rooms):
        self.number = number
        self.area = area
        self.num_rooms = num_rooms

    def __str__(self):
        return f"Apartment {self.number}: {self.num_rooms} rooms, {self.area} sq. m."

def information1():
    apartment1 = Apartment(101, 80, 3)

    my_house = House("123 Gagarina")


    my_house.add_apartment(apartment1)

    with open('newfile.txt', 'wb') as f:
        pickle.dump(apartment1, f)
    with open('newfile.txt', 'rb') as f:
        data = pickle.load(f)
        return str(data)




def information2():
    apartment2 = Apartment(102, 65, 2)

    my_house = House("123 Gagarina")

    my_house.add_apartment(apartment2)

    with open('newfile.txt', 'wb') as f:
        pickle.dump(apartment2, f)
    with open('newfile.txt', 'rb') as f:
        data = pickle.load(f)
        return str(data)


def information3():
    apartment3 = Apartment(103, 100, 4)

    my_house = House("123 Gagarina")

    my_house.add_apartment(apartment3)


    with open('newfile.txt', 'wb') as f:
        pickle.dump(apartment3, f)
    with open('newfile.txt', 'rb') as f:
        data = pickle.load(f)
        return str(data)


startServer()






