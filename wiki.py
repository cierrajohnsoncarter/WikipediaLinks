import datetime

answer_format = '%m/%d/%y'
url_format = '%b_%d_%y'
url = 'https://www.wikipedia.org/wiki/{}'

while True:
    answer = input(
        'What date would you like? Use MM/DD/YY format. Enter "quit" to quit. ')
    if answer.upper() == 'QUIT':
        break

    try:
        date = datetime.datetime.strptime(answer, answer_format)
        output = url.format(date.strftime(url_format))
        print(f'Things that happend on {answer}: \n  {output}')
    except ValueError:
        print('Please enter a valid date')
