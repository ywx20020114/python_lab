
# 1. 给定一个无序列表，列表中元素均为不重复的整数。请找出列表中有没有比它前面元素都大，
# 比它后面的元素都小的数，如果不存在则返回-1，存在则显示其索引，存在多个时只显示第一个解的索引
import string
def func1(list):
    ans = -1
    for i in range(1,len(list)):
        if list[i] > max(list[0:i]) and list[i] < min(list[i+1:len(list)]):
            ans = i;
    return ans

# 2. 将list中的重复数据去重，至少使用两种方案。可以尝试结合其他数据结构。不要求保持原list顺序。
# 2.1 将list转换为set进行去重
def func2_1(listx):
    return list(set(listx))

# 2.2 遍历去重
def func2_2(listx):
    new_list = []
    for i in listx:
        if i not in new_list:
            new_list.append(i)
    return new_list

#3. 元组基本操作练习
# - 创建一个元组，分别进行索引、添加、长度计算、切片操作。
# 元组是不可以直接添加元素的，如果真的需要进行添加，可以使用什么样的方式实现？
# - 创建两个元组，进行连接操作。
# - 创建一个列表和元组，将其连接后打印出来。

# 3.1 元组索引操作
def func3_1(tuple,index):
    return tuple[index]

# 3.2 元组添加
def func3_2(tuplex,data):
    tmp_list = list(tuplex)
    tmp_list.append(data)
    ans = tuple(tmp_list)
    return ans

# 3.3 元组长度计算
def func3_3(tuple):
    return len(tuple)

# 3.4元组切片操作     !!!包头不包尾!!!
def func3_4(tuple,head,tail):
    return tuple[head:tail]

# 3.5 两个元组进行相连接
def func3_5(tuple1,tuple2):
    return tuple1 + tuple2

# 3.6 元组与列表相连接
def func3_6(tuple,list):
    ans = [*tuple, *list]
    return ans

# 4. 分别打印出以下集合的值，并说明原因。
def func4():
    s1 = {32, 5, 'c', '32', '11'}
    s2 = set({32, '46', 32, 'aa'})   # set不允许有重复的元素，会进行去重
    s3 = set('4,32,46,11,32')   # set会将string进行拆分后进行去重
    s4 = set([1, 2, 3])    # 将list转换为set
    s5 = set((1, 2, 3))   # 将tuple转换为set
    s6 = set({'a': 1, 'b': 2, 'c': 3})   #进行了格式化输出，冒号后面指定了输出的顺序
    print(s1)
    print(s2)
    print(s3)
    print(s4)
    print(s5)
    print(s6)

#5. 有如下值集合[11,22,33,44,55,66,77,88,99,100,110,200,230,330]。
# 将所有大于66的值保存至字典的第一个key中，
# 将等于小于66的值保存至第二个key中。
# 即：{‘k1’:大于66的值,‘k2’:小于等于66的值}
def func5(set):
    list1 = []
    list2 = []
    for i in set:
        if i > 66:
            list1.append(i)
        else:
            list2.append(i)
    dict = {'k1':list1,'k2':list2}
    return dict

#6. 以list1中的元素作为key，以list2中的元素作为value生成一个新的字典dict2。
def func6(list1,list2):
    dict = {}
    if len(list1) != len(list2):
        return -1
    else:
        for i in range(0,len(list1)):
            dict[list1[i]] = list2[i]
    return dict

#7. 文本词频统计：：一篇文章，出现了哪些词？哪些词出现的最多？
#请统计hamlet.txt文件中出现的英文单词情况，统计并输出出现最多的10个单词，以及出现的次数。注意：
# (1) 单词不区分大小写，即单词的大小写或组合形式一样；
# (2) 请在文本中剔除如下特殊符号：!"#$%&()*+,-./:;<=>?@[\]^_‘{|}~
# (3) 输出10个单词和它们的次数，每个单词和次数一行；
# (4) 输出单词为小写形式。
def func7(file_path):
    words = open(file_path).read()
    words = words.lower()  # 英文文档中有大小写，lower函数用来统一成小写，方便统计
    for i in '!"#$%&()*+,-./:;<=>?@[\]^_‘{|}~':
        words = words.replace(i, " ")  # 将特数字符进行转换，用空格代替
    words = words.split()
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1  # 字典的get方法用来返回对应键的值，如果没有该键则返回0
    items = list(count.items())
    items.sort(key=lambda x: x[1], reverse=True)
    for i in range(10):
        word, counts = items[i]
        print("{0:<10}{1:>5}".format(word, counts))

# 8. 给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。
# 如果可以，返回 true ；否则返回 false 。
# magazine 中的每个字符只能在 ransomNote 中使用一次。

# 此问题提出两种解决方式
# 第一种、将magazine中的字母进行提取到words，每当ransomNote出现一次，words中的相应字母remove，
# 如果words中没有相应字母，则return False
def func8_1(ransomNote,magazine):
    words = []
    for i in range(0,len(magazine)):
        words.append(magazine[i])
    for i in ransomNote:
        if i in words:
            words.remove(i)
        else:
            return False
    return True

# 第二种，将ransomNote中的字母和出现的次数构造成dict，
# 如果某个字母再magazine中出现的次数小于再ransomNote中出现的次数，则return Flase
def func8_2(ransomNote,magazine):
    ranset = set(ransomNote)
    randic = {}
    for i in ranset:
        randic[i] = ransomNote.count(i)
    for key,value in randic.items():
        if magazine.count(key) < value:
            return False
    return True

if __name__ == '__main__':
    # test第一个问题
    print('第1个问题')
    list1 = [4, 3, 6, 9, 7]
    print(func1(list1))
    list2 = [6, 3, 4, 9, 1]
    print(func1(list2))
    print('--------------------------------------')

    # test第二个问题
    print('第2个问题')
    list3 = [1,1,2,3,3,4,5,5]
    print(func2_1(list3))
    print(func2_2(list3))
    print('--------------------------------------')

    # test第三个问题
    print('第3个问题')
    tuple1 = (1,2,3,4)
    print(tuple1)
    print(func3_1(tuple1,2))
    print(func3_2(tuple1,5))
    print(func3_3(tuple1))
    print(func3_4(tuple1,1,3))
    tuple2 = (5,6,7)
    print(func3_5(tuple1,tuple2))
    list4 = [5,6,7]
    print(func3_6(tuple1,list4))
    print('--------------------------------------')

    # test第四个问题
    print('第4个问题')
    func4()
    print('--------------------------------------')

    # test 第五个问题
    print('第5个问题')
    set1 = {11,22,33,44,55,66,77,88,99,100,110,200,230,330}
    print(func5(set1))
    print('--------------------------------------')

    # test 第六个问题
    print('第6个问题')
    list5 = [1,2,3,4,5,6,7]
    list6 = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
    print(func6(list5,list6))
    print('--------------------------------------')

    # test 第七个问题
    print('第7个问题')
    file_path = 'hamlet.txt'    # file_path ： txt文件的路径
    func7(file_path)
    print('--------------------------------------')

    # test 第八个问题
    print('第8个问题')
    ransomNote = "aa"
    magazine = "aab"
    print(func8_1(ransomNote,magazine))
    print(func8_2(ransomNote,magazine))
    print('--------------------------------------')



