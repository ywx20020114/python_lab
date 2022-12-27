
# 总校区类
class school:
    def __init__(self, name):
        self.name = name
        self.areas = []
        self.students = []
        self.teachers = []

    # 获取area校区的学生人数
    def show_st_num(self, area):
        print(area.name, "学生人数为：", self.areas[self.areas.index(area)].st_num)

    # 获取area校区的员工人数
    def show_em_num(self, area):
        print(area.name, "员工人数为：", self.areas[self.areas.index(area)].em_num)

    # 获取area校区的教师人数
    def show_te_num(self, area):
        print(area.name, "教师人数为：", self.areas[self.areas.index(area)].te_num)

    # 获取area校区的收入
    def show_count(self, area):
        print(area.name, "账户余额为：", self.areas[self.areas.index(area)].em_num)


# 分校区类
class area:
    def __init__(self, name, school):
        self.school = school
        self.name = name
        self.st_num = 0
        self.em_num = 0
        self.balance = 0
        self.te_num = 0
        self.students = []
        self.teachers = []
        self.employees = []
        self.courses = []
        school.areas.append(self)

    # 展示校区所有的课
    def show_courses(self):
        for i in self.courses:
            print(i.name)

# 学生类
class student:
    # 初始化
    #  姓名，电话，校区，学号，班级
    def __init__(self, name,tel,area,id,cls):
        self.name = name
        self.tel = tel
        self.area = area
        self.id = id
        self.area.st_num = self.area.st_num + 1
        self.cls = cls
        self.courses = []
        area.students.append(self)
        area.school.students.append(self)
    # 查看信息
    def show_info(self):
        print("姓名:",self.name)
        print("学号:",self.id)
        print("电话:",self.tel)
        print("校区:",self.area.name)
        print("班级:",self.cls)

    # 选课
    def add_course(self,course,teacher):
        self.courses.append(course)
        course.students.append(self)
        print("恭喜你成功选择",teacher.name,"老师的",course.name,"课程")

    # 缴纳学费
    def pay(self):
        for i in self.courses:
            self.area.balance = self.area.balance + i.price

    # 退学
    def drop(self):
        print("从", area.name, "退学成功！")
        self.area.st_num = area.st_num - 1

# 教师类
class teacher:
    # 初始化
    #  姓名，电话，校区，工号
    def __init__(self, name,tel,area,id):
        self.name = name
        self.tel = tel
        self.area = area
        self.id = id
        self.area.te_num = self.area.te_num + 1
        self.courses = []
        area.teachers.append(self)
        area.school.teachers.append(self)

    # 查看教师基本信息 姓名，电话，校区，工号
    def show_info(self):
        print("姓名:", self.name)
        print("工号:", self.id)
        print("电话:", self.tel)
        print("校区:", self.area.name)

    # 查看教师授课列表
    def show_course(self):
        for i in self.courses:
            print(i.name)

    # 增加教师的授课
    def add_course(self, course):
        self.courses.append(course)
        course.teachers.append(self)

# 课程类
class course:
    # 初始化
    # 名字，价格，校区
    def __init__(self, name, price,area):
        self.name = name
        self.price = price
        self.area = area
        self.teachers = []
        self.students = []
        area.courses.append(self)

    # 展示授课教师:
    def show_teachers(self):
        for i in self.teachers:
            print(i.name)

    # 查看学生列表
    def show_students(self):
        for i in self.students:
            print(i.name)


# 员工模块
class employee:
    # 初始化
    # 名字，工号，校区、类型
    def __init__(self, name, id,area,type):
        self.name = name
        self.area = area
        self.id = id
        self.type = type
        area.em_num = area.em_num + 1
        area.employees.append(self)

    # 展示信息
    def show_info(self):
        print("姓名:", self.name)
        print("工号:", self.id)
        print("校区:", self.area.name)
        print("类型:",self.type)

