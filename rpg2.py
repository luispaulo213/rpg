import random
import time
dificuldade = 0
class personagem:
    def criacaodepersonagem():
        print('Olá eu sou ANA, sua assistente de vida antes de relembrar os acontecimentos seria bom que você me ajudasse com algumas outras coisas')
       # time.sleep(3)
        nomeusuario = input('O seu nome ')
        #time.sleep(3)
        racausuarionumero = int(input('A sua raça. As opções são 1. tielfing 2. Orc 3. Elfo 4. Halfling 5. Draconato 6. Anão, favor digitar o numero correspondente a sua escolha '))
        while racausuarionumero not in (1,2,3,4,5,6):
            racausuarionumero = int(input('Por favor digite um número entre 1 e 6 para escolher sua raça '))
        if racausuarionumero == 1:
            racausuario = 'tielfing'
        elif racausuarionumero == 2:
            racausuario = 'orc'
        elif racausuarionumero == 3:
            racausuario = 'Elfo'
        elif racausuarionumero == 4:
            racausuario = 'Halfling'
        elif racausuarionumero == 5:
            racausuario = 'Draconato'
        elif racausuarionumero == 6:
            racausuario = 'Anão'
        # time.sleep(3)
        classeusuarionumero = int(input('E por ultimo qual a sua classe. As opções são 1. Monge, 2. Mago, 3. Ladino, 4. Paladino, 5. clérigo, 6. Druida '))
        while classeusuarionumero not in (1,2,3,4,5,6):
            classeusuarionumero = int(input('Por favor digite um número entre 1 e 6 para escolher sua classe '))
        if classeusuarionumero == 1:
            classeusuario = 'monge'
        elif classeusuarionumero == 2:
            classeusuario = 'mago'
        elif classeusuarionumero == 3:
            classeusuario = 'ladino'
        elif classeusuarionumero == 4:
            classeusuario = 'paladino'
        elif classeusuarionumero == 5:
            classeusuario = 'clérigo'
        elif classeusuarionumero == 6:
            classeusuario = 'druida'
        corretocriacaodepersonagem = input(f'Ok {nomeusuario} você é um(a) {racausuario} e {classeusuario}(Sim ou Não)  ')
        while corretocriacaodepersonagem in ('nao','não','Nao','Não','n','N'):
            print('Ok agora como você já sabe o qu tem que colocar eu só vou te falar as opções.')
            racausuarionumero = int(input('1. tielfing, 2. orc, 3. elfo, 4. Halfing, 5. draconato, 6. anão '))
            if racausuarionumero == 1:
                racausuario = 'tielfing'
            elif racausuarionumero == 2:
                racausuario = 'orc'
            elif racausuarionumero == 3:
                racausuario = 'Elfo'
            elif racausuarionumero == 4:
                racausuario = 'Halfling'
            elif racausuarionumero == 5:
                racausuario = 'Draconato'
            elif racausuarionumero == 6:
                racausuario = 'Anão'
            classeusuarionumero = int(input('1. monge, 2. mago, 3. ladino, 4. paladino, 5. clérigo, 6. druida '))
            if classeusuarionumero == 1:
                classeusuario = 'monge'
            elif classeusuarionumero == 2:
                classeusuario = 'mago'
            elif classeusuarionumero == 3:
                classeusuario = 'ladino'
            elif classeusuarionumero == 4:
                classeusuario = 'paladino'
            elif classeusuarionumero == 5:
                classeusuario = 'clérigo'
            elif classeusuarionumero == 6:
                classeusuario = 'druida'
            corretocriacaodepersonagem = input(f'Ok {nomeusuario} você é um(a) {racausuario} e {classeusuario}(Sim ou Não)' )
        if corretocriacaodepersonagem in ('sim','Sim','s','S'):
            pontos(racausuarionumero, classeusuarionumero)            #agora tem que mostrar pro jogador que ele tem 30 pontos para distribuir como
            #quiser que é força, destreza, constituição, inteligencia, sabedoria e carisma 
            #depois disso vai ter x pontos para x pericias a qual ele distribuira 5 em cada no maximo
def pontos(racausuario, classeusuario):
    pontostotais = 30
    print('Bom agora que está tudo certo eu acharia bom que você definisse os pontos em cada atributo')
    forcausuario = int(input('Primeiro eu gostaria de te informar que você tem 30 pontos para gastar no total, agora quantos pontos você vai colocar em força? '))
    while pontostotais < forcausuario or 0 > forcausuario:
        forcausuario = int(input('por favor digite um número valido entre 0 e 30 '))
    pontostotais = pontostotais - forcausuario
    destrezausuario = int(input('Bom agora que você definiu sua força para entender quanto de dano você vai causar, quantos pontos você vai colocar em destreza'))
    while pontostotais < destrezausuario or 0 > destrezausuario:
        destrezausuario = int(input(f'por favor digite um número valido entre 0 e {pontostotais} '))
    pontostotais = pontostotais - destrezausuario
    constituicaousuario = int(input('Agora qeuvocê definiu a sua capacidade de fazer as coisas em destreza coloque os pontos de constituição para definir sua quantidade de vida'))
    while pontostotais < constituicaousuario or 0 > constituicaousuario:
        constituicaousuario = int(input(f'por favor digite um número valido entre 0 e {pontostotais} '))
    pontostotais = pontostotais - constituicaousuario
    inteligenciausuario = int(input('Agora para definir o seu intelecto quantos pontos gostaria de por em inteligencia? '))
    while pontostotais < inteligenciausuario or 0 > inteligenciausuario:
        inteligenciausuario = int(input(f'por favor digite um número valido entre 0 e {pontostotais} '))
    pontostotais = pontostotais - inteligenciausuario
    sabedoriausuario = int(input('na jornada de um guerreiro é importante saber a diferença entre inteligenca que é a sua capacidade de processar as informações e sabedoria que é o seu conjunto de conhecimentos. '))
    while pontostotais < sabedoriausuario or 0 > sabedoriausuario:
        sabedoriausuario = int(input(f'por favor digite um número valido entre 0 e {pontostotais} '))
    pontostotais = pontostotais - sabedoriausuario
    carismausuario = int(input('se você acha que sempre a melhor opção é lutar então você já pode se jogar aos dragões pois as vezaes é mais fácil se passar por um velho conhecido de negócios do que só sair na porrada então quantos pontos colocará em carisma? '))
    while pontostotais < carismausuario or 0 > carismausuario:
        carismausuario = int(input(f'por favor digite um número valido entre 0 e {pontostotais} '))
    pontostotais = pontostotais - carismausuario
def dados():
    print('')
print(personagem.criacaodepersonagem())