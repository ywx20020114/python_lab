def mul_table():
    for i in range(10):
        for j in range(i+1):
            if i!=0 and j!=0:
                print(j,'✖',i,'=',i*j,'  ',end='')
        print("\n")
if __name__ == '__main__':
    mul_table()