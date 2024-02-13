from square import findSquare

def main():
    test_findSquare()

def test_findSquare():
    assert findSquare(2) == 4
    assert findSquare(3) == 9
    assert findSquare(0) == 0
    assert findSquare(-2) == 4
    assert findSquare(-3) == 9
    
'''print    try:
        assert findSquare(2) == 4
    except AssertionError:
        print("Square of 2 is not equal to 4")
        
    try:
        assert findSquare(3) == 9
    except AssertionError:
        print("Square of 2 is not equal to 4")
        
    try:
        assert findSquare(0) == 0
    except AssertionError:
        print("Square of 2 is not equal to 4")
        
    try:
        assert findSquare(-2) == 4
    except AssertionError:
        print("Square of 2 is not equal to 4")
        
    try:
        assert findSquare(-3) == 9
    except AssertionError:
        print("Square of 2 is not equal to 4")    '''
    
'''    if findSquare(2) != 4:
        print("Square of 2 is not equal to 4")
    if findSquare(3) != 9:
        print("Square of 2 is not equal to 9")
    if findSquare(0) != 0:
        print("Square of 2 is not equal to 0")
    if findSquare(-2) != 4:
        print("Square of 2 is not equal to 4")
    if findSquare(-3) != 9:
        print("Square of 2 is not equal to 9")      '''
        
if __name__=="__main__":
    main()