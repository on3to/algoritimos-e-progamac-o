#Entrada 

n1=int(input("Qual a primeira nota do aluno?"))

n2=int(input("Qual a segunda nota do aluno?"))

n3=int(input("Qual a terceira nota do aluno?"))

p1=2

p2=3

p3=4

#Processamento

nota=(n1 * p1) + (n2 * p2) + (n3 * p3)

peso= p1 + p2 +p3

notafinal= nota / peso

#saida

print(f"A media ponderada sera de:{notafinal}")