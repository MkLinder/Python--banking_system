import json

def extract(acc_operations):
    
    print("\n============ EXTRATO ============")
    print(
        "Não foram realizadas movimentações." if not acc_operations["extract"] else json.dumps(acc_operations["extract"], indent=4)
    )
    print(f"\nSaldo: R$ {acc_operations["balance"]:.2f}")
    print("=================================")