from q6_calculo import cal_hora

def main():

    t = input("Em qual turno e alino estuda, sendo M para matutino, V para Vespertino ou N para Noturno:").upper()

    horario = cal_hora(t)
    print(horario)

main()    