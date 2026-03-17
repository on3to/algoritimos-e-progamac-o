def main():

    a = int(input("qual o valor inicial:"))
    l = int(input("qual o valor do limite:"))
    r = int(input("qual o valor da razão:"))

    for i in range(1000):
        termo = a + (i * r)

        if termo >= l:
            break

        print(termo)

main()    