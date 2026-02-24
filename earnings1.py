tasks = ["check tires", "pick up order", "deliver food"]
print(f"Current task:{tasks}")
first_task= tasks[0]
print(f"First thing to do:{first_task}")
print("New order received")
tasks.append("Fill gas")
print("Task 1 complete")
completed = tasks.pop(0)
print(f"Finished:{completed}")
print(f"Remaining tasks:{tasks}")