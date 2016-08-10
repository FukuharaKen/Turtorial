from . level2 import Animate


class Animals(Animate):
    def breathe(self):
        print('breathing')
        pass


    def move(self):
        print('moving')
        pass


    def eat_food(self):
        print('eating food')
        pass



class Mammals(Animals):
    def feed_young_with_milk(self):
        print('feeding young')
        pass


class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        pass


class Cat(Mammals):
    pass


class Human(Mammals):
    def __init__(self,name):
        self.name = name

    def self_introduction(self):
        print("Hi,I'm",self.name,'.')

        pass