from random import randint

lixeiras = {
    'lixeira1': {
        'ID': '101',
        'local': 'Rua A, Número 123',
        'status_coleta': 'Pendente',
        'enchimento': 85,
        'ultima_coleta': '2023-09-01 10:30:00',
        'responsavel': 'Equipe A'
    },
    'lixeira2': {
        'ID': '202',
        'local': 'Rua B, Número 456',
        'status_coleta': 'Concluída',
        'enchimento': 40,
        'ultima_coleta': '2023-08-28 15:45:00',
        'responsavel': 'Equipe H'
    },
    'lixeira3': {
        'ID': '303',
        'local': 'Rua C, Número 789',
        'status_coleta': 'Pendente',
        'enchimento': 95,
        'ultima_coleta': '2023-09-03 09:15:00',
        'responsavel': 'Equipe A'
    }
}


# Simulação dos sensores 
for k in lixeiras:
    sensor_enchimento = randint(0, 100)
    lixeiras[k].update({'enchimento':sensor_enchimento})
    if sensor_enchimento < 50:
        lixeiras[k].update({'coleta':'Concluída'})
    elif sensor_enchimento >= 50 and sensor_enchimento < 75:
        lixeiras[k].update({'coleta':'Pendente'})
    else:
        lixeiras[k].update({'coleta':'Em andamento'})

for k, v in lixeiras['lixeira1'].items():
    print(f'- {k}: {v}')