 # AMAZONCC - Sistema de Supermercado em Python #

# 📌 Sobre o Projeto #

O AMAZONCC é um sistema de simulação de compras em supermercado desenvolvido em Python para execução via terminal.
O projeto permite que usuários realizem cadastro, login, naveguem por um catálogo de produtos, adicionem itens ao carrinho e finalizem compras com controle de crédito.
Além disso, o sistema inclui um recurso de gamificação, onde o usuário pode ganhar desconto ao testar sua sorte.

# 🚀 Funcionalidades #
# 👤 Cadastro de Usuário #

`Registro com:`

Nome
CPF (validado)
E-mail
Senha (6 dígitos numéricos)
Verificação de dados duplicados
Crédito inicial automático de R$ 1000,00


# 🔐 Login #

Autenticação por CPF e senha

Validação de acesso


# 🛍️ Sistema de Compras #

Catálogo com 20 produtos
Escolha por ID
Seleção de quantidade
Cálculo automático do valor
Controle de crédito em tempo real


# 🧺 Carrinho de Compras #

Visualização do total da compra
Listagem detalhada dos itens
Exibição do crédito restante


# 💳 Pagamento #

Resumo completo da compra:

Total de itens
Tipos de produtos
Valor total


Opção de confirmação ou cancelamento
Reset do crédito após pagamento


# 🎲 Teste sua sorte (Desconto) #

O usuário pode participar de um minigame:

Adivinhar um número entre 0 e 100


`Se acertar:`

Ganha 10% de desconto


Adiciona interatividade ao sistema


# 🧠 Estrutura do Sistema #
# 📦 Produtos #
 
Lista fixa contendo:

ID
Nome
Preço

# 👥 Clientes #

`Armazenados em um dicionário:`

clientes = {


    "cpf": {
    
        "nome": "Nome do cliente",
        
        "senha": "123456",
        
        "email": "email@email.com",
        
        "credito": 1000.00,
        
        "carrinho": [],
        
        "desconto": 0.0
        
    }
    
}

# ✅ Validações Implementadas #
✔ CPF válido (cálculo oficial dos dígitos verificadores)

✔ Nome contendo apenas letras

✔ Senha numérica com exatamente 6 dígitos

✔ E-mail com:

Um único "@"

Ponto após "@"

Formato válido

# 🎯 Objetivo do Projeto #
`Este projeto tem fins educacionais e foi desenvolvido para praticar:`

Lógica de programação
Estruturas de dados (listas e dicionários)
Funções e modularização
Validação de dados
Simulação de regras de negócio reais
