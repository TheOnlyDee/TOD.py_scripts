#Progetto a pagina 134 del libro "CODING: Guida Facile Per Principianti" (apogeonline.com)
#messo in pratica da TOD (https://github.com/TheOnlyDee)

import csv

from collections import namedtuple

import Tkinter

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
#tasks = read_task("project.csv")
#print(tasks[1].title)
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


tasks = read_task("project.csv")
otasks = order_tasks(tasks)
print(otasks)

root = tkinter.Tk()

root.title("Ploject Planner")

open_button = tkinter.Button(root, text="Apri progetto...", command=open_project)

open_button.pack(side="tod")

canvas = tkinter.Canvas(root, width=800, height=400, bg="white")

canvas.pack(side="bottom")
tkinter.mainloop()