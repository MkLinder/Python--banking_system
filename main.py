from controllers.menu.Home_menu import home_menu
# from controllers.menu.Menu_account_options import menu

# from controllers.account.Deposit import deposit
# from controllers.account.Withdrawal import withdrawal
# from controllers.account.Extract import extract
from controllers.account.Create_account import create_account

from controllers.user.Register_user import get_user_data


# from database.default_inf import default


while True:

    option = input(home_menu)

    if option == "c":
         get_user_data()
    elif option == "a":
        create_account()
   





    # create_account("Mike Linder", "123456")
    # option = input(menu)

    # if option == "d":
    #     deposit_amount = float(input("Digite o valor que deseja depositar: R$"))
    #     if deposit_amount <= 0:
    #         print("Valor inválido!")
    #     else:
    #         deposit(deposit_amount)
    
    # elif option == "s":
    #     if default["withdrawals_made"] >= default["WITHDRAWALS_LIMIT"]:
    #         print("Você atingiu o limite de saques diários, volte amanhã.")
        
    #     elif default["balance"] == 0:
    #         print("Você não possui saldo para sacar!")    
            
    #     else:
    #         withdrawal_amount = float(input("Digite o valor que deseja sacar: R$"))
    #         if withdrawal_amount <= 0:
    #             print("Valor inválido!")

    #         elif withdrawal_amount > default["limit"]:
    #             print(f"O valor limite por saque é de R${default["limit"]:.2f}")

    #         elif withdrawal_amount > default["balance"]:
    #             print("Valor de saque superior ao saldo!")
                
    #         else:
    #             withdrawal(withdrawal_amount)

    # elif option == "e":
    #     extract()

    # elif option == "q":
    #     break    
    
    # else:
    #     print("Operação inválida! Por favor, digite uma operação válida.")