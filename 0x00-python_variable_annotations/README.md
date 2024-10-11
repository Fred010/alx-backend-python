# Python - Variable Annotations

### Introduction
Variable annotations in Python provide a way to specify the expected type of values that a variable can hold. This can improve code readability, maintainability, and type safety.

### Syntax
Variable annotations are added after the variable name, separated by a colon. Here's the general syntax:

```
variable_name: type = value
```

For example:
```
name: str = "Alice"
age: int = 30
is_active: bool = True
```
### Types
Python supports a variety of built-in types that can be used for annotations:
* Numeric types: int, float, complex
* Boolean type: bool
* String type: str
* List type: list
* Tuple type: tuple
* Dictionary type: dict
* Set type: set
* None type: NoneType
* Custom types: Classes and other user-defined types

### Type Hints
Type hints are optional annotations that provide more information about the expected type of a variable. They are enclosed in parentheses after the type:
```
variable_name: type(hint) = value
```

For example:
```
numbers: list(int) = [1, 2, 3]
person: dict(name=str, age=int) = {"name": "Bob", "age": 25}
```
