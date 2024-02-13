def main():
    bricks(3)
    
def bricks(side):
    for length in range(side):
        for width in range(side):
            print("?", end = '')
        print()
      
if __name__ == "__main__":  
    main()