from sets import *

def test_task1():
    assert task1([1,2,3,4]) == set([1,2,3,4])
    assert task1(["a","b","c","d"]) == set(["a","b","c","d"])
    assert task1([0,0,0,0,0,0]) == set([0,0,0,0,0,0])
    assert task1([11,12,13,14,15]) == set([11,12,13,14,15])

def test_task2():
    new_set = set([1,2,3])
    assert task2(new_set,4) == set([1,2,3,4])
    new_set = set([1,1,1,1,1])
    assert task2(new_set,1) == set([1,1,1,1,1,1])
    new_set = set(["a","b","c","d"])
    assert task2(new_set,"e") == set(["a","b","c","d","e"])
    new_set = set([-1,0,1])
    assert task2(new_set,-1) == set([-1,1,0,-1])

def test_task3():
    first_set = set([1,2,3])
    second_set = set([3,4,5])
    assert task3(first_set,second_set) == set([1,2])
    first_set = set([1,22,333,4444,55555])
    second_set = set([5,4,3,2,1,333])
    assert task3(first_set,second_set) == set([22,4444,55555])
    first_set = set(["a","b","c","d","e","f","g"])
    second_set = set(["d","e","f","g"])
    assert task3(first_set,second_set) == set(["a","b","c"])
    first_set = set([0,0,0])
    second_set = set([0,0,0])
    assert task3(first_set,second_set) == set([])


def test_task4():
    first_set = set([1,2,3])
    second_set = set([4,5,6])
    assert task4(first_set,second_set) == set([1,2,3,4,5,6])
    first_set = set([1,2,3])
    second_set = set([1,2,3])
    assert task4(first_set,second_set) == set([1,2,3])
    first_set = set(["Luther"])
    second_set = set(["College"])
    assert task4(first_set,second_set) == set(["College","Luther"])
    first_set = set([-1,0,0,0,0,0,0,-1])
    second_set = set([4,5,6])
    assert task4(first_set,second_set) == set([-1,0,4,5,6])

def test_task5():
    first_set = set([1,2,3])
    second_set = set([3,4,5])
    assert task5(first_set,second_set) == set([1,2,4,5])
    first_set = set([1,22,333,4444,55555])
    second_set = set([5,4,3,2,1,333])
    assert task5(first_set,second_set) == set([5,22,3,4444,55555,2,4])
    first_set = set(["a","b","c","d","e","f","g"])
    second_set = set(["d","e","f","g"])
    assert task5(first_set,second_set) == set(["a","b","c"])
    first_set = set([0,0,0])
    second_set = set([0,0,0])
    assert task5(first_set,second_set) == set([])