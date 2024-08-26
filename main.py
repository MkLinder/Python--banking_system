menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
"""

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Digite o valor que deseja depositar: R$"))
        if valor_deposito <= 0:
            print("Valor inválido!")
        else:
            saldo += valor_deposito
            extrato.append({
                "deposito": valor_deposito
                }) 
            print(f"Seu depósito de R${valor_deposito} foi efetuado!")
    
    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES:
            print("Você atingiu o limite de saques diários, volte amanhã.")
        
        elif saldo == 0:
            print("Você não possui saldo para sacar!")    
            
        else:
            valor_saque = float(input("Digite o valor que deseja sacar: R$"))
            if valor_saque > limite:
                print(f"O valor limite por saque é de R${limite},00")

            elif valor_saque > saldo:
                print("Valor de saque superior ao saldo!")
                
            else:
                saldo -= valor_saque
                numero_saques += 1
                extrato.append({
                "saque": valor_saque
                }) 
                print(f"Saque de R${valor_saque} realizado!")

    elif opcao == "e":
        print(f"{extrato} \n R${saldo:.2f}")

    elif opcao == "q":
        break    
    
    else:
        print("Operação inválida! Por favor, digite uma operação válida.")