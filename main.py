menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
"""

saldo = 0
limite = 500
extrato = ""
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
            extrato += f"Deposito: R$ {valor_deposito:.2f}\n" 
            print(f"Seu depósito de R$ {valor_deposito:.2f} foi efetuado!")
    
    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES:
            print("Você atingiu o limite de saques diários, volte amanhã.")
        
        elif saldo == 0:
            print("Você não possui saldo para sacar!")    
            
        else:
            valor_saque = float(input("Digite o valor que deseja sacar: R$"))
            if valor_saque <= 0:
                print("Valor inválido!")

            elif valor_saque > limite:
                print(f"O valor limite por saque é de R${limite:.2f}")

            elif valor_saque > saldo:
                print("Valor de saque superior ao saldo!")
                
            else:
                saldo -= valor_saque
                numero_saques += 1
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                print(f"Saque de R$ {valor_saque:.2f} realizado!")

    elif opcao == "e":
        print("\n============ EXTRATO ============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=================================")

    elif opcao == "q":
        break    
    
    else:
        print("Operação inválida! Por favor, digite uma operação válida.")