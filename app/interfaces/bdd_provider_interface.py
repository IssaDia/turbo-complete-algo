from abc import abstractmethod

class BDD_PROVIDER_INTERFACE():
    @abstractmethod
    def get_description(self):
        pass
    @abstractmethod
    def get_image(self):
        pass
