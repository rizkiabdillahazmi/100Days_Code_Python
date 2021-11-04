age = input("What is your current age ? ")

age_day_remaining = (90*365)-(int(age)*365)
age_week_remaining = (90*52)-(int(age)*52)
age_month_remaining = (90*12)-(int(age)*12)

print(
    f"You have {age_day_remaining} days, {age_week_remaining} weeks, and {age_month_remaining} months left.")
