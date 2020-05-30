class Car:
    def __init__(self, speed, unit):
        self.speed = speed
        self.unit = unit
        self.__str__()

    def __str__(self):
        return "Car with the maximum speed of {} {}".format(self.speed, self.unit)

class Boat:
    def __init__(self, speed):
        self.speed = speed
        self.__str__()

    def __str__(self):
        return "Boat with the maximum speed of {} knots".format(self.speed)

def main():
    car = Car(15, "mph")
    car2 = Car(15, "km/h")
    boat = Boat(15)
    print(car)
    print(car2)
    print(boat)

if __name__ == "__main__":
    main()