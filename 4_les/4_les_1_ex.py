from sys import argv

script_name, output_in_hours, rate_per_hour, prize = argv

print("Output in hours: ", output_in_hours)
print("Rate per hour: ", rate_per_hour)
print("Prize: ", prize)

wage = (int(output_in_hours) * int(rate_per_hour)) + int(prize)
print(f"Wage = {wage}")
