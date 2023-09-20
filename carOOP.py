class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def driving(self):
        print(f"{self.make} {self.model} is driving.")

    def stopped(self):
        print(f"{self.make} {self.model} is stopped.")


is_true = True

while is_true:
    car_1 = Car("Toyota", "Prius", 2015, "Green")
    car_2 = Car("Ford", "Mustang", "2022", "Blue")
    car_3 = Car("Chevrolet", "Silverado", "2021", "White")
    car_4 = Car("Volkswagen", "Beetle", "2013", "Silver")
    car_5 = Car("Toyota", "4runner", "2016", "Red")\

    print("Car 1:", car_1.make, car_1.model,car_1.year, car_1.color)
    print("Car 2:", car_2.make, car_2.model, car_2.year, car_2.color)
    print("Car 3:", car_3.make, car_3.model,car_3.year, car_3.color)
    print("Car 4:", car_4.make, car_4.model, car_4.year, car_4.color)
    print("Car 5:", car_5.make, car_5.model, car_5.year, car_5.color)

    which_car = input("Which car would you like to drive? Enter car make. (e.g. toyota prius): ").lower()

    while which_car == 'toyota prius':
        car_1.driving()
        keep_going = input("Do you want to keep driving? y/n")
        if keep_going == 'n':
            car_1.stopped()
            break

    while which_car == 'ford mustang':
        car_2.driving()
        keep_going = input("Do you want to keep driving? y/n")
        if keep_going == 'n':
            car_2.stopped()
            break

    while which_car == 'toyota 4runner':
        car_5.driving()
        keep_going = input("Do you want to keep driving? y/n")
        if keep_going == 'n':
            car_5.stopped()
            break

    while which_car == "chevrolet silverado":
        car_3.driving()
        keep_going = input("Do you want to keep driving? y/n")
        if keep_going == 'n':
            car_3.stopped()
            break
    while which_car == "volkswagen beetle":
        car_4.driving()
        keep_going = input("Do you want to keep driving? y/n")
        if keep_going == 'n':
            car_4.stopped()
            break

    again = input("Drive another car? y/n: ")
    if again == 'n':
        is_true = False

































