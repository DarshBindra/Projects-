import tkinter as tk
import matplotlib.pyplot as plt

def get_user_input(prompt, min_value=None, max_value=None):
    while True:
        try:
            user_input = float(input(prompt))
            if min_value is not None and user_input < min_value:
                print("Invalid input. Please enter a value greater than or equal to {}.".format(min_value))
            elif max_value is not None and user_input > max_value:
                print("Invalid input. Please enter a value less than or equal to {}.".format(max_value))
            else:
                return user_input
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def calculate_insulin_sensitivity_factor(bg_before, bg_after, carbs_total, insulin_dose, carbohydrate_ratio):
    bg_change = bg_after - bg_before
    isf = (bg_change / carbs_total) * carbohydrate_ratio / insulin_dose
    return isf


def calculate_insulin_dose(carbs_total, bg_current, isf, insulin_type):
    insulin_carbs = (carbs_total / 15) * ICT_RATIO
    insulin_correction = (bg_current - BG_TARGET_LOWER) * CORRECTION_FACTOR / (BG_TARGET_UPPER - BG_TARGET_LOWER)
    insulin_total = insulin_carbs + insulin_correction

    if insulin_type == "rapid-acting":
        insulin_total *= 1.1
    elif insulin_type == "short-acting":
        insulin_total *= 1.2
    elif insulin_type == "intermediate-acting":
        insulin_total *= 1.3
    elif insulin_type == "long-acting":
        insulin_total *= 1.4

    return insulin_total


def calculate_health_score(sugar_levels):
    health_score = 100 - (sugar_levels / 5)
    return health_score


def suggest_solutions(sugar_levels):
    if sugar_levels > 180:
        return "Your sugar levels are high. Consider adjusting your insulin dose and increasing physical activity."
    elif sugar_levels < 70:
        return "Your sugar levels are low. Consume some carbohydrates to raise your blood sugar."
    else:
        return "Your sugar levels are within the target range. Keep up the good work!"


def suggest_meals():
    return "For a balanced meal, consider having grilled chicken with quinoa and steamed vegetables."


def suggest_physical_activities():
    return "For physical activity, consider a 30-minute brisk walk followed by 15 minutes of bodyweight exercises."


def display_blood_glucose_history():
    blood_glucose_history = [85, 95, 110, 120, 130]  # Sample blood glucose readings
    print("Blood Glucose History:")
    for i, reading in enumerate(blood_glucose_history, 1):
        print("Reading {}: {} mg/dL".format(i, reading))


def calculate_health_score_gui():
    sugar_levels = float(sugar_levels_entry.get())
    health_score = calculate_health_score(sugar_levels)
    solution = suggest_solutions(sugar_levels)
    health_score_label.config(text="Health Score: {:.0f}%".format(health_score))
    solution_label.config(text=solution)


def calculate_insulin_dose_gui():
    carbs_total = int(carbs_total_entry.get())
    bg_current = int(bg_current_entry.get())
    isf = float(isf_entry.get())
    insulin_type = insulin_type_var.get()
    insulin_total = calculate_insulin_dose(carbs_total, bg_current, isf, insulin_type)
    insulin_dose_label.config(text="Insulin Dose: {:.1f} units".format(insulin_total))


def calculate_insulin_sensitivity_factor_gui():
    bg_before = int(bg_before_entry.get())
    bg_after = int(bg_after_entry.get())
    carbs_total = int(carbs_total_entry.get())
    insulin_dose = float(insulin_dose_entry.get())
    carbohydrate_ratio = float(carbohydrate_ratio_entry.get())
    isf = calculate_insulin_sensitivity_factor(bg_before, bg_after, carbs_total, insulin_dose, carbohydrate_ratio)
    isf_label.config(text="Insulin Sensitivity Factor: {:.2f} mg/dL per unit of insulin".format(isf))


def display_blood_glucose_history_gui():
    blood_glucose_history = [85, 95, 110, 120, 130]  # Sample blood glucose readings
    plt.plot(blood_glucose_history)
    plt.xlabel("Reading")
    plt.ylabel("Blood Glucose (mg/dL)")
    plt.show()


def suggest_meals_gui():
    meal_suggestion = suggest_meals()
    meal_label.config(text=meal_suggestion)


def suggest_physical_activities_gui():
    activity_suggestion = suggest_physical_activities()
    activity_label.config(text=activity_suggestion)


ICT_RATIO = 10
CORRECTION_FACTOR = 50
BG_TARGET_LOWER = 80
BG_TARGET_UPPER = 120

root = tk.Tk()
root.title("Diabetes Management")

sugar_levels_label = tk.Label(root, text="Enter your sugar levels (mg/dL):")
sugar_levels_label.grid(row=0, column=0)
sugar_levels_entry = tk.Entry(root)
sugar_levels_entry.grid(row=0, column=1)
calculate_button = tk.Button(root, text="Calculate Health Score", command=calculate_health_score_gui)
calculate_button.grid(row=0, column=2)

