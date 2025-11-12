clientes = {}
produtos = [
    {"id": 1, "nome": "Pasta de dente", "preco": 5.00},
    {"id": 2, "nome": "Arroz 5kg", "preco": 10.00},
    {"id": 3, "nome": "Feijão 1kg", "preco": 4.00},
    {"id": 4, "nome": "Açúcar 1kg", "preco": 2.00},
    {"id": 5, "nome": "Café 500g", "preco": 8.00},
    {"id": 6, "nome": "Leite 1L", "preco": 4.50},
    {"id": 7, "nome": "Óleo de soja 900ml", "preco": 6.00},
    {"id": 8, "nome": "Macarrão 500g", "preco": 3.50},
    {"id": 9, "nome": "Sal 1kg", "preco": 2.00},
    {"id": 10, "nome": "Farinha de trigo 1kg", "preco": 4.00},
    {"id": 11, "nome": "Sabão em pó 1kg", "preco": 12.00},
    {"id": 12, "nome": "Detergente 500ml", "preco": 2.50},
    {"id": 13, "nome": "Papel higiênico", "preco": 15.00},
    {"id": 14, "nome": "Sabonete", "preco": 3.00},
    {"id": 15, "nome": "Shampoo 400ml", "preco": 10.00},
    {"id": 16, "nome": "Condicionador 400ml", "preco": 10.00},
    {"id": 17, "nome": "Desodorante", "preco": 8.00},
    {"id": 18, "nome": "Creme dental", "preco": 5.00},
    {"id": 19, "nome": "Água sanitária 1L", "preco": 3.50},
    {"id": 20, "nome": "Esponja de limpeza", "preco": 2.00}
]


#função que valida o cpf
def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    
    if len(cpf) != 11:
        return False
    
    if cpf == cpf[0] * 11: #verifica se são todos os números são iguais
        return False
    
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    
    digito1 = 0 if soma % 11 < 2 else 11 - (soma % 11)
    
    if int(cpf[9]) != digito1:
        return False
    
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))

    digito2 = 0 if soma % 11 < 2 else 11 - (soma % 11)
    return int(cpf[10]) == digito2

def cadastrar_cliente():
    print("\n=== CADASTRO DE CLIENTE ===")
    nome = input("Nome: ")
    
    while not nome.replace(" ", "").isalpha(): #replce remove o espaço, o isalpha aceita somente caracteres, se tirar o replace, nomes com espaço não ira funcionar
        print("Erro: Use apenas letras!")
        nome = input("Nome: ")
    
    cpf = input("CPF (11 dígitos): ")

    while not validar_cpf(cpf):
        print("Erro: CPF inválido!")
        cpf = input("CPF (11 dígitos): ")
    
    cpf = ''.join(filter(str.isdigit, cpf)) #ira pegar numero por numero e juntar 123.456 **> 123456
    

    if cpf in clientes:
        print("Erro: CPF já cadastrado!")
        return
    
    senha = input("Senha (6 dígitos): ")
    
    while not (senha.isdigit() and len(senha) == 6): #isdigit verifica se são somente números inseridos
    #while len(senha) != 6: para liberar numeros + caracteres 
        #print("Erro: Senha deve ter 6 digitos!!")
        print("Erro: Senha deve ter 6 dígitos e somente números!!")
        senha = input("Senha (6 dígitos): ")
    
    email = input("E-mail: ")
    
    while True:
        if "@" not in email:
           print("Error: o E-mail precisa de '@'!!")
        
        elif email.count('@') != 1:
            print("Error: o E-mail deve conter apenas um '@'!!")

        else:
            posicao_at = email.index("@")
            if posicao_at == 0 or posicao_at == - 1:
                print("Error: o '@' não deve estar no começo/final do E-mail!!")
            elif "." not in email[posicao_at:]:
                print("Error: o E-mail deve conter '.' após o @!!")
            else:
                break
        email = input("E-mail: ")         
    
  
    clientes[cpf] = {
        "nome": nome,
        "senha": senha,
        "email": email,
        "credito": 1000.00,
        "carrinho": [],
        "desconto": 0.0
    }
    
    print(f"\nCliente {nome} cadastrado com sucesso!")
    print(f"Limite de crédito: R$ 1000.00")

