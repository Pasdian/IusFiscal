from efos_app.models import Art74Reduction
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

def parse_amount(data):
    return float(data.replace(',', '') if data is not '' else 0)


def run():
    with open('static/Art74Red_13_OCT_2023.csv', encoding='latin-1') as file:
        count = 0
        reader = csv.reader(file)
        next(reader)

        person_arr = []

        for row in reader:
            count += 1

            reduction = Art74Reduction(rfc=row[0],
                                  social_reason=row[1],
                                  type_of_person=row[2],
                                  authorization_date=parse_normal_date(row[4]),
                                  amount=parse_amount(row[5]),
                                  date_published=parse_normal_date(row[6]),
                                  state=row[7],
                                  )
            person_arr.append(reduction)
            print(reduction)
        
        Art74Reduction.objects.bulk_create(person_arr)
        print(count)
