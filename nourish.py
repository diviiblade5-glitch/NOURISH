from db import foods


print("==============================")
print("          NOURISH")
print("   Personalized Food Planner")
print("==============================")


# ----------------------------
# USER INFORMATION
# ----------------------------

name = input("What is your name?: ")
date_of_birth = input("What is your date of birth? (dd/mm/yyyy): ")
country = input("Which country do you live in?: ")


# ----------------------------
# WORK ACTIVITY
# ----------------------------

print()
print("What best describes your usual work activity?")
print("1. Mostly sitting or desk work")
print("2. Mostly standing or light walking")
print("3. Physically demanding work")
print("4. Regular sports or gym training")
print("5. Night-shift work")
print("6. My activity varies")

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


# ----------------------------
# NUTRITION GOAL
# ----------------------------

print()
print("What is your nutrition goal?")
print("1. Eat healthier")
print("2. Lose weight")
print("3. Gain weight")
print("4. Build muscle")
print("5. Maintain my current weight")
print("6. Create a regular eating schedule")

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


# ----------------------------
# NUTRITION FOCUS
# ----------------------------

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


# ----------------------------
# ACTIVITY FOCUS
# ----------------------------

if activity_type == "High physical activity":
    activity_focus = "Focus on adequate energy, protein and carbohydrates"

elif activity_type == "Light physical activity":
    activity_focus = "Focus on balanced meals and adequate protein"

elif activity_type == "Low physical activity":
    activity_focus = "Focus on balanced meals, fiber, protein and appropriate portions"

elif activity_type == "Night-shift work":
    activity_focus = "Focus on balanced meals and consistent nutrition during shifts"

elif activity_type == "Variable activity":
    activity_focus = "Adjust food intake according to daily activity levels"

else:
    activity_focus = "Focus on balanced nutrition"


# ----------------------------
# PROFILE
# ----------------------------

print()
print("==============================")
print("       YOUR NOURISH PROFILE")
print("==============================")

print("Name:", name)
print("Date of Birth:", date_of_birth)
print("Country:", country)
print("Work Activity:", activity_type)
print("Goal:", nutrition_goal)
print("Nutrition goal:", nutrition_focus)
print("Activity Focus:", activity_focus)


# ----------------------------
# PREPARING RECOMMENDATIONS
# ----------------------------

print()

# ----------------------------
# FOOD DATABASE
# ----------------------------

print("=========================")
print("     AVAILABLE FOODS")
print("=========================")

print()
print("Foods currently available to Nourish:")

for food in foods:
    print("-", food["name"])


# ----------------------------
# CALCULATE FOOD SCORE
# ----------------------------
def get_nutritional_needs(nutrition_goal, activity_type):

    needs = []

    if nutrition_goal == "Build muscle":
        needs.append("Protein")
        needs.append("Carbohydrates")

    elif nutrition_goal == "Gain weight":
        needs.append("Protein")
        needs.append("Carbohydrates")
        needs.append("Healthy fats")

    elif nutrition_goal == "Lose weight":
        needs.append("Protein")
        needs.append("Fiber")

    elif nutrition_goal == "Eat healthier":
        needs.append("Protein")
        needs.append("Vitamins")
        needs.append("Minerals")
        needs.append("Fiber")

    elif nutrition_goal == "Maintain my current weight":
        needs.append("Balanced nutrition")

    elif nutrition_goal == "Create a regular eating schedule":
        needs.append("Balanced meals")

    # Activity can add another nutritional priority
    if activity_type == "High physical activity":
        needs.append("Energy")

    elif activity_type == "Low physical activity":
        needs.append("Moderate energy intake")

    return needs

nutritional_needs = get_nutritional_needs(
    nutrition_goal,
    activity_type
)

print()
print("Nutritional needs:")
for need in nutritional_needs:
    print("-", need)

def explain_food_classes(food):

    benefits = []

    if "Protein" in food["classes"]:
        benefits.append(
            "Provides protein to support muscle maintenance."
        )

    if "Carbohydrates" in food["classes"]:
        benefits.append(
            "Provides carbohydrates for energy."
        )

    if "Healthy fats" in food["classes"]:
        benefits.append(
            "Provides healthy fats that support normal body functions."
        )

    if "Vitamins" in food["classes"]:
        benefits.append(
            "Provides vitamins that support normal body functions and immune health."
        )

    if "Minerals" in food["classes"]:
        benefits.append(
            "Provides minerals that support bones, metabolism, and other body functions."
        )

    if "Fiber" in food["classes"]:
        benefits.append(
            "Provides dietary fiber that supports digestion."
        )

    return benefits


def check_nutritional_need(food, need):

    if need == "Protein":
        return "Protein" in food["classes"]

    if need == "Carbohydrates":
        return "Carbohydrates" in food["classes"]

    if need == "Healthy fats":
        return "Healthy fats" in food["classes"]

    if need == "Vitamins":
        return "Vitamins" in food["classes"]

    if need == "Minerals":
        return "Minerals" in food["classes"]

    if need == "Fiber":
        return food["fiber"] >= 3

    return False



