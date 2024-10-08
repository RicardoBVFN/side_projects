import json 



class crud_cadastro: 

    def menuFuncionalidadesProfissionalDeSaúde(): 

        while True:

            userChoise = str(input('\nqual funcionalidade você deseja utilizar\n\n[1] perfil\n[2] dicas saúde\n[3] sair do menu de funcionalidades\n\n'))

            try:
                userChoise = int(userChoise)

            except:
                print('\nresposta inválida, tente novamente')

            if userChoise in (1, 2, 3):
                break

            else:
                print('\nvalor inválido, tente novamente')

        return userChoise 

    def menuFuncionalidadesAdm(): 

        while True:       
        
            while True:

                userChoise = input('\nqual funcionalidade você deseja utilizar?\n\n[1] criar um usuário adiministrador\n[2] consultar um usuário cadastrado\n[3] editar seus dados de usuário\n[4] deletar um usuário\n\n')
           
                try:    
                    
                    userChoise = int(userChoise)
                    break

                except:
                    
                    print('\nresposta inválida')

            if userChoise in (1, 2, 3, 4):
                break
            
            else:

                print('\nresposta inválida, tente novamente')

        return userChoise 
    
    def menuPerfilUsuário(): 

        while True:

            userChoise = str(input('\nqual ação deseja realizar?\n\n[1] consultar os dados do seu perfil\n[2] editar o seu perfil\n[3] deletar o seu perfil\n\n'))

            try:
                userChoise = int(userChoise)

                if userChoise in (1, 2, 3):
                    break

                else:
                    print('\nvalor inválido, tente novamente')

            except:
                print('\nresposta inválida, tente novamente')

        return userChoise 
    
    def matchPerfilUsuário(userChoise, userName): 
        
        

        from classesCrudCadastros import crud_cadastro 
        classe = crud_cadastro 

        match userChoise:

            case 1:
                classe.print_user_user(userName) 

            case 2:

                classe.edição_usuário(userName) 

            case 3:
                with open('Glicode/crudCadastros.json', 'r+') as database:

                    dicCrud = json.load(database)
                    del dicCrud[userName]           
                    database.seek(0)
                    json.dump(dicCrud, database, indent=2)
                    database.truncate()
                    print('\nalterações salvas com sucesso!')

    def edição_usuário(userName): 
        
        

        from classesCrudCadastros import Inputs 
        classeInputs = Inputs 

        from classesCrudCadastros import crud_cadastro 
        classeCrud = crud_cadastro 

        with open('Glicode/crudCadastros.json', 'r+') as database:

            dicCrud = json.load(database)

            try:

                userProfile = dicCrud[userName]
                classeCrud.print_user_user(userName) 
                userChoise2 = classeCrud.menu_edição() 

                match userChoise2: 

                    case 1:
                        change = classeInputs.input_string('seu novo nome de usuário') 
                        del dicCrud[userName]
                        dicCrud[change] = userProfile

                    
                    case 2:
                        change = classeInputs.input_classe_usuario_comum() 
                        userProfile[(userChoise2 - 2)] = change
                        dicCrud[userName] = userProfile

                    case 3:
                        change = classeInputs.input_tipo_diabetes() 
                        userProfile[(userChoise2 - 2)] = change
                        dicCrud[userName] = userProfile

                    case 4:
                        change = str(input('\ndigite sua nova senha: ')).strip() 
                        userProfile[(userChoise2 - 2)] = change
                        dicCrud[userName] = userProfile

                database.seek(0)
                json.dump(dicCrud, database, indent=2)
                database.truncate()
                print('\nalterações salvas com sucesso!')

            except:
                print('\nnome de usuário alterado, faça login novamente para alterar outros dados')


    def CreateOrdinaryUser(): 

        from classesCrudCadastros import Inputs 
        classe = Inputs 

        listaIntermediária = [] 

        userName = classe.input_string('seu nome de usuário') 
        userClass = classe.input_classe_usuario_comum() 

        listaIntermediária.append(userClass) 

        match userClass: 

            case 'paciente':
                userType = classe.input_tipo_diabetes() 
                listaIntermediária.append(userType) 

            case 'profissional de saúde':
                userType = '-' 
                listaIntermediária.append(userType) 

        password = str(input('\ndigite a sua senha: ')).strip() 
        listaIntermediária.append(password) 

        with open('Glicode/crudCadastros.json', 'r+') as database:

            dicCrud = json.load(database) 

            dicCrud[userName] = listaIntermediária[:] 

            database.seek(0)

            json.dump(dicCrud, database, indent=2)
        
        listaIntermediária.clear() 

    def CreateAdmUser(): 

        from classesCrudCadastros import Inputs 
        classe = Inputs 

        listaIntermediária = [] 

        userName = classe.input_string('o nome de usuário do adiministrador') 

        userClass = 'adiministrador' 
        listaIntermediária.append(userClass) 

        userType = '-' 
        listaIntermediária.append(userType) 

        password = str(input('\ndigite a sua senha de adiministrador: ')).strip() 
        listaIntermediária.append(password) 

        with open('Glicode/crudCadastros.json', 'r+') as database:

            dicCrud = json.load(database) 

            dicCrud[userName] = listaIntermediária[:] 

            database.seek(0)

            json.dump(dicCrud, database, indent=2)
        
        listaIntermediária.clear()

    def Read(): 

        from classesCrudCadastros import Inputs 
        classeInputs = Inputs 

        from classesCrudCadastros import crud_cadastro 
        classeCrud = crud_cadastro 

        from classesCrudCadastros import Funcionalidades 
        classeFuncionalidades = Funcionalidades 

        classeCrud.print_users() 

        while True:

            userChoise = 1

            userKey = classeInputs.input_string('o nome do usuário a ser consultado') 

            with open('Glicode/crudCadastros.json', 'r') as database:

                dicCrud = json.load(database)

                if userKey in dicCrud:

                    classeCrud.print_user(userKey) 
                    break

                else:

                    print('\nusuário não encontrado em nosso banco de dados')
                    userChoise = classeFuncionalidades.verificacao_de_prossegimento('tentando', 'retornar ao menu anterior') 
                    if userChoise == 2: 
                        break
        
        if userChoise == 2: 
            return userChoise
    
    def Delete(): 
        from classesCrudCadastros import Inputs 
        classeInputs = Inputs 

        from classesCrudCadastros import Funcionalidades 
        classeFuncionalidades = Funcionalidades 

        from classesCrudCadastros import crud_cadastro 
        classeCrud = crud_cadastro 

        while True:
            userChoise = 'defoult'

            classeCrud.print_users() 
            userDel = classeInputs.input_string('o nome do usuário a ser deletado') 

            with open('Glicode/crudCadastros.json', 'r+') as database:

                dicCrud = json.load(database)

                if userDel in dicCrud:

                    del dicCrud[userDel]
                    database.seek(0)
                    json.dump(dicCrud, database, indent=2)
                    database.truncate()
                    print('\nalterações salvas com sucesso!')
                    break

                else:
                    print('\neste usuário não existe em nosso banco de dados')

                    userChoise = classeFuncionalidades.verificacao_de_prossegimento('tentando', 'retornar ao menu anterior') 

                    if userChoise == 2: 
                        break

        return userChoise

    def login():

        from classesCrudCadastros import Inputs
        classe = Inputs

        while True:

            nameLogin = classe.input_string('seu nome de usuário')

            with open('Glicode/crudCadastros.json', 'r') as database:

                dicCrud = json.load(database)

                if nameLogin in dicCrud:

                    passwordLogin = str(input('digite sua senha: ')).strip()

                    userProfile = dicCrud[nameLogin]

                    if passwordLogin == userProfile[2]:
                        return nameLogin
                    
                    else:
                        return 'defoult'
                else:
                    return 'defoult'
                
    def verificação_classe_usuário(key):

        with open('Glicode/crudCadastros.json') as database:

            dicCrud = json.load(database)

            lista = dicCrud[key]

            userClass = lista[0]

            return userClass
        
    def menu_edição():

        while True:

            userChoise = str(input('\ndigite o que você deseja alterar no perfil selecionado\n\n[1] nome de usuário\n[2] classe do usuário\n[3] tipo de diabetes\n[4] alterar senha\n\n')).strip()

            try:

                userChoise = int(userChoise)
                break

            except:
                
                print('\nvalor inválido, tente novamente')

            if userChoise in (1, 2, 3, 4):
                break

            else:
                print('\nvalor inválido, tente novamente')

        return userChoise
    
    def print_user(userName):

        import json

        with open('Glicode/crudCadastros.json') as database:

            dicCrud = json.load(database)
            userProfile = dicCrud[userName]

            print('=' * 45)
            print(f'\nnome do usuário: {userName}\nclasse do usuário: {userProfile[0]}\ntipo de diabetes: {userProfile[1]}\n')
            print('=' * 45)

    def print_user_user(userName):

        import json

        with open('Glicode/crudCadastros.json') as database:

            dicCrud = json.load(database)

            try:
                userProfile = dicCrud[userName]

                print('=' * 45)
                print(f'\nnome do usuário: {userName}\nclasse do usuário: {userProfile[0]}\ntipo de diabetes: {userProfile[1]}\nsenha: {userProfile[2]}\n')
                print('=' * 45)

            except:
                print('\nnome de usuário alterado, faça lpgin novamente para resalisar novas alterações')

    def print_users():

        contador = 0

        with open('Glicode/crudCadastros.json') as database:

            dicCrud = json.load(database)

            keysList = list(dicCrud.keys())

            print('=' * 4, 'usuários cadastrados', '=' * 4)

            for key in dicCrud:

                print(f'usuário nº{contador + 1}: {keysList[contador]}')

                contador += 1

            print('=' * 29)

