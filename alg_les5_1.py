#Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
#для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно
#вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

def getAvProfit(companies):
    profit = 0
    for company in companies:
        profit += company.profit
    return profit / len(companies)

Company = namedtuple('Company', 'name, q1, q2, q3, q4, profit')

count = int(input('Введите количество компаний: '))

companies = []

for i in range(count):
    name = input(f'Введите наименование компании  №{i+1}: ')
    q1 = float(input(f'Введите прибыль компании  "{name}" за 1 квартал: '))
    q2 = float(input(f'Введите прибыль компании  "{name}" за 2 квартал: '))
    q3 = float(input(f'Введите прибыль компании  "{name}" за 3 квартал: '))
    q4 = float(input(f'Введите прибыль компании  "{name}" за 4 квартал: '))
    profit = q1 + q2 + q3 + q4
    companies.append(Company(name, q1, q2, q3, q4, profit))


av_profit = getAvProfit(companies)

companies_less = [company.name for company in companies if company.profit < av_profit]
companies_more = [company.name for company in companies if company.profit > av_profit]

print(f'Средняя прибыль {av_profit}')
print(f'Наименование компаний с прибылью ниже среднего {companies_less}')
print(f'Наименование компаний с прибылью выше среднего {companies_more}')

