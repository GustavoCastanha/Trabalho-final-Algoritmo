usuarios = []

while True:
    
    login = str(input("insira seu nome, ou '0' para pular etapa: "))
    if login == "*":
            print("Saindo!")
            break
    elif login in usuarios:
           print("Este usuario ja está cadastrado")
    else:
            usuarios.append(login)
print(usuarios)