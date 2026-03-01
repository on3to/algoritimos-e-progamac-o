from q1_escrever import escrever


def main():
    escrever("questão1")

    a = float(input("escreva o primeiro numero:"))
    b = float(input("escreva o segundo numero:"))
    c = float(input("escreva o terceiro numero:"))  

    #verificar se são iguais 
    if a == b == c: 
        escrever(f'existem 3 numeros iguais')
    
    elif a == b or a == c or b == c:
        escrever (f"existem 2 numeros iguais")
    
    else:
        escrever (f"n existe nenhum numero igual")
    
main()

#SE COLOCASSE (PRINT) NO LIGAR DE CRIAR "ESCREVER" TBM DARIA CERTO  
