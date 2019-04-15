# coding=UTF-8

class Robot:
    """a robot with a name"""
    population = 0 # class variable for recording the numbers of robot

    def __init__(self, name):
        """initialization"""
        self.name = name
        print("(Initializing {})".format(self.name))

        # while a new object is created, the population increases 1
        Robot.population += 1

    def die(self):
        """termination"""
        print("{} is being destroyed".format(self.name))
        Robot.population -=1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("there are still {:d} robot working.".format(Robot.population))

    def say_hi(self):
        """sincely greeting from robot
        you can make it, no problem"""
        print("Greeting, my masters call me {}".format(self.name))

    @classmethod
    def how_many(cls):
        """output present population"""
        print("we have {:d} robots.".format(cls.population))

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\n Robots can do some work here.\n")

print("destroy robots")
droid1.die()
droid2.die()

Robot.how_many()