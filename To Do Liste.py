import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry("500x450")
window.title("Todo Liste")
window.config(bg="#111111")


def aufgabe_dazu():
    aufgabe = aufgabe_eingabe.get()

    if aufgabe != "":
        if aufgabe == "Aufgabe eingeben digger":
            messagebox.showwarning("Error", "Bitte eine Aufgabe eingeben")

        else:
            aufgabenliste_liste.insert(tk.END, aufgabe)
            aufgabe_eingabe.delete(0, "end")

    else:
        messagebox.showwarning("Error", "Bitte eine Aufgabe eingeben")


def aufgabe_weg():
    aufgabenliste_liste.delete(tk.ANCHOR)


def eingabe_entfernen(event, eingabe):
    eingabe.delete(0, tk.END)



frame = tk.Frame(window)
frame.pack(pady=10)

aufgabenliste_liste = tk.Listbox(frame, width=25, height=8, font=("Times", 18),
                                 fg="#464646", selectbackground="#333333", activestyle="none")
aufgabenliste_liste.pack(side=tk.LEFT, fill=tk.BOTH)

scroll_bar = tk.Scrollbar(frame)
scroll_bar.pack(side=tk.RIGHT, fill=tk.BOTH)

aufgabenliste_liste.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=aufgabenliste_liste.yview)

aufgabe_eingabe = tk.Entry(window, font=("Times", 24))
aufgabe_eingabe.insert(0, "Aufgabe eingeben digger")
aufgabe_eingabe.bind("<Button-1>", lambda event: eingabe_entfernen(event, aufgabe_eingabe))
aufgabe_eingabe.pack(pady=20)

button_frame = tk.Frame(window)
button_frame.pack(pady=20)

aufgabe_dazu_btn = tk.Button(button_frame, text="Aufgabe hinzufügen Rügen", font=("Times", 14),
                             bg="green", fg="white", padx=20, pady=10, command=aufgabe_dazu)

aufgabe_dazu_btn.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)



aufgabe_weg_btn = tk.Button(button_frame, text="Aufgabe löschen", font=("Times", 14),
                             bg="red", fg="white", padx=20, pady=10, command=aufgabe_weg)

aufgabe_weg_btn.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

window.mainloop()