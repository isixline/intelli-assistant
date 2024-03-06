from abc import ABC, abstractmethod

class Distributor(ABC):
    @abstractmethod
    def subscribe(self):
        pass

    @abstractmethod
    def distribute(self):
        pass

