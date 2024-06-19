import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        
        self.tasks = []
        
        # Create the input frame
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=10)
        
        self.task_input = tk.Entry(self.input_frame, width=50)
        self.task_input.pack(side=tk.LEFT, padx=10)
        
        self.add_button = tk.Button(self.input_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)
        
        # Create the tasks frame
        self.tasks_frame = tk.Frame(self.root)
        self.tasks_frame.pack(pady=10)
        
        self.tasks_listbox = tk.Listbox(self.tasks_frame, width=50, height=10, selectmode=tk.SINGLE)
        self.tasks_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        
        self.scrollbar = tk.Scrollbar(self.tasks_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        
        self.tasks_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.tasks_listbox.yview)
        
        # Create the buttons frame
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=10)
        
        self.complete_button = tk.Button(self.buttons_frame, text="Mark as Complete", command=self.mark_complete)
        self.complete_button.pack(side=tk.LEFT, padx=10)
        
        self.delete_button = tk.Button(self.buttons_frame, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=10)
    
    def add_task(self):
        task = self.task_input.get()
        if task != "":
            self.tasks.append(task)
            self.update_tasks_listbox()
            self.task_input.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    
    def mark_complete(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            self.tasks[selected_task_index] = self.tasks[selected_task_index] + " (Completed)"
            self.update_tasks_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")
    
    def delete_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_tasks_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")
    
    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
