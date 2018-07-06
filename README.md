# Python Refresher

This repository is simply a bunch of testable problems put together. Its primary goal is to help people strengthen their `python` skills.

## Workflow

1. Install `pytest`
2. Complete the tasks
3. Test your solutions

---

### 1. Installation and getting started

You can install `pytest` by running either of these two commands:

- `pip install -U pytest`
- `easy_install -U pytest`

For more information on getting started with `pytest`, please visit [pytest documentation page](https://docs.pytest.org/en/3.0.0/getting-started.html).

### 2. Completing tasks
Problems are arranged by the level of difficulty and accordingly, put in separate folders.
Tasks are usually in the file `example.py` where example is the difficulty of tasks (e.g., `easy.py` , `medium.py`, `hard.py` etc.).

All the tasks are commented out. Thus, you should uncomment the tasks and you are good to start working on them.

Tasks are usually commented out like this:  

```
# Remove duplicates from a string
'''def taskN(string)'''
```

### 3. Testing
After completing the task(-s), your must run the tests to ensure you've done them correctly. To do this you can run either of these two commands:

1. `pytest example.py`
2. `pytest -vv example.py`

Note that these commands run all the test cases at once meaning that you have to complete all the tasks prior to running the command. Otherwise, you will get an error since the test file will try to run incomplete function(-s).

If you want to run individual test instead of running all of them at once, you can comment the test cases in the `example_test.py` file or specify the test cases you want to run. You can do it by running the following command:

```
# Tests task1
pytest example_test.py::test_task1

# Tests task1, task2, and task3
pytest example_test.py::test_task1 example_test.py::test_task2 example_test.py::test_task3
```

---

#### References

- [Python documentation](https://docs.python.org/3.6/)
- [pytest documentation](https://docs.pytest.org/en/latest/)
- [Project Euler](https://projecteuler.net)