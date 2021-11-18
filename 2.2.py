


def isLeapYear(year):

    if 1900  < 1900 and rok < 10000:
        if rok % 4 == 0:
            if rok % 100 == 0:
                if rok % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    else:
        return False;
        
if __name__ == '__main__':
    while True:
        i = int(input())
        print(rok_przestepny(i))