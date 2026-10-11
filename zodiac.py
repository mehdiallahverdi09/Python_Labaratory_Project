def start():
    year=int(input("enter your birth year: ", ))
    zodiac_list=["monkey","rooster","dog","pig","rat", "ox","tiger","rabbit","dragon","snake","horse","sheep"]
    first=1896
    print(zodiac_list[(year-first)%12]) 