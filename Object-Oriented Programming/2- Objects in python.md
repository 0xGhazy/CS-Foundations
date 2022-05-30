# Chapter 2
Chapter about:
- Python's type hints
- Organizing classes into packages and modules.
- How to suggest that people don't clobber an object's data.
---

## Type hints
```python
def odd(n: int) -> bool:
    return n % 2 != 0
```
```
to test this we need to use mypy lib
install it by using `python -m pip install mypy`
```

```powershell
# Powershell
mypy –-strict src\bad_hints.py
```

```python
class Point:
    """
    Represents a point in two-dimensional geometric coordinates
    >>> p_0 = Point()
    >>> p_1 = Point(3, 4)
    >>> p_0.calculate_distance(p_1)
    5.0
    """

    def __init__(self, x: float = 0, y: float = 0) -> None:
        """
        Initialize the position of a new point. The x and yObjects in Python
        [ 54 ]
        coordinates can be specified. If they are not, the
        point defaults to the origin.
        :param x: float x-coordinate
        :param y: float x-coordinate
        """
        self.move(x, y)

    def move(self, x: float, y: float) -> None:
        """
        Move the point to a new location in 2D space.
        :param x: float x-coordinate
        :param y: float x-coordinate
        """
        self.x = x
        self.y = y

    def reset(self) -> None:
        """
        Reset the point back to the geometric origin: 0, 0
        """
        self.move(0, 0)

    def calculate_distance(self, other: "Point") -> float:
        """
        Calculate the Euclidean distance from this point
        to a second point passed as a parameter.
        :param other: Point instance
        :return: float distance
        """
        return math.hypot(self.x - other.x, self.y - other.y)
```


```
Most object-oriented programming languages have the concept of a constructor, a special method that creates and initializes the object when it is created. Python is a little different; it has a constructor and an initializer. The constructor method, __new__(), is rarely used unless you're doing something very exotic. So, we'll start our discussion with the much more common initialization method, __init__().
```

```python
# tip: avoid this syntax
from database import *

#- Can bring unexpected objects into our local namespace.
#- If there are conflicting names, we're doomed.
```

## Absolute imports
```
specify the complete path to the module, function, or class we
want to import

>>> import ecommerce.products
>>> product = ecommerce.products.Product("name1")
```

## Relative imports
```
Identify a class, function,
or module as it is positioned relative to the current module.
from .database import Database


Relative imports aren't as useful as they might seem. As mentioned earlier, the Zen
of Python (you can read it when you run import this) suggests "flat is better than nested".
```

```
Make it a policy to wrap all your scripts in an
if __name__ == "__main__": test, just in case you write a
function that you may want to be imported by other code at some
point in the future.
```

```
python dosen't have access control concept.
We often remind each other of this by saying "We're all adults here." There's no need
to declare a variable as private when we can all see the source code.

By convention, we generally prefix an internal attribute or method with an
underscore character, _. Python programmers will understand a leading underscore
name to mean this is an internal variable, think three times before accessing it directly. But
there is nothing inside the interpreter to stop them from accessing it if they think it
is in their best interest to do so. Because, if they think so, why should we stop them?
We may not have any idea what future uses our classes might be put to, and it may
be removed in a future release. It's a pretty clear warning sign to avoid using it.

```




```
On a home computer – where you have access to the privileged files – you can
sometimes get away with installing and working with a single, centralized systemwide Python. In an enterprise computing environment, where system-wide
directories require special privileges, a virtual environment is required. Because
the virtual environment approach always works, and the centralized system-level
approach doesn't always work, it's generally a best practice to create and use virtual
environments.

It's typical to create a different virtual environment for each Python project. You can
store your virtual environments anywhere, but a good practice is to keep them in
the same directory as the rest of the project files. When working with version control
tools like Git, the .gitignore file can make sure your virtual environments are not
checked into the Git repository
```

```bash
~$ python -m venv env
~$ source env/bin/activate # on Linux or macOS
c\> env/Scripts/activate.bat # on Windows
```