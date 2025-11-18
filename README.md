# 🎮 Campo Minado – Python + Tkinter  
### Trabalho da disciplina de Programação – BICT / UFMA

Este projeto consiste em uma implementação simples do jogo **Campo Minado**, desenvolvida em **Python** utilizando a biblioteca **Tkinter** como interface gráfica.  
O objetivo é exercitar os conceitos fundamentais da disciplina de Fundamentos da Computação (CT) do **Bacharelado Interdisciplinar em Ciência e Tecnologia (BICT)** da **Universidade Federal do Maranhão (UFMA)**, aplicando lógica, estruturas condicionais, eventos, funções e manipulação de GUI.

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
```

---

## ▶️ Como executar

Baixe ou clone o repositório:

```bash
git clone https://github.com/matheuszmz/campominado.git
```

Acesse o diretório do projeto:

```bash
cd campominado
```

Execute o jogo:

```bash
python campominado.py
```
A janela principal será aberta automaticamente.

## 🖼️ Interface do Jogo

A interface contém:

- Um título: **Campo Minado**
- Um contador de pontos
- Um campo **5×10** com 50 botões
- Rodapé com assinatura do aluno

### Legendagem por cor

| Cor do Botão | Significado |
|--------------|-------------|
| 🟩 Verde     | Botão seguro clicado (ganhou pontos) |
| 🟥 Vermelho  | Bomba (fim do jogo) |

### Popup ao clicar em uma bomba

Quando uma bomba é pressionada, o jogo exibe:

- Aviso de explosão  
- Pontuação final da rodada  
- Pergunta: **Deseja reiniciar?**

Ações possíveis:

- ✔️ **Sim** → reinicia o jogo  
- ❌ **Não** → fecha a aplicação  

---

## 🧩 Estrutura do Código

### Classe `App`
Centraliza toda a lógica do jogo e a interface gráfica.

---

### 🔹 `__init__`
- Inicializa a janela principal  
- Cria os frames  
- Exibe título e contador de pontos  
- Gera o primeiro campo  
- Monta o rodapé  

---

### 🔹 `cria_campo`
- Limpa o campo anterior  
- Gera novos botões  
- Define aleatoriamente bombas e botões seguros (80/20)  
- Zera e exibe a pontuação  

---

### 🔹 `cria_botao_normal`
- Cria botões seguros  
- Associa callback para somar pontos  

---

### 🔹 `cria_botao_bomba`
- Cria botões explosivos  
- Associa callback para o fim de jogo  

---

### 🔹 `naoExplode`
- Soma **10 pontos**  
- Muda a cor do botão para verde  
- Desabilita o botão  
- Atualiza o placar  

---

### 🔹 `explode`
- Muda a cor do botão para vermelho  
- Mostra o popup de explosão  
- Informa a pontuação final  
- Reinicia ou fecha o jogo conforme escolha do usuário  

---

## 📝 Versão Inicial em Modo Texto (CLI)

Além da versão principal com interface gráfica em Tkinter, o projeto também inclui um arquivo chamado **`campominado_cmd.py`**, que representa a **primeira versão do jogo**, desenvolvida inteiramente no terminal (CLI – Command Line Interface).

Essa versão foi criada como **protótipo inicial** para testar a lógica do jogo antes da implementação da interface gráfica. Ela funciona diretamente no console e utiliza:

- Impressão do tabuleiro em modo texto  
- Entrada de linha e coluna pelo teclado  
- Limpeza de tela via `os.system()`  
- Pontuação acumulada  
- Sistema de recorde  
- Mensagens de derrota e reinício  
- Geração de bombas e áreas seguras de forma aleatória

Essa implementação foi essencial para validar:

- Estrutura do campo  
- Regras de explosão  
- Sistema de pontuação  
- Loop principal da partida  

A versão atual em Tkinter mantém a lógica central inspirada nesse protótipo, porém acrescenta elementos visuais, eventos gráficos e uma experiência de jogo mais amigável.

O código completo da versão CLI está disponível no arquivo:

```bash
python campominado_cmd.py
```

## 📚 Instituição

**Universidade Federal do Maranhão – UFMA**  
**BICT – Bacharelado Interdisciplinar em Ciência e Tecnologia**  
**Disciplina:** Fundamentos de Computação (CT)  
**Aluno:** Matheus de Andrade Santana  

---

## 📝 Licença

Este projeto é destinado a fins educacionais, podendo ser utilizado, modificado e distribuído livremente conforme os princípios do software aberto.

