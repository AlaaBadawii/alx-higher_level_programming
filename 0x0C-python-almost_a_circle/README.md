# 0x0C. Python - Almost a circle

## 0. If it's not tested it doesn't work
    tests directory for all tests all testcases are within this file

## 1. Base class
    first class Base

## 2. First Rectangle
    class Rectangle that inherits from Base

## 3. Validate attributes
    Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded):

## 4. Area first
    build area method

## 5. Display #0
    Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character #

## 6. __str__
    Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>

## 7. Display #1
    Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y

## 8. Update #0
    Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute:

        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute

    This type of argument is called a “no-keyword argument” - Argument order is super important.

## 9. Update \#1
    Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes:

## 10. And now, the Square!
    the class Square that inherits from Rectangle

## 11. Square size
    Update the class Square by adding the public getter and setter size

## 12. Square update
    Update the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes:
## 13. Rectangle instance to dictionary representation
    Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle

## 14. Square instance to dictionary representation
    Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square

## 16. JSON string to file
    Update the class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file: