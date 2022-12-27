def Is_prime_number(number):
    if number <= 1:
        print(number,'不是素数')
        return
    else:
        i = 2
        while(i<number):
            if number%i == 0:
                print(number,'不是素数')
                return
            else:
                i = i + 1
                continue
    print(number,'是素数')
if __name__ == '__main__':
    while True:
        number = int(input('请输入数字'))
        Is_prime_number(number)