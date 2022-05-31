import tkinter as tk

def button_function():  
    
    good = True
    while good:
        A = entry1.get()
        print('A=', A)
        good = False
       
    
  
   
root = tk.Tk()

canvas = tk.Canvas(root)
canvas.pack()

entry1 = tk.Entry(root)
entry1.place(relwidth=0.5, relheight=0.5)



button = tk.Button(root, text = "confirm", command= button_function)
button.place(relx=0.5, relwidth=0.5, relheight=1)

root.mainloop()