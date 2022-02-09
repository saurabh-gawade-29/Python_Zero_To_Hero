# BMI : BODY MASS INDEX
# BMI = KG/M^2

weight_in_kg = float(input("Enter your Weight: "))
height_in_meter = float(input("Enter your Height "))
bmi = weight_in_kg/(height_in_meter*height_in_meter)

print("BMI is: " , bmi)