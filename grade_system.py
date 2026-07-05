def grade_system():
  
    try:
        print("Welcome to the Grade System!")
        mark = float(input("Enter your mark (0 - 100): "))
        if mark <= 0 or mark > 100:
            print("Invalid mark. Please enter a value between 0 and 100.")
        elif mark >= 90 and mark <= 100:
            print(f"Mark: {mark} -> Grade: A")
        elif mark >= 80 and mark <= 89:
            print(f"Mark: {mark} -> Grade: B")
        elif mark >= 70 and mark <= 79:
            print(f"Mark: {mark} -> Grade: C")
        elif mark >= 60 and mark <= 69:
            print(f"Mark: {mark} -> Grade: D")
        else:
            print(f"Mark: {mark} -> Grade: E")

    except:
        print("Please enter a numeric valid input.")
grade_system()