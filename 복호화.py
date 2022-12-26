n = int(input("N의 값을 입력하세요 : "))
eori = int(input("암호문을 입력하세요 : "))
d = int(input("개인키를 입력하세요 : "))

ori = (eori**d)%n
print("평서문 : {}".format(ori))
input()