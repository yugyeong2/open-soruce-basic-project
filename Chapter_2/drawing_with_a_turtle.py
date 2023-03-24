import turtle
import random

# 마우스 왼쪽 클릭 - 클릭한 지점까지 설정된 색상으로 선을 그린다
def screenLeftClick(x, y) :
    global r, g, b
    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.goto(x, y)

# 마우스 오른쪽 클릭 - 선을 그리지 않고 이동
def screenRightClick(x, y) :
    turtle.penup()
    turtle.goto(x, y)

# 마우스 휠 클릭 - 거북이 크기, 선의 색상 랜덤 설정
def screenMidClick(x, y) :
    global r, g, b
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()

# 변수 선언
pSize = 10
r, g, b = 0.0, 0.0, 0.0

# 메인
turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()
