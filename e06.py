# Faça um Programa que leia três números e mostre o maior deles.

num1 = int(input('Digite um número'))
num2 = int(input('Digite um número'))
num3 = int(input('Digite um número'))

if num1 > num2 and num1 > num3:
    print(num1)
elif num1 < num2 and num2 > num3:
    print(num2)
else:
    print(num3)
