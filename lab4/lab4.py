from functools import reduce

# 判断是否为素数
def isSushu(x):
    for i in range(2,x):
        if x%i == 0:
            return False
    return True

# 第一个问题 fliter,reduce  求素数及其和
def func1():
    sushu = filter(isSushu,[x for x in range(2,101)])
    sushu_list = list(sushu)
    print('100以内的素数：')
    print(sushu_list)
    sum = reduce(lambda x, y: x + y,sushu_list)
    print('加和为：')
    print(sum)

# 名字转换函数
def tran(name):
    return name.capitalize()

# 第二个问题 map 规范姓名
def func2():
    # 第一个例子
    name_list = ['lisa','JACK','Adam']
    print('原先姓名为：')
    print(name_list)
    name_list2 = list(map(tran,name_list))
    print('转换后的姓名为：')
    print(name_list2)
    # 第二个例子
    name_list3 = ['jack', 'ROSE', 'marry']
    print('原先姓名为：')
    print(name_list3)
    name_list4 = list(map(tran, name_list3))
    print('转换后的姓名为：')
    print(name_list4)


# 第三个问题 sorted 按照排名对list进行排序
def func3():
    # 第一个例子
    list_tuples = [(1, 'byd'), (3, 'xiaopeng'), (2, 'tesla'), (4, 'weilai')]
    print('排序前的列表为：')
    print(list_tuples)
    listed_tuples = sorted(list_tuples, key=lambda x: x[0])
    print('排序后的列表为：')
    print(listed_tuples)
    # 第二个例子
    list_tuples = [(3, 'lianxiang'), (2, 'dell'), (1, 'accer'), (4, 'huipu')]
    print('排序前的列表为：')
    print(list_tuples)
    listed_tuples = sorted(list_tuples, key=lambda x: x[0])
    print('排序后的列表为：')
    print(listed_tuples)


# 闭包函数定义
def count_steps(original_step=0):
    def wrapper(new_steps):
        nonlocal original_step
        original_step = original_step + new_steps
        return original_step
    return wrapper

if __name__ == '__main__':
    print('1. fliter,reduce  求素数及其和 ')
    func1()
    print('2. map 规范姓名')
    func2()
    print('3. sorted 按照排名对list进行排序')
    func3()
    # 执行语句
    print('4. 使用闭包实现步数记录')
    count_steps = count_steps(10)
    print(count_steps(5))
    print(count_steps(5))
    print(count_steps(8))