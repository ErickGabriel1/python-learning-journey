perguntas = [

    {
        'Pergunta': 'Quanto é 10 x 11?',
        'Alternativas': ['100', '200', '110', '1100'],
        'Resposta': '110',

    },
    {
        'Pergunta': 'Quanto é 10 x 100?',
        'Alternativas': ['100', '200', '110', '1000'],
        'Resposta': '1000',

    },
    {
        'Pergunta': 'Quanto é 10 x 20?',
        'Alternativas': ['100', '200', '110', '1100'],
        'Resposta': '200',

    }

]

vida = 1
rodada = 0

while(vida>0):


    if rodada == len(perguntas):
        print('Você ganhou o jogo!')
    print(pergunta_atual['Pergunta'])

    for n in pergunta_atual['Alternativas']:
        print(f'{pergunta_atual['Alternativas'].index(n)+1}) {n}')
    
    escolha = int(input(": ")) - 1
     
    if pergunta_atual['Alternativas'][escolha] == pergunta_atual['Resposta']:
        print("Você Acertou!")
        print('--------------------------------------------------------\n')
        rodada += 1
    else:
        print('O jogo acabou!\n')
        vida -= 1