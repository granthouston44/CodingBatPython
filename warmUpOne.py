
def sleep_in(weekday, vacation):
    if weekday == True and vacation == False:
        return False
    else :
        return True

def monkey_trouble(a_smile, b_smile):
    if a_smile == b_smile:
        return True
    else:
        return False

def sum_double(a, b):
    if a == b:
        return (a+b)*2
    else: 
        return a+b

def diff21(n):
    result = abs(n-21)
    if n > 21:
        return result * 2
    else:
        return result

def parrot_trouble(talking, hour):
    if ((hour < 7) or (hour > 20)) and (talking == True):
        return True
    else: 
        return False

def makes10(a,b):
    if (a+b == 10) or ((a == 10) or (b == 10)):
        return True
    else:
        return False
