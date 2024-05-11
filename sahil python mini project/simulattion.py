import tkinter as tk

def binary_search(array, target):
    left = 0
    right = len(array) - 1
    steps = []

    while left <= right:
        mid = (left + right) // 2
        steps.append(mid)

        if array[mid] == target:
            return mid, steps
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1, steps

def simulate_binary_search():
    array = [int(x) for x in entry_array.get().split(",")]
    target = int(entry_target.get())

    index, steps = binary_search(array, target)

    if index == -1:
        lbl_result.config(text="Target not found in array!")
    else:
        lbl_result.config(text=f"Target found at index {index}")

    lbl_steps.config(text=f"Steps taken: {steps}")

    # Visualize search process
    canvas.delete("all")
    canvas_width = 600
    canvas_height = 100
    bar_width = canvas_width // len(array)

    for i, value in enumerate(array):
        color = "lightgray"
        if i in steps:
            color = "lightblue"
        canvas.create_rectangle(i * bar_width, 0, (i + 1) * bar_width, canvas_height, fill=color)
        canvas.create_text((i + 0.5) * bar_width, canvas_height / 2, text=str(value))

# Create GUI
root = tk.Tk()
root.title("Binary Search Simulation")

frame_input = tk.Frame(root)
frame_input.pack(padx=10, pady=10)

lbl_array = tk.Label(frame_input, text="Enter sorted array (comma-separated):")
lbl_array.grid(row=0, column=0, padx=5, pady=5, sticky="e")

entry_array = tk.Entry(frame_input, width=40)
entry_array.grid(row=0, column=1, padx=5, pady=5)

lbl_target = tk.Label(frame_input, text="Enter target value:")
lbl_target.grid(row=1, column=0, padx=5, pady=5, sticky="e")

entry_target = tk.Entry(frame_input, width=10)
entry_target.grid(row=1, column=1, padx=5, pady=5)

btn_search = tk.Button(frame_input, text="Search", command=simulate_binary_search)
btn_search.grid(row=2, column=1, padx=5, pady=5)

frame_result = tk.Frame(root)
frame_result.pack(padx=10, pady=10)

lbl_result = tk.Label(frame_result, text="")
lbl_result.pack(padx=5, pady=5)

lbl_steps = tk.Label(frame_result, text="")
lbl_steps.pack(padx=5, pady=5)

canvas = tk.Canvas(root, width=600, height=100)
canvas.pack(padx=10, pady=10)

root.mainloop()
