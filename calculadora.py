for i in range(5):
    user = input("Informe seu nome de usuario: ")
    pas = int(input("Informe sua senha: "))

    if user == "Luana" and pas == 1234:
        n = int(input("Digie um número: "))
        op = input("Digite a operação (+, -, *, / ou = para sair): ")

        while op != "=":
            n2 = int(input("Digite outro número: "))

            if op == "+":
                n = n + n2

            elif op == "-":
                n = n - n2

            elif op == "*":
                n = n * n2

            elif op == "/":
                if n2 != 0:
                    n = n / n2
                else:
                    print("Impossivel dividir por 0!")
                    break
            else:
                print("Operador invalido!")
                break

            op = input("Digite a operação: ")

        user = input("Informe seu nome de usuario: ")
        pas = int(input("Informe sua senha: "))

        if user == "Luana" and pas == 1234:
            print(f"Resultado = {n}")

        else:
            print("Acesso negado!")
        break

    else:
        print("Usuario ou senha incorretos!")


