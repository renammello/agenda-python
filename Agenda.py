# dicionário vazio para armazenar os contatos.
agenda = {}

# funções para manipular a agenda.

def adicionar_contato(nome, telefone):
    agenda[nome] = telefone

def remover_contato(nome):
    if nome in agenda:
        del agenda[nome]

def buscar_contato(nome):
    if nome in agenda:
        return agenda[nome]
    else:
        return "Contato não encontrado."

def listar_contatos():
    for nome, telefone in agenda.items():
        print(f"Nome: {nome}, Telefone: {telefone}")

# contatos de exemplo.
adicionar_contato("João", "123456789")
adicionar_contato("Maria", "987654321")

# listar os contatos.
listar_contatos()

# buscar um contato específico
print(buscar_contato("João"))

# remover um contato
remover_contato("João")
listar_contatos()
