from abc import ABC, abstractmethod

class InterfaceView(ABC):

    @abstractmethod
    def build(self):
        pass