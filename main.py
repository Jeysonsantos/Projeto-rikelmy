
def cadastrar():















def principal():
    print()
    print("--------MENU--------")
    print()
    print("1)Cadastrar aluno."
            "\n2)Desempenho."
          "\n3)Sair.")
    while True:
        try:
            opcao=int(input("\nQual opção deseja?: "))
        except:
            print()
            print("Você digitou algo inválido, reiniciando...")
            print()
            principal()

        if opcao==1:
            print()
            cadastrar()
            print()
        elif opcao==2:
            print()
            print()
        elif opcao==3:
            print()
            print("Obrigado, volte sempre.")
            print()
            break
        else:
            print()
            print("-Digite apenas o inteiro que corresponde a opção desejada.-")
            print()
principal()






