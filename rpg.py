class personagem:
    def __init__(self, nome, raca, classe) -> None:
        self.nome = nome 
        self.raça = raca
        self.classe = classe

     
    def criacaopersonagem():
       
        nomepersonagem = input('por favor digite o nome do seu personagem ')
        racapersonagem = ["tielfing","arcanjo","elfo","anão","orc","duende"]
        print('1.Tielfing, 2.arcanjo, 3.elfos, 4.anão, 5.orc, 6.duende')
        racaAtributoCarisma = 0
        racaAtributoForca = 0
        racaAtributoSabedoria = 0
        racaAtributoDestreza = 0
        racaAtributoCon = 0
        racaAtributoInteligencia = 0
        numeroraca = int(input(' selecione o número correspondente a raça desejada disponibilizadas acima'))
        
        if numeroraca == 1:
            print('você escolheu a raça tielfing')
            nomeraca = "tielfing"
            racaAtributoCarisma +=2
            racaAtributoForca +=1
            racaAtributoCon +=1
        elif numeroraca == 2:
            print('você escolheu a raça arcanjo')
            nomeraca = "arcanjo"
            racaAtributoDestreza +=1
            racaAtributoCon +=1
            racaAtributoSabedoria +=1
            racaAtributoCarisma +=1
        elif numeroraca == 3:
            print('você escolheu a raça elfo')
            nomeraca = "elfo"
            racaAtributoDestreza +=2
            racaAtributoCon +=1
            racaAtributoInteligencia +=1
        elif numeroraca == 4:
            print('você escolheu a raça anão')
            nomeraca = "anão"
            racaAtributoForca +=2
            racaAtributoCon +=1
            racaAtributoInteligencia +=1
            racaAtributoSabedoria +=1
        elif numeroraca == 5:
            print(f'você escolheu a raça orc')
            nomeraca = "orc"
            racaAtributoForca +=3
            racaAtributoDestreza =-1
            racaAtributoCon +=2
            racaAtributoInteligencia =-1
        elif numeroraca == 6:
            print('você escolheu a raça duende')
            nomeraca = "duende"
            racaAtributoDestreza +=1
            racaAtributoCon +=1
            racaAtributoInteligencia +=2
        else:
            print("Digite um número correto referente a sua raca")
        
        classepersonagem = ["tielfing","arcanjo","elfo","anão","orc","duende"]
       
        print('1.Bruto, 2.Ladino, 3.Bardo, 4.Mago, 5.Arqueiro, 6.Curandeiro')
        numeroclasse = int(input(' selecione o número correspondente a classe desejada disponibilizadas acima'))
        
        if numeroclasse == 1:
            print('você escolheu a classe bruto')
            nomeclasse = "bruto"
        elif numeroclasse == 2:
            print('você escolheu a classe ladino')
            nomeclasse = "Ladino"
        elif numeroclasse == 3:
            print('você escolheu a classe bardo')
            nomeclasse = "bardo"
        elif numeroclasse == 4:
            print('você escolheu a classe mago')
            nomeclasse = "mago"
        elif numeroclasse == 5:
            print(f'você escolheu a classe arqueiro, {nomepersonagem}')
            nomeclasse = "arqueiro"
        elif numeroclasse == 6:
            print(f'você escolheu a classe curandeiro')
            nomeclasse = "curandeiro"
        else:
            print("Digite um número correto referente a sua classe")

        print(f"seu nome é: {nomepersonagem}, {nomeraca}, {nomeclasse}")


        #Escolha do jogador para atributo força 🦾

        pontos = 30
        perguntaAtributoForca = int(input('Quantos pontos voce quer colocar no atributo Força? (Lembrando que o máximo é 5)'))
        while perguntaAtributoForca > 5:
            print("Por favor coloque um número menor que 5")            
            perguntaAtributoForca = int(input('Quantos pontos voce quer colocar no atributo Força? (Lembrando que o máximo é 5)'))
        
        if perguntaAtributoForca < 6: 
            atributoforca = perguntaAtributoForca 
            pontos -= perguntaAtributoForca
            atributoforca += racaAtributoForca
            print(f"Voce tem {atributoforca} de forca")


        perguntaAtributodestreza = int(input('Quantos pontos voce quer colocar no atributo destreza? (Lembrando que o máximo é 5)'))
        while perguntaAtributodestreza > 5:
            print("Por favor coloque um número menor que 5")            
            perguntaAtributodestreza = int(input('Quantos pontos voce quer colocar no atributo destreza? (Lembrando que o máximo é 5)'))
        
        if perguntaAtributodestreza < 6: 
            Atributodestreza = perguntaAtributodestreza 
            pontos -= perguntaAtributodestreza 
            Atributodestreza += racaAtributoDestreza
            print(f"Voce tem {Atributodestreza} de destreza")
        perguntaAtributoCon = int(input('Quantos pontos voce quer colocar no atributo Vida? (Lembrando que o máximo é 5)'))
        
        while perguntaAtributoCon > 5:
            print("Por favor coloque um número menor que 5")            
            perguntaAtributoCon = int(input('Quantos pontos voce quer colocar no atributo Vida? (Lembrando que o máximo é 5)')) 
        if perguntaAtributoCon < 6: 
            atributoCon = perguntaAtributoCon 
            pontos -= perguntaAtributoCon 
            atributoCon += racaAtributoCon
            print(f"Voce tem {atributoCon} de vida")

        perguntaAtributoInteligencia = int(input('Quantos pontos voce quer colocar no atributo Inteligencia? (Lembrando que o máximo é 5)'))
        while perguntaAtributoInteligencia > 5:
            print("Por favor coloque um número menor que 5")            
            perguntaAtributoInteligencia = int(input('Quantos pontos voce quer colocar no atributo inteligencia? (Lembrando que o máximo é 5)'))
        
        if perguntaAtributoInteligencia < 6: 
            atributointeligencia = perguntaAtributoInteligencia 
            pontos -= perguntaAtributoInteligencia 
            atributointeligencia += racaAtributoInteligencia
            print(f"Voce tem {atributointeligencia} de inteligencia")

        perguntaAtributoSabedoria = int(input('Quantos pontos voce quer colocar no atributo Sabedoria? (Lembrando que o máximo é 5)'))
        while perguntaAtributoSabedoria > 5:
            print("Por favor coloque um número menor que 5")            
            perguntaAtributoSabedoria = int(input('Quantos pontos voce quer colocar no atributo Sabedoria? (Lembrando que o máximo é 5)'))
        
        if perguntaAtributoSabedoria < 6: 
            atributoSabedoria = perguntaAtributoSabedoria 
            pontos -= perguntaAtributoSabedoria 
            atributoSabedoria += racaAtributoSabedoria
            print(f"Voce tem {atributoSabedoria} de Sabedoria")

        perguntaAtributoCarisma = int(input('Quantos pontos voce quer colocar no atributo Carisma? (Lembrando que o máximo é 5)'))
        while perguntaAtributoCarisma > 5:
            print("Por favor coloque um número menor que 5")            
            perguntaAtributoForca = int(input('Quantos pontos voce quer colocar no atributo Carisma? (Lembrando que o máximo é 5)'))
        
        if perguntaAtributoCarisma < 6: 
            AtributoCarisma = perguntaAtributoCarisma 
            pontos -= AtributoCarisma 
            AtributoCarisma += racaAtributoCarisma
            print(f"Voce tem {AtributoCarisma} de carisma")     
        
        #thielfing=[atributoforca +=1, atributodestrezaestreza+=0, atributoCon = +1, atributoInteligencia = "normal", Sabedoria = "Normal", Carisma= +2]
        #Arcanjo: Força: Normal, Destreza: +1, Vida: +1, Inteligencia: Normal, Sabeddoria: +1, Carisma: +1
        #Elfo: Força: Normal, Detreza: +2, Vida: +1, Inteligencia: +1, Sabedoria: Normal, Carisma: Normal
        #Anão: Força: +2, Detreza: Normal, Vida: +1, Inteligencia: +1, Sabedoria: +1, Carisma: Normal
        #Orc: Força: +3, Detreza: -1, Vida: +2, Inteligencia: -1, Sabedoria: Normal, Carisma: Normal
        #Duende: Força: Normal, Detreza: +1, Vida: +1, Inteligencia: +2, Sabedoria: +2, Carisma: Normal

        
        
        
        
        if pontos == 0:
            print(f"{nomepersonagem}, {nomeraca},{nomeclasse},Força: {atributoforca}, Destreza: {Atributodestreza}, Vida: {atributoCon}, Inteligencia: {atributointeligencia}, Sabedoria: {atributoSabedoria}, Carisma: {AtributoCarisma}, você não tem mais pontos, Pronto para jogar?")
            simnaojogar = input('Sim ou Não')
            if simnaojogar == 'Sim':
                 #desenrola-le fala e vai pro quebra pau de treino
                print('teste')
                jogoComeça(nomeraca)            
            elif simnaojogar == 'Não':
                    print('Você chega até aqui e diz não vai volta desde o inicio logo tá bom vai vai')
            else:
                    print('Por favor escolha uma opção correta')
                    input('Sim/Não')



def jogoComeça(nomeraca):
    print("Jogo começou")
    nomerival = input('Escolha o nome do seu rival')
    batalha(nomerival, nomeraca)

def batalha(rival, nomeraca):
    print(f'A batalha começou o seu inimigo é {rival}')
    print('O que irá fazer agora: fugir, batalhar, itens')
    acaojogador = input('...')
    if acaojogador in ('Batalhar','batalhar','BATALHAR'):
        print('1. ataque corpo a corpo')
        print('2. ataque a distancia')
        print('3. Recuperar vida')
        print('4. Ataque especial')
        acaoataquejogador = input('Agora escolha qual ataque você irá usar(selecoine com os números)...')
        if acaoataquejogador in ('1','2','3','4'):
            if acaoataquejogador in ('1','um','UM','Um','uM'):
                if nomeraca in ('tielfing'):
                    print('') 
        else:
            print('')
         



print(personagem.criacaopersonagem())