if __name__ == '__main__':
    # 创建基础信息
    # 创建校区
    NKU = school("南开大学")
    balitai = area("八里台",NKU)
    jinnan = area("津南",NKU)
    taida = area("泰达",NKU)

    all_students = []
    all_teachers = []
    all_employees = []

    while(True):
        operate1 = input("请选择身份："
                        "1、学生"
                        "2、教师"
                        "3、管理员")
        if operate1 == "学生":
            name = input("请输入你的姓名：")
            for i in NKU.students:
                if i.name == name:
                    print("欢迎你",name)
                    while(True):
                        operate2 = input("请输入操作："
                                         "1、选课"
                                         "2、查看信息"
                                         "3、缴纳学费"
                                         "4、退课"
                                         "5、重新选择身份")
                        if operate2 == "选课":
                            area = input("请输入选课校区")
                            for j in NKU.areas:
                                if j.name == area:
                                    print(j.name,"共有如下课程：")
                                    j.show_courses()
                                    course = input("请输入选择的课程：")
                                    for k in j.courses:
                                        if course == k.name:
                                            print("此门课有如下老师讲授：")
                                            k.show_teachers()
                                            teacher = input("请输入老师")
                                            for m in k.teachers:
                                                if teacher == m.name:
                                                    i.add_course(k,m)
                                                    break
                                            break

                                    break
                        if operate2 == "查看信息":
                            i.show_info()
                        if operate2 == "缴纳学费":
                            i.pay()
                        if operate2 == "退课":
                            i.drop()
                        if operate2 == "重新选择身份":
                            break
                    break
        if operate1 == "教师":
            name = input("请输入您的名字：")
            for i in NKU.teachers:
                if name == i.name:
                    print("欢迎您：",i.name,"老师")
                    while(True):
                        operate3 = input("请输入操作："
                                         "1、教授课程"
                                         "2、查看信息"
                                         "3、查看授课课程"
                                         "3、重新选择身份"
                                         )
                        if operate3 == "教授课程":
                            area = input("请输入课程校区")
                            for j in NKU.areas:
                                if j.name == area:
                                    print(j.name, "共有如下课程：")
                                    j.show_courses()
                                    course = input("请输入选择的课程：")
                                    for k in j.courses:
                                        if course == k.name:
                                            i.add_course(k)
                                            break
                                    break
                        if operate3 == "查看信息":
                            i.show_info()
                        if operate3 == "查看授课课程":
                            i.show_courses()
                        if operate3 == "重新选择身份":
                            break
                    break
        if operate1 == "管理员":
            operate4 = input("请输入操作："
                             "1、添加学生"
                             "2、添加教师"
                             "3、添加员工"
                             "4、添加课程"
                             "5、查看校区人数"
                             "6、查看校区收入")
            if operate4 == "添加学生":
                #name, tel, area, id, cls
                name = input("请输入名字")
                tel = input("请输入电话")
                area = input("请输入校区")
                id  = input("请输入学号")
                cls = input("请输入班级")
                for i in NKU.areas:
                    if area == i.name:
                        st = student(name,tel,i,id,cls)
                        break
            if operate4 == "添加教师":
                #姓名，电话，校区，工号
                name = input("请输入名字")
                tel = input("请输入电话")
                area = input("请输入校区")
                id  = input("请输入工号")
                for i in NKU.areas:
                    if area == i.name:
                        teacher = teacher(name,tel,i,id)
                        break

            if operate4 == "添加员工":
                #名字，工号，校区、类型
                name = input("请输入名字")
                id = input("请输入工号")
                area = input("请输入校区")
                type  = input("请输入类型")
                for i in NKU.areas:
                    if area == i.name:
                        em = employee(name,id,i,type)
                        break

            if operate4 == "查看校区人数":
                area = input("请输入校区：")
                for i in NKU.areas:
                    if area == i.name:
                        NKU.show_st_num(i)
                        NKU.show_te_num(i)
                        NKU.show_em_num(i)
                        break
            if operate4 == "查看校区收入":
                area = input("请输入校区:")
                for i in NKU.areas:
                    if area == i.name:
                        NKU.show_count(i)
                        break
            if operate4 == "添加课程":
                name = input("请输入课程名字：")
                price = int(input("请输入价格"))
                area = input("请输入校区")
                for i in NKU.areas:
                    if area == i.name:
                        course = course(name,price,i)
                        break
               # 名字，价格，校区