#função que possibilita realizar as compras
def fazer_compras(cpf):
    
    cliente = clientes[cpf]
    
    while True:
        print("\n=== CATÁLOGO DE PRODUTOS ===")
        
        for p in produtos:
            print(f"{p['id']:2d} - {p['nome']:25s} R$ {p['preco']:.2f}")
        
        print(f"\nCrédito disponível: R$ {cliente['credito']:.2f}")
        
        escolha = input("\nEscolha o produto (1-20) ou 0 para voltar: ")

        if escolha == "0":
            break
        
        try:s
            id_produto = int(escolha)
 
            if id_produto < 1 or id_produto > 20:
                print("Produto inválido!")
                continue

            produto = produtos[id_produto - 1]
            quantidade = input(f"Quantidade de {produto['nome']}: ")
            quantidade = int(quantidade)
            
            if quantidade <= 0:
                print("Quantidade deve ser maior que zero!")
                continue
        
            valor_total = produto['preco'] * quantidade
            
            if cliente['credito'] < valor_total:
                print("\nLIMITE DE CRÉDITO EXCEDIDO!")
                print(f"Você não pode realizar esta compra.")
                print(f"Valor da compra: R$ {valor_total:.2f}")
                print(f"Crédito disponível: R$ {cliente['credito']:.2f}")
                continue
            
            cliente['carrinho'].append({
                'id': produto['id'],
                'nome': produto['nome'],
                'preco': produto['preco'],
                'quantidade': quantidade,
                'subtotal': valor_total
            })
            
            cliente['credito'] -= valor_total
            
            print(f"\n{quantidade} x {produto['nome']} adicionado ao carrinho!")
            print(f"Subtotal: R$ {valor_total:.2f}")
            print(f"Crédito restante: R$ {cliente['credito']:.2f}")
        
        except:
            print("Entrada inválida!")


#função para visualizar o carrinho de compras
def mostrar_carrinho(cpf):  
   
    cliente = clientes[cpf]
    
    print("\n=== MEU CARRINHO ===")
    
    if not cliente['carrinho']:
        print("Carrinho vazio!")
        return
    
    total = sum(item['subtotal'] for item in cliente['carrinho'])
    print(f"\nValor total: R$ {total:.2f}")
    
    print(f"Crédito disponível: R$ {cliente['credito']:.2f}")
    
    ver_itens = input("\nVer todos os itens? (s/n): ")
    
    if ver_itens.lower() == 's': #lower pega a caracter e coloca em caixa alta
        print("\nItens no carrinho:")
        
        for i, item in enumerate(cliente['carrinho'], 1): #o enumerate faz o i percorrer o carrrinho e pega a quantidade e o item pega o nome dele 
            print(f"{i}. {item['quantidade']} x {item['nome']} - R$ {item['preco']:.2f} cada = R$ {item['subtotal']:.2f}")


