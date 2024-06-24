estoque = []
lista_clientes = []
registros_vendas = []
 
def cadastrar_produtos(estoque):
    print("Cadastro de Produtos\n")
    codigo = input("Insira o código do produto: ")
    nome = input("Insira o nome do produto: ")
    data = input("Insira a data de cadastro do produto: ")
    valor_compra = float(input("Escreva o valor de compra: "))
    valor_venda = float(input("Escreva o valor de venda: "))
    qtd_estoque = int(input("Quantidade de produtos presentes em estoque: "))
 
    estoque.append((codigo, nome, data, valor_compra, valor_venda, qtd_estoque))
    print("Produto cadastrado com sucesso!")
 
def cadastro_cliente(lista_clientes):
    nome = input("Insira o nome do cliente  que deseja: ")
    codigo = input("Insira o código do cliente que deseja: ")
    endereco = input("Insira o endereço do cliente que deseja: ")
    email = input("Insira o email do cliente que deseja: ")
   
    lista_clientes.append((nome, codigo, endereco, email))
    print("Seu cliente foi cadastrado com sucesso!")
 
def vender(lista_clientes, estoque, registros_vendas):
    codigo_cliente = input("Digite o código do cliente que você está à procura: ")
    for cliente in lista_clientes:
        if cliente[1] == codigo_cliente:
            break
        else:
            print("Cliente não encontrado!")
            return
    
    codigo_produto = input("Digite o código do produto que você procura: ")
    for i, produto in enumerate(estoque):
        if produto[0] == codigo_produto and produto[5] > 0:
            estoque[i] = produto[:5] + (produto[5] - 1,)
            venda_total = produto[4]
            lucro = venda_total - produto[3]
            registros_vendas.append((produto[1], 1, venda_total, lucro))
            print("Venda realizada com sucesso!")
            return
    print("O produto não foi encontrado ou está sem estoque!")
 
def relatorio_estoque(estoque):
    print("Relatório de produtos em estoque:")
    for produto in estoque:
        print(f"Código: {produto[0]}, Nome: {produto[1]}, quantidade em estoque: {produto[5]}")
 
def relatorio_vendas(registros_vendas):
    total_vendas = 0
    total_lucro = 0
    print("\nRelatório de vendas:")
    for venda in registros_vendas:
        total_vendas += venda[2]
        total_lucro += venda[3]
        print(f"Produto: {venda[0]}, quantidade: {venda[1]}, total da venda: {venda[2]}, lucro: {venda[3]}")
    print(f"\nTotal de Vendas: {total_vendas}")
    print(f"Lucro Total: {total_lucro}")
 
def menu(estoque, lista_clientes, registros_vendas):
    while True:
        opcao = input("Insira uma opção:\n1 - Cadastrar produtos\n2 - Cadastrar clientes\n3 - Vendas\n4 - Relatório de produtos em estoque\n5 - Relatório de vendas\n6 - Sair\nOpção: ")
       
        if opcao == "1":
            cadastrar_produtos(estoque)
        elif opcao == "2":
            cadastro_cliente(lista_clientes)
        elif opcao == "3":
            vender(lista_clientes, estoque, registros_vendas)
        elif opcao == "4":
            relatorio_estoque(estoque)
        elif opcao == "5":
            relatorio_vendas(registros_vendas)
        elif opcao == "6":
            break
        else:
            print("A opção escolhida é inválida!")
 
menu(estoque, lista_clientes, registros_vendas)
