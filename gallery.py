from garage import *

print("Garage is opening...")

time.sleep(1)

print("""

##########################################

        Operations;

        1. Show cars
        2. Car inquiry
        3. Add car
        4. Delete car

        Please press <Q> to quit.\n

##########################################
""")

g = Garage()

while True:

    operation = input("Operation that you choose:")

    if operation == "Q" or operation == "q":

        print("The garage program is closing...")
        time.sleep(1)
        print("The garage program has been ended.")
        break

    elif operation == "1":

        g.show_cars()

    elif operation == "2":

        c = input("Please enter name of the company that want to search:")
        time.sleep(1)
        print("Car is searching on the garage...")
        time.sleep(1)
        g.query_car(c)

    elif operation == "3":

        company = input("Please enter the company of the car:")
        time.sleep(1)
        model =  input("Please enter the model of the car:")
        time.sleep(1)
        year = int(input("Please enter the year of the car:"))
        time.sleep(1)
        kind = input("Please enter the type of the car:")
        time.sleep(1)
        color = input("Please enter the color of the car:")
        new_car = Car(company, model, year, kind, color)
        print("The car is adding at the garage...")
        time.sleep(1)
        g.add_car(new_car)
        print("The car has been added at the garage...")

    elif operation == "4":

        name = input("Please enter the model of the car:")
        time.sleep(1)
        answer = input("Are you sure to delete {}?(Y/N)".format(name))

        if answer == "y" or answer == "Y":

            print("The car is deleting from garage...")
            time.sleep(2)
            g.delete_car(name)
            print("The car has been deleted from garage...")

    else:
        print("The chosen operation is not valid!")
