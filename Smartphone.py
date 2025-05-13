# Base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.__storage = storage  # Encapsulated attribute

    def get_storage(self):
        return self.__storage

    def set_storage(self, new_storage):
        if new_storage > 0:
            self.__storage = new_storage
        else:
            print("Storage must be positive!")

    def specs(self):
        return f"{self.brand} {self.model} with {self.__storage}GB storage"

# Subclass
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, gpu):
        super().__init__(brand, model, storage)
        self.gpu = gpu

    # Polymorphism: Overriding specs method
    def specs(self):
        return f"{self.brand} {self.model} (Gaming) with {self.get_storage()}GB and {self.gpu} GPU"
