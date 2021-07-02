from datetime import date

dob = input("enter your date of birth as dd.mm.yyyy : ")

year_dob = int(dob[-4:])
print('year : ',year_dob)

year_death = year_dob + 90
print('year of death : ',year_death)
month = int(dob[3:5])
print('month : ',month)
day = int(dob[0:2])
print('date : ',day)

today_date = date.today()

leap_monthly_dict = {1:31,2:29,3:31,4:31,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
normal_monthly_dict = {1:31,2:28,3:31,4:31,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

leap_year = 'n'

if (year_dob % 4) == 0:
   if (year_dob % 100) == 0:
       if (year_dob % 400) == 0:
            monthly_dict = leap_monthly_dict
            leap_year = 'y'
       else:
            monthly_dict = normal_monthly_dict
            leap_year = 'n'
   else:
        monthly_dict = leap_monthly_dict
        leap_year = 'y'
else:
    monthly_dict = normal_monthly_dict
    leap_year = 'n'


def validate(dob) :
    val = [0,1,3,4,6,7,8,9]
    for i in val:
        if not (dob[i].isnumeric()):
            return False
    
    if not(dob[2] == '.' and dob[5] == '.'):
        return False
    print('montly day',monthly_dict[month])
    if month > 12 or day > monthly_dict[month]:
        return False

    if month <= 0 or year_dob <= 0 or day <=0:
        return False


    return True



if validate(dob):

    print('this seems to work')

    date_dob = date(year_dob,month,day)
    if leap_year == 'y':
        date_death = date(year_death,month+1,1)
    else:
        date_death = date(year_death,month,day)
    print('D.O.B :',date_dob)
    print('D.O.D :',date_death)
    print('TODAY :',today_date)

    days_lived = (today_date-date_dob).days

    days_remaining = (date_death - today_date).days

    if days_remaining < 1 :
        print("Am I speaking with a Ghost ? ")
    else:
        print(f"You've lived {days_lived} days and you've got {days_remaining} left. Enjoy...!!!")
else:
    print("nope, your d.o.b is wrong buddy.")
