from fileIO import *

def test_task1():
    assert task1() == ['Hello, my name is Alice\n', 'I am from a wonderland\n', 'It is nice to meet you']

def test_task2():
    task2()
    new_file = open("data/hello.txt",'r')
    string = ""
    for i in new_file:
        string += i
    assert string == "Hello, world!"

def test_task3():
    task3()
    path = "data/hello.txt"
    assert os.path.isfile(path) == False

def test_task4():
    assert task4() == 3

def test_task5():
    assert task5() == 1