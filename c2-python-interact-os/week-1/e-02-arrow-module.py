import arrow

date = arrow.get('2020-01-18', 'YYYY-MM-DD')
print(date)

print(date.shift(weeks=+6).format('MM DD YYYY'))
