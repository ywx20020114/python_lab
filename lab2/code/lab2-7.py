def move(x,y):
    print(x,'->',y)

def Hanoi(n,a,b,c):
    if n==1:
        move(a,c)
    else:
        Hanoi(n-1,a,c,b)
        move(a,c)
        Hanoi(n-1,b,a,c)

if __name__ == '__main__':
    while True:
        n = int(input('请输入盘子数量'))
        Hanoi(n,'A','B','C')
