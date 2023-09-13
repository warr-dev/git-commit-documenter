import tkinter as tk
from tkcalendar import Calendar
from datetime import datetime

def generate_report():
    start_date = start_cal.get_date()
    end_date = end_cal.get_date()
    
    # Use the start and end date values for generating the report
    # Replace this with your report generation logic
    
    result_label.config(text=f"Start Date: {start_date}\nEnd Date: {end_date}\nReport Generated!")

# Create the main window
root = tk.Tk()
root.title("Git Commit Report Generator")

# Create and place labels and calendar widgets for start and end dates
start_label = tk.Label(root, text="Start Date:")
start_label.pack()

start_cal = Calendar(root, selectmode='day', date_pattern='yyyy-mm-dd')
start_cal.pack()

end_label = tk.Label(root, text="End Date:")
end_label.pack()

end_cal = Calendar(root, selectmode='day', date_pattern='yyyy-mm-dd')
end_cal.pack()

# Create a button to generate the report
generate_button = tk.Button(root, text="Generate Report", command=generate_report)
generate_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Start the GUI application
root.mainloop()
