import tkinter as tk

root = tk.Tk()
root.title("notes")

notes = []

def load_notes():
    global notes
    notes = []
    try:
        with open("test_note.txt", "r", encoding="utf-8") as file:
            for line in file:
                note = line.rstrip("\n")
                notes.append(note)
    except FileNotFoundError:
        notes = []
        save_notes()
    refresh_list_gui()

def save_notes():
    with open("test_note.txt", "w", encoding="utf-8") as file:
        for note in notes:
            file.write(note + "\n")

def refresh_list_gui():
    showlist.delete(0, tk.END)  
    for note in notes: 
        showlist.insert(tk.END, note)



def add_note():
    text = entry.get().strip()
    if text:
        notes.append(text)
        save_notes()
        refresh_list_gui()
        entry.delete(0, tk.END)

#add_note is given data from entry and sent to notes
#then save_notes is save to file then refresh_list_gui is shown to gui
#afterthat entrt will reset

def delete_note():
    seleted = showlist.curselection()
    if seleted:
        index = seleted[0]
        notes.pop(index)
        save_notes()
        refresh_list_gui()

#delete note is get data from notes index
#then delete and save then show to gui

def edit_note():
    seleted = showlist.curselection()
    if seleted:
        index = seleted[0]
        notes[index] = entry.get()
        save_notes()
        refresh_list_gui()

def seleted_note(event=None):
    seleted = showlist.curselection()
    if seleted:
        index = seleted[0]
        entry.delete(0, tk.END)
        entry.insert(0, notes[index])



showlist = tk.Listbox(root, width=50, height=20)
showlist.pack()

entry = tk.Entry(root, width=50)
entry.pack()



add_button = tk.Button(root, text="Add Notes", command=add_note)
add_button.pack()

edit_button = tk.Button(root, text="Edit", command=edit_note)
edit_button.pack()

delete_button = tk.Button(root, text="Delete", command=delete_note)
delete_button.pack()

showlist.bind("<<ListboxSelect>>", seleted_note)

load_notes()
refresh_list_gui()

root.mainloop()