from datetime import datetime

Data_hota_atual = datetime.now()
data_hora_str = '2024-04-20 23:05'
mascara_ptbr = '%d/%m/%Y %a'
mascara_en = '%Y-%m-%d %H:%M'

print(Data_hora_atual.strftime(mascara_ptbr))

print(datetime.strptime(data_hora_str, mascara_en))