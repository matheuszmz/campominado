from tkinter import *
from tkinter import messagebox
import random

class App:
    def __init__(self, master):
        self.master = master
        self.pontos = 0

        # Frames
        self.principal = Frame(master)
        self.principal.pack()

        self.topo = Frame(self.principal, width=600, height=50)
        self.topo.pack()

        self.centro = Frame(self.principal, width=600, height=400)
        self.centro.pack()

        self.rodape = Frame(self.principal, width=600, height=50)
        self.rodape.pack()

        # Objeto do Frame TOPO
        self.titulo = Label(self.topo, text="Campo Minado", height=2,
                            font=("Verdana", 12, "bold"))
        self.titulo.pack()

        # Label de Pontos
        self.label_pontos = Label(self.topo, text=f"Pontos: {self.pontos}",
                                  font=("Verdana", 10))
        self.label_pontos.pack()

        # Cria o primeiro campo
        self.cria_campo()

        # Objeto do Frame Rodapé
        self.rodapeLabel = Label(self.rodape, text="BICT - Matheus")
        self.rodapeLabel.pack()

    def cria_campo(self):
        # Cria/recria o campo com 50 botões (80% normais, 20% bomba).
        # Limpa o frame central (para novo jogo)
        for widget in self.centro.winfo_children():
            widget.destroy()

        # Zera pontos
        self.pontos = 0
        self.atualiza_pontos()

        linhas = 5
        colunas = 10

        for linha in range(linhas):
            for coluna in range(colunas):
                # 20% de chance de ser bomba
                if random.random() < 0.2:
                    self.cria_botao_bomba(linha, coluna)
                else:
                    self.cria_botao_normal(linha, coluna)

    def cria_botao_bomba(self, linha, coluna):
        botao = Button(
            self.centro,
            width=3,
            height=1
        )
        botao.configure(command=lambda b=botao: self.explode(b))
        botao.grid(row=linha, column=coluna, padx=2, pady=2)


    def cria_botao_normal(self, linha, coluna):
        botao = Button(
            self.centro,
            width=3,
            height=1
        )
        botao.configure(command=lambda b=botao: self.naoExplode(b))
        botao.grid(row=linha, column=coluna, padx=2, pady=2)


    def atualiza_pontos(self):
        self.label_pontos.config(text=f"Pontos: {self.pontos}")

    def explode(self, botao):
        # Desabilita o botão bomba clicado e fica vermelho
        botao.config(bg="red", state="disabled")

        # Mostra popup com pontos e pergunta se quer jogar de novo
        msg = (
            "BOOOM! Você clicou em uma bomba!\n"
            f"Você obteve {self.pontos} pontos!\n"
            "Vamos tentar de novo?"
        )
        resposta = messagebox.askyesno("Fim de jogo", msg)

        if resposta:  # Sim
            self.cria_campo()
        else:  # Não
            self.master.destroy()

    def naoExplode(self, botao):
        # Desabilita o botão para não somar pontos duas vezes e fica verde
        if botao["state"] == "normal":
            botao.config(bg="green", state="disabled")
            self.pontos += 10
            self.atualiza_pontos()

root = Tk()
root.title("Campo Minado")
root.geometry("400x250")
root.maxsize(width=400, height=250)
App(root)
root.mainloop()
