from django.shortcuts import render
import csv


def inflation_view(request):
    template_name = 'inflation.html'
    list_of_percents = list()
    with open('inflation_russia.csv', 'r', encoding='utf8', ) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        for row in reader:
            list_of_percents.append(
                {'year': int(row['Год']),
                 'percents': [float(row['Янв']), float(row['Фев']), float(row['Мар']), float(row['Апр']),
                              float(row['Май']), float(row['Июн']), float(row['Июл']), float(row['Авг']),
                              float(row['Сен']), float(row['Окт']), float(row['Ноя']), float(row['Дек']),
                              float(row['Суммарная'])]
                 }
            )
    context = {'inflation': list_of_percents,
               }
    return render(request, template_name,
                  context)
