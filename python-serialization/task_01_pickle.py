#!/usr/bin/python3
import pickle


class CustomObject:

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, "wb") as my_file:
                pickle.dump(self, my_file)
        except Exception as e:
            print(f"An error occured while serializing the object: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as my_file:
                return pickle.load(my_file)
        except Exception as e:
            print(f"An error occurred while deserializing the object: {e}")
            return None
