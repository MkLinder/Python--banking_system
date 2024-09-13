def extract(acc_operations):
     
    print("\n============ EXTRATO ============")
    print(
        "Não foram realizadas movimentações." if not acc_operations["extract"] else 
        acc_operations["extract"]
    )
    print(f"\nSaldo:\t\tR$ {acc_operations["balance"]:.2f}")
    print("=================================")