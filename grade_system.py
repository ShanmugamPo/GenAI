def grade_system():
    print("Welcome to the Grade System!")
    
    while True:
        try:
            mark = float(input("Enter your mark (0 - 100): "))
            
            if mark < 0 or mark > 100:
                print("Invalid mark. Please enter a value between 0 and 100.")
                continue
            
            elif mark >= 90:
                print(f"Mark: {mark} -> Grade: A")
            elif mark >= 80:
                print(f"Mark: {mark} -> Grade: B")
            elif mark >= 70:
                print(f"Mark: {mark} -> Grade: C")
            elif mark >= 60:
                print(f"Mark: {mark} -> Grade: D")
            else:
                print(f"Mark: {mark} -> Grade: E")
            break

        except ValueError:
            print("Please enter a valid numeric input.")
grade_system()
