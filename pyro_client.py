import Pyro4

num_ap = 1

while num_ap != 101 and num_ap != 102 and num_ap != 103:
    print('Available apartments:\n101\n102\n103\n')
    num_ap = int(input("Enter number of apartment or '0' for exit: "))
    if num_ap == 101 or num_ap == 102 or num_ap == 103:
        server = Pyro4.Proxy("PYRONAME:server")
        print(server.welcomeMessage(num_ap))
    elif num_ap == 0: break




