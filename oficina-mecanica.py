def gravar_dados(nome_arquivo, dicionario):
    ref_arq = open(nome_arquivo, 'w', encoding="utf-8")
    for chave in dicionario.keys():
        linha = ''
        linha += chave + ';'
        for item in dicionario[chave]:
            for j in item:
                linha+=j+';'       
        linha += '\n'
        ref_arq.write(linha)
    ref_arq.close()

def gravar_dados_con(nome_arquivo, dicionario):
    ref_arq = open(nome_arquivo, 'w', encoding="utf-8")
    for chave in dicionario:
        linha = ''
        for elemento in chave:
            linha += elemento + ';'
        for item in dicionario[chave]:
            for j in item:
                linha+=j+';'
        linha+='\n'
        ref_arq.write(linha)
    ref_arq.close()

def existe_arquivo(nome_arquivo):
    import os
    if os.path.exists(nome_arquivo):
        return True #Retorna Verdadeiro, quando encontra o arquivo
    else:
        return False #Retorna falso, quando não encontra o arquivo
    
def ler_arquivo_mec(nome_arquivo):
    dicionario = {}
    ems = '@'
    if existe_arquivo(nome_arquivo):
        ref_arq = open(nome_arquivo, 'r', encoding="utf-8")
        for linha in ref_arq:
            emails = []
            telefones = []
            achou = False
            if linha != '\n':
                linha = linha.split(';')
                chave = linha[0]
                dicionario[chave] = []
                i = 1
                while i in range(len(linha)):
                    if linha[i] != '\n' and achou == False and ems not in linha[i]:
                        lista = []
                        lista.append(linha[i])
                        dicionario[chave].append(lista)
                    elif ems in linha[i]:
                        achou = True
                        new_str = ''
                        j = 0
                        while j < len(linha[i]):
                            if linha[i][j] != '\n':
                                new_str+=linha[i][j]
                                j+=1
                                if j == len(linha[i]):
                                    emails.append(new_str)
                    elif linha[i] != '\n' and achou == True:
                        new_str = ''
                        k = 0
                        while k < len(linha[i]):
                            if linha[i][k] != '\n':
                                new_str+=linha[i][k]
                            k+=1
                        telefones.append(new_str)
                    i+=1
                dicionario[chave].append(emails)
                dicionario[chave].append(telefones)
        ref_arq.close()
    return dicionario

def ler_arquivo_vei(nome_arquivo):
    dicionario = {}
    if existe_arquivo(nome_arquivo):
        ref_arq = open(nome_arquivo, 'r', encoding="utf-8")
        for linha in ref_arq:
            if linha != '\n':
                linha = linha.split(';')
                chave = linha[0]
                dicionario[chave] = []
                i = 1
                while i in range(len(linha)):
                    if linha[i] != '\n':
                        lista = []
                        lista.append(linha[i])
                        dicionario[chave].append(lista)
                    i+=1
        ref_arq.close()
    return dicionario

def ler_arquivo_con(nome_arquivo):
    dicionario = dict()
    if existe_arquivo(nome_arquivo):
        ref_arq = open(nome_arquivo, 'r', encoding="utf-8")
        for linha in ref_arq:
            if linha != '\n':
                linha = linha.split(';')
                chave = ()
                cpf = linha[0]
                chave+=(cpf,)
                placa = linha[1]
                chave+=(placa,)
                data_entrada = linha[2]
                chave+=(data_entrada,)
                dicionario[chave] = []
                i = 3
                while i in range(len(linha)):
                    if linha[i] != '\n':
                        lista = []
                        lista.append(linha[i])
                        dicionario[chave].append(lista)
                    i+=1
        ref_arq.close()
    return dicionario

