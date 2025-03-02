def main():
    # ask the user for the number of rows and how many seats per row 
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of seats per row: "))
    total_seats = rows * cols

# Store student info
    students = []
    for i in range(10):
        name = input(f"Enter name of student {i+1}: ")
        absences = input(f"Enter number of absences for {name}: ")
        students.append((name, absences))

# Create the chart
    seating_chart = []
    student_index = 0
    for r in range(rows):
        row = []
        for c in range(cols):
            if student_index < len(students):
                row.append(students[student_index])
                student_index += 1
            else:
                # If there are extra seats, mark them as empty.
                row.append(("Empty", ""))
        seating_chart.append(row)

# Output the seating chart in the given structure.
    print("\nSeating Chart:")
    for row in seating_chart:
        for seat in row:
            if seat[0] == "Empty":
                print("Empty", end="\t")
            else:
# Print name and absences with new line after each row
                print(f"{seat[0]} ({seat[1]} absences)", end="\t")
        print()  
if __name__ == '__main__':
    main()
