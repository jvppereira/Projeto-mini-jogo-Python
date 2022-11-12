#bibliotecas que eu vou usar -- random, time,

jogar = input('\033[31m'+ 'Para jogar digite sim: ' +'\033[0;0m')

print("\n")

while jogar != "sim":

    jogar = input('\033[31m'+"para jogar digite sim "+'\033[0;0m')

if jogar == "sim":
    print("\n")
    Falas = []
    print('\033[32m'+"Ola jogador, esse é o começo de uma aventura!"+'\033[0;0m')
    print('\033[32m'"quando o jogo pedir para escolher aperte um dos botões, (A ou B) e para falar digite na caixa de texto e envie."+'\033[0;0m')
    print('\033[32m'"Essa hisotria tem até 8 finais possiveis,tudo depende das escolhas que voce fizer"+'\033[0;0m')
    print('\033[32m'"vamos começar"+'\033[0;0m')

    print("\n")

    Texto1 = f"Em meados do século IX, no sul da França, aparece sem roupa alguma, um homem nos jardins do enorme reino de Royaume de France."
    Texto2 = f"Os guardas do reino percebem a ocasião anômala fora do castelo do rei e partem para a abordagem."
    print(Texto1)
    print(Texto2)

    Texto3 = "-Qual é o seu nome vassalo imundo? (perguntou o guarda)"
    print(Texto3)
    nome = input('\033[31m'+ 'Escreva o nome na caixa de texto: ' +'\033[0;0m')


    Texto4 = '\033[32m'+f'E o homem respondeu: meu nome é {nome}'+'\033[0;0m' #verde

    print(Texto4)

    Texto5 = f"-Levante-se! (disse o guarda)"
    print(Texto5)

    Texto6 = f"-Você não pode perambular pelo reino dessa maneira, vou conduzi-lo para a cadeia do castelo imediatamente, qual a sua idade? (perguntou o guarda)"
    print(Texto6)

    idade = input('\033[31m'+ 'Escreve a idade na caixa de texto: ' +'\033[0;0m')

    Texto7 = '\033[32m'+f'E então o homem respondeu: eu tenho {idade} anos'+'\033[0;0m'
    print(Texto7)

    #escolha (1/3)

    Texto8 = "E então o guarda diz"
    print(Texto8)

    Texto9 = "-Venha comigo, ou sofra as consequências, quer fazer isso do jeito fácil ou do difícil?"
    print(Texto9)

    escolha1 = input('\033[31m'+ "Decida uma das opções: Facíl (A) | Difícil (B): " +'\033[0;0m')

    if escolha1 == "A":

        Texto10 = f"-Ok {nome}, então levante-se e venha comigo imediatamente."
        print(Texto10)

        print(f"Então, {nome} foi até o castelo com ele.")

    elif escolha1 == "B":

        Texto10 = f"-Pois bem {nome} , você escolheu o jeito difícil, e é assim que vai ser a partir de agora(disse o guarda)."
        print(Texto10)

        print(f"O guarda amarrou uma corda nos pés de {nome} ainda sem roupa e foi puxando-o com um cavalo.")
        print(f"{nome} chegou bem machucado.")


    Texto11 = f"Chegando no castelo {nome} ainda sem roupa é questionado pelo guarda."
    print(Texto11)

    Texto12 = "-O que você veio fazer aqui, e sem roupas? (Disse o guarda)"
    print(Texto12)

    fala1 = input('\033[31m'+ "(Digite algo na caixa de texto e clique em enviar): " +'\033[0;0m')

    Texto13 = '\033[32m'+f'E então {nome} respondeu:'+'\033[0;0m'
    print(Texto13)

    print('\033[32m'+f'-{fala1}'+'\033[0;0m')

    Texto14 = f'O guarda ficou surpreso com a resposta, mesmo sem entender exatamente o motivo daquela situação,\ndemonstrou uma certa perplexidade com a resposta de {nome}.'
    print(Texto14)

    Texto15 = f"Os guardas do castelo levaram {nome} até o rei, para decidir o que fazer.\nChegando ao trono, o Rei questiona com braveza a situação. Os guardas rapidamente explicaram.\nE o Rei se sentiu ameaçado, então faz uma proposta ao homem: "
    print(Texto15)

    print("\n")

    Texto16 = "-Vassalo, vou lhe dar uma chance de se redimir após essa situação tão embaraçosa, vou te dar duas opções:\nVou te libertar se você sair e conseguir caçar um unicórnio para mim! \nMas se falhar, Morre! Ou, eu te prendo por 30 anos agora... você é quem decide (disse o rei)"
    print(Texto16)

    escolha2 = input('\033[31m'+ "Decida uma das opções: caçar o Unicórnio (opção A) | Prisão (opção B): " +'\033[0;0m')


    #essa e a esolha a que tem 2 subs
    if escolha2 == "A":
        print('\033[32m'+f'{nome} pensou bem e decidiu caçar o unicórnio!'+'\033[0;0m')

        print(f"O rei ficou impressionado")
        print(f"E deu alguns equipamentos para {nome} caçar o tão sonhado unicórnio.")
        print("Ele disse:")
        print("-Meu caro, vou te dar 4 objetos para sua jornada, esolha 2")
        print("-voce pode escolher uma lança e uma faca, ou um pouco de milho uma flauta")


        #itens
        escolha_itens = input('\033[31m'+ "Decida entre a lança/faca (A) ou milho/flauta (B): " +'\033[0;0m')
        itens = {}

        if escolha_itens == "A":
            print('\033[32m'+f'{nome} escolheu a lança e a faca'+'\033[0;0m')

            pair = {'item1': "lança", 'item2': "faca"}
            itens.update(pair)

        elif escolha_itens == "B":
            print('\033[32m'+f'{nome} escolheu '+'\033[0;0m')

            pair = {'item1': "milho", 'item2': "flauta"}
            itens.update(pair)

        print(f"E então {nome} foi em sua jornada, em busca do unicórnio , direto para a floresta.")

        print("Chegando la ele começou a se questionar e colocar suas faculdades mentais em dia, ele pensou: \n“por que eu estou seguindo as ordens desse rei? Eu poderia fugir!”")
        escolhasubA = input('\033[31m'+ 'Decida uma das opções: Fugir (A) | Permanecer na jornada (B): ' +'\033[0;0m')


        #subA resolveu fugir e morre
        if escolhasubA == "A":
            print('\033[32m'+f'{nome} resolveu fugir! '+'\033[0;0m')
            print("largou os equipamentos e saiu correndo para a floresta")
            print("Andando por uns 30 minutos ele começou a ficar cansado, e parou para descansar.")
            print("O rei e o exercito real armam uma emboscada e o encurralam o obre coitado.")
            print("O rei diz: isso foi apenas um teste, eu queria saber se você era leal, não existe isso de unicórnio, se você tivesse continuado na jornada eu teria lhe dado um pote cheio de moedas...")
            print("Diga suas ultimas palavras vassalo!")

            ultimaspalavras = input('\033[31m' + 'Digite as ultimas palavras: ' + '\033[0;0m')
            print('\033[32m' + f'E então {nome} disse {ultimaspalavras}' + '\033[0;0m\n')
            print('\033[31m' + "FIM  DA HISTORIA " + '\033[0;0m')  # RUIM

        #subB resolveu ficar na floresta
        elif escolhasubA == "B":

            #unicornio pode aparecer
            import random
            x = random.randint(1,5)

            if x > 2:
                print("Ele começou a ouvir um barulho")
                print("escolheu um item para tentar se defender")
                # escolha de item -- mostra o inventario
                print("seu inventario:")
                for i in itens.keys():
                    print(i, ":", itens[i])
                escolha_item = input('\033[31m' + "(ecolha entre item 1(A) ou item 2(B)): " + '\033[0;0m')

                itemmao = []
                #escolha de itens dentro do inventario
                if escolha_item == "A":
                    pair2 = itens["item1"]
                    itemmao.append(pair2)
                    for i in itemmao:
                        print('\033[32m' + f"{nome} escolheu o item 2, {i}" + '\033[0;0m')

                elif escolha_itens == "B":
                    pair2 = itens["item2"]
                    itemmao.append(pair2)
                    for i in itemmao:
                        print('\033[32m' + f"{nome} escolheu o item 2, {i}" + '\033[0;0m')

                print("Então o unicornio apareceu em sua frente, e ele não estava acreditando!")


                #finais unicornio
                for i in itemmao:
                    #milho
                    if i == "milho":
                        print(f"{nome} resolve jogar um pouco de milho para o unicornio\n")
                        print('\033[32m' + 'FIM DA HISTORIA' + '\033[0;0m')  # BOM
                    #flauta
                    elif i == "flauta":
                        print(f"{nome} resolve tocar uma musica para o unicornio")
                        print("Ele consegue fazer amizade com o unicornio, e resolve não leva-lo par o rei.")
                        print("E os dois viveram na floresta isolados felizes para sempre.\n")
                        print('\033[32m' + 'FIM DA HISTORIA' + '\033[0;0m')  # BOM

                    #lança
                    elif i == "lança":
                        print(f"{nome} resolve matar o unicornio")
                        print("Ele mata o unicornio e leva ate o rei")
                        print(f"O rei se aproximou de {nome} e disse:")

                        print("Isso foi um teste para com a sua lealdade ao reino, não era para existir isso de unicórnio...\nMas por ter matado uma criatura tão linda eu vou te matar")
                        print("-Diga suas ultimas palavras")

                        ultimaspalavrinhas = input('\033[31m' + "(Digite algo na caixa de texto e clique em enviar): " + '\033[0;0m')
                        print('\033[32m' + f'Suas ultimas palvras foram: "{ultimaspalavrinhas}"' + '\033[0;0m')
                        print(f"E então {nome} morreu ali mesmo.\n ")
                        print('\033[31m' + "FIM  DA HISTORIA " + '\033[0;0m')  # RUIM
                    #faca
                    elif i == "faca":
                        print(f"{nome} resolve matar o unicornio")
                        print(f'porem o unicornio era mais forte e ele morre em combate\n')
                        print('\033[31m' + "FIM  DA HISTORIA " + '\033[0;0m')  # RUIM
        #final que o rei aparece e da dinheiro
            else:
                print('\033[32m' + f'{nome} resolveu ficar! ' + '\033[0;0m')
                print(f"{nome} estava tendo dificuldades para encontrar o unicornio")
                print("Andando por uns 30 minutos ele começou a ficar cansado, e parou para descansar.")

                print("Passou-se um tempo e ele começou a escutar a cavalaria se aproximando. \nEra o rei com o exercito real, mas o que estava acontecendo?")
                print(f"O rei chegou ate {nome} se aproximou e disse:")

                print("-Isso foi um teste para com a sua lealdade ao reino, não existe isso de unicórnio...\nMas por não ter fugido da jornada eu vou te dar esse pote de ouro aqui! E também as minhas lindas filhas, as 3!")
                print(f"E então {nome} disse:")

                falasla = input('\033[31m'+ "(Digite algo na caixa de texto e clique em enviar): "+'\033[0;0m')
                print('\033[32m' +f'{falasla}' +'\033[0;0m')
                print(f"E então {nome} viveu podre de rico para o resto da vida.\n ")
                print('\033[32m' + 'FIM DA HISTORIA' + '\033[0;0m')  # BOM
    #final da cadeia
    elif escolha2 == "B":
        print("E então o Rei o mandou para a cadeia, e ele morreu pobre e solitário, por estar pelado, no lugar errado, na hora errada.")

        ultimasp = input('\033[31m'+ '(Digite as ultimas palavras dele na caixa de texto e clique em enviar): ' +'\033[0;0m')
        print('\033[32m'+f'E suas ultimas palavras foram:\n"{ultimasp}."'+'\033[0;0m')
        print(f'Parabéns jogador "{nome}"! voce consegiuu o final mais trágico da história.\n')
        print('\033[31m' + "FIM  DA HISTORIA " + '\033[0;0m')  # RUIM







