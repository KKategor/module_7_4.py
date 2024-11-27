# Task "Форматирование строк"


# Использование %
team1 = 'Мастера кода'
team2 = 'Волшебники данных'

def num(team1_num=0, team2_num=0):
    print('В команде "%s" участников: %s !' % (team1, team1_num))
    print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))


# Использование format()
score1 = 0
score2 = 0

def time(team1_time = 0,  team2_time=0):
    time1 = team1_time
    time2 = team2_time
    print('Команда "{}" решила задач: {} !'.format(team2, score2))
    print('"{}" решили задачи за {} с !'.format(team2, time2))

# Использование f-строк
def challenge_result(team1_time = 0,  team2_time=0):
    print(f'Команды решили {score1} и {score2} задач.')
    tasks_total = (score1 + score2)
    time_avg = round(((team1_time + team2_time) / tasks_total),2)
    print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')

    if score1 > score2 or score1 == score2 and team1_time > team2_time:
        challenge_result = (f'Результат битвы: победа команды "{team1}"')
    elif score1 < score2 or score1 == score2 and team1_time < team2_time:
        challenge_result = (f'Результат битвы: победа команды "{team2}"')
    else:
        challenge_result = ('Ничья!')
    result = challenge_result
    print(result)




num(team1_num = 5, team2_num = 6)
score1 = 40
score2 = 42
time(team1_time = 1552.512, team2_time = 2153.31451)
challenge_result(team1_time = 1552.512, team2_time = 2153.31451)
