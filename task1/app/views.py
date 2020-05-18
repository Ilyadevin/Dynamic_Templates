from django.shortcuts import render
import csv


def inflation_view(request):
    template_name = 'inflation.html'
    list_of_percents = list()
    with open('inflation_russia.csv', 'r', encoding='utf8', ) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        for row in reader:
            list_of_percents.append(
                {'year': row['Год'], 'percents': [row['Янв'], row['Фев'], row['Мар'], row['Апр'],
                                                  row['Май'], row['Июн'], row['Июл'], row['Авг'], row['Сен'],
                                                  row['Окт'], row['Ноя'], row['Дек'], row['Суммарная']]
                 }
            )
    context = {'inflation': list_of_percents,
               }
    return render(request, template_name,
                  context)
