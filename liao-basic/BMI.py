height = 1.83
weight = 78
BMI = weight/(height**2)

if BMI > 32:
    print("overobese")
elif BMI > 28:
    print("obese")
elif BMI > 25:
    print("overweight")
elif BMI > 18.5:
    print("normal")
else:
    print("underweight")
