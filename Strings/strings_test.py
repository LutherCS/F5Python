from strings import *

def test_task1(capfd):
    task1("Hello, world!")
    out, err = capfd.readouterr()
    assert out == "H\n"
    task1("Luther College")
    out, err = capfd.readouterr()
    assert out == "L\n"
    task1("abdefghijklmnopqrstuvwxyz")
    out, err = capfd.readouterr()
    assert out == "a\n"
    task1("lalala")
    out, err = capfd.readouterr()
    assert out == "l\n"

def test_task2(capfd):
    task2("Hello, world!")
    out, err = capfd.readouterr()
    assert out == "13\n"
    task2("Luther College")
    out, err = capfd.readouterr()
    assert out == "14\n"
    task2("abcdefghijklmnopqrstuvwxyz")
    out, err = capfd.readouterr()
    assert out == "26\n"
    task2("lalala")
    out, err = capfd.readouterr()
    assert out == "6\n"

def test_task3(capfd):
    task3("Hello, world!")
    out, err = capfd.readouterr()
    assert out == "Hello\n"
    task3("Luther College")
    out, err = capfd.readouterr()
    assert out == "Luthe\n"
    task3("abdefghijklmnopqrstuvwxyz")
    out, err = capfd.readouterr()
    assert out == "abdef\n"
    task3("lalala")
    out, err = capfd.readouterr()
    assert out == "lalal\n"

def test_task4():
    task4("Hello, world!") == "!dlrow ,olleH"
    task4("Luther College") == "egeLLoc rethuL"
    task4("abdefghijklmnopqrstuvwxyz") == "zyxwvutsrqponmlkjihgfedba"
    task4("lalala") == "lalala"

def test_task5():
    task5("Hello, world!") == "Helo, word!"
    task5("Luther College") == "Luther Cog"
    task5("abdefghijklmnopqrstuvwxyz") == "abdefghijklmnopqrstuvwxyz"
    task5("lalala") == "la"