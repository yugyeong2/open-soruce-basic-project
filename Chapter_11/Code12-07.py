class Car:
    speed=0
    def upSpeed(self,value):
        self.speed+=value

        print("현재속도 (슈퍼 크래스):%d"%self.speed)

class Sedan(Car):
    def upSpeed(self,value):
        self.speed+=value

        if self.speed>150:
            self.speed=150
            print("현재 속도(서브 클래스):%d"%self.speed)

class Truck(Car):
    pass

sedan1,truck1=None,None

truck1=Truck()
sedan1=Sedan()

print("트럭-->",end="")
truck1.upSpeed(200)

print("승용차-->",end="")
sedan1.upSpeed(200)
