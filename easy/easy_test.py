from easy import *

def test_task1(capfd):
    task1(0)
    out, err = capfd.readouterr()
    assert out == "Hello, world!\n"
    task1(1)
    out, err = capfd.readouterr()
    assert out == "Goodbye, world!\n"
    task1(12)
    out, err = capfd.readouterr()
    assert out == "Hello, world!\n"
    task1(13)
    out, err = capfd.readouterr()
    assert out == "Goodbye, world!\n"

def test_task2(capfd):
    task2("John", "Doe")
    out, err = capfd.readouterr()
    assert out == "Hello, John Doe!\n"
    task2("Donald", "Trump")
    out, err = capfd.readouterr()
    assert out == "Hello, Donald Trump!\n"
    task2("Isaac", "Newton")
    out, err = capfd.readouterr()
    assert out == "Hello, Isaac Newton!\n"
    task2("", "")
    out, err = capfd.readouterr()
    assert out == "Hello,  !\n"

def test_task3(capfd):
    task3("uSain Bolt")
    out, err = capfd.readouterr()
    assert out == "Usain Bolt\n"
    task3("Christiano Ronaldo")
    out, err = capfd.readouterr()
    assert out == "Christiano Ronaldo\n"
    task3("Dave bAUtIsta")
    out, err = capfd.readouterr()
    assert out == "Dave Bautista\n"
    task3("gEoRGe hIlL")
    out, err = capfd.readouterr()
    assert out == "George Hill\n"

def test_task4():
    assert task4("katakuri",4,'k') == "katakuri"
    assert task4("Hall",0,'B') == "Ball"
    assert task4("Horse",0,'N') == "Norse"
    assert task4("London",3,"") == "Lonon"

def test_task5():
    assert task5(0) == 0
    assert task5(1) == 1
    assert task5(20) == 210
    assert task5(999) == 499500

def test_task6():
    assert task6(0) == 1
    assert task6(5) == 120
    assert task6(10) == 3628800
    assert task6(16) == 20922789888000

def test_task7():
    assert task7(1, 2, 3) == 2
    assert task7(200, 300, 300) == 300
    assert task7(17, 17, 17) == 17
    assert task7(27, 13, 15) == 15

def test_task8():
    assert task8(1) == "One"
    assert task8(5) == "Five"
    assert task8(6) == "Six"
    assert task8(9) == "Nine"

def test_task9():
    assert task9(0) == 0
    assert task9(5) == 5
    assert task9(9) == 34
    assert task9(12) == 144

def test_task10():
    assert task10("cat loves mouse but mouse does not love cat") == 'b'
    assert task10("param pam pam, param param, pam pam pam?") == '?'
    assert task10("When the traces of dark come to fade in the light") == 'W'
    assert task10("When the world is too tall, you can jump, you won’t fall") == 'W'

def test_task11():
    assert task11("121") == True
    assert task11("Gold") == False
    assert task11("") == True
    assert task11("A") == True

def test_task12():
    assert task12("AbcaS") == "AbcS"
    assert task12("Luther College") == "Luther Cog"
    assert task12("112233592") == "12359"
    assert task12("") == ""

def test_task13():
    assert task13("abc") == "cba"
    assert task13("Locomotive") == "evitomocoL"
    assert task13("1") == "1"
    assert task13("Catalan's Conjecture") == "erutcejnoC s'nalataC"

def test_task14():
    assert task14("A") == 1
    assert task14("Z") == 26
    assert task14("P") == 16
    assert task14("U") == 21

def test_task15():
    assert task15(253, 2) == "11111101"
    assert task15(253, 5) == "2003"
    assert task15(253, 8) == "375"
    assert task15(3735928559, 16) == "DEADBEEF"

def test_task16():
    assert task16("uytighjSAAGSSVCX") == "UYTIGHJsaagssvcx"
    assert task16("Christopher Columbus") == "cHRISTOPHER cOLUMBUS"
    assert task16("LeBron James") == "lEbRON jAMES"
    assert task16("aaaaaBBBBB1111122222") == "AAAAAbbbbb1111122222"

def test_task17():
    assert task17("RollBallHall", 4) == "Roll\nBall\nHall\n"
    assert task17("abracadabra", 2) == "ab\nra\nca\nda\nbr\na"
    assert task17("Halloween", 10) == "Halloween"
    assert task17("Scottie Pippen", 8) == "Scottie \nPippen"

def test_task18():
    assert task18("GHDSGHGHHGH","GH") == 4
    assert task18("lalalalalalalalalalalalala","lalala") == 11
    assert task18("Srinivasa","Ramanujan") == 0
    assert task18("Harley Quinn","n") == 2

def test_task19():
    assert task19([[1, 2]]) == [[1], [2]]
    assert task19([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    assert task19([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    assert task19([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

def test_task20():
    assert task20(16) == False
    assert task20(17) == True
    assert task20(353) == True
    assert task20(1001) == False

def test_task21():
    assert task21(1) == []
    assert task21(2) == [2]
    assert task21(23) == [2, 3, 5, 7, 11, 13, 17, 19, 23]
    assert task21(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

def test_task22():
    assert task22([1]) == 0
    assert task22([1, 2, 3]) == 2
    assert task22([12, 43, 1, 2, 456, -2]) == 458
    assert task22([12, 14, 152, 25, 67, 12, 980, 345, 786, -12, -124, 124, 789, 46, -1]) == 1104

def test_task23():
    assert task23([0]) == 0
    assert task23([2, 31, 23, 21, 31, 3]) == 1
    assert task23([12, 345, 876, 69, 7, 456]) == 5
    assert task23([87, 79, 345, 90, 878, 180, 748, 450, 314, 250]) == 3

def test_task24():
    assert task24([0], [0, 1]) == [0, 1]
    assert task24([1, 2, 3, 4], [1, 2, 3, 4]) == [1, 2, 3, 4]
    assert task24([1, 3], [2, 4, 6]) == [1, 2, 3, 4, 6]
    assert task24([1, 2, 5], [12, 42, 2, 12, 65, 5]) == [1, 2, 5, 12, 42, 65]

def test_task25():
    assert task25(0) == 1
    assert task25(2) == 2
    assert task25(17) == False
    assert task25(39916800) == 11