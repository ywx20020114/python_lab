
# 问题1
# 初始水平为1，一年365天
# 1. 每天进步1‰，一年之后的水平是多少？
# 2. 每天退步1‰，一年之后的水平是多少？
# 3. 将前面两问的数值改为5‰和1%，结果分别是多少？

# 参数：rate：进步或者退步的比率      type：1：进步   0：退步
def question1(rate,type):
    ans = 1
    if type == 1:
        for i in range(365):
            tmp = ans * rate
            ans = ans + tmp
    else:
        for i in range(365):
            tmp = ans * rate
            ans = ans - tmp
    return ans




# 问题2
# 一年365天，初始水平为1，一周5个工作日，每天进步1%，2个休息日，每天退步1%。一年后的结果是都多少？

#rate1:进步程度  rate2：退步程度
def question2(rate1,rate2):
    ans = 1
    for i in range(365):
        tmp1 = ans * rate1
        tmp2 = ans * rate2
        if ((i+1)%7) == 0 or ((i+2)%7 == 0):
            ans = ans - tmp2
        else:
            ans = ans + tmp1
    return ans



# 问题3
# 每周工作5天休息2天，计算工作日的进步系数是多少才能与每天努力1%一样？
# -A君: 一年365天，每天进步1%，不停歇
# -B君: 一年365天，每周工作5天休息2天，休息日退步1% ，要多努力呢？

def question3():
    ans = 0.01
    while question2(ans,0.01) < question1(0.01,1):
        ans += 0.001
    return ans
if __name__ == '__main__':
    a = int(input('请输入问题序号'))
    if a == 1:
        print('如果每天进步1‰，一年之后的水平是： ',"%.3f" % question1(0.01,1))
        print('如果每天退步1‰，一年之后的水平是： ',"%.3f" % question1(0.01,0))
        print('如果每天进步5‰，一年之后的水平是： ',"%.3f" % question1(0.05,1))
        print('如果每天退步5‰，一年之后的水平是： ',"%.3f" % question1(0.05, 0))
    else:
        if a == 2:
            print('一年365天，初始水平为1，一周5个工作日，每天进步1%，2个休息日，每天退步1%。一年后的结果是： ',"%.3f" % question2(0.01,0.01))
        else:
            if a == 3:
                print('每周工作5天休息2天，计算工作日的进步系数是: ',"%.3f" % question3(),'才能与每天努力1%一样')