def icluir_mec(mecanicos):
    chave = input('Digite o CPF do mecânico para iniciar o cadastro (sem pontuações): ')
    if chave not in mecanicos:
        i = 0
        lista = []
        telefones = []
        emails = []
        while i < 6:
            if i == 0:
                nome = input('Nome: ').upper()
                lista.append([nome])
                i+=1
            elif i == 1:
                nascimento = input('Data de Nascimento no formato DD/MM/AAAA: ')
                lista.append([nascimento])
                i+=1
            elif i == 2:
                sexo = input('Sexo: ').upper()
                lista.append([sexo])
                i+=1
            elif i == 3:
                salario = input('Salário: ').upper()
                lista.append([salario])
                i+=1
            elif i == 4:
                email = input('E-mail: ')
                emails.append(email)
                x = 'S'
                while x == 'S':
                    x = input('Deseja adicionar mais um e-mail? Digite "s" para sim e "n" para não: ').upper()
                    if x == 'S':
                        email = input('E-mail: ')
                        emails.append(email)
                    else:
                        lista.append(emails)
                        i+=1
            elif i == 5:
                telefone = input('Telefone: ')
                telefones.append(telefone)
                x = 'S'
                while x == 'S':
                    x = input('Deseja adicionar mais um telefone? Digite "s" para sim e "n" para não: ').upper()
                    if x == 'S':
                        telefone = input('Telefone: ')
                        telefones.append(telefone)
                    else:
                        lista.append(telefones)
                        i+=1
        mecanicos[chave] = lista
        return True
    else:
        return False

def icluir_vei(veiculos):
    chave = input('Digite a placa do veículo para iniciar o cadastro: ').upper()
    if chave not in veiculos:
        i = 0
        lista = []
        while i < 7:
            if i == 0:
                tipo = input('Tipo: ').upper()
                lista.append([tipo])
                i+=1
            elif i == 1:
                marca = input('Marca: ').upper()
                lista.append([marca])
                i+=1
            elif i == 2:
                modelo = input('Modelo: ').upper()
                lista.append([modelo])
                i+=1
            elif i == 3:
                ano = input('Ano: ')
                lista.append([ano])
                i+=1
            elif i == 4:
                portas = input('Portas: ')
                lista.append([portas])
                i+=1
            elif i == 5:
                combustivel = input('Combustível: ').upper()
                lista.append([combustivel])
                i+=1
            elif i == 6:
                cor = input('Cor: ').upper()
                lista.append([cor])
                i+=1
        veiculos[chave] = lista
        return True
    else:
        return False

def icluir_con(consertos, mecanicos, veiculos):
    cpf = input('Insira o CPF do mecânico (sem pontuações): ')
    if cpf in mecanicos:
        tupla = ()
        tupla+=(cpf,)
        placa = input('Insira a placa do carro: ').upper()
        if placa in veiculos:
            tupla+=(placa,)
            data_entrada = input('Insira a data de entrada (no formato DD/MM/AAAA): ')
            tupla+=(data_entrada,)
            if tupla not in consertos:
                i = 0
                lista = []
                while i < 3:
                    if i == 0:
                        data_saida = input('Data de saída: ')
                        lista.append([data_saida])
                        i+=1
                    elif i == 1:
                        descricao = input('Descrição dos problemas: ').upper()
                        lista.append([descricao])
                        i+=1
                    elif i == 2:
                        valor = input('Valor do conserto: ').upper()
                        lista.append([valor])
                        i+=1
                consertos[tupla] = lista
                return True
            else:
                return False  
        else:
            print('-- Veículo não encontrado.')
    else:
        print('-- CPF do mecânico não encontrado.')

def listar_todos_mec(mecanicos):
    if len(mecanicos) != 0:
        for item in mecanicos:
            i = 0
            print('')
            print('CPF do mecânico: {}'.format(item))
            elementos = mecanicos[item]
            while i < len(elementos):
                if i == 0:
                    for h in elementos[i]:
                        print('Nome: ', h, end='')
                        print('')
                        i+=1
                elif i == 1:
                    for h in elementos[i]:
                        print('Data de Nascimento: ', h, end='')
                        print('')
                        i+=1
                elif i == 2:
                    for h in elementos[i]:
                        print('Sexo: ', h, end='')
                        print('')
                        i+=1
                elif i == 3:
                    for h in elementos[i]:
                        print('Salário: ', h, end='')
                        print('')
                        i+=1
                elif i == 4:
                        print('E-mails: ', end=' - ')
                        for h in elementos[i]:
                            print(h, end=' - ')
                        i+=1
                        print('')
                elif i == 5:
                        print('Telefones: ', end=' - ')
                        for h in elementos[i]:
                            print(h, end=' - ')
                        i+=1
                        print('')
    else:
        print('-- Não há mecânicos cadastrados.')

