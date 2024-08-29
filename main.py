import json
from controllers.Menu_options import menu
from controllers.Deposit import deposit

from database.default_inf import default


while True:
    opcao = input(menu)

    if opcao == "d":
        deposit_amount = float(input("Digite o valor que deseja depositar: R$"))
        if deposit_amount <= 0:
            print("Valor inválido!")
        else:
            deposit(deposit_amount)
    
    elif opcao == "s":
        if default["withdrawals"] >= default["WITHDRAWALS_LIMIT"]:
            print("Você atingiu o limite de saques diários, volte amanhã.")
        
        elif default["balance"] == 0:
            print("Você não possui saldo para sacar!")    
            
        else:
            valor_saque = float(input("Digite o valor que deseja sacar: R$"))
            if valor_saque <= 0:
                print("Valor inválido!")

            elif valor_saque > default["limit"]:
                print(f"O valor limite por saque é de R${default["limit"]:.2f}")

            elif valor_saque > default["balance"]:
                print("Valor de saque superior ao saldo!")
                
            else:
                default["balance"] -= valor_saque
                default["withdrawals"] += 1
                default["extract"].append(f"Saque: R$ {valor_saque:.2f}")
                print(f"Saque de R$ {valor_saque:.2f} realizado!")

    elif opcao == "e":
        print("\n============ EXTRATO ============")
        print(
            "Não foram realizadas movimentações." if not default["extract"] else json.dumps(default["extract"], indent=4)
        )
        print(f"\nSaldo: R$ {default["balance"]:.2f}")
        print("=================================")

    elif opcao == "q":
        break    
    
    else:
        print("Operação inválida! Por favor, digite uma operação válida.")


