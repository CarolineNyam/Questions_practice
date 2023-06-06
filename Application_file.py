# Author: Caroline Nyamupanda
# don't for get f strings

OPTION_1 = 'full_time'
OPTION_2 = 'part time'

job = input('What job are you applying for?')
company_name = input('What is the name of the company you are applying to?')

type_of_employment = int(input(f'Is it 1. {OPTION_1} or 2. {OPTION_2}? '))

if OPTION_1:
    print(f'Our {OPTION_1}, hours are 40 hours a week ')

elif OPTION_2:
    print(f'Our {OPTION_2},hours are 30 hours a week ')

experience = input('Do you need experience for this job (y/n)? ')

if experience == 'y' or experience == 'Y':
    print('That is good')

elif experience == 'n' or experience == 'N':
    print("That's okay we provide training to all our stuff")

rate_of_pay = float(input('What is the rate of pay?'))

connection = open("fulltime.txt", 'w')
if OPTION_1:
    print(f'{job}', file=connection)
    print(f'{company_name}', file=connection)
    print(f'{type_of_employment}', file=connection)
    print(f'{experience}', file=connection)
    print(f'{rate_of_pay}', file=connection)

connection.close()

connection = open("parttime.txt", 'w')
if OPTION_2:
    print(f'{job}', file=connection)
    print(f'{company_name}', file=connection)
    print(f'{type_of_employment}', file=connection)
    print(f'{experience}', file=connection)
    print(f'{rate_of_pay}', file=connection)
connection.close()

try:
    with open("fulltime.txt", "r") as reading_connection:
        for line in reading_connection:
            line = line.rstrip()
            info = line.split(',')
            job = info[0]
            company_name = info[1]
            type_of_employment = info[2]
            experience = info[3]
            rate_of_pay = info[4]

        print(line)
except IndexError:
    print('Incorrect data')

try:
    with open("parttime.txt", "r") as reading_connection:
        for line in reading_connection:
            line = line.rstrip()
            info = line.split(',')
            job = info[0]
            company_name = info[1]
            type_of_employment = info[2]
            experience = info[3]
            rate_of_pay = info[4]

            print(line)
except IndexError:
    print('Incorrect data')


