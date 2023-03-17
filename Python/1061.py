# Lê a data de início do evento
entrada = input().split()
dia_inicio = int(entrada[1])

# Lê o horário de início do evento
entrada = input().split(":")
hora_inicio = int(entrada[0])
minuto_inicio = int(entrada[1])
segundo_inicio = int(entrada[2])

# Lê a data de término do evento
entrada = input().split()
dia_termino = int(entrada[1])

# Lê o horário de término do evento
entrada = input().split(":")
hora_termino = int(entrada[0])
minuto_termino = int(entrada[1])
segundo_termino = int(entrada[2])

# Calcula a duração do evento em segundos
segundos_inicio = segundo_inicio + minuto_inicio*60 + hora_inicio*3600 + (dia_inicio-1)*86400
segundos_termino = segundo_termino + minuto_termino*60 + hora_termino*3600 + (dia_termino-1)*86400
duracao_segundos = segundos_termino - segundos_inicio

# Calcula a duração do evento em dias, horas, minutos e segundos
dias = duracao_segundos // 86400
duracao_segundos %= 86400
horas = duracao_segundos // 3600
duracao_segundos %= 3600
minutos = duracao_segundos // 60
duracao_segundos %= 60

# Imprime a duração do evento
print("{} dia(s)".format(dias))
print("{} hora(s)".format(horas))
print("{} minuto(s)".format(minutos))
print("{} segundo(s)".format(duracao_segundos))
