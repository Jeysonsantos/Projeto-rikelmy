import pickle

'''----------------------------------------------------------------------------'''

def cadastrar_aluno(lista_disciplina,dici_mat_nome,dici_listas_notas):
    '''Função cadastra novo aluno.'''
    while True:
        print('------------- Opção atual: CADASTRO/EXCLUIR ALUNO. ------------')
        print()
        print("1)Cadastrar aluno"
              "\n2)Excluir aluno"              
              "\n\n3)Menu inicial")
        print()
        opc=str(input("Digite a opção desejada(1,2 ou 3):"))

        if opc=='1':
            print()
            while True:
                nome = str(input("Digite o nome do aluno:"))
                if nome=="":
                    print()
                    print("-> NOME PRECISA CONTER PELO MENOS UMA LETRA.")
                    print()
                    input("---> Pressione ENTER para continuar.")
                    print()
                else:
                    break
            nome=nome.upper()
            print()
            print("---> OBS: A matrícula do aluno são inteiros de 4 digitos.")
            print()
            while True:
                matricula=str(input("Digite a matrícula do aluno.(xxxx):"))
                try:
                    matricula = int(matricula)
                    if (matricula < 1000) or (matricula > 9999):
                        print()
                        print("---> Número de matrícula inválida. Modelo = xxxx")
                        print()
                        input("---> Pressione ENTER para continuar.")
                        print()
                        break
                    elif matricula in dici_mat_nome:
                        print()
                        print("---> Número de matrícula pertence à {}.".format(dici_mat_nome[matricula]))
                        print()
                        input("---> Pressione ENTER para continuar.")
                        print()
                        break
                    else:
                        print()
                        dici_mat_nome[matricula]=nome
                        dici_listas_notas[matricula]=[]
                        for i in lista_disciplina:
                            dici_listas_notas[matricula].append(i)
                        print()
                        print("---> ALUNO CADASTRADO COM SUCESSO. ")
                        print()
                        input("---> Pressione ENTER para continuar.")
                        print()
                        break
                except:
                    print()
                    print("---> Digite apenas números inteiros.")
                    print()
                    input("---> Pressione ENTER para continuar.")
                    print()
        elif opc == '2':
            if len(dici_mat_nome)==0:
                print()
                print('---> Necessário cadastrar no mínimo 1 aluno.(opção 1)')
                print()
                input("---> Pressione ENTER para continuar.")
                print()
            else:
                print()
                print("---> ALUNOS CADASTRADOS:")
                print()
                for matricula in (dici_mat_nome):
                    print('-> {} ) {}.'.format(matricula, dici_mat_nome[matricula]))
                print()
                print('-> 0 ) Voltar.')
                print()
                while True:
                    matricula = str(input("Digite a matricula do aluno que deseja excluir:"))
                    try:
                        matricula = int(matricula)
                        if matricula==0:
                            print()
                            break
                        elif matricula < 1000 or matricula > 9999:
                            print()
                            print("Digite um número de matricula válido.(XXXX)")
                            print()
                            input("---> Pressione ENTER para continuar.")
                            print()
                        else:
                            print()
                            if matricula in dici_mat_nome:
                                dici_mat_nome.pop(matricula)
                                dici_listas_notas.pop(matricula)
                                print()
                                print("---> ALUNO EXCLUÍDO COM SUCESSO.")
                                print()
                                input("---> Pressione ENTER para continuar.")
                                print()
                            else:
                                print()
                                print("---> Número de matrícula não consta no sistema.")
                                print()
                                input("---> Pressione ENTER para continuar.")
                                print()

                            break
                    except:
                        print()
                        print("Digite um número de matricula válido.(XXXX)")
                        print()
                        input("---> Pressione ENTER para continuar.")
                        print()

        elif opc == '3':
            break
        else:
            print()
            print('Digite apenas 1,2 ou 3.')
            print()
            input("---> Pressione ENTER para continuar.")
            print()

    return dici_listas_notas

