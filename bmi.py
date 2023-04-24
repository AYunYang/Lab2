def calculate_bmi( height , weight):
 print("Height = " + str(height))
 print("Weight = " + str(weight))
 bmi=weight/(height**2)
 if bmi < 18.5:
    print("Under Weight")
 elif bmi >= 18.5 and bmi < 25:
    print("Normal Weight")
 elif bmi >= 25 and bmi < 30:
    print("Over Weight")
 else:
    print("Obese")
calculate_bmi(weight=57, height=1.73)