def listar_todos_vei(veiculos):
    if len(veiculos) != 0:
        for item in veiculos:
            i = 0
            print('')
            print('Placa do veículo: {}'.format(item))
            elementos = veiculos[item]
            while i < len(elementos):
                if i == 0:
                    for h in elementos[i]:
                        print('Tipo: ', h, end='')
                        print('')
                        i+=1
                elif i == 1:
                    for h in elementos[i]:
                        print('Marca: ', h, end='')
                        print('')
                        i+=1
                elif i == 2:
                    for h in elementos[i]:
                        print('Modelo: ', h, end='')
                        print('')
                        i+=1
                elif i == 3:
                    for h in elementos[i]:
                        print('Ano: ', h, end='')
                        print('')
                        i+=1
                elif i == 4:
                    for h in elementos[i]:
                        print('Portas: ', h, end='')
                        i+=1
                        print('')
                elif i == 5:   
                    for h in elementos[i]:
                        print('Combustível: ', h, end='')
                        i+=1
                        print('')
                elif i == 6:
                    for h in elementos[i]:
                        print('Cort: ', h, end='')
                        print('')
                        i+=1
    else:
        print('-- Não há mecânicos cadastrados.')

def listar_todos_con(consertos):
    if len(consertos) != 0:
        for item in consertos:
            i = 0
            print('')
            print('CPF do mecânico responsável pelo conserto: {}'.format(item[0]))
            print('Placa do veículo: {}'.format(item[1]))
            print('Data de entrada: {}'.format(item[2]))
            elementos = consertos[item]
            while i < len(elementos):
                if i == 0:
                    for h in elementos[i]:
                        print('Data de saída: ', h, end='')
                        print('')
                        i+=1
                elif i == 1:
                    for h in elementos[i]:
                        print('Descrição dos problemas: ', h, end='')
                        print('')
                        i+=1
                elif i == 2:
                    for h in elementos[i]:
                        print('Valor do conserto: ', h, end='')
                        print('')
                        i+=1
    else:
        print('-- Não há consertos cadastrados.')

def listar_um_mec(mecanicos):
    cpf = input('Digite o CPF do mecânico para checar suas informações (sem pontuações): ')
    if cpf in mecanicos:
        mecanico = mecanicos[cpf]
        i = 0
        while i < len(mecanico):
            if i == 0:
                for j in mecanico[i]:
                    print('Nome: ', j, end='')
                    print('')
                    i+=1
            elif i == 1:
                for j in mecanico[i]:
                    print('Data de Nascimento: ', j, end='')
                    print('')
                    i+=1
            elif i == 2:
                for j in mecanico[i]:
                    print('Sexo: ', j, end='')
                    print('')
                    i+=1
            elif i == 3:
                for j in mecanico[i]:
                    print('Salário: ', j, end='')
                    print('')
                    i+=1
            elif i == 4:
                    print('E-mails: ', end=' - ')
                    for j in mecanico[i]:
                        print(j, end=' - ')
                    i+=1
                    print('')
                    
            elif i == 5:
                    print('Telefones: ', end=' - ')
                    for j in mecanico[i]:
                        print(j, end=' - ')
                    print('')
                    i+=1

def listar_um_vei(veiculos):
    placa = input('Digite a placa do veículo para checar suas informações: ').upper()
    if placa in veiculos:
        veiculo = veiculos[placa]
        i = 0
        while i < len(veiculo):
            if i == 0:
                for j in veiculo[i]:
                    print('Tipo: ', j, end='')
                    print('')
                    i+=1
            elif i == 1:
                for j in veiculo[i]:
                    print('Marca: ', j, end='')
                    print('')
                    i+=1
            elif i == 2:
                for j in veiculo[i]:
                    print('Modelo: ', j, end='')
                    print('')
                    i+=1
            elif i == 3:
                for j in veiculo[i]:
                    print('Ano: ', j, end='')
                    print('')
                    i+=1
            elif i == 4:
                for j in veiculo[i]:
                    print('Portas: ', j, end='')
                    i+=1
                    print('')        
            elif i == 5:
                for j in veiculo[i]:
                    print('Combustível: ', j, end='')
                    print('')
                    i+=1
            elif i == 6:
                for j in veiculo[i]:
                    print('Cor: ', j, end='')
                    print('')
                    i+=1
    else:
        print('-- Placa não encontrada.')

