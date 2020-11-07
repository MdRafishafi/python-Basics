import datetime
# this is an example progame
def birth_date():
  year = int(input('Which year did u born?\n'))
  current_year = datetime.datetime.now()
  print(f"your age is {current_year.year - year}")