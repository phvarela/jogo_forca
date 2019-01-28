"""
Jogo da forca: versão 2.0
Baseado no jogo da forca criado para rodar no terminal.

Criado por: Paulo Varela
Versão inicial criada em 27/01/2019


*   PALAVRAS DEVEM SER ADICIONDAS NA LINHA 39

Link das imagens:
https://www.atividadesebrincadeiras.com/wp-content/uploads/2013/02/jogo-da-forca.gif
https://www.gratispng.com/png-m8ilok/

"""
from tkinter import *
import random
import ctypes
import sys
import os


class Application:
    def __init__(self, master=None):
        self.erradas = []
        self.reveladas = []
        self.tentativas = 5

        # EXIBE O FRAME COM A PALAVRA OCULTA
        self.exibe_palavra = Frame(master)
        self.exibe_palavra['pady'] = 10
        # self.exibe_palavra.configure(bg='#00ffff')
        self.exibe_palavra.pack()

        self.palavra_label = Label(self.exibe_palavra, text='A palavra é: ')
        self.palavra_label['font'] = ("Arial", "12", "bold")
        self.palavra_label.pack(side=LEFT)

        self.palavras = ['PARANORMAL', 'SOBRENATURAL', 'ESTATISTICAS',
                         'SUPERMERCADO', 'KILOMETRAGEM', 'DESBLOQUEIO', 'RENEGOCIACAO', 'METALURGICA']

        self.palavra = random.choice(self.palavras)
        self.oculto_txt = ('█ ' * len(self.palavra)).split()
        self.oculto = Label(self.exibe_palavra, text=self.oculto_txt, fg='blue')
        self.oculto['font'] = ("Arial", "12", "bold")
        self.oculto.pack(side=LEFT)

        # EXIBE A IMAGEM NA TELA
        self.imagem = PhotoImage(file='IMG_05.gif')
        self.exibe_imagem = Canvas(master, width=370, height=370)
        self.exibe_imagem.pack()

        # Pesquisar e entender o funcionamento do anchor, e como ele é usado para posicionar a imagem na tela
        self.exibe_imagem.create_image(10, 10, anchor=NW, image=self.imagem)

        # EXIBE O FRAME COM AS LETRAS ERRADAS
        self.exibe_erros = Frame(master)
        self.exibe_erros['pady'] = 10
        self.exibe_erros.pack(side=BOTTOM)

        self.erros_label = Label(self.exibe_erros, text='Letras erradas: ', fg='red')
        self.erros_label['font'] = ("Arial", "10", "bold")
        self.erros_label.pack(side=LEFT)

        self.erros = Label(self.exibe_erros, text=self.erradas, fg='red')
        self.erros['font'] = ("Arial", "12", "bold")
        self.erros.pack(side=LEFT)

        # EXIBE O FRAME ONDE A LETRA É DIGITADA
        self.pega_letra = Frame(master)
        self.pega_letra['pady'] = 10
        self.pega_letra.pack(side=BOTTOM)

        self.letra_label = Label(self.pega_letra, text='Escolha uma letra ')
        self.letra_label['font'] = ("Arial", "12", "bold")
        self.letra_label.pack(side=LEFT)

        self.escolha_letra = Entry(self.pega_letra)
        self.escolha_letra['width'] = 20
        self.escolha_letra.pack(side=LEFT)

        self.verifica_letra = Button(self.pega_letra)
        self.verifica_letra['text'] = 'Verificar'
        self.verifica_letra.bind('<Button-1>', self.verificaPalavra)
        self.verifica_letra.pack(side=RIGHT)

    def verificaPalavra(self, event):
        self.letra = self.escolha_letra.get().upper().strip()[0]
        self.escolha_letra.delete(0, END)

        if self.letra in self.erradas or self.letra in self.reveladas:
            ctypes.windll.user32.MessageBoxW(0,
                                             f'A letra [ {self.letra} ]  já foi dita anteriormente. \nTente novamente.',
                                             'Aviso!', 1)
        else:
            if self.letra in self.palavra:
                self.reveladas.append(self.letra)
                for l in range(len(self.palavra)):
                    if self.palavra[l] == self.letra:
                        self.oculto_txt[l] = self.letra
                self.oculto['text'] = self.oculto_txt
                if ''.join(self.oculto_txt) == self.palavra:
                    ctypes.windll.user32.MessageBoxW(0,
                                                     f'PARABÉNS!! VOCÊ VENCEU! \nA PALAVRA COMPLETA É: {self.palavra}',
                                                     'PARABÉNS!', 0)
                    self.restart()
            else:
                self.erradas.append(self.letra)
                self.erros['text'] = self.erradas
                self.tentativas -= 1
                self.muda_img()

    def muda_img(self):
        if self.tentativas == 5:
            self.imagem = PhotoImage(file='IMG_05.gif')
            self.exibe_imagem.create_image(10, 10, anchor=NW, image=self.imagem)
        elif self.tentativas == 4:
            self.imagem = PhotoImage(file='IMG_04.gif')
            self.exibe_imagem.create_image(10, 10, anchor=NW, image=self.imagem)
        elif self.tentativas == 3:
            self.imagem = PhotoImage(file='IMG_03.gif')
            self.exibe_imagem.create_image(10, 10, anchor=NW, image=self.imagem)
        elif self.tentativas == 2:
            self.imagem = PhotoImage(file='IMG_02.gif')
            self.exibe_imagem.create_image(10, 10, anchor=NW, image=self.imagem)
        elif self.tentativas == 1:
            self.imagem = PhotoImage(file='IMG_01.gif')
            self.exibe_imagem.create_image(10, 10, anchor=NW, image=self.imagem)
        elif self.tentativas == 0:
            self.imagem = PhotoImage(file='IMG_00.gif')
            self.exibe_imagem.create_image(10, 10, anchor=NW, image=self.imagem)
        else:
            self.imagem = PhotoImage(file='IMG_FIM.gif')
            self.exibe_imagem.create_image(10, 10, anchor=NW, image=self.imagem)
            self.oculto['text'] = self.palavra
            ctypes.windll.user32.MessageBoxW(0,
                                             f'FIM DE JOGO \nVOCÊ PERDEU!!! \nA PALAVRA COMPLETA ÉRA: {self.palavra}',
                                             'GAME OVER', 1)
            self.restart()

    def restart(self):
        # Pesquisar e entender o funcionamento do código a seguir:
        # Utiliza o os e o sys, entender essas bibliotecas
        os.execv(sys.executable, ['python'] + sys.argv)


root = Tk()
Application(root)
root.geometry('500x500+700+300')
root.title('JOGO DA FORCA v2.0')
root.mainloop()
