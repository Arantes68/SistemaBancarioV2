import textwrap

# FUNÇÃO PARA FILTRAR USUÁRIO POR CPF
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


# FUNÇÃO PARA FILTRAR CONTA POR NÚMERO DE CONTA
def filtrar_conta(numero_conta, contas):
    # Filtra as contas com base no número da conta
    contas_filtradas = [conta for conta in contas if conta["numero_conta"] == numero_conta]
    return contas_filtradas[0] if contas_filtradas else None


# FUNÇÃO PARA CRIAR UM NOVO USUÁRIO
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)
    print("")
    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    print("")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    print("")
    endereco = input("Informe o endereço (logradouro, número , bairro , cidade/sigla estado): ")
    print("")
    print("")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("")
    print("")
    print("=== Usuário criado com sucesso! ===")


# FUNÇÃO PARA CRIAR UMA NOVA CONTA
def criar_conta(agencia, numero_conta, usuarios, contas):
    conta_existente = filtrar_conta(numero_conta, contas)

    if conta_existente:
        print("\n@@@ Já existe uma conta com esse número! @@@")
        return None

    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


# FUNÇÃO PARA LISTAR TODAS AS CONTAS
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))



# MENU INICIAL: É USADO O """ PARA FAZER A PERSONALIZAÇÃO PARA APARECER AO USUÁRIO.
menu = """ 

|versão: 2|
========================================================
                      BANCO DIGITAL              
========================================================


Escolha uma das opções abaixo:

[1] Depositar
[2] Saque
[3] Extrato
[4] Novo Usuário
[5] Nova Conta
[6] Listar Contas
[7] Sair

Por gentileza, insira a opção desejada: 
"""


# VARIÁVEIS
saldo = 0 #Variável que irá armazenar int
limite = 500
extrato = "" #Variável que irá armazenar string
numero_saques = 0
LIMITE_SAQUES = 3 #Variavel constante
usuarios = [] #Listas de usuários
contas = []   #Listas de contas



# O PROGRAMA CONTINUARÁ EXECUTANDO ATÉ QUE O USUÁRIO ESCOLHA A OPÇÃO DE SAIR (OPÇÃO 7).
while True:
    opcao = int(input(menu))

# DEPOSITAR
    if opcao == 1: 
        valor = float(input("Informe o valor do depósito: "))

        #Estrutura de decisão do Depósito
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

# SACAR
    elif opcao == 2:  
        valor = float(input("Informe o valor do saque: "))

        #Condições
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

 # EXTRATO
    elif opcao == 3: 
        print("\n====================== EXTRATO =======================")
        print("")
        print("")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("")
        print("========================================================")


# NOVO USUÁRIO
    elif opcao == 4:  
        criar_usuario(usuarios)   #Chamando a função


# NOVA CONTA
    elif opcao == 5:  
        numero_conta = len(contas) + 1
        conta = criar_conta("0001", numero_conta, usuarios, contas)
        if conta:
            contas.append(conta)  #Chamando a função


# LISTAR CONTAS
    elif opcao == 6: 
        listar_contas(contas)   #Chamando a função


# SAIR DO LOOP; ENCERRANDO A EXECUÇÃO.
    elif opcao == 7:  
        print("Saindo... Até logo!")
        break

# SE O USUÁRIO DIGITAR ALGUMA OPÇÃO QUE NÃO ESTÁ NO MENU, ELE INFORMA QUE A OPERAÇÃO É INVÁLIDA.
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
