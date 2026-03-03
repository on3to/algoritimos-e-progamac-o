from q4_calculo import cal_media

def main():

    n1 = int(input("qual a primiera nota do aluno:"))
    n2 = int(input("qual a segunda nota do aluno:"))
    
    media = cal_media(n1, n2)

    if media == 10:
        print("aprovado com distinção")

    elif media >= 7:
        print("aprovado")
    else:
        print("reprovado")

main()        
            