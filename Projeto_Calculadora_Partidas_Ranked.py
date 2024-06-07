def cabecalho():
    print("-"*38)
    print("Bem-vindo a Calculadora de Ranqueadas")
    print("-"*38)

def informacoes_rank(vitoria_p):
    if vitoria_p < 10:
        vitoria = "Ferro"
    elif vitoria_p <= 20:
        vitoria = "Bronze"
    elif vitoria_p <= 50:
        vitoria = "Prata"
    elif vitoria_p <= 80:
        vitoria = "Ouro"
    elif vitoria_p <= 90:
        vitoria = "Diamante"
    elif vitoria_p <= 100:
        vitoria = "Lendario"
    else:
        vitoria = "Imortal"
    return vitoria

cabecalho()
print("")
n=1

while(n==1):
    nome=input("Digite o nome do seu Heroi")
    vit=int(input("Digite a quantidade de Vitorias do seu Herói: "))
    der=int(input("Digite a quantidade de Derrotas do seu Herói: "))
    vitoria_p=vit-der
    nivel=(informacoes_rank(vitoria_p))
    
    if (vitoria_p==1 or vitoria_p==0):
            print("O Heroi de nome {} tem saldo de {} Vitoria e esta no nivel {}".format(nome,vitoria_p,nivel))
    else:
        print("O Heroi de nome {} tem saldo de {} Vitorias e esta no nivel {}".format(nome,vitoria_p,nivel))
    
    print("")
    
    n=int(input("Deseja saber o nivel de outro Heroi ? 1-SIM / 2-NAO"))
    
    if (n==2):
        break