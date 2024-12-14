## Leap year or not

year = int(input("Enter a year: "))
is_divisible_by_4 = year % 4
is_divisible_by_100 = year % 100
is_divisible_by_400 = year % 400

if is_divisible_by_4 == 0:
    if is_divisible_by_100 == 0:
        if is_divisible_by_400 == 0:
            print ("leap year")
    else:
        print("not a leap year")            
