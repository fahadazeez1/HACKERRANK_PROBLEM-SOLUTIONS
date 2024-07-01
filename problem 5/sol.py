def is_leap(year):
    leap = False
       
    if year % 400 == 0:
        leap= True
        return leap
    if year % 100 == 0:
        leap= False
        return leap
    if year % 4 == 0:
        leap= True
        return leap
    return False
    
    return leap

year = int(input())