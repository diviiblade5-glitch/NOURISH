from db import foods



print("================================")
print("           NOURISH")
print("    Personalized Food Planner")
print("================================")

name = input("What is your name?: ")
date_of_birth = input("What is your date of birth?: ")
country = input("What country do you live in?: ")

print()
print(f"What best describes your usual work activity?\n"
      f"1. Mostly sitting or desk work\n"
      f"2. Mostly standing or light walking\n"
      f"3. Physically demanding work\n"
      f"4. Regular sports or gym training\n"
      f"5. Night-shift work\n"
      f"6. My activity varies")

activity = input("Choose an option (1-6): ")


if activity == "1":
    activity_type = "Low physical activity"

elif activity == "2":
    activity_type = "Light physical activity"

elif activity == "3":
    activity_type = "High physical activity"

elif activity == "4":
    activity_type = "High physical activity"

elif activity == "5":
    activity_type = "Night-shift work"

elif activity == "6":
    activity_type = "Variable activity"

else:
    activity_type = "Not specified"


print()
print(f"What is your nutrition goal?\n"
f"1. Eat healthier\n"
f"2. Lose weight\n"
f"3. Gain weight\n" 
f"4. Build muscle\n"
f"5. Maintain my current weight\n"
f"6. Create a regular eating schedule")

goal = input("Choose an option (1-6): ")


if goal == "1":
    nutrition_goal = "Eat healthier"

elif goal == "2":
    nutrition_goal = "Lose weight"

elif goal == "3":
    nutrition_goal = "Gain weight"

elif goal == "4":
    nutrition_goal = "Build muscle"

elif goal == "5":
    nutrition_goal = "Maintain my current weight"

elif goal == "6":
    nutrition_goal = "Create a regular eating schedule"

else:
    nutrition_goal = "Not specified"


if nutrition_goal == "Build muscle":
    nutrition_focus = "Protein and carbohydrates"

elif nutrition_goal == "Gain weight":
    nutrition_focus = "Nutrient-rich, energy-dense foods"

elif nutrition_goal == "Lose weight":
    nutrition_focus = "Nutrient-dense foods and appropriate portions"

elif nutrition_goal == "Maintain my current weight":
    nutrition_focus = "Balanced nutrition"

elif nutrition_goal == "Eat healthier":
    nutrition_focus = "A balanced variety of nutrients"

else:
    nutrition_focus = "Balanced nutrition"

print()
print("================================")
print("       YOUR NOURISH PROFILE")
print("================================")

print("Name:", name)
print("Date of Birth:", date_of_birth)
print("Country:", country)
print("Work Activity:", activity_type)
print("Goal:", nutrition_goal)
print("Nutrion_goal:", nutrition_focus)

print()
print("Nourish is preparing your")
print("personalized recommendations...")

print()
print("Foods currently available to Nourish:")

for food in foods:
    print("-", food["name"])

print()
print("==============================")
print("     NOURISH RECOMMENDATIONS")
print("==============================")

print("Based on your nutrition goal:")
print(nutrition_goal)
print()

for food in foods:
    if nutrition_goal == "Build muscle":
        if "Protein" in food["classes"]:
            print("-", food["name"])

    elif nutrition_goal == "Gain weight":
        if food["calories"] >= 120:
            print("-", food["name"])

    elif nutrition_goal == "Lose weight":
        if food["calories"] <= 130:
            print("-", food["name"])

    else:
        print("-", food["name"])