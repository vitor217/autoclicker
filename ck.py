import tkinter as Tk
cont = 0
multi = 0
quant = 100
autocp = 10
autoc_at = False

def clique():
    global multi
    global cont
    cont += 1
    cont += multi
    label.config(text=f"{cont}")
    
def rebirth():
    global cont
    global multi
    global quant
    global autoc_at
    if cont >= quant:
        cont = 0
        multi += 2.25
        quant += 100
        autoc_at = False
        label.config(text="0")
        btn2.config(text=f"Rebirth({quant} cliques necessários)")

def click_upg():
    global cont
    global autocp
    global autoc_at
    if cont >= autocp:
        cont -= autocp
        autoc_at = True
        autoclick()
        autocp += 40
        btn3.config(text=f"Autoclick({autocp} cliques necessários)")

def autoclick():
    global autoc_at
    if autoc_at:
        clique()
        janela.after(1000, autoclick)
            
           
janela = Tk.Tk()
janela.geometry("800x600")
janela.title("Clicker")
janela.config(bg="black")
janela.config()
label = Tk.Label(janela, text="0", fg="white", bg="black")
label.pack()
btn1 = Tk.Button(janela, text="Clique", justify="center", fg="black", bg="white", padx=25, pady=25,command=clique)
btn1.pack(expand=True)
btn2 = Tk.Button(janela, text="Rebirth(100 cliques necessários)", justify="center", fg="black", bg="white", padx=25, pady=25,command=rebirth)
btn2.pack(anchor="w")
btn3 = Tk.Button(janela, text=f"Autoclick(10 cliques necessários)", justify="center", fg="black", bg="white", padx=25, pady=25,command=click_upg)
btn3.pack(anchor="w")
janela.mainloop()