a = int(input("Enter a value for a: "))
b= int(input("Enter a value for b: "))
c = int(input("Enter a value for c: "))


expr1 = a < b < c
expr2 = not (a > b or b > c)
expr3 = a <= b and b <= c

print("a < b < c:", expr1)
print("not (a > b or b > c):", expr2)
print("a <= b and b <= c:", expr3)



# Problem 2

# Get user input
temp = int(input("Enter the current temperature (°F): "))
rain = input("Is it raining? (yes/no): ").strip().lower()

# Extreme heat always overrides
if temp > 100:
    print("EXTREME HEAT WARNING: Stay indoors!")

elif temp > 85:
    if rain == "yes":
        print("Warm rain - watch for flash floods.")
    else:
        print("Hot and dry - stay hydrated.")

elif 60 <= temp <= 85:
    if rain == "yes":
        print("Grab an umbrella!")
    else:
        print("Nice weather - enjoy your day!")

elif 32 <= temp <= 59:
    print("It's cold - bundle up!")

else:
    print("FREEZE WARNING: Roads may be icy!")
    

# Problem 3:

# Get student info
first = input("Enter student first name: ")
last = input("Enter student last name: ")

exam1 = float(input("Enter Exam 1 score: "))
exam2 = float(input("Enter Exam 2 score: "))
exam3 = float(input("Enter Exam 3 score: "))

# Calculate average
avg = (exam1 + exam2 + exam3) / 3

# Determine letter grade
if 90 <= avg <= 100:
    grade = "A"
elif 87 <= avg <= 89:
    grade = "A-"
elif 83 <= avg <= 86:
    grade = "B+"
elif 80 <= avg <= 82:
    grade = "B"
elif 77 <= avg <= 79:
    grade = "B-"
elif 73 <= avg <= 76:
    grade = "C+"
elif 70 <= avg <= 72:
    grade = "C"
elif 67 <= avg <= 69:
    grade = "C-"
elif 63 <= avg <= 66:
    grade = "D+"
elif 60 <= avg <= 62:
    grade = "D"
else:
    grade = "F"

# Determine standing
if avg >= 90:
    status = "Dean's List"
elif avg >= 70:
    status = "Good Standing"
elif avg >= 60:
    status = "Academic Probation"
else:
    status = "Academic Suspension Warning"

# Print formatted report
print("\nSTUDENT GRADE REPORT\n")
print("Student:", first, last)
print("Exam 1:", exam1)
print("Exam 2:", exam2)
print("Exam 3:", exam3)
print("Average:", round(avg, 2))
print("Grade:", grade)
print("Status:", status)