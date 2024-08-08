team1_name = "Мастера кода"
team2_name = "Волшебники данных"
team1_num = 6
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

def calc_result():
    challenge_result = "победа команды "
    
    if score1 > score2 or score1 == score2 and team1_time > team2_time:
        challenge_result += f"{team1_name}!"
    elif score1 < score2 or score1 == score2 and team1_time < team2_time:
        challenge_result += f"{team2_name}!"
    else:
        challenge_result = "Ничья!"
        
    return challenge_result

def calc_tasks():
    return score1 + score2

def calc_avg_time():
    return (team1_time + team2_time) / calc_tasks()

# Использование %:
print("В команде %s участников: %s!" % (team1_name, team1_num))
print("Итого сегодняв командах участников: %s и %s!" % (team1_num, team2_num))

# Использование format():
print("Команда {} решила задач: {}!".format(team2_name, score2))
print("{} решили задачи за {} сек!".format(team2_name, team2_time))

# Использование f-строк:
print(f"Команды решили {score1} и {score2} задач.")
print(f"Результат битвы: {calc_result()}")
print(f"Сегодня было решено {calc_tasks()} задач, в среднем по {calc_avg_time()} секунды на задачу!.")      

