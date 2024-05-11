import tkinter as tk
import random
import time

def update_display(array,keyIndex,currentIndex):
    canvas.delete("all")
    for i,value in enumerate(array):
        color='blue' if i==keyIndex else 'green' if i==currentIndex else 'white'
        canvas.create_rectangle(i*30,100-value*5,(i+1)*30,100,fill=color)
        canvas.create_text((i*30)+15,110-value*5,text=str(value))
    root.update_idletasks()

def insertionSort(array):
    for i in range(1,len(array)):
        key=array[i]
        j=i-1
        while j>=0 and array[j]>key:
            array[j+1]=array[j]
            j-=1
            update_display(array,j+1,i)
            time.sleep(0.5)
        array[j+1]=key

def startSort():
    global array
    insertionSort(array)
    update_display(array,-1,-1)
def generateArray():
    global array
    array=[random.randint(1,20) for _ in range(10)]
    update_display(array,-1,-1)

root=tk.Tk()
root.title("Insertion Sort")
canvas=tk.Canvas(root,width=300,height=120)
canvas.pack()

generate_button=tk.Button(root,text='Generate Array',command=generateArray)
generate_button.pack(side=tk.LEFT,padx=10)

sor_button=tk.Button(root,text='Sort',command=startSort)
sor_button.pack(side=tk.LEFT)

array=[]
root.mainloop()
