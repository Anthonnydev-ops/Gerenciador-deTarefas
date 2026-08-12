# 📝 Gerenciador de Tarefas

Um gerenciador de tarefas simples e funcional feito em **Python puro**, utilizando **SQLite** como banco de dados para persistência. Ideal para quem está aprendendo lógica de programação, manipulação de banco de dados e boas práticas de CRUD.

---

## 📌 Sobre o projeto

Este projeto é um sistema de linha de comando (CLI) que permite ao usuário gerenciar uma lista de tarefas de forma prática. Todas as tarefas ficam salvas em um banco de dados **SQLite**, então nada se perde ao fechar o programa.

Com ele é possível:

- ✅ Adicionar tarefas
- 📋 Listar tarefas com status de conclusão
- ✏️ Atualizar o nome de uma tarefa
- ✔️ Marcar tarefas como concluídas
- 🗑️ Remover tarefas já concluídas

---

## 🚀 Funcionalidades

| # | Funcionalidade | Descrição |
|---|-----------------|-----------|
| 1 | **Adicionar tarefa** | Cadastra uma nova tarefa no banco de dados |
| 2 | **Ver tarefas** | Lista todas as tarefas com um indicador visual `[✓]` para concluídas |
| 3 | **Atualizar tarefa** | Permite editar o nome de uma tarefa existente |
| 4 | **Completar tarefa** | Marca uma tarefa como concluída |
| 5 | **Deletar tarefas concluídas** | Remove do banco todas as tarefas já finalizadas |
| 6 | **Sair** | Encerra o programa e fecha a conexão com o banco |

---

## 🛠️ Tecnologias utilizadas

- **Python 3** — lógica do programa e interface via terminal
- **SQLite3** — banco de dados leve, embutido na própria biblioteca padrão do Python (`sqlite3`)

---

## 📂 Estrutura do banco de dados

O programa cria automaticamente uma tabela chamada `tarefas` (caso ainda não exista) com a seguinte estrutura:

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| `id` | INTEGER (PK, AUTOINCREMENT) | Identificador único da tarefa |
| `tarefa` | TEXT | Descrição da tarefa |
| `completada` | INTEGER (0 ou 1) | Indica se a tarefa foi concluída |

---

## ▶️ Como executar

### Pré-requisitos

- Ter o **Python 3** instalado na máquina ([baixar aqui](https://www.python.org/downloads/))

> Não é necessário instalar nenhuma dependência externa — o `sqlite3` já vem embutido no Python.

### Passo a passo

1. Clone o repositório:
```bash
git clone https://github.com/Anthonnydev-ops/Gerenciador-deTarefas.git
```

2. Entre na pasta do projeto:
```bash
cd Gerenciador-deTarefas
```

3. Execute o programa:
```bash
python main.py
```

> ⚠️ Substitua `main.py` pelo nome real do arquivo `.py`, caso seja diferente.

---

## 💻 Como usar

Ao rodar o programa, um menu interativo será exibido no terminal:

```
=== GERENCIADOR DE TAREFAS ===
1. Adicionar tarefa
2. Ver tarefas
3. Atualizar tarefa
4. Completar tarefa
5. Deletar tarefas concluídas
6. Sair
```

Basta digitar o número da opção desejada e seguir as instruções exibidas no terminal.

### Exemplo de uso

```
Digite uma opção: 1
Digite o nome da tarefa: Estudar Python
Tarefa 'Estudar Python' adicionada com sucesso!

Digite uma opção: 2

Lista de tarefas:
1. [ ] Estudar Python
```

---

## 🧠 Aprendizados aplicados neste projeto

- Manipulação de banco de dados com `sqlite3`
- Operações CRUD (Create, Read, Update, Delete)
- Uso de funções para organizar a lógica do sistema
- Estrutura de repetição (`while`) para criar um menu interativo
- Boas práticas com `cursor` e `commit` no controle de transações

---

## 📈 Possíveis melhorias futuras

- [ ] Adicionar interface gráfica (Tkinter, PyQt ou uma versão web com Flask/Django)
- [ ] Implementar categorias/prioridades para as tarefas
- [ ] Adicionar data de criação e prazo para conclusão
- [ ] Criar testes automatizados
- [ ] Empacotar como executável (.exe) usando PyInstaller

---

## 👤 Autor

Feito com 💻 e bastante café por **Anthonny**

[![GitHub](https://img.shields.io/badge/GitHub-Anthonnydev--ops-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Anthonnydev-ops)

---

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e distribuir.
