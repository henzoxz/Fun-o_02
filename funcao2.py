# Crie uma função chamada verificar_paridade que receba um número inteiro como argumento e retorne uma mensagem indicando se o número é par ou ímpar.

num = int(input("Digite o Número: "))

def verificar_idade(num):
    if num % 2==0:
        return "O Número é Par"
    
    else:
        return "O Número é Ímpar"
    
numero = verificar_idade(num)
print(numero)