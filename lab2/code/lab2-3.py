def bodyfat(sex,old,height,weight):
    BMI = weight/(height*height)
    bodyfat = 1.2*BMI+0.23*old-5.4-10.8*sex
    if sex != 0 and sex != 1:
        print('疑似性别输入错误，请检查后再输入')
        return
    if old <= 0 or old > 150:
        print('疑似年龄输入错误，请检查后再输入')
        return
    if height <= 0 or height > 3:
        print('疑似输入身高有误，请检查后再次输入')
        return
    if weight <= 0 or weight > 300:
        print('疑似输入体重有误，请检查后再次输入')
        return
    print(bodyfat)
    if sex == 1:
        print('先生你好')
        if bodyfat < 0.15:
            print('你的身体偏瘦')
        else:
            if bodyfat < 0.18:
                print('你的身体非常健康，请继续保持')
            else:
                print('你的身体偏胖')
    if sex == 0:
        print('女士你好')
        if bodyfat < 0.25:
            print('你的身体偏瘦')
        else:
            if bodyfat < 0.28:
                print('你的身体非常健康，请继续保持')
            else:
                print('你的身体偏胖')


if __name__ == '__main__':
    while True:
        sex = int(input('请输入性别'))
        old = int(input('年龄'))
        height = float(input('身高'))
        weight = float(input('体重'))
        bodyfat(sex,old,height,weight)
