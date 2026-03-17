d_at, m_at, a_at = int(input("Dia atual: ")), int(input("Mês atual: ")), int(input("Ano atual: "))
d_n, m_n, a_n = int(input("Dia nasc: ")), int(input("Mês nasc: ")), int(input("Ano nasc: "))

anos = a_at - a_n
meses = m_at - m_n
dias = d_at - d_n

if dias < 0:
    meses -= 1
    dias += 30

if meses < 0:
    anos -= 1
    meses += 12

print(f"{anos} anos, {meses} meses e {dias} dias")