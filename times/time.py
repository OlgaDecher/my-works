from datetime import datetime

def variables(now_time):
    hours = int((now_time[:2]))
    minutes = int((now_time[3:]))
    return hours, minutes  

def auto_time():
    now_time = str(datetime.now().time())[:5]
    print("Данные введены неверно, будет использовано текущее время")
    hours, minutes = variables(now_time)
    return hours, minutes, now_time

def info_hour(hours):
    if hours >= 12:
        hours = hours - 12
    if hours == 0:
        info = (hours,2)
    elif hours == 1:
        info = (hours,0)
    elif hours < 5 :
        info = (hours,1)
    else:
        info = (hours,2)
    return info
   
def minutes_to(minutes):
    if 60-minutes == 1:
        info = (min_numbers[1][0][1],2)
    elif 60-minutes ==10:
        info = (min_numbers[1][1][1],1)
    elif 60-minutes < 10:
        info = (min_numbers[60-minutes][0][1],1)
    else:
        info = (min_numbers[60-minutes-10][2][1],1)
    return info

def minutes_past(minutes):
    if minutes % 10 == 1 and minutes != 11:
        info = (f'{min_numbers[minutes // 10][1][0]}{min_numbers[minutes % 10][0][0]}',0)
    elif minutes % 10 < 5 and minutes not in range (11,15):
        info = (f'{min_numbers[minutes // 10][1][0]}{min_numbers[minutes % 10][0][0]}',2)
    elif minutes in range (11,20):
        info = (min_numbers[minutes % 10][2][0],1)
    else:
        info = (f'{min_numbers[minutes // 10][1][0]}{min_numbers[minutes % 10][0][0]}',1)
    return info

now_time = input('Укажите время в формате ЧЧ:ММ, в ином случае \
время будет определено автоматически: ')  

while True:
    if (now_time[:2]).isdigit() and (now_time[3:]).isdigit():
        hours, minutes = variables(now_time)
    else:
        hours, minutes, now_time = auto_time()
        break

    if ((len(now_time) != 5) or (hours > 23 or hours < 0) or (minutes > 59 or minutes < 0) 
    or (now_time[2] != ':')):
        hours, minutes, now_time = auto_time()
        break
    break
  
min_numbers = {1:(("одна","одной"),("десять ","десяти"),("одинадцать","одинадцати"))}
min_numbers[2] = (("две","двух"),("двадцать ",''),("двенадцать","двенадцати"))
min_numbers[3] = (("три","трёх"),("тридцать ",''),("тринадцать","тринадцати"))
min_numbers[4] = (("четыре","четырёх"),("сорок ",''),("четырнадцать","четырнадцати"))
min_numbers[5] = (("пять","пяти"),(),("пятнадцать","пятнадцати"))
min_numbers[6] = (("шесть","шести"),(),("шестнадцать",''))
min_numbers[7] = (("семь","семи"),(),("семнадцать",''))
min_numbers[8] = (("восемь","восьми"),(),("восемнадцать",''))
min_numbers[9] = (("девять","девяти"),(),("девятнадцать",''))
min_numbers[0] = (('',''),('',''),())

hour_number = {1:("один","первого")}
hour_number[2] = ("два","второго")
hour_number[3] = ("три","третьего")
hour_number[4] = ("четыре","четвертого")
hour_number[5] = ("пять","пятого")
hour_number[6] = ("шесть","шестого")
hour_number[7] = ("семь","седьмого")
hour_number[8] = ("восемь","восьмого")
hour_number[9] = ("девять","девятого")
hour_number[10] = ("десять","десятого")
hour_number[11] = ("одинадцать","одинадцатого")
hour_number[12] = ("двенадцать","двенадцатого")
hour_number[0] = ("двенадцать","двенадцатого")

time = (('час','часа','часов'),('минута','минут','минуты'))

info_hours = info_hour(hours)

if minutes == 0:
    print(f'{now_time} - {hour_number[info_hours[0]][0]} {time[0][info_hours[1]]} ровно')
elif minutes == 30:
    print(f'{now_time} - половина {hour_number[(info_hours[0])+1][1]}')
elif minutes >= 45:
    info_minutes = minutes_to(minutes)
    print(f'{now_time} - без {info_minutes[0]} {time[1][info_minutes[1]]} {hour_number[(info_hours[0])+1][0]}')
else:
    info_minutes = minutes_past(minutes)
    print(f'{now_time} - {info_minutes[0]} {time[1][info_minutes[1]]} {hour_number[(info_hours[0])+1][1]}')