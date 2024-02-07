from efos_app.models import PersonDetail
import csv
from datetime import date, datetime


def parse_normal_date(data):
    date_format = '%d/%m/%Y'
    if data:
        if len(data) < 6:
            return
        date = data.split()[0]
        if len(date.split('/')[2]) == 2:
            date_format = '%d/%m/%y'
        return datetime.strptime(date, date_format)
    else:
        return


def run():
    with open('static/Sentencias_13_OCT_2023.csv', encoding='latin-1') as file:
        count = 0
        reader = csv.reader(file)
        next(reader)

        person_arr = []

        for row in reader:
            count += 1

            person = PersonDetail(rfc=row[0],
                                  social_reason=row[1],
                                  assumption=row[3],
                                  date_published=parse_normal_date(row[4]),
                                  type_of_person=row[2],
                                  state=row[5],
                                  )
            person_arr.append(person)
            print(person)
        
        PersonDetail.objects.bulk_create(person_arr)
        print(count)
