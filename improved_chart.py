def print_seating_chart(seating_chart):
    # Convert each seat to a string representation.
    table = []
    for row in seating_chart:
        row_cells = []
        for seat in row:
            if seat[0] == "Empty":
                cell_str = "Empty"
            else:
                cell_str = f"{seat[0]} ({seat[1]} absences)"
            row_cells.append(cell_str)
        table.append(row_cells)
    
    # Determine the maximum width for each column.
    cols = len(table[0])
    col_widths = [0] * cols
    for row in table:
        for j, cell in enumerate(row):
            col_widths[j] = max(col_widths[j], len(cell))
    
    # Function to print a horizontal separator.
    def print_separator():
        line = "+"
        for width in col_widths:
            line += "-" * (width + 2) + "+"
        print(line)
    
    # Print the table with borders.
    for row in table:
        print_separator()
        row_line = ""
        for j, cell in enumerate(row):
            row_line += f"| {cell.ljust(col_widths[j])} "
        row_line += "|"
        print(row_line)
    print_separator()

def main():
    # Ensure the seating chart can hold at least 10 students.
    while True:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of seats per row: "))
        if rows * cols < 10:
            print("The seating chart must have at least 10 seats. Please try again.")
        else:
            break

    # Store student info.
    students = []
    for i in range(10):
        name = input(f"Enter name of student {i+1}: ")
        absences = input(f"Enter number of absences for {name}: ")
        students.append((name, absences))
    
    # Create the seating chart.
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
    
    # Output the seating chart in an improved table format.
    print("\nSeating Chart:")
    print_seating_chart(seating_chart)

if __name__ == '__main__':
    main()
