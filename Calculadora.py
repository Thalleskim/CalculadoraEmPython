def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: Divisão por zero"

print("Escolha uma operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

choice = input("Digite o número da operação (1/2/3/4): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if choice == '1':
    print(f"O resultado da adição é: {add(num1, num2)}")
elif choice == '2':
    print(f"O resultado da subtração é: {subtract(num1, num2)}")
elif choice == '3':
    print(f"O resultado da multiplicação é: {multiply(num1, num2)}")
elif choice == '4':
    print(f"O resultado da divisão é: {divide(num1, num2)}")
else:
    print("Opção inválida")
