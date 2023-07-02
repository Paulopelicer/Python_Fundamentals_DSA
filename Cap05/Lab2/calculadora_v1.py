# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

#Função para somar

def somar(a, b):
    return a + b

#Função para subtrair

def subtrair(a, b):
    return a - b

#Função para multuplicar

def multiplicar(a, b):
    return a * b

#Função para dividir

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        print('Divisão não permitida')

#Função Principal

def main():
    
#Solicite ao usuário os números e a operação desejada

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
operacao = input('Digite a operação desejada (+, -, *, /): ')

#Verificar operação e realizar o cálculo

if operacao == '+':
    resultado = somar(num1, num2)
elif operacao == '-':
    resultado = subtrair(num1, num2)
elif operacao == '*':
    resultado = multiplicar(num1, num2)
elif operacao == '/':
    resultado = dividir(num1, num2)
else:
    print('Operação inválida')

#Resultado

print('Resultado: ', resultado)

#Chamada da Função Principal

main()
