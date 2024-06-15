count_of_tasks = 12
total_time_for_all_tasks = 1.5
course_name = "Python"
time_for_one_task = total_time_for_all_tasks / count_of_tasks

# Способ по заданию, но выглядит не красиво, так как после каждой переменной вставляется пробел 
# и получается что запятая отделяется пробелами
print("Курс:", course_name, ", всего задач:", count_of_tasks, 
      ", затрачено часов:", total_time_for_all_tasks, 
      ", среднее время выполнения: ", time_for_one_task, "часов")

# Способ через f-строку
print(f"Курс: {course_name}, всего задач: {count_of_tasks}, затрачено часов: {total_time_for_all_tasks}, среднее время выполнения: {time_for_one_task} часов")
