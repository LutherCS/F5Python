from lists import *

def test_task1(capfd):
    task1(["Hello, world!"],'!')
    out, err = capfd.readouterr()
    assert out == "2\n"
    task1([1,2,3,4,5,6,7],8)
    out, err = capfd.readouterr()
    assert out == "8\n"
    task1(["L","u","t","h","e","r", " ", "C", "o", "l", "l", "e", "g", "e"],'_')
    out, err = capfd.readouterr()
    assert out == "15\n"
    task1([1, "a", "2", "b", 3, "c", 4, "d", 5, "e"],'z')
    out, err = capfd.readouterr()
    assert out == "11\n"

def test_task2(capfd):
    task2(["Hello, world!"])
    out, err = capfd.readouterr()
    assert out == "List is too small\n"
    task2([1,2,3,4,5,6])
    out, err = capfd.readouterr()
    assert out == "6\n"
    task2([13,15,17,2,2,1,5,6,7])
    out, err = capfd.readouterr()
    assert out == "1\n"
    task2([4,4,4,4,4,5,4,4,4,4,4,4,4])
    out, err = capfd.readouterr()
    assert out == "5\n"

def test_task3():
    assert task3([4,4,4,4,4,5,4,4,4,4,4,4,4]) == 53
    assert task3([12,13,14]) == 39
    assert task3([-1,0,1]) == 0
    assert task3([0,0,0,0,0,0,0,0,0,1]) == 1

def test_task4():
    assert task4([1,2,3]) == [3,2,1]
    assert task4(["a","b","c","d","e"]) == ["e","d","c","b","a"]
    assert task4([-1,1,-1,1,-1,1]) == [1,-1,1,-1,1,-1]
    assert task4([0,0,0,0,0,0,0,0,0,0,0,0,0,0]) == [0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def test_task5():
    assert task5([1,2,3,4,5]) == 5
    assert task5([23,24,2,13,12]) == 24
    assert task5([-1,-2,-3,-4,-5]) == -1
    assert task5([1,1,1,1,1,1,1,1,1,1,1,]) == 1