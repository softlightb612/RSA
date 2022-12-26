p = 991
q = 997
n = p * q
tot = (p - 1) * (q - 1)

#최대공약수 구하는 거
def gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1%num2
    return num1

#공개키
def publickey():
    global tot
    e = 2
    while e<tot and gcd(e, tot) != 1:
        e += 1
    return e

#개인키
def privatekey():
    global e
    global tot
    d = 1
    while (publickey() * d) % tot != 1 or d == publickey():
        d += 1
    return d

ori = int((input("평서문 : ")))
eori = ((ori**publickey())%n)

print("암호문 : {}".format(eori))
print("N : {}".format(n))
print("공개키 : {}".format(publickey()))
print("개인키 : {}".format(privatekey()))

input()