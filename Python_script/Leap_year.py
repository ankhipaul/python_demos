def is_leap(year):
    leap = False

    # Write your logic here
    # if year%4==0:
    #   if year%100==0:
    #      if year%400==0:
    #       leap='True'
    #    leap='False'
    # leap='True'
    # else :
    #   leap='False'

    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)


year = int(input())
print(is_leap(year))