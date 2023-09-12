import pickle


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


apartment1 = Apartment(101, 80, 3)
apartment2 = Apartment(102, 65, 2)
apartment3 = Apartment(103, 100, 4)


my_house = House("123 Gagarina")


my_house.add_apartment(apartment1)
my_house.add_apartment(apartment2)
my_house.add_apartment(apartment3)


print(f"House at {my_house.address} contains the following apartments:")

with open('newfile.txt', 'wb') as f:
    pickle.dump(apartment1, f)
with open('newfile.txt', 'rb') as f:
    data = pickle.load(f)
    print(data)

with open('newfile.txt', 'wb') as f:
    pickle.dump(apartment2, f)
with open('newfile.txt', 'rb') as f:
    data = pickle.load(f)
    print(data)

with open('newfile.txt', 'wb') as f:
    pickle.dump(apartment3, f)
with open('newfile.txt', 'rb') as f:
    data = pickle.load(f)
    print(data)







