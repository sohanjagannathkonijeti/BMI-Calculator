def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi


def feet_and_inches_to_meters(feet, inches):
    total_inches = feet * 12 + inches
    height_in_meters = total_inches * 0.0254
    return height_in_meters


def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


if __name__ == "__main__":
    try:
        weight = float(input("Enter your weight in kilograms: "))
        feet = int(input("Enter your height (feet): "))
        inches = int(input("Enter your height (inches): "))

        # Convert height to meters
        height = feet_and_inches_to_meters(feet, inches)

        bmi = calculate_bmi(weight, height)
        print(f"Your BMI is: {bmi:.2f}")
        bmi_category = interpret_bmi(bmi)
        print(f"You are classified as: {bmi_category}")
    except ValueError:
        print("Invalid input. Please enter numeric values for weight, feet, and inches.")
