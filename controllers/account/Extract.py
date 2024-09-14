from middleware.Date_time import compare_date

def extract(acc_operations):
     
    print("\n============ EXTRATO ============\n")
    if not acc_operations["extract"]:
        print("Não foram realizadas movimentações.")
    else:
        for i in acc_operations["extract"]:
            for key, value in i.items():
                print(f"{key}:\t{value}")
            print()
            

    print(f"\nSaldo:\t\tR$ {acc_operations["balance"]:.2f}")
    print("=================================\n")