def listar_um_con(consertos):
    tupla = ()
    cpf = input('Insira o CPF do mecânico (sem pontuações): ')
    tupla+=(cpf,)
    placa = input('Insira a placa do carro: ').upper()
    tupla+=(placa,)
    data_entrada = input('Insira a data de entrada (no formato DD/MM/AAAA): ')
    tupla+=(data_entrada,)
    if tupla in consertos:
        conserto = consertos[tupla]
        i = 0
        while i < len(conserto):
            if i == 0:
                for j in conserto[i]:
                    print('Data de Saída: ', j, end='')
                    print('')
                    i+=1
            elif i == 1:
                for j in conserto[i]:
                    print('Descrição dos Problemas: ', j, end='')
                    print('')
                    i+=1
            elif i == 2:
                for j in conserto[i]:
                    print('Valor do Conserto: ', j, end='')
                    print('')
                    i+=1
    else:
        print('-- Não existe conserto cadastrado com esses dados.')
                
def alt_exc_mec(dicionario):
    opt = int(input('Digite 1 para alterar ou 2 para excluir um elemento: '))
    chave = input('Insira o CPF do mecânico: ')
    if chave in dicionario:
        elemento = int(input(' 1. Nome \n 2. Data de Nascimento \n 3. Sexo \n 4. Salário \n 5. E-mails \n 6. Telefones \n Insira o número da opção que deseja alterar ou excluir: '))
        if opt == 1:
            if elemento == 1:
                del dicionario[chave][0]
                nome = input('Digite o novo nome do mecânico: ').upper()
                dicionario[chave][0].insert(0, nome)
            elif elemento == 2:
                del dicionario[chave][1]
                nascimento = input('Digite a nova Data de Nascimento do mecânico: ')
                dicionario[chave][1].insert(0, nascimento)
            elif elemento == 3:
                del dicionario[chave][2]
                sexo = input('Digite o sexo do mecânico: ').upper()
                dicionario[chave][2].insert(0, sexo)
            elif elemento == 4:
                del dicionario[chave][3]
                salario = input('Digite o novo salário do mecânico: ').upper()
                dicionario[chave][3].append(0, salario)
            elif elemento == 5:
                lista = dicionario[chave][4]
                print('E-mails cadastrados:', end=' ')
                for j in lista:
                    print(j, end=' ')
                print('')
                ema = input('Insira o e-mail que deseja alterar: ')
                if ema in lista:
                    for i in range(len(lista)):
                        if lista[i] == ema:
                            del lista[i]
                            elemento = input('Qual o novo e-mail que deseja adicionar? ')
                            dicionario[chave][4].insert(0, elemento)
                else:
                    print('-- E-mail não encontrado.')
            elif elemento == 6:
                lista = dicionario[chave][5]
                print('Números cadastrados: ', end='')
                for j in lista:
                    print(j, end=' ')
                print('')
                num = input('Insira o número que deseja alterar: ')
                if num in lista:
                    for i in range(len(lista)):
                        if lista[i] == num:
                            del lista[i]
                            elemento = input('Qual o novo número que deseja adicionar? ')
                            dicionario[chave][5].insert(0, elemento)
                else:
                    print('-- Número não encontrado.')
            print('-- Dados alterados!')
        elif opt == 2:
            choice = input('Você realmente deseja excluir o cadastro desse mecânico? Para confirmar insira "S" e para cancelar e voltar ao número anterior insira "N": ')
            if choice == 'S':
                del dicionario[chave]
    else:
        print('-- Dados não encontrados.')

