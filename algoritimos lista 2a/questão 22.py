h_ini = int(input("Hora início: "))
m_ini = int(input("Minuto início: "))
h_fim = int(input("Hora fim: "))
m_fim = int(input("Minuto fim: "))

total_ini = h_ini * 60 + m_ini
total_fim = h_fim * 60 + m_fim

if total_fim <= total_ini:
    duracao = (24 * 60 - total_ini) + total_fim
else:
    duracao = total_fim - total_ini

print(f"Duração: {duracao // 60}h e {duracao % 60}min")