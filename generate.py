from random import randrange, choice
from datetime import timedelta, datetime
import names 

def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return datetime.strftime(start + timedelta(seconds=random_second), '%d/%m/%Y')


d1 = datetime.strptime('1/1/1980 1:30 PM', '%d/%m/%Y %I:%M %p')
d2 = datetime.strptime('1/1/2000 4:50 AM', '%d/%m/%Y %I:%M %p')
N = 100

# cities:
cities = ["Moscow", "Petersburg", "Kazan"]

#id:
id = list(range(1, N+1))

fp= open('data.txt', 'w')
for i in range(N):
    
    p_id = id[i]
    p_name = str(names.get_full_name())
    p_date = random_date(d1, d2)
    p_city_work = choice(cities)
    p_city_live = choice(cities)
    
    
    temp_list = [p_id, p_name, p_date, p_city_live, p_city_work]
    fp.write("(")
    fp.write("%d, " % temp_list[0])
    for item in temp_list[1:-1]:
        fp.write("'%s', " % item)
    fp.write("'" + temp_list[-1] + "'")
    fp.write("),\n")