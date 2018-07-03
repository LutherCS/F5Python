from dictionaries import *

def test_task1():
    assert task1(['a','b','c'],[1,2,3]) == {'a': 1, 'b': 2, 'c': 3}
    assert task1(['1','2'],['3','4']) == {'1': '3', '2': '4'}
    assert task1([1,2,3,4,5],[0,0,0,0,0]) == {1:0,2:0,3:0,4:0,5:0}
    assert task1(["keys"],["values"]) == {"keys": "values"}

def test_task2():
    assert task2({'a': 1, 'b': 2, 'c': 3}) == ['a','b','c']
    assert task2({'1': '3', '2': '4'}) == ['1','2']
    assert task2({1:0,2:0,3:0,4:0,5:0}) == [1,2,3,4,5]
    assert task2({"keys": "values"}) == ["keys"]

def test_task3():
    assert task3({'a': 1, 'b': 2, 'c': 3}) == [1,2,3]
    assert task3({'1': '3', '2': '4'}) == ['3','4']
    assert task3({1:0,2:0,3:0,4:0,5:0}) == [0,0,0,0,0]
    assert task3({"keys": "values"}) == ["values"]

def test_task4():
    assert task4({'a': 1, 'b': 2, 'c': 3},'b') == True
    assert task4({'1': '3', '2': '4'},'3') == False
    assert task4({1:0,2:0,3:0,4:0,5:0},0) == False
    assert task4({"keys": "values"},'keys') == True

def test_task5():
    assert task5("Luther College") == 'e'
    assert task5("aaaabbbbccccc") == 'c'
    assert task5('01223344') == '4'
    assert task5('theonethatoccursthemost') == 't'