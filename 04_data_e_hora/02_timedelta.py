from datetime import timedelta, datetime, date

tipo = 'p' #p, m ou g
pequeno = 30
medio = 45
grande = 60
data_atual = datetime.now()

if tipo == 'p':
  data_estimada = data_atual + timedelta(minutes=pequeno)
  print(f'O carro chegou: {data_atual} e ficara pronto em: {data_estimada}')

elif tipo == 'm':
  data_estimada = data_atual + timedelta(minutes=medio)
  print(f'O carro chegou: {data_atual} e ficara pronto em: {data_estimada}')

else:
  data_estimada = data_atual + timedelta(minutes=grande)
  print(f'O carro chegou: {data_atual} e ficara pronto em: {data_estimada}')


print(date.today() - timedelta(days=1))

resultado = datetime(2024, 4, 20, 22, 23) - timedelta(hours=2)
print(resultado.time())