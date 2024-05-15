menu = """
========= SISTEMA BANCÁRIO =========
[1] Depositar
[2] Sacar
[3] Gerar Extrato
[0] Sair

Digite a opção desejada: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao ==  "1":
        valor_depositado = float(input("Digite o valor a ser Depositado: R$ "))
        if valor_depositado >= 0:
            saldo += valor_depositado
            extrato += f"Depósito: R$ {valor_depositado:.2f}\n"
            print(f"\n*** Realizado o depósito no valor de R$ {valor_depositado:.2f}\n- Saldo atual: R$ {saldo:.2f}")
        else:
            print("\n*** Operação Recusada ***\nO valor digitado não é válido!")

    elif opcao == "2":
        if numero_saques < LIMITE_SAQUES:
            valor_sacado = float(input("Digite o valor a ser Sacado: R$ "))
            if saldo > valor_sacado:
                if 0 <= valor_sacado <= 500:
                    saldo -= valor_sacado
                    numero_saques += 1
                    extrato += f"Saque: R$ {valor_sacado:.2f}\n"
                    print(f"\n*** Realizado o saque no valor de R$ {valor_sacado:.2f}\n- Saldo atual: R$ {saldo:.2f}")
                elif valor_sacado > 500:
                    print("\n*** Operação Recusada ***\nO valor limite por saque é R$ 500,00.")
                else:
                    print("\n*** Operação Recusada ***\nO valor digitado não é válido!")
            else:
                print(f"\n*** Operação Recusada ***\nSaldo insuficiente para saque:\n- Saque desejado: R$ {valor_sacado:.2f}\n- Saldo disponível: R$ {saldo:.2f}")
        else:
            print("*** Operação Recusada ***\nSomente é possível sacar 3 vezes ao dia!")

    elif opcao == "3":
        print("\n--------------- EXTRATO BANCÁRIO ---------------")
        print("       Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n    *Saldo: R$ {saldo:.2f}*")
        print("------------------------------------------------")

    elif opcao == "0":
        print("=> Obrigado por utilizar os serviços do nosso banco!\nTenha um ótimo dia!")
        break

    else: 
        print("=> Opção inválida, por favor selecione novamente a operação desejada.")