def alt_exc_vei(dicionario):
    opt = int(input('Digite 1 para alterar ou 2 para excluir um elemento: '))
    chave = input('Insira placa do veículo: ').upper()
    if chave in dicionario:
        elemento = int(input(' 1. Tipo \n 2. Marca \n 3. Modelo \n 4. Ano \n 5. Portas \n 6. Combustível \n 7. Cor \n Insira o número da opção que deseja alterar ou excluir: '))
        if opt == 1:
            if elemento == 1:
                del dicionario[chave][0]
                tipo = input('Digite o novo tipo do veículo: ').upper()
                dicionario[chave][0].insert(0, tipo)
            elif elemento == 2:
                del dicionario[chave][1]
                marca = input('Digite a nova marca do veículo: ')
                dicionario[chave][1].insert(0, marca)
            elif elemento == 3:
                del dicionario[chave][2]
                modelo = input('Digite o novo modelo do veículo: ').upper()
                dicionario[chave][2].insert(0, modelo)
            elif elemento == 4:
                del dicionario[chave][3]
                ano = input('Digite o novo ano do veículo: ').upper()
                dicionario[chave][3].append(0, ano)
            elif elemento == 5:
                del dicionario[chave][4]
                portas = input('Digite quantas portas tem o veículo: ').upper()
                dicionario[chave][4].append(0, portas)
            elif elemento == 6:
                del dicionario[chave][5]
                combustivel = input('Digite o novo combustível do veículo: ').upper()
                dicionario[chave][5].append(0, combustivel)
            elif elemento == 7:
                del dicionario[chave][6]
                dicionario[chave].append([])
                cor = input('Digite a nova cor do veículo: ').upper()
                dicionario[chave][6].insert(0, cor)
            print('-- Dados alterados!')
        elif opt == 2:
            choice = input('Você realmente deseja excluir o cadastro desse veículo? Para confirmar insira "S" e para cancelar e voltar ao número anterior insira "N": ')
            if choice == 'S':
                del dicionario[chave]
    else:
        print('-- Dados não encontrados.')

def alt_exc_con(dicionario):
    opt = int(input('Digite 1 para alterar ou 2 para excluir um elemento: '))
    tupla = ()
    cpf = input('Insira o CPF do mecânico: ')
    tupla+=(cpf,)
    placa = input('Insira placa do veículo: ').upper()
    tupla+=(placa,)
    data_entrada = input('Insira a data de entrada (no formato DD/MM/AAAA): ')
    tupla+=(data_entrada,)
    if tupla in dicionario:
        elemento = int(input(' 1. Data de saída \n 2. Descrição dos problemas \n 3. Valor do conserto \n Insira o número da opção que deseja alterar ou excluir: '))
        if opt == 1:
            if elemento == 1:
                del dicionario[tupla][0]
                tipo = input('Digite a nova data de saída: ')
                dicionario[tupla][0].insert(0, tipo)
            elif elemento == 2:
                del dicionario[tupla][1]
                marca = input('Digite uma nova descrição dos problemas: ').upper()
                dicionario[tupla][1].insert(0, marca)
            elif elemento == 3:
                del dicionario[tupla][2]
                modelo = input('Digite o novo valor do conserto: ').upper()
                dicionario[tupla][2].insert(0, modelo)
            print('-- Dados alterados!')
        elif opt == 2:
            choice = input('Você realmente deseja excluir o cadastro desse conserto? Para confirmar insira "S" e para cancelar e voltar ao número anterior insira "N": ')
            if choice == 'S':
                del dicionario[tupla]
    else:
        print('-- Dados não encontrados.')


def menu():
    print('-- Menu de Opções:')
    print('1. Mecânicos')
    print('2. Veículos')
    print('3. Consertos')
    print('4. Relatórios')
    print('5. Sair')   
    op = int(input('Insira o número da opção desejada: '))
    return op

def menu_mecanicos():
    print('-- Submenu mecânicos:')
    print('1. Listar mecânicos cadastrados')
    print('2. Informações de um mecânico cadastrado')
    print('3. Cadastrar mecânico')
    print('4. Alterar ou excluir cadastro de um mecânico')
    print('5. Voltar')
    op = int(input('Insira o número da opção desejada: '))
    return op

