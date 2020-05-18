from django.shortcuts import render
import csv


def inflation_view(request):
    template_name = 'inflation.html'
    list_of_percents = list()
    with open('inflation_russia.csv', 'r', encoding='utf8', ) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        for row in reader:
            list_of_percents.append(
                {'year': row['Год'], 'jan': row['Янв'], 'feb': row['Фев'], 'mar': row['Мар'], 'apr': row['Апр'],
                 'may': row['Май'], 'jun': row['Июн'], 'jul': row['Июл'], 'aug': row['Авг'], 'sep': row['Сен'],
                 'oct': row['Окт'], 'nov': row['Ноя'], 'des': row['Дек'], 'sum': row['Суммарная']
                 }
            )
    context = {'inflation': list_of_percents,
               }
    return render(request, template_name,
                  context)