health_score_label = tk.Label(root, text="Health Score:")
health_score_label.grid(row=1, column=0)
solution_label = tk.Label(root, text="")
solution_label.grid(row=1, column=1)

carbs_total_label = tk.Label(root, text="Enter the total amount of carbohydrates you are going to consume (in grams):")
carbs_total_label.grid(row=2, column=0)
carbs_total_entry = tk.Entry(root)
carbs_total_entry.grid(row=2, column=1)
bg_current_label = tk.Label(root, text="Enter your current blood glucose level (mg/dL):")
bg_current_label.grid(row=3, column=0)
bg_current_entry = tk.Entry(root)
bg_current_entry.grid(row=3, column=1)
isf_label = tk.Label(root, text="Enter your insulin sensitivity factor (mg/dL per unit of insulin):")
isf_label.grid(row=4, column=0)
isf_entry = tk.Entry(root)
isf_entry.grid(row=4, column=1)
insulin_type_var = tk.StringVar(root)
insulin_type_var.set("rapid-acting")
insulin_type_options = ["rapid-acting", "short-acting", "intermediate-acting", "long-acting"]
insulin_type_dropdown = tk.OptionMenu(root, insulin_type_var, *insulin_type_options)
insulin_type_dropdown.grid(row=5, column=1)
calculate_button = tk.Button(root, text="Calculate Insulin Dose", command=calculate_insulin_dose_gui)
calculate_button.grid(row=6, column=0)
insulin_dose_label = tk.Label(root, text="Insulin Dose:")
insulin_dose_label.grid(row=6, column=1)

bg_before_label = tk.Label(root, text="Enter your blood glucose level (mg/dL) before the meal:")
bg_before_label.grid(row=7, column=0)
bg_before_entry = tk.Entry(root)
bg_before_entry.grid(row=7, column=1)
bg_after_label = tk.Label(root, text="Enter your blood glucose level (mg/dL) after the meal:")
bg_after_label.grid(row=8, column=0)
bg_after_entry = tk.Entry(root)
bg_after_entry.grid(row=8, column=1)
carbs_total_label = tk.Label(root, text="Enter the total amount of carbohydrates consumed (in grams):")
carbs_total_label.grid(row=9, column=0)
carbs_total_entry = tk.Entry(root)
carbs_total_entry.grid(row=9, column=1)
insulin_dose_label = tk.Label(root, text="Enter the insulin dose taken (in units):")
insulin_dose_label.grid(row=10, column=0)
insulin_dose_entry = tk.Entry(root)
insulin_dose_entry.grid(row=10, column=1)
carbohydrate_ratio_label = tk.Label(root, text="Enter your carbohydrate ratio (grams of carbs per unit of insulin):")
carbohydrate_ratio_label.grid(row=11, column=0)
carbohydrate_ratio_entry = tk.Entry(root)
carbohydrate_ratio_entry.grid(row=11, column=1)
calculate_button = tk.Button(root, text="Calculate Insulin Sensitivity Factor", command=calculate_insulin_sensitivity_factor_gui)
calculate_button.grid(row=12, column=0)
isf_label = tk.Label(root, text="Insulin Sensitivity Factor:")
isf_label.grid(row=12, column=1)

display_button = tk.Button(root, text="Display Blood Glucose History", command=display_blood_glucose_history_gui)
display_button.grid(row=13, column=0)

meal_button = tk.Button(root, text="Suggest Meals", command=suggest_meals_gui)
meal_button.grid(row=14, column=0)
meal_label = tk.Label(root, text="")
meal_label.grid(row=14, column=1)

activity_button = tk.Button(root, text="Suggest Physical Activities", command=suggest_physical_activities_gui)
activity_button.grid(row=15, column=0)
activity_label = tk.Label(root, text="")
activity_label.grid(row=15, column=1)
def save_data_to_file():
    data = {
        "sugar_levels": sugar_levels_entry.get(),
        "carbs_total": carbs_total_entry.get(),
        "bg_current": bg_current_entry.get(),
        "isf": isf_entry.get(),
        "insulin_type": insulin_type_var.get(),
        "bg_before": bg_before_entry.get(),
        "bg_after": bg_after_entry.get(),
        "insulin_dose": insulin_dose_entry.get(),
        "carbohydrate_ratio": carbohydrate_ratio_entry.get()
    }
    with open("diabetes_data.txt", "w") as f:
        for key, value in data.items():
            f.write(f"{key}: {value}\n")

save_button = tk.Button(root, text="Save Data to File", command=save_data_to_file)
save_button.grid(row=16, column=0)


root.mainloop()