def menu_veiculos():
    print('-- Submenu veículos:')
    print('1. Listar veículos cadastrados')
    print('2. Informações de um veículo no cadastro')
    print('3. Cadastrar veículo')
    print('4. Alterar ou excluir cadastro de um veículo')
    print('5. Voltar')
    op = int(input('Insira o número da opção desejada: '))
    return op

def menu_consertos():
    print('-- Submenu consertos:')
    print('1. Listar consertos agendados')
    print('2. Informações de um agendamento de conserto específico')
    print('3. Agendar conserto')
    print('4. Alterar ou excluir agendamento de um conserto')
    print('5. Voltar')
    op = int(input('Insira o número da opção desejada: '))
    return op

def menu_relatorios():
    print('-- Submenu relatórios:')
    print('1. Mostrar os cadastros de mecânicos que possuem mais do que x anos de idade')
    print('2. Mostrar todos os veículos cadastrados de determinada marca')
    print('3. Mostrar as informações de mecânico, veículo e agendamento em um espaço de tempo')
    print('4. Voltar')
    op = int(input('Insira o número da opção desejada: '))
    return op

def main():
    nome_arq_mec = 'Mecânicos.txt'
    mecanicos = ler_arquivo_mec(nome_arq_mec)
    nome_arq_vei = 'Veículos.txt'
    veiculos = ler_arquivo_vei(nome_arq_vei)
    nome_arq_con = 'Consertos.txt'
    consertos = ler_arquivo_con(nome_arq_con)
    op_menu = 1
    while op_menu != 5:
        op_menu = menu()
        if op_menu == 1:
            op_mecanicos = menu_mecanicos()
            if op_mecanicos == 1:
                listar_todos_mec(mecanicos)
            elif op_mecanicos == 2:
                listar_um_mec(mecanicos)
            elif op_mecanicos == 3:
                if icluir_mec(mecanicos):
                    print('-- Mecânico cadastrado com sucesso!')
                else:
                    print('-- Já existe um mecânico cadastrado com esse CPF.')
            elif op_mecanicos == 4:
                alt_exc_mec(mecanicos)
            elif op_mecanicos == 5:
                print('-- Voltando ao menu principal...')
                menu()
            else:
                print('-- Opção inválida! Voltando ao menu principal...')
        elif op_menu == 2:
            op_veiculos = menu_veiculos()
            if op_veiculos == 1:
                listar_todos_vei(veiculos)
            elif op_veiculos == 2:
                listar_um_vei(veiculos)
            elif op_veiculos == 3:
                if icluir_vei(veiculos):
                    print('-- Veículo cadastrado com sucesso!')
                else:
                    print('-- Já existe um veículo cadastrado com essa placa.')
            elif op_veiculos == 4:
                alt_exc_vei(veiculos)
            elif op_veiculos == 5:
                print('-- Voltando ao menu principal...')
                menu()
            else:
                print('-- Opção inválida! Voltando ao menu principal...')
        elif op_menu == 3:
            op_consertos = menu_consertos()
            if op_consertos == 1:
                listar_todos_con(consertos)
            elif op_consertos == 2:
                listar_um_con(consertos)
            elif op_consertos == 3:
                if icluir_con(consertos, mecanicos, veiculos):
                    print('-- Conserto cadastrado com sucesso!')
            elif op_consertos == 4:
                alt_exc_con(consertos)
            elif op_consertos == 5:
                print('-- Voltando ao menu principal...')
                menu()
            else:
                print('-- Opção inválida!')
        elif op_menu == 4:
            op_relatorios = menu_relatorios()
            if op_relatorios == 1:
                print('oi')#espaço para função de relatórios 1
            elif op_relatorios == 2:
                print('oi')#espaço para função de relatórios 2
            elif op_relatorios == 3:
                print('oi')#espaço para função de relatórios 3
            elif op_relatorios == 4:
                print('-- Voltando ao menu principal...')
                menu()
            else:
                print('-- Opção inválida! Voltando ao menu principal...')
        elif op_menu == 5:
            gravar_dados(nome_arq_mec, mecanicos)
            gravar_dados(nome_arq_vei, veiculos)
            gravar_dados_con(nome_arq_con, consertos)
            print('-- Encerrando o programa...')
        else:
            print('-- Opção inválida!')

main()