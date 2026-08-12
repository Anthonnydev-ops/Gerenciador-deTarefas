import sqlite3


# BANCO DE DADOS
conexao = sqlite3.connect("tarefas.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tarefa TEXT NOT NULL,
    completada INTEGER DEFAULT 0
)
""")

conexao.commit()


# FUNÇÕES
def adicionar_tarefa(nome_tarefa):
    cursor.execute(
        "INSERT INTO tarefas (tarefa, completada) VALUES (?, ?)",
        (nome_tarefa, 0)
    )

    conexao.commit()

    print(f"Tarefa '{nome_tarefa}' adicionada com sucesso!")


def ver_tarefas():
    cursor.execute(
        "SELECT id, tarefa, completada FROM tarefas ORDER BY id"
    )

    tarefas = cursor.fetchall()

    print("\nLista de tarefas:")

    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for indice, tarefa in enumerate(tarefas, start=1):
        id_tarefa, nome, completada = tarefa

        status = "✓" if completada else " "

        print(f"{indice}. [{status}] {nome}")


def obter_id_real(posicao):
    cursor.execute(
        "SELECT id FROM tarefas ORDER BY id"
    )

    ids = cursor.fetchall()

    if 1 <= posicao <= len(ids):
        return ids[posicao - 1][0]

    return None


def atualizar_nome_tarefa(id_tarefa, novo_nome):
    cursor.execute(
        "UPDATE tarefas SET tarefa = ? WHERE id = ?",
        (novo_nome, id_tarefa)
    )

    conexao.commit()

    print("Tarefa atualizada com sucesso!")


def completar_tarefa(id_tarefa):
    cursor.execute(
        "UPDATE tarefas SET completada = 1 WHERE id = ?",
        (id_tarefa,)
    )

    conexao.commit()

    print("Tarefa marcada como concluída!")


def deletar_tarefas_completadas():
    cursor.execute(
        "DELETE FROM tarefas WHERE completada = 1"
    )

    conexao.commit()

    print("Tarefas concluídas removidas!")



# MENU
while True:

    print("\n=== GERENCIADOR DE TAREFAS ===")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas concluídas")
    print("6. Sair")

    escolha = input("Digite uma opção: ")

    if escolha == "1":
        nome = input("Digite o nome da tarefa: ")
        adicionar_tarefa(nome)

    elif escolha == "2":
        ver_tarefas()

    elif escolha == "3":
        ver_tarefas()

        posicao = int(input("Digite o número da tarefa: "))
        novo_nome = input("Digite o novo nome da tarefa: ")

        id_real = obter_id_real(posicao)

        if id_real:
            atualizar_nome_tarefa(id_real, novo_nome)
        else:
            print("Tarefa inválida!")

    elif escolha == "4":
        ver_tarefas()

        posicao = int(input("Digite o número da tarefa que deseja concluir: "))

        id_real = obter_id_real(posicao)

        if id_real:
            completar_tarefa(id_real)
        else:
            print("Tarefa inválida!")

    elif escolha == "5":
        deletar_tarefas_completadas()
        ver_tarefas()

    elif escolha == "6":
        print("Programa finalizado!")
        break

    else:
        print("Opção inválida!")

conexao.close()