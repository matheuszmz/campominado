# 🎮 Campo Minado – Python + Tkinter  
### Trabalho da disciplina de Programação – BICT / UFMA

Este projeto consiste em uma implementação simples do jogo **Campo Minado**, desenvolvida em **Python** utilizando a biblioteca **Tkinter** como interface gráfica.  
O objetivo é exercitar os conceitos fundamentais da disciplina de Programação do **Bacharelado Interdisciplinar em Ciência e Tecnologia (BICT)** da **Universidade Federal do Maranhão (UFMA)**, aplicando lógica, estruturas condicionais, eventos, funções e manipulação de GUI.

---

## 🚀 Funcionalidades

- Geração automática de um campo com **50 botões**  
  - **80%** de botões normais  
  - **20%** de botões bomba  
- Cada botão normal:
  - Soma **+10 pontos**
  - Fica **verde**
  - É desativado
- A bomba:
  - Fica **vermelha**
  - Exibe mensagem de explosão
  - Mostra os pontos obtidos
  - Pergunta ao jogador se deseja reiniciar
- O jogador pode:
  - **Reiniciar o jogo**
  - **Encerrar a aplicação**

---

## 🧠 Conceitos aplicados no projeto

Este trabalho reforça diversos conteúdos vistos na disciplina:

- Estruturas condicionais (`if`, `else`)
- Laços de repetição (`for`)
- Manipulação de funções
- Uso de classes e orientação a objetos
- Eventos e callbacks com Tkinter
- Randomização (`random.random`)
- Atualização dinâmica de interface
- Organização modular do código

---

## 📦 Pré-requisitos

- **Python 3.8+**
- Tkinter (já incluso na maioria das instalações do Python)

Para testar se o Tkinter está instalado:

```bash
python -m tkinter
