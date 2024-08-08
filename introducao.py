import random
import criaçãodepersonagem
def introducao():
    print('lorem')
    print('bom agora que você estpá aqui nessa simulação vamostreinar uma coisa básica movimentação')
    print('WIP')
    listnames = ['Alaric', 'Beatrix', 'Cedric', 'Dante', 'Eleanor', 'Faramir', 'Giselle', 'Harold', 'Isolde', 'Jocelyn', 'Leofric', 'Matilda', 'Niall', 'Odette', 'Percival', 'Quillian', 'Rhiannon', 'Sigmund', 'Thaddeus', 'Ulf', 'Violetta', 'Wulfric', 'Yseult', 'Agravain', 'Brynhild', 'Catriona', 'Dorian', 'Eadric', 'Fenella', 'Godfrey', 'Hildegarde', 'Ingmar', 'Jareth', 'Kenelm', 'Lancelot', 'Morgana', 'Osric', 'Rowena', 'Theobald', 'Wilfred']
    nomeinimigo = random.choice(listnames)
    danoinimigo = 16
    hpinimigo = 160
    defesainimigo = 16
    destrezainimigo = 16
    velocidadeinimigo = 16
    carismainimigo = 16
    percepcaoinimigo = 16
    #atazanaplayer2.0 clocar em vários prints uma coisa que podia ser resumida e normalmente é "primeiro vc vai na agressão"
    print(f'agora vamos começar a batalha seu inimigo é {nomeinimigo}')
    print('vamos lá aqui nessa interface inicial de uma batalha você tem 3 opções tentar fugir que não é o objetivo de hoje, atacar e itens agor aeu quero que você entre em itens')
#jogadorseleciona itens
    print('aqui você pode trocar a arma escudo, armadura agora vamos voltar ao menu principal e ir na batalha')
#jogador vai par o menu e selciona atacar e a opção ataque 
    print('bom como pode ver você tem 4 ataques que variam de acordo com as suas escolhas de classe e raça agora vamos ver as opções de defesa')
#jogador volta e seleciona defesa
    print('bom agora em defesa você tem duas opções o escudo que gasta x de stamina ou a esquiva que gasta y de stamina')
print(introducao())
