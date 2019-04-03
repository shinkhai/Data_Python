# Implement your own class

Grasp the basic concept of objects by writing your very first class.

## Guidelines
Choose something from the real world that you would like to model. Restaurants, vehicles, users, games, recipes.. It's your call!

Once chosen, create a file in the `lib` directory which has the name of your object. For instance, if you chose to model `Restaurant`, create the restaurant.py file:

### Convention
Pay attention to your class file and your class name. Remember, `lower_snake_case.py` for file name, `UpperCamelCase` for class name in the class definition. Both must be singular! Remember, the class is the structure that allows you to create lots of different objects of that class.

NB: in practice, in Python we can create multiple classes within the same file,
which means we don't always follow said convention.

### What are the inner properties of your objects?
What are the characteristics of a restaurant? Of a user? Of a game? Choose some characteristics of your class that you want to model. They will be your **instance variables**, sometimes named **attributes**.

### Define the constructor
__init__  is the instance method called when calling your class (e.g.
`Restaurant()`. For instance:

```python
class Car:

  def __init__(self, model, brand, kilometers):
      self.model = model
      self.brand = brand
      self.kilometers = kilometers

new_tesla = Car("Model S", "Tesla", 0)
delorean = Car("DeLorean", "silver", 1e64)
```

### Define an instance method
Time to add some behavior to your class with an instance method.

Here's an example of how we might want to use a start instance method on a Car class:

```python
from lib.car import Car
car = Car("T", "Ford", 0)
car.start()
```

## General tips
You can use the `interface.py`file defined in the `src` directory to test your
class. You'll need to import your class into `interface.py`. 😉
