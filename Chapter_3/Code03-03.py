# for문을 이용해 다이아몬드 모양으로 *을 출력한다.

count = 0

for i in range(0, 9) : # 줄 수

    # 5~8줄 역삼각형 출력
    if i >= 5 :
        for j in range(0, i-4) : # 공백
            print(" ", end="")
        for k in range(7, 0, -1+(2*count)) :
            print("*", end="")
        print("\n", end="")
        count += 1

    # 0~4줄 삼각형 출력
    for j in range(4-i, 0, -1) : #공백
        print(" ", end="")
    for k in range(0, 1+(2*i)) : #별
        print("*", end="")
    print("\n", end="")