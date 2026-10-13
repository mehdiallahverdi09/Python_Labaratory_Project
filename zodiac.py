def start():
    year=int(input("enter your birth year: ", ))
    zodiac_list=["monkey","rooster","dog","pig","rat", "ox","tiger","rabbit","dragon","snake","horse","sheep"]
    a=year%12
    print(zodiac_list[a]) 
