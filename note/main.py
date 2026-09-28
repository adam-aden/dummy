import tkinter as tk

backg       = "#DDDDE0"
welcometext = "#1D6A96"

root = tk.Tk()
root.title("notes")
root.configure(bg=backg)

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
    refresh_list_gui() #this line can add space but I didn't and it worked

#load_notes is read("r") from old notes
#if don't have it, new notes will show up

def save_notes():
    with open("test_note.txt", "w", encoding="utf-8") as file:
        for note in notes:
            file.write(note + "\n")

#self_notes is open notes and write("w") on it

def refresh_list_gui():
    showlist.delete(0, tk.END)  
    for note in notes: 
        showlist.insert(tk.END, note)

#refrech_list_gui is delete all data off notes then
#then get new data from notes and show

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

#edit_note is get notes index then sent to entry(ui)
#and then save to notes then show to ui 

def seleted_note(event=None):
    seleted = showlist.curselection()
    if seleted:
        index = seleted[0]
        entry.delete(0, tk.END)
        entry.insert(0, notes[index])

#UI
label = tk.Label(root, text="\n", bg=backg)  #I add space
label.pack()

welcome = tk.Label(root, text="welcome 2 my note", fg=welcometext, bg="pink")
welcome.place(x=625, y = 10)


showlist = tk.Listbox(root, width=70, height=30)
showlist.pack()

entry = tk.Entry(root, width=70)
entry.pack()

#button
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