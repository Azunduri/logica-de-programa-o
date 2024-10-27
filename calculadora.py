nume1 = float(input("Digite um número aqui"))
nume2 = float(input("Digite o segundo número aqui"))
operacao = input("escolha um operador ( +,-,*,/")

if operacao  == "+":
    resultado = nume1 + nume2
elif operacao == "-":
    resultado = nume1 - nume2
elif operacao == "*":
    resultado = nume1 * nume2
elif  operacao == "/":
    if nume2 != 0:
        resultado =  nume1 / nume2
    else:
        print("Não é possível dividir por zero")
else:
    print("Operador inválido")
print("O resultado da operação é:", resultado)


