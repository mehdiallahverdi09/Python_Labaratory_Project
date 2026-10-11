def start():
    weight=int(input("enter weight in kg: " ,))
    height=float(input("enter heigh in meters: " ,))
    BMI=weight/(height*height)
    if BMI < 18.5:
        print("Underweight")
    elif 18.5 <= BMI <= 24.9:
        print("Normal")
    elif 25 <= BMI <= 29.9:
        print("Overweight")
    else:
        print("Obese")