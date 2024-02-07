from efos_app.models import Cancellation
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
    with open('static/Cancelados_13_OCT_2023.csv', encoding='latin-1') as file:
        count = 0
        reader = csv.reader(file)
        next(reader)

        person_arr = []

        for row in reader:
            count += 1

            match row[3].lower():
                case 'cancelados':
                    cancel_reason = 'C'
                case 'cancelados por insolvencia':
                    cancel_reason = 'INSO'
                case 'cancelados por incosteabilidad':
                    cancel_reason = 'INCO'

            cancellation = Cancellation(rfc=row[0],
                                  social_reason=row[1],
                                  type_of_person=row[2],
                                  cancel_reason=cancel_reason,
                                  cancellation_date=parse_normal_date(row[4]),
                                  amount=int(row[5].replace(',', '')),
                                  date_published=parse_normal_date(row[6]),
                                  state=row[7],
                                  )
            person_arr.append(cancellation)
            print(cancellation)
        
        Cancellation.objects.bulk_create(person_arr)
        print(count)
