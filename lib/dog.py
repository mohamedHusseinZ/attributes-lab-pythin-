#!/usr/bin/env python3


    APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name, breed):
        self._name = None
        self._breed = None
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 25):
            print("Name must be a string between 1 and 25 characters.")
        else:
            self._name = value

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value not in APPROVED_BREEDS:
            print("Breed must be in the list of approved breeds.")
        else:
            self._breed = value

# Example usage:
dog_instance = Dog(name="Buddy", breed="Mastiff")
dog_instance.name = "Max"  # Valid name
dog_instance.breed = "Chihuahua"  # Valid breed

# Invalid name and breed
dog_instance.name = 123  # Invalid name
dog_instance.breed = "Husky"  # Invalid breed

