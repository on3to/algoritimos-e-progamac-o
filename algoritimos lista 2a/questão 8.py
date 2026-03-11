d_at = int(input("Dia atual: "))
m_at = int(input("Mês atual: "))
a_at = int(input("Ano atual: "))

d_nasc = int(input("Dia de nascimento: "))
m_nasc = int(input("Mês de nascimento: "))
a_nasc = int(input("Ano de nascimento: "))

idade = a_at - a_nasc

if (m_at < m_nasc) or (m_at == m_nasc and d_at < d_nasc):
    idade -= 1

print(f"Idade exata: {idade} anos")