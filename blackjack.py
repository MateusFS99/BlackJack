def novo_deck():
    naipes = ['\u2660','\u2661','\u2662','\u2663']
    cartas = '1,2,3,4,5,6,7,8,9,10,J,Q,K'
    cartas = cartas.split(',')
    deck = [[carta, naipe] for naipe in naipes for carta in cartas]

    import random
    random.shuffle(deck)
    
    return deck

def tirar_carta(deck):
    carta = deck.pop()
    if carta[0] in 'JQK':
        pontos = 10
    else:
        pontos = int(carta[0])

    return carta, pontos

def jogada(deck):
    carta, pontos = tirar_carta(deck)
    print(carta)

    return pontos
    
deck = novo_deck()
carta, pontos = tirar_carta(deck)

pontos_jogador = 0
pontos_mesa = 0

jogar = 'sim'
jogo_acabou = False

while jogar == 'sim':
    pontos_jogador += jogada(deck)

    if pontos_jogador == 21:
        print('VOCÊ GANHOU')
        jogo_acabou = True
        break
    elif pontos_jogador > 21:
        print('VOCÊ PERDEU')
        jogo_acabou = True
        break
    else:    
        jogar = input('Mais uma carta?: ')

if not jogo_acabou:
    print('Mesa:')

while not jogo_acabou:
    carta, pontos = tirar_carta(deck)
    print(carta)
    pontos_mesa += pontos

    if pontos_mesa == 21:
        print('VOCÊ PERDEU!')
        jogo_acabou = True

    if pontos_mesa > 21:
        print('VOCÊ GANHOU!')
        jogo_acabou = True
        break
    if pontos_mesa > pontos_jogador:
        print('VOCÊ PERDEU!')
        jogo_acabou = True
