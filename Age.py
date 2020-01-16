import datetime
def age():
    Present_time = datetime.datetime.now()
    year = int (Present_time.year)
    month = int(Present_time.strftime("%m"))
    date =  int(Present_time.strftime("%d"))
    hour = int (Present_time.strftime("%H"))
    mint = int(Present_time.strftime("%M"))
    seconds = int(Present_time.strftime("%S"))

    l = 0 
    if month == 1 or 3 or 5 or 7 or 8 or 10 or 12 :
        l = 31
    elif month == 4 or 6 or 9 or 11:
        l = 30
    elif month == 2 :
        if year%4 == 0:
            l = 29
        elif year%4 != 0:
            l = 28
    print ("Please input you'r date of birth here ")

    enter_year_msg = "input your birth year here:"

    y = 0

    while True:
        y = input(enter_year_msg)
        try:
            y = int(y)
            if y > year or y == 0:
                enter_year_msg = "Date is in future  input a valid year :"
                continue
            else:
                break
        except ValueError as e:
            enter_year_msg = "please input valid   year here:"
            continue

    m = 0
    enter_month_msg = "input you'r birth month here: "
    while  True:
        m = input(enter_month_msg)
        try: 
            m = int(m)
            if int(m) > 12 or m == 0 or  (int(m) > month and int(y) >= year):
                enter_month_msg = "Please input a valid month: "
                continue
            else:
                break
        except ValueError as e:
            enter_month_msg = "Please input vald month here: "
            continue

    d = 0
    enter_date_msg = "input you'r birth date here: "
    while  d < l:
        d = input(enter_date_msg )
        try:
            d = int (d) 
            if int(d) > l or d == 0 or (int(m) >= month and int(y) >= year and int(d)>date):
                enter_date_msg = "Please input valid birth date here: "
            else:
                break
        except ValueError as t:
            enter_date_msg = "Please input valid birth date here: "
            continue
          
    z =  year - y - 1
    n =  z + y
    if  int(y) == year:
        z+= 1

    tt = 12- m
    if n < year:
        tt += month
    if int(y) == year and int(m)<= month:
        tt = month - int(m)
    if tt == 12 :
        tt = 0
        z += 1  

    dd = 0
    if date >= d:
        dd = date - d
    elif date < d:
        tt -=1
        dd = (l - d) + date

    weeks = dd // 7
    days = dd % 7

    print ("your duration on this planet is " + str(z)+ "years "+ str(tt)+"months "+ str(weeks) + "weeks " + str(days)+ "days " + str(hour)+ "hours " + str(mint)+ "minutes "+ str(seconds)+ "seconds ")

age()




    
