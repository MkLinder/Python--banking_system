from controllers.account.Deposit import deposit
from controllers.account.Withdrawal import withdrawal
from controllers.account.Extract import extract

def account_operations_menu(user_name, acc_operations):
    menu_options = f"""
    ========== FICTI BANK ==========\n
    \tOlá, {user_name.split(' ')[0]}.
    \tO que deseja fazer?
    
    [D] Depositar
    [S] Sacar
    [E] Extrato
    [Q] Sair
    ================================
    """

    option = input(menu_options)

    while option != 'q':
        if option == 'd':
            deposit(acc_operations)
            option = input(menu_options)
            
        elif option == 's':
            withdrawal(acc_operations)
            option = input(menu_options)

        elif option == "e":
            extract(acc_operations,)
            option = input(menu_options)

        elif option == "q":
            break    
        
        else:
            print("\nOperação inválida! Por favor, digite uma opção válida.")
            option = input(menu_options)