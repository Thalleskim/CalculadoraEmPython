import math

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

def power(x, y):
    return x ** y

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Erro: Raiz quadrada de número negativo"

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def calculator():
    while True:
        print("\nEscolha uma operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Potência")
        print("6. Raiz quadrada")
        print("7. Sair")

        choice = input("Digite o número da operação (1/2/3/4/5/6/7): ")

        if choice in ['1', '2', '3', '4', '5']:
            num1 = get_float("Digite o primeiro número: ")
            num2 = get_float("Digite o segundo número: ")

            if choice == '1':
                print(f"O resultado da adição é: {add(num1, num2)}")
            elif choice == '2':
                print(f"O resultado da subtração é: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"O resultado da multiplicação é: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"O resultado da divisão é: {divide(num1, num2)}")
            elif choice == '5':
                print(f"O resultado da potência é: {power(num1, num2)}")
        elif choice == '6':
            num = get_float("Digite o número para calcular a raiz quadrada: ")
            print(f"O resultado da raiz quadrada é: {square_root(num)}")
        elif choice == '7':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    calculator()
