from plates import is_valid

def test_is_valid1():
    assert is_valid("AA") == True
    assert is_valid("A1") == False


# def test_is_valid2():
#     assert  is_valid("AAA222") == True
#     assert  is_valid("AAA22254") == False
#     assert  is_valid("a") == False
#     assert  is_valid("A") == False
#     assert  is_valid("1A") == False
#
#
# def test_is_valid3():
#     assert is_valid("a23df") == False
#     assert is_valid("az05")  == False
#     assert is_valid("CS50")  == True
#
#
# def test_is_valid4():
#     assert is_valid("3.14") == False
#     assert is_valid("HI!!!") == False
#     assert is_valid("cs 50") == False

def test_isvalid1():
    assert is_valid("AA") == True
    assert is_valid("A1") == False
    assert is_valid("1A") == False
    assert is_valid("11") == False
    assert is_valid("a") == False
    assert is_valid("A") == False
    assert is_valid("H") == False

def test_isvalid2():
    assert is_valid("some word") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("cs50") == True
    assert is_valid(".!") == False
    assert is_valid("cs50!") == False
    assert is_valid("cs 50") == False
    assert is_valid("cs05") == False


def test_isvalid3():
    assert is_valid("ABCDEF") == True
    assert is_valid("ABCDEFABC") == False
    assert is_valid("AAA111") == True
    assert is_valid("111AAA") == False
    assert is_valid("AAA11A") == False
    assert is_valid("AAA11") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("PI3.14") == False
    assert is_valid("AA22ZA") == False
    assert is_valid("aa22Za") == False



