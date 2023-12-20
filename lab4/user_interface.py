def start_interface(cube_state):
    import tkinter as tk
    root = tk.Tk()

    texts = ['X Y', 'X Z', 'Y Z']
    vars = [tk.StringVar(value='1'), tk.StringVar(value='0'), tk.StringVar(value='0')]
    def cb():
        print('--- languages ---')

        cube_state.X_Y = int(vars[0].get())
        cube_state.X_Z = int(vars[1].get())
        cube_state.Y_Z = int(vars[2].get())

        for i, s in enumerate(texts):
            print(s, vars[i].get())
    tk.Checkbutton(root, text=texts[0], variable=vars[0], command=cb).pack(side="left")
    tk.Checkbutton(root, text=texts[1], variable=vars[1], command=cb).pack(side="left")
    tk.Checkbutton(root, text=texts[2], variable=vars[2], command=cb).pack(side="left")

    
    def stop():
        vars[0].set(0)
        vars[1].set(0)
        vars[2].set(0)
        cb()
        
    tk.Button(root, text="Stop!",command=stop).pack(side="left")

    #############3
    var3 = tk.StringVar()
    var3.set('All')
    def cb1():
        cube_state.Color = var3.get()
        print(var3.get())
    tk.Radiobutton(root, text='All', variable=var3, value='All', command=cb1).pack(side="left")
    tk.Radiobutton(root, text='Green', variable=var3, value='Green', command=cb1).pack(side="left")
    tk.Radiobutton(root, text='Blue', variable=var3, value='Blue', command=cb1).pack(side="left")
    tk.Radiobutton(root, text='Red', variable=var3, value='Red', command=cb1).pack(side="left")
    tk.Radiobutton(root, text='None', variable=var3, value='None', command=cb1).pack(side="left")
    ###############
    var4 = tk.StringVar()
    var4.set(30)
    def cb2():
        cube_state.FPS = int(var4.get())
        print(var4.get())
    tk.Radiobutton(root, text='60 FPS', variable=var4, value=60, command=cb2).pack(side="left")
    tk.Radiobutton(root, text='30 FPS', variable=var4, value=30, command=cb2).pack(side="left")
    tk.Radiobutton(root, text='10 FPS', variable=var4, value=10, command=cb2).pack(side="left")

    root.mainloop()

