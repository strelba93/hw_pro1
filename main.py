from application.db.people import get_employess
from application.salary import calculate_salary
from datetime import datetime, date, time


if __name__ == '__main__':
    print(calculate_salary(5, 7))
    print(get_employess('Антон', 'Антонов'))
    print(datetime.today())


