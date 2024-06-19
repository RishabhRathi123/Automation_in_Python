import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
from threading import Thread
import time
from plyer import notification
from PyDictionary import PyDictionary
import random

class ReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reminder Application")
        
        self.reminder_time = tk.StringVar()
        self.message = tk.StringVar()
        self.reminders = []
        self.dictionary = PyDictionary()
        
        tk.Label(root, text="Set Reminder Time (HH:MM)").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.reminder_time).grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(root, text="Reminder Message").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.message).grid(row=1, column=1, padx=10, pady=10)
        
        tk.Button(root, text="Set Reminder", command=self.set_reminder).grid(row=2, column=0, columnspan=2, pady=10)
        
        # Start a separate thread to check reminders
        self.check_thread = Thread(target=self.check_reminders)
        self.check_thread.daemon = True
        self.check_thread.start()
    
    def set_reminder(self):
        try:
            reminder_time_str = self.reminder_time.get()
            reminder_time = datetime.strptime(reminder_time_str, "%H:%M").time()
            reminder_datetime = datetime.combine(datetime.now(), reminder_time)
            
            if reminder_datetime < datetime.now():
                reminder_datetime += timedelta(days=1)
            
            message = self.message.get()
            
            self.reminders.append((reminder_datetime, message))
            messagebox.showinfo("Reminder Set", f"Reminder set for {reminder_time_str}")
        except ValueError:
            messagebox.showerror("Invalid Time", "Please enter the time in HH:MM format")
    
    def get_random_word(self):
        words = self.dictionary.get_synonyms("example")  # Using "example" to get a list of random words
        if words:
            return random.choice(words)
        else:
            return "example"
    
    def check_reminders(self):
        while True:
            current_time = datetime.now()
            for reminder in self.reminders:
                reminder_datetime, message = reminder
                if current_time >= reminder_datetime:
                    random_word = self.get_random_word()
                    notification.notify(
                        title="Reminder",
                        message=f"{message}\n\nDictionary Word: {random_word}",
                        timeout=10
                    )
                    self.reminders.remove(reminder)
            time.sleep(1)

if __name__ == "__main__":
    root = tk.Tk()
    app = ReminderApp(root)
    root.mainloop()
