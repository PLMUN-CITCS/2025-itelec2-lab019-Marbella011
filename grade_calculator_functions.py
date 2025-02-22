def determine_letter_grade():
    try:
        grade_str = input("Enter your numeric grade: ")
        grade = int(grade_str)

        if grade >= 90:
            letter_grade = "A"
        elif grade >= 80:
            letter_grade = "B"
        elif grade >= 70:
            letter_grade = "C"
        elif grade >= 60:
            letter_grade = "D"
        else:
            letter_grade = "F"

        print(f"Your grade is: {letter_grade}")

    except ValueError:
        print("Invalid input. Please enter an integer.")

determine_letter_grade()