'''----------------------------------------------------------------------------'''

def cadastrar_disciplinas(lista_disciplinas,dici_listas_notas,dici_mat_nome):
    '''Função cadastra nova disciplina.'''
    print()
    while True:
        print('------------- Opção atual: CADASTRAR/EXCLUIR DISCIPLINA ------------')
        print()
        print("1)Cadastrar disciplina"
              "\n2)Excluir disciplina"              
              "\n\n3)Voltar")
        print()
        opc=str(input("Digite a opção desejada(1,2 ou 3):"))

        if opc=='1':
            print()
            print('---> DISCIPLINAS CADASTRADAS:')
            print()
            for k in lista_disciplinas:
                print("-> {}.".format(k))
            print()
            disciplina = str(input("Digite o nome da disciplina para cadastro:"))
            lista_disciplinas.append(disciplina.upper())
            for i in dici_listas_notas:
                dici_listas_notas[i].append(disciplina.upper())
            print()
            print("---> Disciplina [{}] foi cadastrada com sucesso.".format(disciplina.upper()))
            print()
            input("---> Pressione ENTER para continuar.")
            print()
        elif opc=='2':
            print()
            if len(lista_disciplinas)>0:
                print('---> DISCIPLINAS CADASTRADAS:')
                for i, j in enumerate(lista_disciplinas):
                    print("{}){}".format(i+1, j))
                print()
                print("{})Voltar".format(0))
                print()
                print("Digite apenas o número que representa opção.")
                print()
                num_disci = str(input(" :"))
                try:
                    num_disci = int(num_disci)
                    if num_disci == 0:
                        print()
                    elif num_disci<0:
                        print()
                        print("---> Não digite números negativos. <---")
                        print()
                        input("---> Pressione ENTER para continuar.")
                        print()
                    elif num_disci>0:
                        if len(dici_listas_notas) > 0:
                            del lista_disciplinas[num_disci - 1]
                            try:
                                for a in dici_listas_notas:
                                    del dici_listas_notas[a][num_disci-1]
                            except:
                                print("DEU ERRO")


                        else:
                            del lista_disciplinas[num_disci-1]
                            print()
                            print("---> Disciplina excluída.")
                            print()
                            input("---> Pressione ENTER para continuar.")
                            print()
                    else:
                        print()
                        print("---> Error <---")
                        print()
                        input("---> Pressione ENTER para continuar.")
                        print()
                except:
                    print()
                    print('---> Error <---')
                    print()
                    input("---> Pressione ENTER para continuar.")
                    print()
            else:
                print()
                print("---> Não existe disciplina cadastrada. ")
                print()
                input("---> Pressione ENTER para continuar.")
                print()
        elif opc=='3':
            break
        else:
            print()
            print('Digite apenas 1,2 ou 3.')
            print()
            input("---> Pressione ENTER para continuar.")
            print()


    return lista_disciplinas

'''----------------------------------------------------------------------------'''
def isnumber(value):
    try:
         float(value)
    except ValueError:
         return False
    return True

'''---------------------------------------------------------------------------------'''

def isnumber1(value):
    try:
         int(value)
    except ValueError:
        return False
    return True

