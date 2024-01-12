class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass  # Placeholder for the make_sound method

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self):
        return "Woof! Woof!"

    def wag_tail(self):
        return f"{self.name} is wagging its tail."

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        return "Meow!"

    def purr(self):
        return f"{self.name} is purring."

# Example usage:
dog_instance = Dog("Buddy", 3, "Golden Retriever")
cat_instance = Cat("Whiskers", 2, "Gray")

# Accessing attributes and methods of Dog instance
print(f"{dog_instance.name} is a {dog_instance.breed} and says: {dog_instance.make_sound()}")
print(dog_instance.wag_tail())

# Accessing attributes and methods of Cat instance
print(f"{cat_instance.name} is {cat_instance.color} and says: {cat_instance.make_sound()}")
print(cat_instance.purr())
