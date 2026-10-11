def start():
    set1 = [4,5,6,7,12,13,14,15,20,21,22,23,28,29,30,31]
    set2 = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]
    set3 = [8,9,10,11,12,13,14,15,24,25,26,27,28,29,30,31]
    set4 = [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    set5 = [2,3,6,7,10,11,14,15,18,19,22,23,26,27,30,31]
    
    sets = [set1, set2, set3, set4, set5]

    day = 0 

    for i in range(0,5):
        print("Set", i + 1, ":", sets[i])
        print("Is your birthday included in this set?")
        answer = int(input("Enter 1 for Yes and 0 for No: "))
        if answer == 1:
            day = day + sets[i][0] 

    print("Your birthday is:", day)

