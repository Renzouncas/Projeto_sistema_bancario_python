### Primeiro projeto de sistema bancário

## Menu do banco
saldo = 0
numero_saques = 0
limite_saque = 3
valor_limite = 500
extrato =""
while True:
    menu = (input("""\n======Menu======
    [1] Deposito
    [2] Saque
    [3] Extrato
    [0] Sair

Digite uma das opções acima: """))
    
    # Operação de depósito
    if menu == "1":
        valor = float(input("Quanto deseja depositar: "))
        if valor > 0:
            saldo += valor
            extrato +=f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")

        else:
            print("Operação invalida, o valor informado é inválido.")                
    
    # Operação de saque 
    elif menu == "2":
        valor = float(input("Quanto deseja sacar: "))
        if valor > saldo:
            print("Operação invalida, saldo insuficiente.")
        
        elif valor > valor_limite:
            print("Operação invalida, o valor informado excedo o limite.")
        
        elif numero_saques >= limite_saque:
            print("Operação invalida, pois já ultrapassou o numero limite de saque.")
        
        elif valor > 0:
            saldo -= valor
            extrato +=f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")
        
        else:
            print("Operação invalida, o valor informado é invalido.") 
    
    # Operação de Extrato
    elif menu == "3":
        print("\n==============Extrato==============")
        print("Não foram realizada movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================================\n")
    
    # Saindo do menu
    elif menu == "0":
        print("Saindo.\n")
        break
    
    # Operação invalida
    else:
        print("Operação invalida, tente novamente.\n")

    