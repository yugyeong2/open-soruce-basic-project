sel = int(input('입력 진수 결정(16/10/8/2) : '))

if sel != 16 or 10 or 8 or 2 :
    print('16, 10, 8, 2 숫자 중 하나만 입력하세요.')
    exit()

num = input('값 입력 : ')

if sel == 16 :
    re = int(num, 16)
elif sel == 10 :
    re = int(num, 10)
elif sel == 8 :
    re = int(num, 8)
elif sel == 2 :
    re = int(num, 2)

print('16진수 ==>', hex(re))
print('10진수 ==>', re)
print('8진수 ==>', oct(re))
print('2진수 ==>', bin(re))
