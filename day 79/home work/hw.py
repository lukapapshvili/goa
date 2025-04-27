def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Yes"
    else:
        return "No"

years = [2100, 2104, 2400]

for year in years:
    print(f"{year} - {is_leap_year(year)}")
    #BONUS
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def nearest_leap_year(year):
    # ვეძებთ უახლოეს ნაკიან წელს
    up = year + 1
    down = year - 1

    while True:
        if is_leap_year(down):
            return down
        if is_leap_year(up):
            return up
        up += 1
        down -= 1

years = [2100, 2104, 2400]

for year in years:
    if is_leap_year(year):
        print(f"{year} - Yes")
    else:
        nearest = nearest_leap_year(year)
        print(f"{year} - No, nearest leap year is {nearest}")
