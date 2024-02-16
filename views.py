import sys
import csv


# Trabalhando com csv -----------------------------------

# ver dados

def ver_dados():
    todos_dados = []
    # acessando o arquivo csv
    with open('dados.csv') as file:
        ler_csv = csv.reader(file)
        for row in ler_csv:
            todos_dados.append(row)

    return todos_dados

    # print(todos_dados)


# funcao adicionar item no arquivo
def adicionar_dados(i):
    # acessando o arquivo csv
    with open('dados.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(i)


# funcao remover item no arquivo
def remover_dados(i):
    def adicionar_novalista(j):
        # acessando o arquivo csv
        with open('dados.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(j)

    nova_lista = []
    telefone = i

    with open('dados.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            nova_lista.append(row)
            for campo in row:
                if campo == telefone:
                    nova_lista.remove(row)

    adicionar_novalista(nova_lista)


# funcao atualizar dados no arquivo
def atualizar_dados(i):
    def atualizar_novalista(i):
        # acessando o arquivo csv
        with open('dados.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(i)

    nova_lista = []
    telefone = i[0]

    with open('dados.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            nova_lista.append(row)
            for campo in row:
                if campo == telefone:
                    nome = i[1]
                    sexo = i[2]
                    telefone = i[3]
                    email = i[4]

                    dados = [nome, sexo, telefone, email]

                    # trocando lista por index
                    index = nova_lista.index(row)
                    nova_lista[index] = dados

                    print(nova_lista)

    atualizar_novalista(nova_lista)


# funcao procurar dados no arquivo
def procurar_dados(i):
    dados = []
    telefone = i

    with open('dados.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for campo in row:
                if campo == telefone:
                    dados.append(row)

    return dados
