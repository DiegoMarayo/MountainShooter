# 🎮 Mountain Shooter

Projeto desenvolvido em Python utilizando Pygame como atividade prática da disciplina de Linguagem de Programação.

O jogo é um arcade shooter 2D com múltiplos modos de jogo, sistema de pontuação, persistência em banco de dados SQLite e dois níveis progressivos.

---

## 📖 Sobre o Projeto

Mountain Shooter é um jogo estilo arcade onde o jogador deve sobreviver a ondas de inimigos, eliminá-los para acumular pontos e avançar pelas fases.

O projeto foi desenvolvido utilizando conceitos de:

* Programação Orientada a Objetos (POO)
* Design Patterns
* Manipulação de Eventos
* Persistência de Dados com SQLite
* Desenvolvimento de Jogos com Pygame

---

## 🚀 Tecnologias Utilizadas

* Python 3.x
* Pygame
* SQLite3

---

## 🎯 Funcionalidades

* Menu principal interativo
* Modo Single Player
* Modo Cooperativo (2 jogadores)
* Modo Competitivo (2 jogadores)
* Sistema de disparos
* Sistema de colisões
* Inimigos com IA simples
* Dois níveis de jogo
* Música por tela
* Ranking persistente em SQLite
* Sistema de pontuação

---

## 🎮 Controles

### Jogador 1

| Ação                | Tecla      |
| ------------------- | ---------- |
| Mover para cima     | ↑          |
| Mover para baixo    | ↓          |
| Mover para esquerda | ←          |
| Mover para direita  | →          |
| Atirar              | Right Ctrl |

### Jogador 2

| Ação                | Tecla     |
| ------------------- | --------- |
| Mover para cima     | W         |
| Mover para baixo    | S         |
| Mover para esquerda | A         |
| Mover para direita  | D         |
| Atirar              | Left Ctrl |

---

## 🏆 Sistema de Pontuação

Os jogadores acumulam pontos ao eliminar inimigos.

| Inimigo | Pontuação |
| ------- | --------- |
| Enemy1  | 100       |
| Enemy2  | 125       |

Ao finalizar o jogo, a pontuação é armazenada em banco de dados SQLite e exibida no ranking Top 10.

---

## 🗂 Estrutura do Projeto

```text
MountainShooter/
│
├── assets/
│   ├── imagens
│   ├── músicas
│
├── src/
│   ├── background.py
│   ├── DBProxy.py
│   ├── enemy.py
│   ├── enemyShot.py
│   ├── entity.py
│   ├── entityFactory.py
│   ├── entityMediator.py
│   ├── game.py
│   ├── level.py
│   ├── menu.py
│   ├── player.py
│   ├── playerShot.py
│   ├── score.py
│   └── const.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Instalação

Clone o repositório:

```bash
git clone https://github.com/DiegoMarayo/MountainShooter.git
```

Entre na pasta:

```bash
cd MountainShooter
```

Crie o ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente:

Windows:

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## ▶️ Executando o Projeto

```bash
python main.py
```

---

## 🗄 Banco de Dados

O projeto utiliza SQLite para armazenar os 10 melhores resultados dos jogadores.

Tabela:

```sql
dados
```

Campos:

* ID
* name
* score
* date

---

## 📚 Conceitos Aplicados

* Classes e Objetos
* Herança
* Polimorfismo
* Encapsulamento
* Factory Pattern
* Mediator Pattern
* Manipulação de Eventos
* Persistência de Dados
* Desenvolvimento de Jogos 2D

---

## 👨‍💻 Autor

Diego Marayo

GitHub:
https://github.com/DiegoMarayo

Curso: Engenharia de Software – UNINTER

Disciplina: Linguagem de Programação

Ano: 2026

---

## 📄 Licença

Projeto desenvolvido para fins acadêmicos.
