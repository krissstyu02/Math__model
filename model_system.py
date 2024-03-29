import random
import numpy as np

details = 500
time = 0
time_issues = 0
breakage_interval = np.random.normal(20, 2)
processing_time = 0
queue = []
expectation = 0
count_breakdown = 0
troubleshooting_issues_total_time = 0

time_entrance = []
interval_entrance = []

for i in range(details):
    entrance = random.expovariate(1)
    if i == 0:
        time_entrance.append(entrance)
    else:
        time_entrance.append(entrance + time_entrance[-1])
    interval_entrance.append(entrance)


# print(time_entrance)


def check_breakage(setting_up):
    global time, processing_time
    if breakage_interval <= 0:
        time += setting_up + breakage_interval
        processing_time += setting_up + breakage_interval
        breakdown()
        return True
    else:
        time += setting_up
        processing_time += setting_up
        return False


def breakdown():
    global breakage_interval, time, processing_time, time_issues
    breakage_interval = np.random.normal(20, 2)
    troubleshooting_issues = np.random.uniform(0.1, 0.5)
    time += troubleshooting_issues
    time_issues += troubleshooting_issues
    processing_time += troubleshooting_issues


i = 0
obrabotka = 0

while i != details:
    if i == 0:
        time += time_entrance[0]
    else:
        if time < time_entrance[i]:
            time += time_entrance[i] - time

    # print(i + 1,'деталь')
    # print('Время появления детали:', round(time_entrance[i],4))
    # print('Проводится обработка детали')
    setting_up = np.random.uniform(0.2, 0.5)
    breakage_interval -= setting_up

    # print('Наладка станка:', round(setting_up,4),'ч')
    if check_breakage(setting_up):
        i -= 1
        # print('Поломка')
        count_breakdown += 1

    task_execution = np.random.normal(0.5, 0.1)
    breakage_interval -= task_execution

    if check_breakage(task_execution):
        i -= 1
        # print('Поломка')
        count_breakdown += 1

    i += 1
    # print('Время выполнения задания:', round(task_execution,4),'ч')
    # print('Время обработки детали :', round(processing_time,4),'ч')
    # obrabotka += processing_time
    # print('Итоговое время работы станка составляет', round(time,4),'ч')
    # processing_time = 0
    # print("До поломки осталось : ", round(breakage_interval,4),'ч')
    # print()

print()
print('Полное время работы станка=', round(time,1),'ч')
print('Среднее время поступления детали=', round((sum(interval_entrance) / details),1),'ч')
print('Время, затраченное на исправление поломок=', round(time_issues,1),'ч')
print('Количество поломок=', count_breakdown)
