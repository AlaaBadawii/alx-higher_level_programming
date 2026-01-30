#!/usr/bin/python3
""" 4-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 12, 0, 0)
    r2 = Rectangle(10, 12, 1, 0)
    r3 = Rectangle(5, 4, 4, 3)

    r1.display()

    print("---")

    r2.display()

    
    print("---")

    r3.display()


