# Python - Async
![image](https://github.com/user-attachments/assets/50710ee6-bc72-4b9d-b036-fbb669f6c631)

## Master

**By:** Emmanuel Turlay, Staff Software Engineer at Cruise  
**Weight:** 1  
**Migrated to checker v2:** Your score will be updated as you progress.

## Concepts

For this project, we expect you to look at these concepts:

- [Python - Asynchronous execution](#)
- [Python - Asynchronous Programming](#)

## Resources

**Read or watch:**

- [Async IO in Python: A Complete Walkthrough](#)
- [asyncio - Asynchronous I/O](#)
- [random.uniform](#)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- `async` and `await` syntax
- How to execute an async program with `asyncio`
- How to run concurrent coroutines
- How to create `asyncio` tasks
- How to use the `random` module

## Requirements

### General

- A `README.md` file at the root of the folder of the project is mandatory.
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7).
- All your files should end with a new line.
- All your files must be executable.
- The length of your files will be tested using `wc`.
- The first line of all your files should be exactly `#!/usr/bin/env python3`.
- Your code should use the `pycodestyle` style (version 2.5.x).
- All your functions and coroutines must be type-annotated.
- All your modules should have a documentation:```python3 -c 'print(__import__("my_module").__doc__)'```
- All your classes should have a documentation ```(python3 -c 'print(__import__("my_module").MyClass.__doc__)')```
- All your functions (inside and outside a class) should have a documentation ```(python3 -c 'print(__import__("my_module").my_function.__doc__)'``` and ```python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')```
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## tasks

| Number | Name                                                  | Description                                                                                                                                                                                                                           | Filename                         |
|--------|-------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
| 0      | The basics of async                                   | Write an asynchronous coroutine `wait_random` that waits for a random delay between 0 and `max_delay` (float) seconds and returns it.                                                                                                 | `0-basic_async_syntax.py`        |
| 1      | Let's execute multiple coroutines at the same time    | Write an async routine `wait_n` that spawns `wait_random` `n` times with the specified `max_delay`. Returns the list of delays in ascending order.                                                                                     | `1-concurrent_coroutines.py`     |
| 2      | Measure the runtime                                   | Create a `measure_time` function that measures the total execution time for `wait_n(n, max_delay)` and returns `total_time / n`.                                                                                                       | `2-measure_runtime.py`           |
| 3      | Tasks                                                 | Write a function `task_wait_random` that takes an integer `max_delay` and returns an `asyncio.Task`.                                                                                                                                   | `3-tasks.py`                     |
| 4      | Tasks                                                 | Alter the `wait_n` function to create a new function `task_wait_n` where `task_wait_random` is called instead of `wait_random`.                                                                                                        | `4-tasks.py`                     |
