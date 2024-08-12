# Project Badge

## Python - Variable Annotations
![image](https://github.com/user-attachments/assets/0ae575c4-eac8-40e4-b07f-a4fb9dd7c3f6)

**Master**

By: Emmanuel Turlay, Staff Software Engineer at Cruise  
Weight: 1  
Migrated to checker v2:  

Your score will be updated as you progress.

---

## Concepts

For this project, we expect you to look at this concept:

- Advanced Python

---

## Resources

Read or watch:

- [Python 3 typing documentation](https://docs.python.org/3/library/typing.html)
- [MyPy cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

---

## Learning Objectives

### General

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- Type annotations in Python 3
- How you can use type annotations to specify function signatures and variable types
- Duck typing
- How to validate your code with mypy

---

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation:```python3 -c 'print(__import__("my_module").__doc__)'```
- All your classes should have a documentation ```(python3 -c 'print(__import__("my_module").MyClass.__doc__)')```
- All your functions (inside and outside a class) should have a documentation ```(python3 -c 'print(__import__("my_module").my_function.__doc__)'``` and ```python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')```
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Tasks

| Number | Name                             | Short Description                                                                                          | Filename                  |
|--------|----------------------------------|------------------------------------------------------------------------------------------------------------|---------------------------|
| 0      | Basic annotations - add          | Write a type-annotated function `add` that takes a float `a` and a float `b` as arguments and returns their sum as a float. | `0-add.py`                |
| 1      | Basic annotations - concat       | Write a type-annotated function `concat` that takes a string `str1` and a string `str2` as arguments and returns a concatenated string. | `1-concat.py`             |
| 2      | Basic annotations - floor        | Write a type-annotated function `floor` which takes a float `n` as argument and returns the floor of the float. | `2-floor.py`              |
| 3      | Basic annotations - to string    | Write a type-annotated function `to_str` that takes a float `n` as argument and returns the string representation of the float. | `3-to_str.py`             |
| 4      | Define variables                 | Define and annotate the following variables: `a` (int = 1), `pi` (float = 3.14), `i_understand_annotations` (bool = True), `school` (str = "Holberton"). | `4-define_variables.py`   |
| 5      | Complex types - list of floats   | Write a type-annotated function `sum_list` which takes a list `input_list` of floats as argument and returns their sum as a float. | `5-sum_list.py`           |
| 6      | Complex types - mixed list       | Write a type-annotated function `sum_mixed_list` which takes a list `mxd_lst` of integers and floats and returns their sum as a float. | `6-sum_mixed_list.py`     |
| 7      | Complex types - string and int/float to tuple | Write a type-annotated function `to_kv` that takes a string `k` and an int or float `v` as arguments and returns a tuple. | `7-to_kv.py`              |
| 8      | Complex types - functions        | Write a type-annotated function `make_multiplier` that takes a float `multiplier` as argument and returns a function that multiplies a float by `multiplier`. | `8-make_multiplier.py`     |
| 9      | Let's duck type an iterable object | Annotate the parameters and return values of the function `element_length(lst)`.                          | `9-element_length.py`      |
