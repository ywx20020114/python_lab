class User:
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd


class Account:
    def __init__(self):
        self.user_list = []  # 用户列表，数据格式：[User 对象, User 对象, User 对象]

    def login(self):
        """
        用户登录，用户输入用户名和密码并去 self.user_list 中检查用户是否合法
        """
        name = input('请输入用户名')
        pwd = input('请输入密码')
        for i in self.user_list:
            if i.name == name:
                if i.pwd == pwd:
                    print("登陆成功")
                    return 1
                else:
                    print('密码错误')
                    return 0
        print('该用户不存在')
        return 0

    def register(self):
        """
        用户注册，动态创建 User 对象，并添加到 self.user_list 中
        """
        name = input('请输入用户名')
        pwd = input('请输入密码')
        usr = User(name,pwd)
        self.user_list.append(usr)
        print('注册成功')
        return

    def run(self):
        """
        主程序，先进行 2 次用户注册，再进行用户登录（3 次重试机会）
        """
        print('第一次用户注册：')
        self.register()
        print('第二次用户注册：')
        self.register()
        print('进行登录，你有三次重试机会')
        for i in range(4):
            print('第',i+1,'次登录')
            if self.login() == 1:
                break
        print('任务结束！')
        return

if __name__ == "__main__":
    obj = Account()
    obj.run()