class Inputs:
                
    def input_string(complemento):  

        while True:

            string = str(input(f'\ndigite {complemento}: ')).strip().upper()

            if string != '':
                break

            print('\nfrase inválida, tente novamente')
        return string
    
    def input_float(complemento):

        while True:

            userNumber = str(input(f'\ndigite {complemento}: ')).strip()

            try:
                userNumber = float(userNumber)
                break

            except:
                print('\nvalor inválido, tente novamente')

        return userNumber

    def input_classe_usuario_comum():  

        while True:

            classe_usuário = str(input('\ndigite o seu tipo de usuário\n\n[1] paciente\n[2] profissional de saúde\n\n')).strip()

            try:
                classe_usuário = int(classe_usuário)

                if classe_usuário in (1, 2):
                    break

                else:
                    print('\nvalor inválido, tente novamente')

            except:
                print('\nresposta inválida, tente novamente')
                    
        match classe_usuário:

            case 1:
                return 'paciente'
            
            case 2:
                return 'profissional de saúde'
            
    def input_tipo_diabetes():  

        while True:

            tipo = str(input("\nInsira seu tipo de diabetes: \n \n[1] diabetes tipo 1\n[2] diabetes tipo 2\n[3] diabetes gestacional\n[4] pré diabetes\n\n")).strip()

            try:
                tipo = int(tipo)

            except:
                print('\nresposta inválida, tente novamente')

            if tipo in (1, 2, 3, 4):
                break

        match tipo:

            case 1:
                return 'diabetes tipo 1'
            
            case 2:
                return 'diabetes tipo 2'
            
            case 3:
                return 'diabetes gestacional'
            
            case 4:
                return 'pré diabetes'
            
