from django.shortcuts import render
import csv


def inflation_view(request):
    template_name = 'inflation.html'
    list_of_percents = list
    with open('inflation_russia.csv', 'r', encoding='utf8', ) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            list_of_percents.append(
                dict(Год=row['Год'], Янв=row['Янв'], Фев=row['Фев'], Мар=row['Мар'], Апр=row['Апр'], Май=row['Май'],
                     Июн=row['Июн'], Июл=row['Июл'], Авг=row['Авг'], Сен=row['Сен'], Окт=row['Окт'], Ноя=row['Ноя'],
                     Дек=row['Дек'], Суммарная=row['Суммарная']))
    context = {
        }
    return render(request, template_name,
                  context)
