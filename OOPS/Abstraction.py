# Abstraction is the process of hiding implementation details and showing only essential features using abstract classes and methods.




from abc import ABC, abstractmethod

class Car(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class BMW(Car):
    def start(self):
        print("BMW started")

    def stop(self):
        print("BMW stopped")


class Bentley(Car):
    def start(self):
        print("Bentley started")

    def stop(self):
        print("Bentley stopped")


c = BMW()
c.start()
c.stop()


c = Bentley()
c.start()
c.stop()