def tempura_tran (HUA):
    return (HUA-32)/1.8

if __name__ == '__main__':
    HUA = float(input('请输入华氏温度:'))
    print("%.2f" % tempura_tran(HUA))
