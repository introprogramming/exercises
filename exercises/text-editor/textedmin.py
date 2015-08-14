import Tkinter as Tk
import tkFileDialog


# A minimal implementation, what a solution might look like

def on_new():
    global path
    path = ''
    delete_all_text()


def on_open():
    global path
    dialog = tkFileDialog.Open()
    new_path = dialog.show()

    if new_path != '':
        text = read_file(new_path)
        delete_all_text()
        text_input.insert('1.0', text)
        path = new_path


def on_save():
    global path
    new_path = path

    if new_path == '':
        dialog = tkFileDialog.SaveAs(defaultextension='txt')
        new_path = dialog.show()

    if new_path:
        path = new_path
        text = get_all_text()
        save_file(path, text)


def on_save_as():
    global path
    dialog = tkFileDialog.SaveAs(defaultextension='txt')
    new_path = dialog.show()

    if new_path:
        text = get_all_text()
        save_file(new_path, text)
        path = new_path


def get_all_text():
    return text_input.get('1.0', 'end-1c')


def delete_all_text():
    text_input.delete('1.0', Tk.END)


def save_file(save_path, text):
    file_to_save = open(save_path, 'w')
    file_to_save.write(text)
    file_to_save.close()


def read_file(file_path):
    file_content = open(file_path, 'r')
    text = file_content.read()
    return text


# Initialize application
app = Tk.Tk()
app.title("Simple Text Editor")
app.geometry("300x400+300+300")

# Create menubar
menubar = Tk.Menu()

# Set menubar as menu for parent
app.config(menu=menubar)

# Fill menubar with "File" menu
filemenu = Tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=on_new)
filemenu.add_command(label="Open...", command=on_open)
filemenu.add_command(label="Save", command=on_save)
filemenu.add_command(label="Save as...", command=on_save_as)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quit)
menubar.add_cascade(label="File", menu=filemenu)

# Save path
path = ''

# Create scrollbar
scrollbar = Tk.Scrollbar(orient=Tk.VERTICAL)
scrollbar.pack(side=Tk.RIGHT, fill=Tk.Y)

# Create text box
text_input = Tk.Text(yscrollcommand=scrollbar.set, height=100, width=80)
text_input.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)

# Make the scrollbar react to
scrollbar.config(command=text_input.yview)

# Start the main event loop (i.e. run the tkinter program)
app.mainloop()
