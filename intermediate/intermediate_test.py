from intermediate import *

def test_task1():
    assert task1([[1, 2, 3]], [[4], [5], [6]]) == [[32]]
    assert task1([[1, 2],[3, 4]], [[5, 6], [7, 8]]) == [[19, 22], [43, 50]]
    assert task1([[1, 2]], [[3, 4], [5, 6]]) == [[13, 16]]
    assert task1([[1, 2], [3, 4], [5, 6]], [[7, 8, 9], [10, 11, 12]]) == [[27, 30, 33], [61, 68, 75], [95, 106, 117]]

def test_task2():
    assert task2("Sorting0123456789") == "ginortS0246813579"
    assert task2("Tbilisi458") == "biiilsT485"
    assert task2("foobar1237348421") == "abfoor2244811337"
    assert task2("789765445whjdbjwhwfbs977865") == "bbdfhhjjswww446688555777799"

def test_task3():
    assert task3(379081, 9) == True
    assert task3(69, 2) == False
    assert task3(131, 16) == True
    assert task3(1312, 8) == False

def test_task4():
    assert task4([1, 2, 2, 2]) == 1
    assert task4([6, 6, 7, 7, 1, 1, 2, 2, 2]) == 6
    assert task4([12, 12, 4, 12, 12, 4, 4, 4, 8, 9, 7, 5]) == 8
    assert task4([5]) == 0

def test_task5():
    assert task5(1) == True
    assert task5(2) == False
    assert task5(0) == True
    assert task5(5) == False

def test_task6():
    assert task6("Hello, my name is Scarlet, my email address is scarlet@email.com") == "scarlet@email.com"
    assert task6("Say hello at hello@example.com") == "hello@example.com"
    assert task6("business@company.com is our email for business inquiries") == "business@company.com"
    assert task6("For further information about the product email at sales@ltd.com have a wonderful day") == "sales@ltd.com"
