class Point:
    def __init__(self,x=0 ,y=0):
        self.__x = x
        self.__y = y

    def show(self):
        print(self.get())

    def set(self,x,y):
        self.__x = x
        self.__y = y

    def get(self):
        return self.__x, self.__y

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        lt = Point(x1,y1)
        rb = Point(x2,y2)
        self.__x1, self.__y1 = lt.get()
        self.__x2, self.__y2 = rb.get()

    def show(self):
        print(f'좌측 상단 꼭지점이 ({self.__x1}, {self.__y1})이고 우측 하단 꼭지점이 ({self.__x2}, {self.__y2})인 사각형입니다.')

    def getWidth(self):
        return self.__x2 - self.__x1

    def getHeight(self):
        return self.__y2 - self.__y1

    def getArea(self):
        return self.getWidth() * self.getHeight()

    def getPerimeter(self):
        return 2 * (self.getWidth() + self.getHeight())

r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f'넓이는 {a}, 둘레는 {p}')