'''---------------------------------------------------------------------------------'''
def modificar_aluno(lista_disciplinas,dici_mat_nome,dici_listas_notas):
    '''Função modifica aluno.'''
    while True:
        print('------------- Opção atual: ADICIONAR/EXCLUIR NOTAS  ------------')
        print()
        print("1)Cadastrar nota"
              "\n2)Excluir nota"
              "\n\n3)Menu inicial")
        print()
        opc = str(input("Digite a opção desejada(1,2 ou 3):"))

        if opc=="1":
            cont2 = 0
            for k in dici_listas_notas:
                if isnumber1(k):
                    cont2 = cont2 + 1
            if cont2>0:
                print()
                while True:
                    matricula1 = str(input("Digite o número da matrícula:"))
                    try:
                        matricula1=int(matricula1)
                        if matricula1 <1000 or matricula1>9999:
                            print()
                            print("---> Digite um número de matricula válido.(XXXX)")
                            print()
                            input("---> Pressione ENTER para continuar.")
                            print()

                        else:
                            print()
                            break
                    except:
                        print()
                        print("--->Digite um número de matricula válido.")
                        print()
                        input("---> Pressione ENTER para continuar.")
                        print()

                if matricula1 in dici_listas_notas:
                    while True:
                        print("---> Disciplinas cadastradas:")
                        print()
                        for j,i in enumerate(lista_disciplinas):
                            print("-> {} ) {}".format(j+1,i))
                        print("\n-> 0 ) Voltar")
                        print()
                        disci=str(input("---> Digite a opção desejada:"))
                        print()
                        try:
                            disci=int(disci)
                            if disci==0:
                                print()
                                break
                            elif disci<0:
                                print()
                                print("---> Digite um inteiro maior que 0.")
                                print()
                                input("---> Pressione ENTER para continuar.")
                                print()
                            elif disci>(j+1):
                                print()
                                print("--->Opção inválida.")
                                print()
                                input("---> Pressione ENTER para continuar.")
                                print()
                            else:
                                print()
                                while True:
                                    print("---> Obs: Ultilize ponto(.) para colocar nota com casas decimais. <---")
                                    print()
                                    nota=str(input("-> Digite a nota em ({}) (0 à 10):".format(lista_disciplinas[disci-1])))
                                    try:
                                        nota=float(nota)
                                        if nota<0:
                                            print()
                                            print("--> Não digite números negativos.")
                                            print()
                                            input("---> Pressione ENTER para continuar.")
                                            print()
                                        elif nota>10:
                                            print()
                                            print("---> Nota máxima ultrapassada")
                                            print()
                                            input("---> Pressione ENTER para continuar.")
                                            print()
                                        else:
                                            dici_listas_notas[matricula1][disci - 1] = nota
                                            break

                                    except:
                                        print()
                                        print("--->Digite uma nota de 0 à 10.")
                                        print()
                                        input("---> Pressione ENTER para continuar.")
                                        print()

                                print()
                                print("---> Nota ({}) cadastrada em {} para o aluno ({}).".format(nota, lista_disciplinas[disci - 1], dici_mat_nome[matricula1]))
                                print()
                                input("> Pressione ENTER para continuar.")
                                print()
                                break
                        except:
                            print()
                            print("--->Digite um número válido.")
                            print()
                            input("> Pressione ENTER para continuar.")
                            print()
                else:
                    print()
                    print("---> Matrícula não cadastrada.")
                    print()
                    input("> Pressione ENTER para continuar.")
                    print()
                    break
            else:
                print()
                print("--> Não possui alunos cadastrados.")
                print()
                input("> Pressione ENTER para continuar.")
                print()

        elif opc=='2':
            cont1=0
            for j in dici_listas_notas:
                for i in dici_listas_notas[j]:
                    if isnumber(i):
                        cont1=cont1+1
            if cont1==0:
                print()
                print("---> Não existe nota cadastrada.")
                print()
                input("-> Pressione ENTER para continuar.")
                print()
            else:
                while True:
                    matricula1 = str(input("Digite o número da matrícula:"))
                    try:
                        matricula1 = int(matricula1)
                        if matricula1 < 1000 or matricula1 > 9999:
                            print()
                            print("---> Digite um número de matricula válido.(XXXX)")
                            print()
                            input("---> Pressione ENTER para continuar.")
                            print()

                        else:
                            print()


                    except:
                        print()
                        print("Digite um número de matricula válido.")
                        print()
                        input("---> Pressione ENTER para continuar.")
                        print()

                    if matricula1 in dici_listas_notas:
                        print()
                        print("--->NOTAS CADASTRADAS EM ({}):".format(matricula1))
                        print()
                        for j, i in enumerate(dici_listas_notas[matricula1]):
                            if isnumber(i):
                                print("{}) {} : {}.".format(j+1, lista_disciplinas[j], i))
                        print("\n0)Voltar.")
                        print()
                        excluir=str(input("Qual nota deseja excluir?(Digite apenas o número que representa a opção.):"))
                        try:
                            excluir=int(excluir)
                            if excluir==0:
                                print()
                                break

                            elif excluir<0:
                                print()
                                print("---> Opção inválida.")
                                print()
                                input("---> Pressione ENTER para continuar.")
                                print()
                            elif excluir>(j+1):
                                print()
                                print("---> Opção inválida.")
                                print()
                                input("---> Pressione ENTER para continuar.")
                                print()
                                break
                            else:
                                print()
                                dici_listas_notas[matricula1][excluir - 1] = lista_disciplinas[excluir - 1]
                                print()
                                print("---> Nota excluída com sucesso.")
                                print()
                                input("---> Pressione ENTER para continuar.")
                                print()
                                break
                        except:
                            print()
                            print("---> Digite apenas inteiros.")
                            print()
                            input("---> Pressione ENTER para continuar.")
                            print()
                            break

                    else:
                        print()
                        print("---> Matrícula não cadastrada.")
                        print()
                        break

        elif opc=='3':
            print()
            break
        else:
            print()
            print("---> Opção inválida.")
            print()
            input("---> Pressione ENTER para continuar.")
            print()


    return dici_listas_notas