class Funcionalidades:
    def main_remedinhos():
        import json, time, os

        def limpar_tela():
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')

        def carregar_json():
            global medicamentos  
            try:
                with open('crus.py/dados.json', 'r') as file:
                    medicamentos = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                medicamentos = []

        def salvar_json():
            objeto_json = json.dumps(medicamentos, indent=4)
            with open('crus.py/dados.json', 'w') as file:
                file.write(objeto_json)

        def adicionar_medicamentos():
            nome = input("Informe o nome do medicamento >>>> ")
            horario = input("Informe o horario que você irá tomar esse medicamento (HH:MM) >>>> ")
            dosagem = input("Informe a dosagem do medicamento >>>> ")
            medicamento = {
                'Nome': nome,
                'Horario': horario,
                'Dosagem': dosagem        
            }
            medicamentos.append(medicamento)
            salvar_json()

        def visualizar_medicamentos_menu():
            if not medicamentos:
                print("\nNenhum medicamento cadastrado!! (PRECIONE [ENTER] PARA CONTINUAR)")
            for num, medicamento in enumerate(medicamentos, start=1):
                print(f"\n{num}. Nome: {medicamento['Nome']}, Horario: {medicamento['Horario']}, Dosagem: {medicamento['Dosagem']}\n")
            print("Digite [sair] para parar de visualizar")
            opcao = input(">>> ")
            if opcao.lower() == 'sair':
                return

        def visualizar_medicamentos():
            if not medicamentos:
                print("\nNenhum medicamento cadastrado!! (PRECIONE [ENTER] PARA CONTINUAR)")
            for num, medicamento in enumerate(medicamentos, start=1):
                print(f"\n{num}. Nome: {medicamento['Nome']}, Horario: {medicamento['Horario']}, Dosagem: {medicamento['Dosagem']}\n")

        def atualizar_medicamento():
            visualizar_medicamentos()
            indice = int(input("\nInforme o indice do medicamento que voce deseja atualizar [0] PARA VOLTAR AO MENU >>>> ")) - 1
            if 0 <= indice < len(medicamentos):
                nome = input("\nInforme o novo nome do medicamento >>>> ")
                horario = input("\nInforme o novo horario que você irá tomar esse medicamento (HH:MM) >>>> ")
                dosagem = input("\nInforme a nova dosagem do medicamento >>>> ")
                medicamentos[indice]['Nome'] = nome
                medicamentos[indice]['Horario'] = horario
                medicamentos[indice]['Dosagem'] = dosagem
                salvar_json()
                print("Atualizado...")
                time.sleep(3)
                limpar_tela()
            elif indice == -1:
                print("Voltando ao menu principal...")
                time.sleep(2)
                limpar_tela()
                return
            else:
                print("Indice Invalido!")
                time.sleep(3)
                limpar_tela()

        def deletar_medicamento():
            visualizar_medicamentos()
            indice = int(input("Informe o numero do medicamento que voce deseja excluir >>>> ")) - 1
            if 0 <= indice < len(medicamentos):
                medicamentos.pop(indice)
                salvar_json()
                print("Excluido...")
                time.sleep(2)
                print("Excluido com sucesso!")
            else:
                print("Indice invalido...")

        def main_remedios():
            carregar_json()
            while True:
                limpar_tela()
                print("\n\n[1] Adicionar Medicamento")
                print("[2] Visualizar Medicamento")
                print("[3] Atualizar Medicamento")
                print("[4] Remover Medicamento")
                print("[5] Sair")
                try:
                    opcao = int(input("\nescolha uma opcao>>>> "))
                    match opcao:
                        case 1:
                            limpar_tela()
                            adicionar_medicamentos()
                        case 2:
                            limpar_tela()
                            visualizar_medicamentos_menu()
                        case 3:
                            limpar_tela()
                            atualizar_medicamento()
                        case 4:
                            limpar_tela()
                            deletar_medicamento()
                        case 5:
                            limpar_tela()
                            print("Voltando ao menu Principal")
                            time.sleep(3)
                            break
                        case _:
                            print("\nOpcao Invalidada, tente novamente...")
                except ValueError:
                    limpar_tela()
                    print("Opcao invalida! Informe outra opcao...")
                    time.sleep(3)

        main_remedios()
    
    def dicas_saude():
       
        import json


        def main():
                 while True:
                                print("\n=== Dicas para um estilo de vida saudável ===")
                                print("1. Exibir dicas")
                                print("2. Voltar para menu principal")
                                opcao = input("Selecione uma opção: ")


                                if opcao == "1":
                                    exibir_dicas()


                                elif opcao == "2":
                               
                                    break
                                else:
                                    print("Opção inválida. Tente novamente.")
                       




     
       
        def exibir_dicas():
            dicass = (
                        "1. Alimentação Balanceada: Priorize alimentos ricos em \n fibras, como frutas, legumes, grãos integrais e proteínas magras. \n Evite alimentos processados, ricos em açúcar e carboidratos refinados.\n \n-------------------------------------------------------------------------"
                        "\n2. Controle de Porções: Monitore o tamanho das porções \n para controlar a ingestão de carboidratos e calorias. Isso ajuda a manter os \n níveis de glicose no sangue estáveis.\n\n------------------------------------------------------------------------"
                        "\n3. Refeições Regulares: Mantenha um horário regular para \n as refeições e evite pular refeições. Isso ajuda a evitar picos e quedas nos \n níveis de açúcar no sangue.\n\n-------------------------------------------------------------------------"
                        "\n4. Monitoramento da Glicose: Meça regularmente os níveis \n de glicose no sangue para entender como os alimentos, atividades e medicamentos \n afetam seus níveis de açúcar no sangue.\n\n-------------------------------------------------------------------------"
                        "\n5. Exercício Regular: Pratique atividades físicas regularmente,\n  como caminhada, natação ou ioga. O exercício ajuda a controlar o \n açúcar no sangue, reduzir o peso e melhorar a sensibilidade à insulina.\n\n-------------------------------------------------------------------------"
                        "\n6. Hidratação Adequada: Beba bastante água ao longo do \n dia para ajudar na digestão, manter a hidratação e controlar o apetite.\n\n-------------------------------------------------------------------------"
                        "\n7. Gestão do Estresse: Encontre maneiras saudáveis de \n lidar com o estresse, como meditação, ioga, hobbies ou conversando com amigos \n e familiares.\n\n-------------------------------------------------------------------------"
                        "\n8. Sono de Qualidade: Priorize o sono adequado e \n consistente todas as noites. O sono insuficiente pode afetar negativamente \n  os níveis de açúcar no sangue e a sensibilidade à insulina.\n\n-------------------------------------------------------------------------"
                        "\n9. Evitar o Tabagismo e o Álcool em Excesso: O tabagismo e o consumo excessivo de álcool \n podem piorar os problemas de saúde associados ao diabetes.\n  Evite-os ou limite seu uso.\n\n-------------------------------------------------------------------------"
                        "\n10. Consulta Médica Regular: Mantenha consultas regulares \n  com seu médico e equipe de saúde para monitorar seu diabetes,\n ajustar o plano de tratamento conforme necessário e receber apoio e orientação.\n------------------------------------------------------------------------"
                             
 )          


            print(dicass)
           
             
           






        main()

    
        
    def verificacao_nivel_glicose(glicose):

        if glicose <= 70:
            print("\nvocê está em estado de Hipoglicemia, procure ajuda assim que possível")

        elif 70 < glicose <= 150:
            print("\nGlicose dentro do intervalo ideal")

        elif 150 < glicose <= 300:
            print("\nGlicose acima do intervalo ideal, recomenda-se a adoção de uma medida preventiva assim que possível")

        else:
            print("\n você está em estado de Hiperglicemia, faça uso da dose adequada de insulina asim que possível")

    def calculador_quant_insulina(glicose, qtd_carbo):  

        fator_correcao = 50
        glicemia_alvo = 100
        razao_carbo = 15

        unidades_insulina = (((glicose - glicemia_alvo) / fator_correcao) + (qtd_carbo / razao_carbo))

        return unidades_insulina

    def formatacao_unidades_de_isulina(unidades_insulina):  

        import math

        insulina_inteiro = math.trunc(unidades_insulina)

        if (unidades_insulina - insulina_inteiro) == 0:
            insulina_print = unidades_insulina

        elif (unidades_insulina - insulina_inteiro) > 0 and (unidades_insulina - insulina_inteiro) < 0.5:
            insulina_print = math.floor(unidades_insulina)

        elif (unidades_insulina - insulina_inteiro) > 0.5:
            insulina_print = math.ceil(unidades_insulina)

        return insulina_print

    def monitoramento_consulta():  
        data_ultima_consulta = str(input('\ndigite a data da sua última consulta médica (ex: 01/01/2001): ')).strip()

        dia_ultima_consulta = int(data_ultima_consulta[:2])
        mes_ultima_consulta = int(data_ultima_consulta[3:5])
        ano_ultima_consulta = int(data_ultima_consulta[6:10])

        data_atual = '21/05/2024'

        dia_atual = int(data_atual[:2])
        mes_atual = int(data_atual[3:5])
        ano_atual = int(data_atual[6:10])

        if ((dia_ultima_consulta - dia_atual)**2 + ((mes_ultima_consulta - mes_atual) * 30)**2 + ((ano_ultima_consulta - ano_atual) * 365)**2) > 180 ** 2:
            print('\nparece que faz muito tempo desde a sua última consulta, vá imadiatamente consular o seu médico')

        elif ((dia_ultima_consulta - dia_atual)**2 + ((mes_ultima_consulta - mes_atual) * 30)**2 + ((ano_ultima_consulta - ano_atual) * 365)**2) > 90 ** 2:
            print('\nparece que faz um tempo desde a sua última consulta, é recomendado que você volte para uma nova conúlta com o seu médico responsável')

        else:
            print('\nparece que você ainda está dentro do prazo recomendado, continue com um bom acompanhamento')

    def calculadora_alimentos():  
        json_file = "alimentos.json"

        try:
            with open('crus.py/json_alimentos', "r") as arquivo:
                alimentos = json.load(arquivo)
        except FileNotFoundError:
            alimentos = []

        def salvar_alimentos():
            with open('crus.py/json_alimentos', "w") as arquivo:
                json.dump(alimentos, arquivo, ensure_ascii=False, indent=4)

        def adicionar_alimento():
            print("1 - Arroz\n2 - Macarrão\n3 - Feijão\n4 - Uva\n5 - Batata Inglesa")
            alimento = input("Qual alimento você vai consumir? ")
            qtd_alimento = int(input("Qual a porção desse alimento a ser consumida em gramas? "))
            qtd_carboidratos = int(input("Qual a quantidade de carboidratos em 100 gramas desse alimento? "))
            calculo_carbos = (qtd_carboidratos / 100) * qtd_alimento
            alimentos.append({"Nome": alimento, "Carboidratos": calculo_carbos})
            print("a quantidade de carboidratos nesse alimento é:",calculo_carbos)
            salvar_alimentos()
            print(f"O alimento '{alimento}' foi adicionado à lista.")

        def exibir_alimentos():
            if alimentos:
                print("\nLista de Alimentos:")
                for i, alimento in enumerate(alimentos, start=1):
                    print(f"{i}. {alimento['Nome']} - Carboidratos: {alimento['Carboidratos']}g")
            else:
                print("A lista de alimentos está vazia.")

        def buscar_alimento():
            nome_alimento = input("Qual alimento você deseja procurar? ").strip()
            encontrado = False
            for alimento in alimentos:
                if alimento["Nome"].lower() == nome_alimento.lower():
                    print(f"Alimento encontrado: {alimento['Nome']}")
                    encontrado = True
                    break
            if not encontrado:
                print(f'{nome_alimento} não encontrado na lista.')

        def remover_alimento():
            exibir_alimentos()
            if alimentos:
                indice = int(input("Digite o número do alimento que deseja remover: "))
                if 1 <= indice <= len(alimentos):
                    alimento_removido = alimentos.pop(indice - 1)
                    salvar_alimentos()
                    print(f"O alimento '{alimento_removido['Nome']}' foi removido da lista.")
                else:
                    print("Número inválido.")
            else:
                print("A lista de alimentos está vazia.")

        while True:
            print("\nMenu:")
            print("1. Adicionar alimento")
            print("2. Exibir lista de alimentos")
            print("3. Buscar alimento na lista")
            print("4. Remover alimento")
            print("5. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                adicionar_alimento()
            elif opcao == "2":
                exibir_alimentos()
            elif opcao == "3":
                buscar_alimento()
            elif opcao == "4":
                remover_alimento()
            elif opcao == "5":
                print("Encerrando o programa")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

    def agendamento_consultas():
        from time import sleep
        arquivo = 'crus.py/consultas.json'

        def carregar_dados():
            try:
                with open(arquivo, 'r') as file:
                    return json.load(file)
            except FileNotFoundError:
                return []
            except json.JSONDecodeError:
                return []
        def salvar_dados(dados):
            with open(arquivo, 'w') as file:
                json.dump(dados, file, indent=4)

        def add_consulta():
            cpf_paciente = input('Informe o CPF do paciente: ')
            nome_paciente = input('Informe o nome do paciente: ')
            data_consulta = input('Informe a data da consulta (dd/mm/aa): ')
            hora_consulta = input('Informe a hora da sua consulta (hh/mm): ')

            nova_consulta = {
                "cpf": cpf_paciente,
                "nome": nome_paciente,
                "data": data_consulta,
                "hora": hora_consulta
            }

            consultas = carregar_dados()
            consultas.append(nova_consulta)
            salvar_dados(consultas)
            print('CONSULTA ADICIONADA COM SUCESSO!')

        def listar_consulta():
            consultas = carregar_dados()

            if consultas:
                for consulta in consultas:
                    print(f"CPF: {consulta['cpf']}, Paciente: {consulta['nome']}, Data: {consulta['data']}, Hora: {consulta['hora']}")
            else:
                print('NENHUMA CONSULTA ENCONTRADA')

        def atualizar_consulta():
            cpf_paciente = input("Digite o CPF da consulta a ser atualizada: ")
            consultas = carregar_dados()
            encontrado = False

            for consulta in consultas:
                if consulta['cpf'] == cpf_paciente:
                    consulta['cpf'] = input("Digite o novo CPF: ")
                    consulta['nome'] = input("Digite o novo nome do paciente: ")
                    consulta['data'] = input(
                        "Digite a nova data da consulta (DD/MM/AAAA): ")
                    consulta['hora'] = input(
                        "Digite a nova hora da consulta (HH:MM): ")
                    encontrado = True
                    break

            if encontrado:
                salvar_dados(consultas)
                print("CONSULTA ATUALIZADA COM SUCESSO!")
            else:
                print("CONSULTA NÃO ENCONTRADA.")

        def excluir_consulta():
            cpf_paciente = input('Digite o CPF a ser excluído: ')
            consultas = carregar_dados()
        
            consultas_atualizadas = [consulta for consulta in consultas if consulta['cpf'] != cpf_paciente]  

            if len(consultas) != len(consultas_atualizadas):
                salvar_dados(consultas_atualizadas)
                print("CONSULTA EXCLUÍDA COM SUCESSO!")
            else:
                print("CONSULTA NÃO ENCONTRADA.")

        def main():
            while True:
                print("\nEscolha uma opção:")
                print("1. Adicionar consulta")
                print("2. Listar consultas")
                print("3. Atualizar consulta")
                print("4. Excluir consulta")
                print("5. Sair")
                opcao = input("Opção: ")


                if opcao == '1':
                    add_consulta()
                elif opcao == '2':
                    listar_consulta()
                elif opcao == '3':
                    atualizar_consulta()
                elif opcao == '4':
                    excluir_consulta()
                elif opcao == '5':
                    print('Saindo..')
                    sleep(2)
                    break
                else:
                    print("Opção inválida! Tente novamente.")

        main()
       
    def menu_funcionalidades_paciente():  

        while True:
            user_choise = str(input('\nselecione a funcionalidade que você deseja utilizar\n\n[1] perfil\n[2] calculadora de carboidratos\n[3] calculadora de alimentos\n[4] situação da glicemia\n[5] monitoramento de  consultas\n[6] agendamento de consultas\n[7] dicas\n[8] diario remédios\n[9] retornar ao menu anterior\n\n')).strip()
            
            try:
                user_choise = int(user_choise)

            except:
                print('\nfrase inválida, tente novamente')

            if user_choise in (1, 2, 3, 4, 5, 6, 7, 8, 9):
                break


        return user_choise

    def verificacao_de_prossegimento(complemento_pergunta, complemento_negacao):  

        while True:

            verificacao = str(input(f'\ndeseja continuar {complemento_pergunta}?\n\n[1] sim\n[2] não, {complemento_negacao}\n\n')).strip()

            try:
                verificacao = int(verificacao)

            except:
                print('\nresposta inválida, tente novamente')

            if verificacao in (1, 2):
                break

            else:
                print('\nvalor inválido, tente novamente')


        return verificacao

    def match_funcionalidades_pacientes(user_choise, userName):

        from classesCrudCadastros import Inputs
        classeInputs = Inputs

        from classesCrudCadastros import crud_cadastro
        classeCrud = crud_cadastro

        from classesCrudCadastros import Funcionalidades
        classeFuncionalidades = Funcionalidades

        match user_choise:

            case 1:
                escolha = classeCrud.menuPerfilUsuário()

                classeCrud.matchPerfilUsuário(escolha, userName)

            case 2:

                glicose = classeInputs.input_float('sua glicemia')
                qtd_carbo = classeInputs.input_float('sua quantidade de carboidratos')

                unidades_insulina = classeFuncionalidades.calculador_quant_insulina(glicose, qtd_carbo)

                insulina_print = classeFuncionalidades.formatacao_unidades_de_isulina(unidades_insulina)

                print(f"A quantidade de insulina a ser tomada é: {insulina_print}Ul")

            case 3:

                classeFuncionalidades.calculadora_alimentos()

            case 4:

                glicemia = classeInputs.input_float('sua glicemia')

                classeFuncionalidades.verificacao_nivel_glicose(glicemia)

            case 5:

                classeFuncionalidades.monitoramento_consulta()
            
            case 6:

                classeFuncionalidades.agendamento_consultas()
            
            case 7:

                classeFuncionalidades.dicas_saude()

            case 8:

                classeFuncionalidades.main_remedinhos()
            