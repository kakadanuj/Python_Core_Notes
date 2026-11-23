# Abstraction: an abstract class defines methods that child classes must implement
from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def chassis(self):
        pass

    @abstractmethod
    def airbag(self):
        pass

    @abstractmethod
    def body(self):
        pass


class TataCar(Car):
    def chassis(self):
        print("Chassis implemented")

    def airbag(self):
        print("Airbag implemented")

    def body(self):
        print("Car body implemented")

    def music_system(self):                   # extra method is allowed
        print("Music system added")


car = TataCar()
car.chassis()
car.airbag()
car.body()
car.music_system()

# Car() would raise TypeError because it has unimplemented abstract methods