'''----------------------------------------------------------------------------'''


def salva(lista_disciplinas,dici_mat_nome,dici_listas_notas):

    tupla = (lista_disciplinas, dici_mat_nome,dici_listas_notas)

    with open("dados_programa.pkl", "wb") as fin:
        pickle.dump(tupla, fin)

    return 0
'''----------------------------------------------------------------------------'''


def carrega():

    with open("dados_programa.pkl", "rb") as fin:
        tupla1 = pickle.load(fin)

    return tupla1

'''----------------------------------------------------------------------------'''
def desempenho(matricula2,dici_mat_nome,dici_listas_notas,lista_disciplinas):
    lista_ranking=[]
    coloc=0
    print("---> ALUNO: {}.".format(dici_mat_nome[matricula2]))
    print()
    for j,i in enumerate(lista_disciplinas):
        for k in dici_listas_notas:
            if isnumber(dici_listas_notas[k][j]):
                lista_ranking.append(dici_listas_notas[k][j])
        lista_ranking=sorted(lista_ranking)
        lista_ranking = reversed(lista_ranking)
        for a,b in enumerate(lista_ranking):
            if dici_listas_notas[matricula2][j]==b:
                coloc=a+1
                break
        if isnumber(dici_listas_notas[matricula2][j])==False:
            print("-> Aluno {} não possui nota em {}".format(dici_mat_nome[matricula2],lista_disciplinas[j]))
        else:
            print("{} : {}° da turma com {}.".format(i,coloc,dici_listas_notas[matricula2][j]))
            if dici_listas_notas[matricula2][j] < 6:
                print()
                print("-> NOTA INFERIOR À MÉDIA 6, PRECISA MELHORAR")
                print()
        print()
        coloc=0
        lista_ranking=[]


    return 0
'''----------------------------------------------------------------------------'''
fechar = 1
conte = 0

