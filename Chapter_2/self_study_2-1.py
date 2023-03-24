import turtle
import random

# 마우스 왼쪽 버튼과 가운데 버튼 통합
# 마우스 왼쪽 클릭 - 거북이의 크기와 선의 색상을 랜덤으로 설정하고,
#                 클릭한 지점까지 설정된 색상으로 선을 그린다
def screenLeftClick(x, y) :
    global r, g, b
    r = random.random()
    g = random.random()
    b = random.random()

    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)

    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.goto(x, y)

# 마우스 오른쪽 클릭 - 선을 그리지 않고 이동
def screenRightClick(x, y) :
    turtle.penup()
    turtle.goto(x, y)

# 변수 선언
pSize = 10
r, g, b = 0.0, 0.0, 0.0

# 메인
turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()
