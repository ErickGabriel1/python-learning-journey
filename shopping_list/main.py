import os

list = []

while(True):
    
    #Menu inicial
    print("\nSelecione uma opção:\n")
    choice = str(input("[I]nserir [A]pagar [L]istar: ")).lower()
    
    #Identificar escolha
    match choice:

        case 'i':
            os.system("cls")
            item = str(input("Digite o que quer adcionar na lista: "))
            list.append(item)
        case 'a':
            os.system("cls")
            item = int(input("Digite o indice que quer excluir da lista: "))
            del list[item]

        case 'l':
            os.system("cls")
            for n, m in enumerate(list):
                print(n, m)

        case _:
            print("Valor inválido! Tente novamente!")