import random
def introducao():
    print('lorem')
    print('bom agora que você estpá aqui nessa simulação vamostreinar uma coisa básica movimentação')
    print('WIP')
    listnames = ['Alaric', 'Beatrix', 'Cedric', 'Dante', 'Eleanor', 'Faramir', 'Giselle', 'Harold', 'Isolde', 'Jocelyn', 'Leofric', 'Matilda', 'Niall', 'Odette', 'Percival', 'Quillian', 'Rhiannon', 'Sigmund', 'Thaddeus', 'Ulf', 'Violetta', 'Wulfric', 'Yseult', 'Agravain', 'Brynhild', 'Catriona', 'Dorian', 'Eadric', 'Fenella', 'Godfrey', 'Hildegarde', 'Ingmar', 'Jareth', 'Kenelm', 'Lancelot', 'Morgana', 'Osric', 'Rowena', 'Theobald', 'Wilfred']
    nomeinimigo = random.choice(listnames)
    pontostotaisinimigo = 30
    forcainimigobruto = random.randint(1, pontostotaisinimigo)
    forcainimigo = forcainimigobruto /10
    #formula
    pontostotaisinimigo = pontostotaisinimigo - forcainimigo
    print(pontostotaisinimigo)
    print(f'agora vamos começar a batalha seu inimigo é {nomeinimigo}')

print(introducao())