import tkinter as tk
import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="your_host",
    user="your_username",
    password="your_password",
    database="BusinessDB"
)

# Create a cursor to execute SQL queries
cursor = db.cursor()

# Function to fetch and display employee data
def show_employees():
    query = "SELECT * FROM Employees"
    cursor.execute(query)
    employees = cursor.fetchall()

    # Display employee data in a simple GUI window
    root = tk.Tk()
    root.title("Employee Data")
    
    # Create a label to display the data
    label = tk.Label(root, text="Employee Data", font=("Arial", 14))
    label.pack()

    # Display employee information in a text widget
    text_box = tk.Text(root, height=10, width=50)
    text_box.pack()

    for employee in employees:
        text_box.insert(tk.END, f"ID: {employee[0]}, Name: {employee[1]}, Department ID: {employee[2]}, Position: {employee[3]}, Salary: {employee[4]}\n")
    
    root.mainloop()

# Call the function to display employee data
show_employees()
