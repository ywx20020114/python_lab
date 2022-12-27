import math
class circle:
    def __init__(self,r):
        self.r = r

    def circumference(self):
        return 2*math.pi*self.r

    def area(self):
        return math.pi*self.r*self.r

if __name__ == "__main__":
    while(1):
        r = int(input('请输入圆的半径：'))
        cir = circle(r)
        print('圆的周长为：',circle.circumference(cir))
        print('圆的面积为：',circle.area(cir))