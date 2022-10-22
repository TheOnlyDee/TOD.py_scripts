#Progetto a pagina 134 del libro "CODING: Guida Facile Per Principianti" (apogeonline.com)
#messo in pratica da TOD (https://github.com/TheOnlyDee)

import csv

from collections import namedtuple

import tkinter

from tkinter.filedialog import askopenfilename

Task = namedtuple("Task", ["title", "duration", "prerequisites"])

import time



def read_task(filename):
    tasks = {}
    for row in csv.reader(open(filename)):
        number = int(row[0])
        title = row[1]
        duration = float(row[2])
        prerequisites = set(map(int, row[3].split()))
        tasks[number] = Task(title, duration, prerequisites)
    return tasks

#read_task("project.csv")

tasks = read_task("project.csv")

#pcanvas = tkinter.Canvas(root, width=800, height=400, bg="white")rint(tasks[1].title)
#time.sleep(1)
def order_tasks(tasks):
    incomplete = set(tasks)
    completed = set()
    start_days = {}
    while incomplete:
        for task_number in incomplete:
            task = tasks[task_number]
            if task.prerequisites.issubset(completed):
                earliest_start_day = 0
                for prereq_number in task.prerequisites:
                    prereq_end_day = start_days[prereq_number] + tasks[prereq_number].duration
                    if prereq_end_day > earliest_start_day:
                        earliest_start_day = prereq_end_day
                start_days[task_number] = earliest_start_day
                incomplete.remove(task_number) 
                completed.add(task_number)
                break
    return start_days

canvas = tkinter.Canvas( width=800, height=400, bg="white")

def draw_chart(tasks, canvas, row_height = 40, title_width = 300, line_height = 40, day_width = 20, bar_height = 300, title_indent = 20, font_size = -16):
    height = canvas["height"]
    width =canvas["width"]
    week_width = 5 * day_width
    canvas.create_line(0, row_height , width, line_height, fill="grey")
    for week_number in range(5):
        x = title_width + week_number  *  week_width
        canvas.create_line(x, 0, x, height, fill="grey")
        canvas.create_text(x + week_width / 2, row_height / 2, row_height / 2, text =f"settimana {week_number+1}", font =("Helvetica", font_size, "bold"))

start_days = order_tasks(tasks)

#self.canvas = Canvas(self.main_window,width = self.__CANVAS_WIDTH,height = self.__CANVAS_HEIGHT)

y = row_height = 40

for task_number in start_days:
    task = tasks[task_number]
    canvas.create_text(title_indent, y + row_height / 2, text=task.title , anchor=tkinter.W, font=("Helvetica", font_size))

    bar_x = title_width + start_days[task_number] * day_width
    bar_y = y + (row_height - bar_height) / 2
    bar_width = task.duration * day_height
    canvas.create_rectangle( bar_x, bar_y, bar_x + bar_width, bar_y + bar_height, fill="red")
    
    y += row_height


def open_project():
    filename = askopenfilename(title="Open Project", initialdir=".", filetypes=[("CSV Document", "*.csv")])
    tasks = read_task("project.csv")
    draw_chart(tasks, canvas)

root = tkinter.Tk()

root.title("Ploject Planner")

root.resizable(width=False, height=False)

button_frame = tkinter.Frame(root, padx=5, pady=5 )

open_button = tkinter.Button(button_frame, text="Apri progetto...", command=open_project)

open_button.pack(side="top")

canvas = tkinter.Canvas(root, width=800, height=400, bg="white")

canvas.pack(side="bottom")

tkinter.mainloop()