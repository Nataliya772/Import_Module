import datetime

from application.db.people import get_employees
from application.salary import calculate_salary

if __name__ == '__main__':
    print(f'Вызов функций в {datetime.datetime.utcnow()}')
    get_employees()
    print(f'{datetime.datetime.utcnow()} - {calculate_salary()}')