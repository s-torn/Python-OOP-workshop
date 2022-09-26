### Mini-assignment to practise functional and object oriented programming.

1. Write a custom decorator
Write a python library that implements a decorator. The decorator should log a
line to a file before and after each execution of our decorated functions. The
log line should contain the name of the decorated function (i.e. "Running
function X"/"Done running function X"). The decorator should keep the name and
docstring of the original functions. The decorator should take the name of the
logfile as an argument, example:

    # Logs calls to my_fn to log1.log 
    @my_decorator("log1.log")
    def my_fn():
        print("a")

The decorator should work irrelevant of how many arguments the target function
takes, and it should return the same return value as the decorated function.

2. Write a custom library for unit testing
Write a library for unit testing our code. It should be runnable as a script
(i.e. `python -m mytestlibrary src/` should run all tests in the `src`
directory). Test cases are to be collected according to the following rules:

- all tests are contained in files whose name begins with `test_` or end with
  `_test.py` 
- all test cases are functions whose name begins with `test_` or end with
  `_test`

The framework should run **all** the tests gathered and show a report on
the CLI (number of gathered tests, number of successfull test, number of
failed tests).

Write your library using OOP practices.

Don't use `unittest`, `pytest` or any other testing library.