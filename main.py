from tkinter.ttk import *
from tkinter import *

from tkinter import messagebox, ttk

import sys
import csv

from views import *

# cores -----------------------------

co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#3fb5a3"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = "#6f9fbd"  # azul
co6 = "#ef5350"  # vermelha
co7 = "#93cd95"  # verde

co2 = co1
co1 = co0

# criando janela --------------------

janela = Tk()
janela.title("")
janela.geometry('500x450')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

################# Frames ####################

frame_cima = Frame(janela, width=500, height=50, bg=co3, relief="flat")
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=500, height=150, bg=co1, relief="flat")
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_tabela = Frame(janela, width=500, height=100, bg=co1, relief="flat")
frame_tabela.grid(row=2, column=0, columnspan=2, padx=10, pady=1, sticky=NW)

# configurando frame_cima

l_nome = Label(frame_cima, text="Agenda Telefônica", height=1, anchor=NE, font=('verdana 17 bold'), bg=co3, fg=co1)
l_nome.place(x=5, y=5)

l_linha = Label(frame_cima, width=500, text="", height=1, anchor=NW, font=('Ivy 1 '), bg=co2)
l_linha.place(x=0, y=46)


# funções --------------------------------------------------
# funcao para mostrar
def mostrar():
    # creating a treeview with dual scrollbars
    list_header = ['Nome', 'Sexo', 'telefone', 'email']

    df_list = ver_dados()

    global tree

    tree = ttk.Treeview(frame_tabela, selectmode="extended",
                        columns=list_header, show="headings")
    # vertical scrollbar
    vsb = ttk.Scrollbar(
        frame_tabela, orient="vertical", command=tree.yview)
    # horizontal scrollbar
    hsb = ttk.Scrollbar(
        frame_tabela, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    hd = ["nw", "nw", "nw", "nw", "nw", ]
    h = [120, 50, 80, 120, 200]
    n = 0

    # tree cabecalho
    tree.heading(0, text='Nome', anchor=NW)
    tree.heading(1, text='Sexo', anchor=NW)
    tree.heading(2, text='Telefone', anchor=NW)
    tree.heading(3, text='E-mail', anchor=NW)

    # tree  corpo
    tree.column(0, width=120, anchor='nw')
    tree.column(1, width=50, anchor='nw')
    tree.column(2, width=100, anchor='nw')
    tree.column(0, width=120, anchor=hd[0])

    for item in df_list:
        tree.insert('', 'end', values=item)


mostrar()


def inserir():
    nome = e_nome.get()
    sexo = c_sexo.get()
    telefone = e_tel.get()
    email = e_email.get()

    dados = [nome, sexo, telefone, email]

    if nome == '' or sexo == '' or telefone == '' or email == '':
        messagebox.showwarning('Dados', 'Por favor preencha todos os campos')

    else:
        adicionar_dados(dados)
        messagebox.showinfo('Dados', 'Dados foram adicionado')
        e_nome.delete(0, 'end')
        c_sexo.delete(0, 'end')
        e_tel.delete(0, 'end')
        e_email.delete(0, 'end')

        # chamar a funcao mostrar dados para atualizar a lista
        mostrar()


def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']

        nome = str(treev_lista[0])
        sexo = str(treev_lista[1])
        telefone = str(treev_lista[2])
        email = str(treev_lista[3])

        e_nome.insert(0, nome)
        c_sexo.insert(0, sexo)
        e_tel.insert(0, telefone)
        e_email.insert(0, email)

        def confirmar():
            novo_nome = e_nome.get()
            novo_sexo = c_sexo.get()
            novo_telefone = e_tel.get()
            novo_email = e_email.get()

            dados = [telefone, novo_nome, novo_sexo, novo_telefone, novo_email]

            atualizar_dados(dados)

            messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')

            e_nome.delete(0, 'end')
            c_sexo.delete(0, 'end')
            e_tel.delete(0, 'end')
            e_email.delete(0, 'end')

            for widget in frame_tabela.winfo_children():
                widget.destroy()

            b_confirmar.destroy()

            mostrar()

        b_confirmar = Button(frame_baixo, command=confirmar, text="Confirmar", width=10, height=1, bg=co2, fg=co4,
                             font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
        b_confirmar.place(x=290, y=110)

    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')


def remover():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = str(treev_lista[2])

        remover_dados(valor)

        messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')

        for widget in frame_tabela.winfo_children():
            widget.destroy()

        mostrar()

    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')


def procurar():
    telefone = e_procurar.get()

    dados = procurar_dados(telefone)

    def delete_command():
        tree.delete(*tree.get_children())

    delete_command()

    for item in dados:
        tree.insert('', 'end', values=item)


# configurando frame_baixo

l_nome = Label(frame_baixo, text="Nome *", width=20, height=1, anchor=NW, font=('Ivy 10 '), bg=co1, fg=co4)
l_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, justify='left', font=("", 10), highlightthickness=1, relief="flat")
e_nome.place(x=80, y=20)

l_sexo = Label(frame_baixo, text="Sexo *", height=1, anchor=NW, font=('Ivy 10 '), bg=co1, fg=co4)
l_sexo.place(x=10, y=50)
c_sexo = Combobox(frame_baixo, width=27)
c_sexo['values'] = ('', 'F', 'M')
c_sexo.place(x=80, y=50)

l_tel = Label(frame_baixo, text="Telefone *", height=1, anchor=NW, font=('Ivy 10 '), bg=co1, fg=co4)
l_tel.place(x=10, y=80)
e_tel = Entry(frame_baixo, width=25, justify='left', font=("", 10), highlightthickness=1, relief="flat")
e_tel.place(x=80, y=80)

l_email = Label(frame_baixo, text="E-mail *", height=1, anchor=NW, font=('Ivy 10 '), bg=co1, fg=co4)
l_email.place(x=10, y=110)
e_email = Entry(frame_baixo, width=25, justify='left', font=("", 10), highlightthickness=1, relief="flat")
e_email.place(x=80, y=110)

b_procurara = Button(frame_baixo, command=procurar, text="Procurar", height=1, bg=co2, fg=co4, font=('Ivy 8 bold'),
                     relief=RAISED, overrelief=RIDGE)
b_procurara.place(x=290, y=20)
e_procurar = Entry(frame_baixo, width=16, justify='left', font=("", 11), highlightthickness=1, relief="flat")
e_procurar.place(x=347, y=21)

b_ver = Button(frame_baixo, command=mostrar, text="Ver dados", width=10, height=1, bg=co2, fg=co4, font=('Ivy 8 bold'),
               relief=RAISED, overrelief=RIDGE)
b_ver.place(x=290, y=50)

b_adicionar = Button(frame_baixo, command=inserir, text="Adicionar", width=10, height=1, bg=co2, fg=co4,
                     font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_adicionar.place(x=400, y=50)

b_atualizar = Button(frame_baixo, command=atualizar, text="Atualizar", width=10, height=1, bg=co7, fg=co1,
                     font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_atualizar.place(x=400, y=80)

b_deletar = Button(frame_baixo, command=remover, text="Deletar", width=10, height=1, bg=co6, fg=co1,
                   font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_deletar.place(x=400, y=110)

janela.mainloop()