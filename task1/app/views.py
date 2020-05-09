from django.shortcuts import render
import csv


def inflation_view(request):
    template_name = 'inflation.html'
    with open('task1/inflation_russia.csv', 'r', encoding='utf8', ) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            context = {row['год']: [row['Янв'], row['Фев'], row['Мар'], row['Апр'], row['Май'], row['Июн'], row['Июл'],
                                    row['Авг'], row['Сен'], row['Окт'], row['Ноя'], row['Дек'], row['Суммарная']]}

    return render(request, template_name,
                  context)