def calculate_score(food, nutrition_goal, activity_type):

    score = 0
    reasons = []


    # ----------------------------
    # GOAL SCORING
    # ----------------------------

    if nutrition_goal == "Build muscle":

        if "Protein" in food["classes"]:
            score += 3
            reasons.append("Good source of protein")

        if "Carbohydrates" in food["classes"]:
            score += 1
            reasons.append("Provides carbohydrates for energy")


    elif nutrition_goal == "Gain weight":

        if food["protein"] >= 8:
            score += 2
            reasons.append("Good source of protein")

        if food["carbohydrates"] >= 20:
            score += 2
            reasons.append("Provides carbohydrates for energy")


    elif nutrition_goal == "Lose weight":

        if "Protein" in food["classes"]:
            score += 2
            reasons.append("Provides protein")

        if food["carbohydrates"] <= 20:
            score += 1
            reasons.append("Contains a moderate amount of carbohydrates")


    elif nutrition_goal == "Eat healthier":

        if food["protein"] >= 5:
            score += 1
            reasons.append("Provides a good amount of protein")

        if food["fat"] <= 10:
            score += 1
            reasons.append("Contains a moderate amount of fat")
        if "Vitamins" in food["classes"]:
            score += 1
            reasons.append("Provides vitamins")

        if "Minerals" in food["classes"]:
            score += 1
            reasons.append("Provides minerals")

        if food["fiber"] >= 3:
           score += 1
           reasons.append("Provides a good amount of fiber")


    elif nutrition_goal == "Maintain my current weight":

        score += 1
        reasons.append("Can contribute to a balanced diet")


    elif nutrition_goal == "Create a regular eating schedule":

        score += 1
        reasons.append("Can be included in a regular meal")


    # ----------------------------
    # ACTIVITY SCORING
    # ----------------------------

    if activity_type == "High physical activity":

        if food["protein"] >= 8:
            score += 2
            reasons.append("Supports higher protein needs")

        if food["carbohydrates"] >= 20:
            score += 2
            reasons.append("Provides energy for physical activity")


    elif activity_type == "Light physical activity":

        if food["protein"] >= 5:
            score += 1
            reasons.append("Provides protein for daily activity")


    elif activity_type == "Low physical activity":

        if food["fat"] <= 10:
            score += 1
            reasons.append("Fits a lower-energy activity pattern")


    elif activity_type == "Night-shift work":

        if food["protein"] >= 5:
            score += 1
            reasons.append("Provides protein during your work schedule")


    elif activity_type == "Variable activity":

        if food["protein"] >= 5:
            score += 1
            reasons.append("Provides protein for varying activity levels")


    return score, reasons


# ----------------------------
# CALCULATE RECOMMENDATIONS
# ----------------------------

recommendations = []


for food in foods:

    score, reasons = calculate_score(
        food,
        nutrition_goal,
        activity_type
    )

    
    benefits = explain_food_classes(food)


    # ----------------------------
    # ADD FOOD TO RECOMMENDATIONS
    # ----------------------------

    if score > 0:

        recommendations.append({
            "name": food["name"],
            "score": score,
            "reasons": reasons,
            "benefits": benefits,
            "protein": food["protein"],
            "carbohydrates": food["carbohydrates"],
            "fat": food["fat"],
            "fiber": food["fiber"]
            
        })


# ----------------------------
# SORT RECOMMENDATIONS
# ----------------------------

recommendations.sort(
    key=lambda food: food["score"],
    reverse=True
)


# ----------------------------
# DISPLAY RECOMMENDATIONS
# ----------------------------

print()
print("==============================")
print("     NOURISH RECOMMENDATIONS")
print("==============================")

print()

print("Nourish is preparing your")
print("personalized recommendations...")

print()

print("Based on your goal and activity:")
print(nutrition_goal)
print(activity_type)

print()

print("Top Nourish Recommendations:")
print()


for recommendation in recommendations[:3]:

    print(
        "-",
        recommendation["name"],
        "| Score:",
        recommendation["score"]
    )

    print(
        "  Protein:",
        recommendation["protein"],
        "g"
    )

    print(
        "  Carbohydrates:",
        recommendation["carbohydrates"],
        "g"
    )

    print(
        "  Fat:",
        recommendation["fat"],
    
        "g"
    )

    print(
        "  Fiber:",
        recommendation["fiber"],

        "g"
    )

    print("  Why Nourish recommends it:")

    for reason in recommendation["reasons"]:
        print("   -", reason)

    print()

    print("  Nutritional benefits:")

    for benefit in recommendation["benefits"]:
        print("   -", benefit)

    print()
    print("--------------------------------")
    print()