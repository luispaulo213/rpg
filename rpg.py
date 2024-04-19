class personagem:
    def __init__(self, nome, raca, classe) -> None:
        self.nome = nome 
        self.raça = raca
        self.classe = classe


    def criacaopersonagem():
        nomepersonagem = input('por favor digite o nome do seu personagem ')
        racapersonagem = ["tielfing","arcanjo","elfo","anão","orc","duende"]
        print('1.Tielfing, 2.arcanjo, 3.elfos, 4.anão, 5.orc, 6.duende')
        numeroraca = int(input(' selecione o número correspondente a raça desejada disponibilizadas acima'))
        if numeroraca == 1:
            print('você escolheu a raça tielfing')
        if numeroraca == 2:
            print('você escolheu a raça arcanjo')
        if numeroraca == 3:
            print('você escolheu a raça elfo')
        if numeroraca == 4:
            print('você escolheu a raça anão')
        if numeroraca == 5:
            print(f'você escolheu a raça orc,{nomepersonagem}')
        if numeroraca == 6:
            print('você escolheu a raça duende')
        classepersonagem = ["tielfing","arcanjo","elfo","anão","orc","duende"]
        print('1.Bruto, 2.Ladino, 3.Bardo, 4.Mago, 5.Arqueiro, 6.Curandeiro')
        numeroclasse = int(input(' selecione o número correspondente a classe desejada disponibilizadas acima'))
        if numeroclasse == 1:
            print('você escolheu a classe bruto')
        if numeroclasse == 2:
            print('você escolheu a classe ladino')
        if numeroclasse == 3:
            print('você escolheu a classe bardo')
        if numeroclasse == 4:
            print('você escolheu a classe mago')
        if numeroclasse == 5:
            print(f'você escolheu a classe arqueiro,{nomepersonagem}')
        if numeroclasse == 6:
            print(f'você escolheu a classe curandeiro')
print(personagem.criacaopersonagem())