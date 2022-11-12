import sys
from paft import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QToolTip, QLabel, QLineEdit
import random
import time

class Paft(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        #botao seguir
        self.pushButton.clicked.connect(self.segui)
        #botao para saber do contador
        #botaoa
        self.btnA.clicked.connect(self.btna)
        #botaob
        self.btnB.clicked.connect(self.btnb)
        #botao enviar
        self.Enviar.clicked.connect(self.respost)

        #botaovoltar
        self.pushButton_3.clicked.connect(self.voltar)

        #btnresetar
        self.pushButton_2.clicked.connect(self.reset)

        #contadores
        self.contador = 1
        self.contadorA = 0
        self.contadorB = 0

        self.conteudo = self.respostas.text()
        self.opAB = "x"
        self.nome = ''
        self.idade = ''
        self.fala1 = ''
        self.fala2 =''
        self.ultimaspalavrinhas = ''
        self.ultimaspalavrinhas2 = ''
        self.ultimaspalavrinhas3 = ''
        self.item = ''


        self.validarA = ''
        self.vallidarB = ''

        #unicornio vai aparecer
        #self.x = 'x'
        #import random
        self.x = random.randint(1, 5)

        self.validadorsubesolha = 1

        self.escolheuitensA = 0
        self.escolheuitensB = 0

        #TEXTO----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





        self.Espaco = "*                                                                                                  "
        self.Escpaco_metade = "*                                               "
        self.umter = "*                        "
        self.Texto1 = "Ola jogador, esse é o começo de uma aventura!"
        self.Texto2 = "quando o jogo pedir para escolher aperte um dos botões, (A ou B) e para falar digite na caixa de texto e envie."
        self.Texto3 = "Essa hisotria tem até 8 finais possiveis,tudo depende das escolhas que voce fizer"
        self.Texto4 = "vamos começar"

        self.Texto5 = f"Em meados do século IX, no sul da França, aparece sem roupa alguma, um homem nos jardins do enorme reino de Royaume de France."
        self.Texto6 = f"Os guardas do reino percebem a ocasião anômala fora do castelo do rei e partem para a abordagem."

        self.Texto7 = "-Qual é o seu nome vassalo imundo? (perguntou o guarda)"

        self.Texto9_nome = 'Escreva o nome na caixa de texto: '

        self.Texto10 = f'E o homem respondeu: --- meu nome é {self.nome}'

        self.Texto11 = f"-Levante-se! (disse o guarda)"

        self.Texto12 = f"-Você não pode perambular pelo reino dessa maneira, vou conduzi-lo para a cadeia do castelo imediatamente, qual a sua idade? (perguntou o guarda)"

        self.Texto13_idade = 'Escreve a idade na caixa de texto: '

        self.Texto14 = f'E então o homem respondeu: eu tenho {self.idade} '
        self.Texto142 = ' anos'
        # escolha (1/3)

        self.Texto15 = "E então o guarda diz:   "

        self.Texto16 = "-Venha comigo, ou sofra as consequências, quer fazer isso do jeito fácil ou do difícil?"

        self.Texto17_escolha1 = "Decida uma das opções: Facíl (A) | Difícil (B): "

    #if self.opAB == "A":

        self.Texto18A = f"-Ok {self.nome}, então levante-se e venha comigo imediatamente."
        self.Texto19A = f"Então, {self.nome} foi até o castelo com ele."
        self.Texto20A = ''

    # contador = 18
    #elif self.opAB == "B":

        self.Texto18B = f"-Pois bem {self.nome} , você escolheu o jeito difícil, e é assim que vai ser a partir de agora(disse o guarda)."
        self.Texto19B = f"O guarda amarrou uma corda nos pés de {self.nome} ainda sem roupa e foi puxando-o com um cavalo."
        self.Texto20B = f"{self.nome} chegou bem machucado."
            # contador = 18

        self.Texto18quetaerrada = f"Chegando no castelo {self.nome} ainda sem roupa é questionado pelo guarda."

        self.Texto19quetaerrada = "-O que você veio fazer aqui, e sem roupas? (Disse o guarda)"

        self.Texto20_fala1 = "(Digite algo na caixa de texto e clique em enviar): "

        self.Texto21 = f' {self.nome} respondeu:  '

        self.Texto22 = f'-{self.fala1}'

        self.Texto23 = f'O guarda ficou surpreso com a resposta, mesmo sem entender exatamente o motivo daquela situação, demonstrou uma certa perplexidade com a resposta de {self.nome}.'

        self.Texto24 = f"Os guardas do castelo levaram {self.nome} até o rei, para decidir o que fazer.Chegando ao trono, o Rei questiona com braveza a situação. Os guardas rapidamente explicaram. E o Rei se sentiu ameaçado, então faz uma proposta ao homem: "

        self.Texto25 = "-Vassalo, vou lhe dar uma chance de se redimir após essa situação tão embaraçosa, vou te dar duas opções: Vou te libertar se você sair e conseguir caçar um unicórnio para mim! Mas se falhar, Morre! Ou, eu te prendo por 30 anos agora... você é quem decide (disse o rei)"

        self.Texto26_escolha2 = "Decida uma das opções: caçar o Unicórnio (opção A) | Prisão (opção B): "

        # essa e a esolha a que tem 2 subs
        #self.Texto26_escolha2 == "A":
        self.Texto27A = f'{self.nome} pensou bem e decidiu caçar o unicórnio!'
        self.Texto28A = f"O rei ficou impressionado"
        self.Texto29A = f"E deu alguns equipamentos para {self.nome} caçar o tão sonhado unicórnio."
        self.Texto30A = "Ele disse:"
        self.Texto31A = "-Meu caro, vou te dar 4 objetos para sua jornada, esolha 2"
        self.Texto32A = "-voce pode escolher uma lança e uma faca, ou um pouco de milho uma flauta"

        # itens
        self.Texto33_escolha_itensA = "Decida entre a lança/faca (A) ou milho/flauta (B): "

        #if self.Texto33_escolha_itensSUBA == "A":
        self.Texto34A = f'{self.nome} escolheu a lança e a faca'
        self.pairA = ' itens em mão --> item1: "lança", item2: "faca" '
        # contador = 34

        #elif self.Texto33_escolha_itens == "B":
        self.Texto34B = f'{self.nome} escolheu milho e flauta'
        self.pairB = ' itens em mão --> item1: milho, item2: flauta'
        # contador = 34

        self.Texto35Aa = f"E então {self.nome} foi em sua jornada, em busca do unicórnio , direto para a floresta."
        self.Texto36Aa = "Chegando la ele começou a se questionar e colocar suas faculdades mentais em dia, ele pensou: “por que eu estou seguindo as ordens desse rei? Eu poderia fugir!”"

        self.Texto37_escolhaAa = 'Decida uma das opções: Fugir (A) | Permanecer na jornada (B): '

        # subA resolveu fugir e morre

        #if selfTexto37_escolhasub == "A":

        self.Texto38Aa2  = f'{self.nome} resolveu fugir! '
        self.Texto39Aa2  = "largou os equipamentos e saiu correndo para a floresta"
        self.Texto40Aa2  = "Andando por uns 30 minutos ele começou a ficar cansado, e parou para descansar."
        self.Texto41Aa2  = "O rei e o exercito real armam uma emboscada e o encurralam o obre coitado."
        self.Texto42Aa2  = "O rei diz: isso foi apenas um teste, eu queria saber se você era leal, não existe isso de unicórnio, se você tivesse continuado na jornada eu teria lhe dado um pote cheio de moedas..."
        self.Texto43Aa2  = "Diga suas ultimas palavras vassalo!"
        self.Texto44Aa2_ultimaspalavras = 'Digite as ultimas palavras: '
        self.Texto45Aa2  = f'E então {self.nome} disse {self.ultimaspalavrinhas}'
        self.Texto46Aa2 = "FIM  DA HISTORIA "  # ess porra de mensagem de fim de jogo eu faço com um label cpa

        # subB resolveu ficar na floresta

        #elif self.Texto37_escolhasub == "B":

        # unicornio pode aparecer



        #if self.x > 2:
        self.Texto38uni = "Ele começou a ouvir um barulho"
        self.Texto39uni = "escolheu um item para tentar se defender"

        # escolha de item -- mostra o inventario

        self.Texto42_escolhaitem = "(ecolha entre item 1(A) ou item 2(B)): "


        # escolha de itens dentro do inventario

        #if self.Texto42_escolhaitem == "A":
        self.Texto43A = f"{self.nome} escolheu o item 1"

        #elif self.Texto42_escolhaitem == "B":
        self.Texto43B = f"{self.nome} escolheu o item 2"

        self.Texto44 = "Então o unicornio apareceu em sua frente, e ele não estava acreditando!"

        # finais unicornio

        # milho
        #if i == "milho":

        #aqui so da par fazer um if se puxar da label, ou seja, a pessoa vai ter que digitar lã.


        self.Texto45mihlo = f"{self.nome} resolve jogar um pouco de milho para o unicornio"
        self.Texto46milho = 'FIM DA HISTORIA'

        # flauta
        #elif i == "flauta":
        self.Texto45flauta = f"{self.nome}resolve tocar uma musica para o unicornio"  # self.conteudonome + "resolve tocar uma musica para o unicornio"
        self.Texto46flauta = "Ele consegue fazer amizade com o unicornio, e resolve não leva-lo par o rei."
        self.Texto47flauta = "E os dois viveram na floresta isolados felizes para sempre."
        self.Texto49flauta = 'FIM DA HISTORIA'

        # lança
        #elif i == "lança":
        self.Texto45lanca = f"{self.nome} resolve matar o unicornio"
        self.Texto46lanca = "Ele mata o unicornio e leva ate o rei"
        self.Texto47lanca = f"O rei se aproximou de {self.nome} e disse:"

        self.Texto48lanca = "Isso foi um teste para com a sua lealdade ao reino, não era para existir isso de unicórnio...Mas por ter matado uma criatura tão linda eu vou te matar"
        self.Texto49lanca = "-Diga suas ultimas palavras"

        self.Texto50_ultimaspalavrinhas = ''
        self.Texto51lanca = "(Digite algo na caixa de texto e clique em enviar): "
        self.Texto52lanca = f'Suas ultimas palvras foram: "{self.ultimaspalavrinhas2}"'
        self.Texto53lanca = f"E então {self.nome} morreu ali mesmo. "
        self.Texto54lanca = "FIM  DA HISTORIA"
        # faca
        #elif i == "faca":
        self.Texto45faca = f"{self.nome} resolve matar o unicornio"
        self.Texto46faca = f'porem o unicornio era mais forte e ele morre em combate'
        self.Texto47faca = "FIM  DA HISTORIA "



        # final que o rei aparece e da dinheiro

        #resolveu ficar
        self.Texto38Bb = f'{self.nome} resolveu ficar! '
        self.Texto39Bb = f"{self.nome} estava tendo dificuldades para encontrar o unicornio"
        self.texto40Bb = "Andando por uns 30 minutos ele começou a ficar cansado, e parou para descansar."


        #unicorno nao apareceu
        self.Texto41Bb = "Passou-se um tempo e ele começou a escutar a cavalaria se aproximando. Era o rei com o exercito real, mas o que estava acontecendo?"
        self.Texto42Bb = f"O rei chegou ate {self.nome} se aproximou e disse:"
        #unicrno nao apareceu
        self.Texto43Bb = "-Isso foi um teste para com a sua lealdade ao reino, não existe isso de unicórnio...Mas por não ter fugido da jornada eu vou te dar esse pote de ouro aqui! E também as minhas lindas filhas, as 3!"
        self.Texto44Bb = f"E então {self.nome} disse:"

        self.Texto45_falaslaBb = "(Digite algo na caixa de texto e clique em enviar): "
        self.Texto46Bb = f'{self.fala2}'
        self.Texto47Bb = f"E então {self.nome} viveu podre de rico para o resto da vida."
        self.Texto48Bb = 'FIM DA HISTORIA'

            # final da cadeia
        #elif self.Texto26_escolha2 == "B":
        self.Texto27B = "E então o Rei o mandou para a cadeia, e ele morreu pobre e solitário, por estar pelado, no lugar errado, na hora errada."
        self.Texto28B = 'Digite as ultimas palavras dele na caixa de texto e clique em enviar): '
        self.Texto29B = f'E suas ultimas palavras foram:"{self.ultimaspalavrinhas3}."'
        self.Texto30B = f'Parabéns jogador "{self.nome}"! voce consegiuu o final mais trágico da história.'
        self.Texto31B = "FIM  DA HISTORIA "


        #DEFs----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def btna(self):
        self.opAB = "A"

    def btnb(self):
        self.opAB = "B"


    def respost(self):


        if self.contador == 5:
            self.nome = self.respostas.text()

        if self.contador == 7:
            self.idade = self.respostas.text()

        if self.contador == 11:
            self.fala1 = self.respostas.text()

        if self.contador == 17:
            self.ultimaspalavrinhas = self.respostas.text()

        if self.contador == 18:
            self.item = self.respostas.text()

        if self.contador == 20:
            self.ultimaspalavrinhas2 = self.respostas.text()

        if self.contador == 51:
            self.ultimaspalavrinhas3 = self.respostas.text()





    def segui(self):
        self.x = random.randint(1, 5)

        self.contador = self.contador + 1

        if self.contador == 0:
            self.textEdit.setText("Para jogar aperto o botão 'seguir'")


        elif self.contador == 2:
            self.textEdit.setText(self.Texto1 + self.Espaco + self.Texto2)

        elif self.contador == 3:
            self.textEdit.setText(self.Texto3)

        elif self.contador == 4:
            self.textEdit.setText(self.Texto4)

        #aqui começa a historia!!!

        #testo5 ao texto7 #nova pagina (1)
        elif self.contador == 5:
            self.textEdit.setText(self.Espaco + self.Texto5 + self.Espaco + self.Espaco + self.Texto6 + self.Espaco + self.Espaco + self.Texto7 + self.Espaco + self.Texto9_nome)

        #texto8 = VARIAVEL PARA O NOME DO PERSONAGEM
        elif self.contador == 6:
            self.textEdit.setText(self.Texto5 + self.Espaco + self.Espaco + self.Texto6 + self.Espaco + self.Espaco + self.Texto7 + self.Espaco + self.Texto9_nome + self.nome)

        elif self.contador == 7:
            self.textEdit.setText(self.Espaco + self.Texto5 + self.Espaco + self.Espaco + self.Texto6 + self.Espaco + self.Espaco + self.Texto7 + self.Espaco + self.Texto9_nome + self.Espaco + self.Texto10 + self.nome + self.Espaco + self.Espaco + self.Texto11 + self.Espaco + self.Espaco + self.Texto12 + self.Espaco + self.Espaco + self.Texto13_idade)

        #idade
        elif self.contador == 8:
            self.textEdit.setText(self.Espaco + self.Texto5 + self.Espaco + self.Espaco + self.Texto6 + self.Espaco + self.Espaco + self.Texto7 + self.Espaco + self.Texto9_nome + self.Espaco + self.Texto10 + self.nome + self.Espaco + self.Espaco + self.Texto11 + self.Espaco + self.Espaco + self.Texto12 + self.Espaco + self.Espaco + self.Texto13_idade + self.Espaco + self.Texto14 + self.idade + self.Texto142)

        #nova pagina (2)
        elif self.contador == 9:
            self.textEdit.setText(self.Texto15 + self.Espaco + self.Espaco + self.Texto16 + self.Espaco + self.Espaco + self.Texto17_escolha1)

        elif self.contador == 10 and self.opAB == "A":
            self.textEdit.setText(self.Texto15 + self.Espaco + self.Espaco + self.Texto16 + self.Espaco + self.Espaco + self.Texto17_escolha1 + self.Espaco + self.Espaco + self.Texto18A + self.Espaco + self.Espaco + self.Texto19A + self.Espaco + self.Espaco + self.Texto20A)

        elif self.contador == 10 and self.opAB == "B":
            self.textEdit.setText(self.Texto15 + self.Espaco + self.Espaco + self.Texto16 + self.Espaco + self.Espaco + self.Texto17_escolha1 + self.Espaco + self.Espaco + self.Texto18B + self.Espaco + self.Espaco + self.Texto19B + self.Espaco + self.Espaco + self.Texto20B)

        elif self.contador == 11:
            self.textEdit.setText('  ' + self.Texto18quetaerrada + self.Espaco + self.Espaco + self.Texto19quetaerrada + self.Espaco + self.Espaco + self.Texto20_fala1)

        elif self.contador == 12:
            self.textEdit.setText(self.Texto18quetaerrada + self.Espaco + self.Espaco + self.Texto19quetaerrada + self.Espaco + self.Espaco + self.Texto20_fala1 + self.Espaco + self.Espaco + self.nome + self.Texto21 + ' - ' + self.fala1)

        elif self.contador == 13:
            self.textEdit.setText(self.Texto18quetaerrada + self.Espaco + self.Espaco + self.Texto19quetaerrada + self.Espaco + self.Espaco + self.Texto20_fala1 + self.Espaco + self.Espaco + self.nome + self.Texto21 + self.fala1 + self.Espaco + self.Espaco + self.Texto23)

        elif self.contador == 14:
            self.textEdit.setText(self.Texto24 + self.Espaco + self.Espaco + self.Texto26_escolha2)

        elif self.contador == 15 and self.opAB == "A":
            self.textEdit.setText(self.Texto24 + self.Espaco + self.Espaco + self.Texto26_escolha2 + self.Espaco + self.Espaco + self.Texto27A + self.Espaco + self.Espaco + self.Texto28A + self.Espaco + self.Espaco + self.Texto30A + self.Espaco + self.Espaco + self.Texto31A + self.Espaco + self.Espaco + self.Texto32A + self.Espaco + self.Espaco + self.Texto33_escolha_itensA)

            # e ai nas sub A coloca um monte de and, exemplo: elif self.contador == 16 and self.opAB == 'A' and self.validarA == 'A'

        #prisao
        elif self.contador == 15 and self.opAB == "B":
            self.textEdit.setText(self.Texto24 + self.Espaco + self.Espaco + self.Texto26_escolha2 + self.Espaco + self.Espaco + self.Texto27B + self.Espaco + self.Espaco + self.Texto28B + self.Espaco + self.Espaco + self.Texto30B + self.Espaco + self.Espaco + self.Texto31B)


            self.contador = 2000

        #escolhasSUBA
        elif self.contador == 16 and self.opAB == 'A':
            self.textEdit.setText(self.nome + self.Texto34A + self.Espaco + self.Espaco + self.pairA + self.Espaco + self.Espaco + self.Texto35Aa + self.Espaco + self.Espaco + self.Texto36Aa + self.Espaco + self.Espaco + self.Texto37_escolhaAa)
            self.escolheuitensA = 1

        elif self.contador == 16 and self.opAB == 'B':
            self.textEdit.setText(self.nome + self.Texto34B + self.Espaco + self.Espaco + self.pairB + self.Espaco + self.Espaco + self.Texto35Aa + self.Espaco + self.Espaco + self.Texto36Aa + self.Espaco + self.Espaco + self.Texto37_escolhaAa)
            self.escolheuitensB = 1

        #resolveu fugir
        elif self.contador == 17 and self.opAB == 'A':
            self.textEdit.setText(self.nome + self.Espaco + self.Espaco + self.Texto38Aa2 + self.Espaco + self.Espaco + self.Texto39Aa2 + self.Espaco + self.Espaco + self.Texto40Aa2 + self.Espaco + self.Espaco + self.Texto41Aa2 + self.Espaco + self.Espaco + self.Texto43Aa2 + self.Espaco + self.Espaco + self.Texto44Aa2_ultimaspalavras)
        elif self.contador == 18 and self.opAB == 'A':
            self.textEdit.setText('Suas utimas palavas foram:' + self.ultimaspalavrinhas)
            self.contador = 2000

        #resolveu ficar
        elif self.contador == 17 and self.opAB == 'B':
            self.textEdit.setText(self.Texto38Bb + self.Espaco + self.Espaco + self.Texto39Bb + self.Espaco + self.Espaco + self.texto40Bb)


        #unicornio apareceu
        elif self.contador == 18 and self.x > 2:
            self.textEdit.setText(self.Texto38uni + self.Espaco + self.Espaco + self.Texto39uni + self.Espaco + self.Espaco + self.Espaco + self.Espaco + 'pressione seguir para escolher o item')
            self.validadorsubesolha = 1

        #opcoe de item
        elif self.contador == 19 and self.escolheuitensA == 1:
            self.textEdit.setText(self.Texto38uni + self.Espaco + self.Espaco + self.Texto39uni + self.Espaco + self.Espaco + self.Espaco + self.Espaco + 'jogador pode escolher entre: faca(a) e lança(b)')
            self.escolheuitensA = 2


        elif self.contador == 19 and self.escolheuitensB == 1:
            self.textEdit.setText(self.Texto38uni + self.Espaco + self.Espaco + self.Texto39uni + self.Espaco + self.Espaco + self.Espaco + self.Espaco + 'jogador pode escolher entre: milho(a) e flauta(b)')
            self.escolheuitensB = 2




        #mortes unicornio

        #faca
        elif self.contador == 20 and self.validadorsubesolha == 1 and self.escolheuitensA == 2 and self.opAB == 'A':
            self.textEdit.setText('jogador escolheu: faca' + self.Espaco + self.Espaco + self.Texto44 + self.Espaco + self.Espaco + self.Texto45faca + self.Espaco + self.Espaco + self.Texto46faca + self.Espaco + self.Espaco + self.Texto47faca)
            self.contador = 2000
        #lança
        elif self.contador == 20 and self.validadorsubesolha == 1 and self.escolheuitensA == 2 and self.opAB == 'B':
            self.textEdit.setText('jogador escolheu: lança' + self.Espaco + self.Espaco + self.Texto44 + self.Espaco + self.Espaco + self.Texto45lanca + self.Espaco + self.Espaco + self.Texto46lanca + self.Espaco + self.Espaco + self.Texto47lanca + self.Espaco + self.Espaco + self.Texto48lanca + self.Espaco + self.Espaco + self.Texto49lanca + self.Espaco + self.Espaco + self.Texto51lanca + self.Espaco + self.Espaco)


        elif self.contador == 21 and self.validadorsubesolha == 1 and self.escolheuitensA == 2 and self.opAB == 'B':
            self.textEdit.setText('jogador escolheu: lança' + self.Espaco + self.Espaco + self.Texto44 + self.Espaco + self.Espaco + self.Texto45lanca + self.Espaco + self.Espaco + self.Texto46lanca + self.Espaco + self.Espaco + self.Texto47lanca + self.Espaco + self.Espaco + self.Texto48lanca + self.Espaco + self.Espaco + self.Texto49lanca + self.Espaco + self.Espaco + self.Texto51lanca + self.Espaco + self.Espaco + self.Texto52lanca + self.ultimaspalavrinhas2 + self.Espaco + self.Espaco + 'E então' + self.nome + 'morreu ali mesmo' + self.Espaco + self.Espaco + self.Texto54lanca)
            self.contador = 2000

        #milho
        elif self.contador == 20 and self.validadorsubesolha == 1 and self.escolheuitensB == 2 and self.opAB == 'A':
            self.textEdit.setText('jogador escolheu: milho' + self.Espaco + self.Espaco + self.Texto44 + self.Texto45mihlo + self.Espaco + self.Espaco + self.Texto46milho)
            self.contador = 3000
        #flauta
        elif self.contador == 20 and self.validadorsubesolha == 1 and self.escolheuitensB == 2 and self.opAB == 'B':
            self.textEdit.setText('jogador escolheu: flauta' + self.Espaco + self.Espaco + self.Texto44 + self.Espaco + self.Espaco + self.Texto45flauta + self.Espaco + self.Espaco + self.Texto46flauta + self.Espaco + self.Espaco + self.Texto47flauta + self.Espaco + self.Espaco + self.Texto49flauta)
            self.contador = 3000

    #unicornio nao apareceu
        elif self.contador == 18 and self.x < 1:
            self.textEdit.setText(self.Texto41Bb + self.Espaco + self.Espaco + self.Texto42Bb + self.Espaco + self.Espaco + self.Texto43Bb + self.Espaco + self.Espaco + self.Texto44Bb + self.Espaco + self.Espaco + self.Texto45_falaslaBb + self.Espaco + self.Espaco + self.Texto46Bb + self.Espaco + self.Espaco + self.Texto47Bb + self.Espaco + self.Espaco + self.Texto48Bb)
            self.contador = 3000
    #nesse caso o rei aparece e mama ele





    ##final ruimsa
        elif self.contador == 2001:
            self.textEdit.setText('voce conseguiu um final tragico!')

    #finalbom
        elif self.contador == 3001:
            self.textEdit.setText('voce conseguiu um final muito bom!')































    def voltar(self):
        self.contador = self.contador - 1
        self.x = random.randint(1, 5)


        if self.contador == 0:
            self.textEdit.setText("Para jogar aperto o botão 'seguir'")


        elif self.contador == 2:
            self.textEdit.setText(self.Texto1 + self.Espaco + self.Texto2)

        elif self.contador == 3:
            self.textEdit.setText(self.Texto3)

        elif self.contador == 4:
            self.textEdit.setText(self.Texto4)

        #aqui começa a historia!!!

        #testo5 ao texto7 #nova pagina (1)
        elif self.contador == 5:
            self.textEdit.setText(self.Espaco + self.Texto5 + self.Espaco + self.Espaco + self.Texto6 + self.Espaco + self.Espaco + self.Texto7 + self.Espaco + self.Texto9_nome)

        #texto8 = VARIAVEL PARA O NOME DO PERSONAGEM
        elif self.contador == 6:
            self.textEdit.setText(self.Texto5 + self.Espaco + self.Espaco + self.Texto6 + self.Espaco + self.Espaco + self.Texto7 + self.Espaco + self.Texto9_nome + self.nome)

        elif self.contador == 7:
            self.textEdit.setText(self.Espaco + self.Texto5 + self.Espaco + self.Espaco + self.Texto6 + self.Espaco + self.Espaco + self.Texto7 + self.Espaco + self.Texto9_nome + self.Espaco + self.Texto10 + self.nome + self.Espaco + self.Espaco + self.Texto11 + self.Espaco + self.Espaco + self.Texto12 + self.Espaco + self.Espaco + self.Texto13_idade)

        #idade
        elif self.contador == 8:
            self.textEdit.setText(self.Espaco + self.Texto5 + self.Espaco + self.Espaco + self.Texto6 + self.Espaco + self.Espaco + self.Texto7 + self.Espaco + self.Texto9_nome + self.Espaco + self.Texto10 + self.nome + self.Espaco + self.Espaco + self.Texto11 + self.Espaco + self.Espaco + self.Texto12 + self.Espaco + self.Espaco + self.Texto13_idade + self.Espaco + self.Texto14 + self.idade + self.Texto142)

        #nova pagina (2)
        elif self.contador == 9:
            self.textEdit.setText(self.Texto15 + self.Espaco + self.Espaco + self.Texto16 + self.Espaco + self.Espaco + self.Texto17_escolha1)

        elif self.contador == 10 and self.opAB == "A":
            self.textEdit.setText(self.Texto15 + self.Espaco + self.Espaco + self.Texto16 + self.Espaco + self.Espaco + self.Texto17_escolha1 + self.Espaco + self.Espaco + self.Texto18A + self.Espaco + self.Espaco + self.Texto19A + self.Espaco + self.Espaco + self.Texto20A)

        elif self.contador == 10 and self.opAB == "B":
            self.textEdit.setText(self.Texto15 + self.Espaco + self.Espaco + self.Texto16 + self.Espaco + self.Espaco + self.Texto17_escolha1 + self.Espaco + self.Espaco + self.Texto18B + self.Espaco + self.Espaco + self.Texto19B + self.Espaco + self.Espaco + self.Texto20B)

        elif self.contador == 11:
            self.textEdit.setText('  ' + self.Texto18quetaerrada + self.Espaco + self.Espaco + self.Texto19quetaerrada + self.Espaco + self.Espaco + self.Texto20_fala1)

        elif self.contador == 12:
            self.textEdit.setText(self.Texto18quetaerrada + self.Espaco + self.Espaco + self.Texto19quetaerrada + self.Espaco + self.Espaco + self.Texto20_fala1 + self.Espaco + self.Espaco + self.nome + self.Texto21 + ' - ' + self.fala1)

        elif self.contador == 13:
            self.textEdit.setText(self.Texto18quetaerrada + self.Espaco + self.Espaco + self.Texto19quetaerrada + self.Espaco + self.Espaco + self.Texto20_fala1 + self.Espaco + self.Espaco + self.nome + self.Texto21 + self.fala1 + self.Espaco + self.Espaco + self.Texto23)

        elif self.contador == 14:
            self.textEdit.setText(self.Texto24 + self.Espaco + self.Espaco + self.Texto26_escolha2)

        elif self.contador == 15 and self.opAB == "A":
            self.textEdit.setText(self.Texto24 + self.Espaco + self.Espaco + self.Texto26_escolha2 + self.Espaco + self.Espaco + self.Texto27A + self.Espaco + self.Espaco + self.Texto28A + self.Espaco + self.Espaco + self.Texto30A + self.Espaco + self.Espaco + self.Texto31A + self.Espaco + self.Espaco + self.Texto32A + self.Espaco + self.Espaco + self.Texto33_escolha_itensA)

            # e ai nas sub A coloca um monte de and, exemplo: elif self.contador == 16 and self.opAB == 'A' and self.validarA == 'A'

        #prisao
        elif self.contador == 15 and self.opAB == "B":
            self.textEdit.setText(self.Texto24 + self.Espaco + self.Espaco + self.Texto26_escolha2 + self.Espaco + self.Espaco + self.Texto27B + self.Espaco + self.Espaco + self.Texto28B + self.Espaco + self.Espaco + self.Texto30B + self.Espaco + self.Espaco + self.Texto31B)


            self.contador = 2000

        #escolhasSUBA
        elif self.contador == 16 and self.opAB == 'A':
            self.textEdit.setText(self.nome + self.Texto34A + self.Espaco + self.Espaco + self.pairA + self.Espaco + self.Espaco + self.Texto35Aa + self.Espaco + self.Espaco + self.Texto36Aa + self.Espaco + self.Espaco + self.Texto37_escolhaAa)
            self.escolheuitensA = 1

        elif self.contador == 16 and self.opAB == 'B':
            self.textEdit.setText(self.nome + self.Texto34B + self.Espaco + self.Espaco + self.pairB + self.Espaco + self.Espaco + self.Texto35Aa + self.Espaco + self.Espaco + self.Texto36Aa + self.Espaco + self.Espaco + self.Texto37_escolhaAa)
            self.escolheuitensB = 1

        #resolveu fugir
        elif self.contador == 17 and self.opAB == 'A':
            self.textEdit.setText(self.nome + self.Espaco + self.Espaco + self.Texto38Aa2 + self.Espaco + self.Espaco + self.Texto39Aa2 + self.Espaco + self.Espaco + self.Texto40Aa2 + self.Espaco + self.Espaco + self.Texto41Aa2 + self.Espaco + self.Espaco + self.Texto43Aa2 + self.Espaco + self.Espaco + self.Texto44Aa2_ultimaspalavras)
        elif self.contador == 18 and self.opAB == 'A':
            self.textEdit.setText('Suas utimas palavas foram:' + self.ultimaspalavrinhas)
            self.contador = 2000

        #resolveu ficar
        elif self.contador == 17 and self.opAB == 'B':
            self.textEdit.setText(self.Texto38Bb + self.Espaco + self.Espaco + self.Texto39Bb + self.Espaco + self.Espaco + self.texto40Bb)


        #unicornio apareceu
        elif self.contador == 18 and self.x > 2:
            self.textEdit.setText(self.Texto38uni + self.Espaco + self.Espaco + self.Texto39uni + self.Espaco + self.Espaco + self.Espaco + self.Espaco + 'pressione seguir para escolher o item')
            self.validadorsubesolha = 1

        #opcoe de item
        elif self.contador == 19 and self.escolheuitensA == 1:
            self.textEdit.setText(self.Texto38uni + self.Espaco + self.Espaco + self.Texto39uni + self.Espaco + self.Espaco + self.Espaco + self.Espaco + 'jogador pode escolher entre: faca(a) e lança(b)')
            self.escolheuitensA = 2


        elif self.contador == 19 and self.escolheuitensB == 1:
            self.textEdit.setText(self.Texto38uni + self.Espaco + self.Espaco + self.Texto39uni + self.Espaco + self.Espaco + self.Espaco + self.Espaco + 'jogador pode escolher entre: milho(a) e flauta(b)')
            self.escolheuitensB = 2




        #mortes unicornio

        #faca
        elif self.contador == 20 and self.validadorsubesolha == 1 and self.escolheuitensA == 2 and self.opAB == 'A':
            self.textEdit.setText('jogador escolheu: faca' + self.Espaco + self.Espaco + self.Texto44Bb + self.Espaco + self.Espaco + self.Texto45faca + self.Espaco + self.Espaco + self.Texto46faca + self.Espaco + self.Espaco + self.Texto47faca)
            self.contador = 2000
        #lança
        elif self.contador == 20 and self.validadorsubesolha == 1 and self.escolheuitensA == 2 and self.opAB == 'B':
            self.textEdit.setText('jogador escolheu: lança' + self.Espaco + self.Espaco + self.Texto44 + self.Espaco + self.Espaco + self.Texto45lanca + self.Espaco + self.Espaco + self.Texto46lanca + self.Espaco + self.Espaco + self.Texto47lanca + self.Espaco + self.Espaco + self.Texto48lanca + self.Espaco + self.Espaco + self.Texto49lanca + self.Espaco + self.Espaco + self.Texto51lanca + self.Espaco + self.Espaco)


        elif self.contador == 21 and self.validadorsubesolha == 1 and self.escolheuitensA == 2 and self.opAB == 'B':
            self.textEdit.setText('jogador escolheu: lança' + self.Espaco + self.Espaco + self.Texto44 + self.Espaco + self.Espaco + self.Texto45lanca + self.Espaco + self.Espaco + self.Texto46lanca + self.Espaco + self.Espaco + self.Texto47lanca + self.Espaco + self.Espaco + self.Texto48lanca + self.Espaco + self.Espaco + self.Texto49lanca + self.Espaco + self.Espaco + self.Texto51lanca + self.Espaco + self.Espaco + self.Texto52lanca + self.ultimaspalavrinhas2 + self.Espaco + self.Espaco + 'E então' + self.nome + 'morreu ali mesmo' + self.Espaco + self.Espaco + self.Texto54lanca)
            self.contador = 2000

        #milho
        elif self.contador == 20 and self.validadorsubesolha == 1 and self.escolheuitensB == 2 and self.opAB == 'A':
            self.textEdit.setText('jogador escolheu: milho' + self.Espaco + self.Espaco + self.Texto44 + self.Texto45mihlo + self.Espaco + self.Espaco + self.Texto46milho)
            self.contador = 3000
        #flauta
        elif self.contador == 20 and self.validadorsubesolha == 1 and self.escolheuitensB == 2 and self.opAB == 'B':
            self.textEdit.setText('jogador escolheu: flauta' + self.Espaco + self.Espaco + self.Texto44 + self.Espaco + self.Espaco + self.Texto45flauta + self.Espaco + self.Espaco + self.Texto46flauta + self.Espaco + self.Espaco + self.Texto47flauta + self.Espaco + self.Espaco + self.Texto49flauta)
            self.contador = 3000

    #unicornio nao apareceu
        elif self.contador == 18 and self.x < 1:
            self.textEdit.setText(self.Texto41Bb + self.Espaco + self.Espaco + self.Texto42Bb + self.Espaco + self.Espaco + self.Texto43Bb + self.Espaco + self.Espaco + self.Texto44Bb + self.Espaco + self.Espaco + self.Texto45_falaslaBb + self.Espaco + self.Espaco + self.Texto46Bb + self.Espaco + self.Espaco + self.Texto47Bb + self.Espaco + self.Espaco + self.Texto48Bb)
            self.contador = 3000






    ##final ruimsa
        elif self.contador == 2000:
            self.textEdit.setText('voce conseguiu um final tragico!')

    #finalbom
        elif self.contador == 3000:
            self.textEdit.setText('voce conseguiu um final muito bom!')

    def reset(self):
        self.contador = 0
        self.textEdit.setText("Para jogar aperto o botão 'seguir'")



if __name__ == '__main__':
    qt = QApplication(sys.argv)
    paft = Paft()
    paft.show()
    qt.exec_()
