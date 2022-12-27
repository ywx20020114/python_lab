from prettytable import PrettyTable
nums = []
names = []
qqs = []
tels = []
mails = []


# 判断姓名合法：
# 姓名全部由英文字母和汉字构成
def isName(name):
    tmp = True
    for i in name:
        if u'\u4e00' <= i <= u'\u9fff' or i.isalpha():
            continue
        else:
            tmp = False
    return tmp

# 判断QQ合法
# QQ全部由数字构成
def isQQ(qq):
    tmp = True
    for i in qq:
        if i.isdigit():
            continue
        else:
            tmp = False
    return tmp


# 判断电话合法
# 电话全部由数字构成
def isTel(tel):
    tmp = True
    for i in tel:
        if i.isdigit():
            continue
        else:
            tmp = False
    return tmp

# 判断邮箱合法
#   1、仅包含一个'@'字符
#   2、最后三个字符必须是'.com'
#   3、字符之间没有空格
#   4、有效字符为 0-9、大小写字母、'.'、'@'、'_'
def isMail(mail):
    # check '@'
    at_count = 0
    for element in mail:
        if element == '@':
            at_count = at_count + 1

    if at_count != 1:
        return False

    # check ' '
    for element in mail:
        if element == ' ':
            return False

    # check '.com'
    postfix = mail[-4:]
    if postfix != '.com':
        return False

    # check char
    for element in mail:
        if element.isalpha() == False and element.isdigit() == False:
            if element != '.' and element != '@' and element != '_':
                return False

    return True



# 增加功能
def add():
    name = input('请输入姓名：')
    while(not isName(name)):
        print('姓名只能包含汉字或者字母！')
        name = input('请重新输入姓名：')
    names.append(name)
    qq = input('请输入QQ：')
    while (not isQQ(qq)):
        print('qq只能包含数字！')
        qq = input('请重新输入qq：')
    qqs.append(qq)
    tel = input('请输入电话：')
    while (not isTel(tel)):
        print('电话只能包含数字！')
        tel = input('请重新输入电话：')
    tels.append(tel)
    mail = input('请输入邮箱：')
    while (not isMail(mail)):
        print('邮箱格式不正确！')
        mail = input('请重新输入邮箱：')
    mails.append(mail)


# 删除功能
def delete():
    if len(nums) == 0:
        print('通讯录中没有记录，不可进行删除操作！')
        return
    num = int(input('请输入删除的序号：'))
    while(num not in nums):
        num = int(input('该序号不存在,请重新输入'))
    no = nums.index(num)
    del nums[no]
    del names[no]
    del qqs[no]
    del tels[no]
    del mails[no]
    for i in range(no, len(nums)):
        nums[i] = nums[i] - 1


#  修改功能
def revise():
    if len(nums) == 0:
        print('通讯录中没有记录，不可进行修改操作！')
        return
    num = int(input('请输入修改的序号：'))
    while(num not in nums):
        num = int(input('没有该记录，无法修改,请重新输入'))
    no = nums.index(num)
    tmp = input('请选择修改的子项：'
                'n：修改姓名'
                'q:修改qq'
                'p：修改电话'
                'm：修改邮箱')
    while(tmp!='n' and tmp!='q' and tmp!='p' and tmp!='m'):
        tmp = input('输入的序号不存在，请重新输入：'
                    'n：修改姓名'
                    'q:修改qq'
                    'p：修改电话'
                    'm：修改邮箱'
                    )
    if tmp == 'n':
        new_name = input('请输入新的姓名，若不修改输入空格：')
        if new_name == ' ':
            return
        else:
            while (not isName(new_name)):
                print('姓名只能包含汉字或者字母！')
                new_name = input('请重新输入姓名：')
            names[no] = new_name
            return
    if tmp == 'q':
        new_qq = input('请输入新的qq，若不修改输入空格：')
        if new_qq == ' ':
            return
        else:
            while (not isQQ(new_qq)):
                print('qq只能包含数字！')
                new_qq = input('请重新输入qq：')
            qqs[no] = new_qq
            return
    if tmp == 'p':
        new_tel = input('请输入新的电话，若不修改输入空格：')
        if new_tel== ' ':
            return
        else:
            while (not isTel(new_tel)):
                print('电话只能包含数字！')
                new_tel = input('请重新输入电话：')
            tels[no] = new_tel
            return
    if tmp == 'm':
        new_mail = input('请输入新的邮箱，若不修改输入空格：')
        if new_mail == ' ':
            return
        else:
            while (not isMail(new_mail)):
                print('邮箱格式不正确！')
                new_mail = input('请重新输入邮箱：')
            mails[no] = new_mail
            return


# 查找功能
def find():
    if len(nums) == 0:
        print('通讯录中没有记录！')
        return
    num = int(input('请输入要查找的记录序号：'))
    while(num not in nums):
        num = int(input('该序号不存在，请重新输入：'))
    no = nums.index(num)
    table = PrettyTable(["序号", "姓名", "QQ", "电话", "邮箱"])
    table.add_row([nums[no], names[no], qqs[no], tels[no] ,mails[no]])
    print(table)


# 展示功能
def show():
    if len(nums) == 0:
        print('无记录')
        return
    table = PrettyTable(['序号','姓名','QQ','电话','邮箱'])
    for i in range(0,len(nums)):
        table.add_row([nums[i],names[i],qqs[i],tels[i],mails[i]])
    print(table)


# 主程序入口
if __name__ ==  '__main__':
    i = 1
    print('欢迎进入通讯录管理功能：')
    while(True):
        type = input('请输入相关操作：'
              'a：增加记录'
              'd：删除记录'
              'c：修改记录'
              'f：查找记录'
              's：展示记录'
              'q：退出系统')
        while(type != 'a' and type != 'd' and type != 'c' and type != 'f' and type != 's' and type != 'q' ):
            type = input('请输入相关操作：'
                         'a：增加记录'
                         'd：删除记录'
                         'c：修改记录'
                         'f：查找记录'
                         's：展示记录'
                         'q：退出系统')
        if type == 'q':
            print('系统已退出!感谢使用！')
            break;
        if type == 'a':
            nums.append(i)
            i = i + 1
            add()
        if type == 'd':
            delete()
            i = i-1
        if type == 'c':
            revise()
        if type == 'f':
            find()
        if type == 's':
            show()





