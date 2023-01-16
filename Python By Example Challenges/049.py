#Correct Value

value = 50
num = 0

while (value != num):
    num = int(input("\nInsira um número: "))
    if (num > 50):
        print("Esse número é mais alto")

    elif (num < 50):
        print("Esse número é mais baixo")
        
print("Parabéns você acertou :)")