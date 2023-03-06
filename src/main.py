"""
modulo: Simula fila de banco
objetivo: Demonstrar o conceito de fila na disciplina estrutura de dados
autor: Rayane Carvalho da Silva Marques
email: rayane.marques1@alunos.unis.edu.br
"""

### Exemplo de filas com prioridade por idade

fila = []
fila_prioritaria = []

def cria_pessoa(nome, idade):
    return {
        "nome": nome,
        "idade": idade
    }


def recepcionar(pessoa):
    print(f"Cliente {pessoa} entrou na fila")
    if pessoa["idade"] >= 65:
        fila_prioritaria.append(pessoa)
    else:
        fila.append(pessoa) # insere no final da fila


def atender(pessoa):
    print(f"Cliente {pessoa['nome']}, foi atendido")


pessoa_1 = cria_pessoa("joao", 42)
pessoa_idosa = cria_pessoa("Nana", 89)
pessoa_2 = cria_pessoa("maria", 24)

recepcionar(pessoa_1)
recepcionar(pessoa_idosa)
recepcionar(pessoa_2)

while len(fila_prioritaria) > 0 or len(fila) > 0:
    while len(fila_prioritaria) > 0:
        proximo_da_fila = fila_prioritaria.pop(0)
        atender(proximo_da_fila)
    if len(fila) > 0:
        proximo_da_fila = fila.pop(0)
        atender(proximo_da_fila)

print(f"fila atual {fila} e fila prioritaria {fila_prioritaria}")