def principal(conte,fechar):
    while fechar == 1:
        lista_disciplinas, dici_mat_nome, dici_listas_notas=carrega()
        print("----------------------------MENU---------------------------")
        print()
        print("1)Cadastrar/Modificar aluno."
              "\n2)Cadastrar/Excluir Disciplina."
              "\n3)Desempenho."
              "\n\n4)Sair.")

        opcao = str(input("\nQual opção deseja?: "))

        if opcao == '1':
            sair = 1
            quant_disciplinas = int(len(lista_disciplinas))
            print()
            if quant_disciplinas > 0:

                print('------------- Opção atual: CADASTRAR/MODIFICAR ALUNO ------------')
                print()
                print("Selecione uma opção:"
                      "\n\n1)Cadastrar/Excluir aluno."
                      "\n2)Adicionar/Excluir nota."
                      "\n\n3)Voltar")
                print()
                while sair == 1:
                    opc = str(input('(1,2 ou 3):'))
                    print()
                    if opc == '1':
                        if quant_disciplinas != 0:
                            print()
                            sair = 0
                            dici_listas_notas = cadastrar_aluno(lista_disciplinas,dici_mat_nome,dici_listas_notas)
                        else:
                            print()
                            print("É necessário cadastrar disciplinas primeiro.")
                            input("---> Pressione ENTER para continuar.")
                            print()
                            sair = 0
                    elif opc == '2':

                        sair = 0
                        dici_listas_notas=modificar_aluno(lista_disciplinas,dici_mat_nome,dici_listas_notas)
                    elif opc == '3':
                        sair = 0
                    else:
                        print("Digite 1,2 ou 3.")
                        print()
                salva(lista_disciplinas, dici_mat_nome, dici_listas_notas)
                fechar = 1
            else:
                print()
                print("É necessário cadastrar pelo menos 1 diciplina.(Opção 2)")
                print()
                input("---> Pressione ENTER para continuar.")
                print()
                salva(lista_disciplinas, dici_mat_nome, dici_listas_notas)
                fechar = 1

        elif opcao == '2':
            print()
            lista_disciplinas = cadastrar_disciplinas(lista_disciplinas, dici_listas_notas, dici_mat_nome)
            conte = 1
            print()
            salva(lista_disciplinas, dici_mat_nome, dici_listas_notas)
            fechar = 1
        elif opcao == '3':
            '''dici_listas_notas = {1911: [8.8, 'MATEMATICA', 8.9], 9111: [7.0, 5.5, 3.7], 1987: [8.8, 0.5, 8.2]}
            dici_mat_nome = {1911: "JEYSON", 9111: "JOAO", 1987: "PEDRO"}
            lista_disciplinas = ['PORTUGUES', 'MATEMATICA', 'FISICA']'''
            while True:
                matricula2 = str(input("Digite o número da matrícula:"))
                try:
                    matricula2 = int(matricula2)
                    if matricula2 < 1000 or matricula2 > 9999:
                        print()
                        print("---> Digite um número de matricula válido.(XXXX)")
                        print()
                        input("---> Pressione ENTER para continuar.")
                        print()
                        break
                    elif matricula2 in dici_mat_nome:
                        print()
                        desempenho(matricula2,dici_mat_nome,dici_listas_notas,lista_disciplinas)
                        print()
                        input("---> Pressione ENTER para continuar.")
                        print()
                        break
                    else:
                        print()
                        print()
                        print("---> Matrícula não cadastrada.")
                        print()
                        input("---> Pressione ENTER para continuar.")
                        break

                except:
                    print()
                    print("Digite um número de matricula válido.")
                    print()
                    input("---> Pressione ENTER para continuar.")
                    print()
                    break
                break

            print()
            salva(lista_disciplinas, dici_mat_nome, dici_listas_notas)
            fechar = 1

        elif opcao == '4':
            print()
            print("Obrigado, volte sempre.")
            salva(lista_disciplinas,dici_mat_nome,dici_listas_notas)
            print()
            sair = input(' Pressione enter para sair...')
            fechar = 0

        else:
            print()
            print("-Digite apenas o inteiro que corresponde a opção desejada.-")
            print()
            input("---> Pressione ENTER para continuar.")
            print()
            fechar = 1

principal(conte,fechar)