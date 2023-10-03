from efos_app.models import Efo, PersonDetail
import csv
from datetime import date, datetime

MONTHS = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
          'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']



def parse_complex_date(data):
    if data:
        arr = data.split()
        if len(arr) > 10:
            return
        if arr[1] == 'de' and arr[2] == 'fecha' and arr[4] == 'de' \
                and (arr[6] == 'de' or arr[6] == 'del'):
            day = int(arr[3])
            month = int(MONTHS.index(arr[5]) + 1)
            if len(arr[7]) > 4:
                year = int((arr[7])[:-1])
            else:
                year = int(arr[7])
        elif arr[1] == 'de' and arr[2] == 'fecha' and len(arr) == 6:
            day = int(arr[3])
            month = int(MONTHS.index(arr[4]) + 1)
            if len(arr[5]) > 4:
                year = int((arr[5])[:-1])
            else:
                year = int(arr[5])
        elif arr[1] == 'de' and arr[3] == 'de' \
                and arr[5] == 'de':
            day = int(arr[2])
            month = int(MONTHS.index(arr[4]) + 1)
            if len(arr[6]) > 4:
                year = int((arr[6])[:-1])
            else:
                year = int(arr[6])
        elif arr[1] == 'de' and arr[2] == 'fecha' and arr[5] == 'de':
            day = int(arr[3])
            month = int(MONTHS.index(arr[4]) + 1)
            if len(arr[6]) > 4:
                year = int((arr[6])[:-1])
            else:
                year = int(arr[6])
        return date(year, month, day)
    return

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
    with open('static/69-B.csv') as file:
        count = 0
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        efo_arr = []        

        for row in reader:
            count += 1
            match row[3].lower():
                case "sentencia favorable":
                    fiscal_sent = 'SFA'
                case "definitivo":
                    fiscal_sent = 'DEF'
                case "desvirtuado":
                    fiscal_sent = 'DES'
                case "presunto":
                    fiscal_sent = 'PRE'

            if row[1] == 'XXXXXXXXXXXX':
                continue          
            efo = Efo(rfc=row[1],
                       social_reason=row[2].split("//")[0],
                       fiscal_situation=fiscal_sent,

                       sat_presumtion_date=parse_normal_date(row[4]),
                       sat_presumtion_file_no=row[5].split(" ", 1)[0],
                       sat_presumtion_file_date=parse_complex_date(row[5]),

                       dof_presumtion_date=parse_normal_date(row[6]),
                       dof_presumtion_file_no=row[7].split(" ", 1)[0],
                       dof_presumtion_file_date=parse_complex_date(row[7]),

                       sat_definitive_date=parse_normal_date(row[8]),
                       sat_definitive_file_no=row[9].split(" ", 1)[0],
                       sat_definitive_file_date=parse_complex_date(row[9]),

                       dof_definitive_date=parse_normal_date(row[10]),
                       dof_definitive_file_no=row[11].split(" ", 1)[0],
                       dof_definitive_file_date=parse_complex_date(row[11]),

                       sat_distorted_date=parse_normal_date(row[12]),
                       sat_distorted_file_no=row[13].split(" ", 1)[0],
                       sat_distorted_file_date=parse_complex_date(row[13]),

                       dof_distorted_date=parse_normal_date(row[14]),
                       dof_distorted_file_no=row[15].split(" ", 1)[0],
                       dof_distorted_file_date=parse_complex_date(row[15]),

                       sat_favorable_ruling_date=parse_normal_date(row[16]),
                       sat_favorable_ruling_file_no=row[17].split(" ", 1)[0],
                       sat_favorable_ruling_file_date=parse_complex_date(row[17]),

                       dof_favorable_ruling_date=parse_normal_date(row[18]),
                       dof_favorable_ruling_file_no=row[19].split(" ", 1)[0],
                       dof_favorable_ruling_file_date=parse_complex_date(row[19]),
                       )
            efo_arr.append(efo)
        Efo.objects.bulk_create(efo_arr)
        print(count)