#função do pagamento
def pagar_conta(cpf):

    cliente = clientes[cpf]

    print("\n=== FINALIZAR COMPRA ===")
    
    if not cliente['carrinho']:
        print("Carrinho vazio! Nada para pagar.")
        return
    
    total = sum(item['subtotal'] for item in cliente['carrinho'])
    
    total_itens = sum(item['quantidade'] for item in cliente['carrinho'])
    
    print(f"\nTotal dos produtos: R$ {total:.2f}")
    print(f"Total de itens: {total_itens}")
    print(f"Tipos de produtos: {len(cliente['carrinho'])}")
    
    if cliente['desconto'] == 0:
        print("\n" + "-"*40)
        jogar = input("Quer testar sua sorte para ganhar desconto? (s/n): ")
        
        if jogar.lower() == 's':
            teste_sua_sorte(cpf)
    
    print("\n" + "="*40)
    print(f"Total dos produtos: R$ {total:.2f}")
    
    if cliente['desconto'] > 0:
        desconto_valor = total * cliente['desconto']
        total_final = total - desconto_valor
        print(f"Desconto ({int(cliente['desconto']*100)}%): -R$ {desconto_valor:.2f}")
        print(f"Total a pagar: R$ {total_final:.2f}")
    else:
        total_final = total
        print(f"Total a pagar: R$ {total_final:.2f}")
    
    confirma = input("\nConfirmar pagamento? (s/n): ")
    
    if confirma.lower() == 's':
        cliente['carrinho'] = []
        cliente['credito'] = 1000.00
        cliente['desconto'] = 0.0
        
        print("\nPAGAMENTO REALIZADO COM SUCESSO!")
        print(f"Valor pago: R$ {total_final:.2f}")
        print(f"Crédito restaurado: R$ 1000.00")
    else:
        print("Pagamento cancelado.")


#função do desconto
def teste_sua_sorte(cpf):

    cliente = clientes[cpf]
    
    print("\n" + "-"*40)
    print("**TESTE SUA SORTE!***")
    print("-"*40)
    print("Adivinhe o número entre 0 e 100!")
    print("Se acertar, ganha 10% de desconto nesta compra!")
    
    numero_sorteado = 50  
    
    try:
        palpite = int(input("\nDigite seu palpite (0-100): "))
        
        if palpite < 0 or palpite > 100:
            print("Número inválido! Deve estar entre 0 e 100.")
            return False
    
        print(f"\nNúmero sorteado: {numero_sorteado}")
        print(f"Seu palpite: {palpite}")

        if palpite == numero_sorteado:
            cliente['desconto'] = 0.10
            print("\n=== PARABÉNS! VOCÊ ACERTOU! ===")
            print("Você ganhou 10% de desconto nesta compra!")
            return True
        else:
            print("\nNão foi dessa vez!")
            print("Sem desconto desta vez.")
            return False
    except:
        print("Entrada inválida!")
        return False


#Apos o usuario fazer o login, ira puxar essa função
def menu_cliente(cpf):    
    while True:
        cliente = clientes[cpf]
        print(f"\n{'='*40}")
        print(f"Bem-vindo(a), {cliente['nome']}!")
        print(f"{'='*40}")
        print("1 - Comprar produtos")
        print("2 - Ver carrinho")
        print("3 - Finalizar compra")
        print("4 - Sair")

        opcao = input("\nEscolha: ")

        if opcao == "1":
            fazer_compras(cpf)
        elif opcao == "2":
            mostrar_carrinho(cpf)
        elif opcao == "3":
            pagar_conta(cpf)
        elif opcao == "4":
            break
        else:
            print("Opção inválida!")


#Login para acessar as opções
def login():
    print("\n=== LOGIN ===")
    cpf = input("CPF: ")
    cpf = ''.join(filter(str.isdigit, cpf)) #.join ele junta os caraceteres ex 106.340 --> 106340
    if cpf not in clientes:   #verifica os cpf cadastrados caso não esteja cadastrado puxa o print
        print("CPF não encontrado!")
        return None
    senha = input("Senha: ")
    if clientes[cpf]['senha'] == senha:
        return cpf

    else:
        print("Senha incorreta!")
        return None


#Função pricipal do codigo
def main():
    print("="*40)
    print("   SISTEMA AMAZONCC - LOJA VIRTUAL")
    print("="*40)
    
    while True: 
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Cadastrar cliente")
        print("2 - Fazer login")
        print("3 - Sair")
    
        opcao = input("\nEscolha: ")
        
        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            cpf = login()
            if cpf:
                menu_cliente(cpf)
        elif opcao == "3":
            print("\nObrigado pela preferência, VOLTE SEMPRE!!:)")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()

