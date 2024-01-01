
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap Year")
            else:
                print("not leap year")
        else:
            print("Leap Year")
    else:
        print("Not Leap Year")

while True:
    year = int(input("Enter the year: "))
    is_leap_year(year)