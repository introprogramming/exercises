# -*- coding: utf-8 -*-

import Tkinter as Tk
import tkFileDialog
import tkSimpleDialog
import tkColorChooser


# An implementation with many features without OOP

def init_menubar():
    # Create menubar
    menubar = Tk.Menu()

    # Set menubar as menu for root
    root.config(menu=menubar)

    # Fill menubar with "File" menu
    filemenu = Tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=on_new, accelerator="Ctrl+N")
    filemenu.add_command(label="Open...", command=on_open, accelerator="Ctrl+O")
    filemenu.add_command(label="Save", command=on_save, accelerator="Ctrl+S")
    filemenu.add_command(label="Save as...", command=on_save_as)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=on_exit, accelerator="Ctrl+Q")
    menubar.add_cascade(label="File", menu=filemenu)

    # Fill menubar with "Edit" menu
    editmenu = Tk.Menu(menubar, tearoff=0)
    editmenu.add_command(label="Find", command=on_find, accelerator="Ctrl+F")
    editmenu.add_command(label="Select all", command=on_select_all, accelerator="Ctrl+A")
    menubar.add_cascade(label="Edit", menu=editmenu)

    # Fill menubar with "Settings" menu
    settingsmenu = Tk.Menu(menubar, tearoff=0)
    settingsmenu.add_command(label="Text color...", command=on_text_color)
    settingsmenu.add_command(label="Background color...", command=on_background_color)
    menubar.add_cascade(label="Settings", menu=settingsmenu)

    # Fill menubar with "Help" menu
    helpmenu = Tk.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About", command=on_about)
    menubar.add_cascade(label="Help", menu=helpmenu)


def init_shortcuts():
    root.bind_all('<Control-n>', handle_shortcuts)
    root.bind_all('<Control-o>', handle_shortcuts)
    root.bind_all('<Control-s>', handle_shortcuts)
    root.bind_all('<Control-q>', handle_shortcuts)
    root.bind_all('<Control-a>', handle_shortcuts)
    root.bind_all('<Control-f>', handle_shortcuts)


# FILE MENU ACTIONS
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


def on_exit():
    f = open("settings.txt", 'w')
    f.write("background_color=" + settings['background_color'] + "\n")
    f.write("text_color=" + settings['text_color'] + "\n")
    f.close()

    quit()


# EDIT MENU ACTIONS
def on_find():
    target = tkSimpleDialog.askstring("Simple Text Editor", "Search for:")
    if target:
        index = text_input.search(target, Tk.INSERT, Tk.END)
        if not index:
            index = text_input.search(target, '1.0', Tk.END)
        if index:
            length = index + ('+%dc' % len(target))
            text_input.tag_add(Tk.SEL, index, length)
            text_input.mark_set(Tk.INSERT, length)
            text_input.see(Tk.INSERT)
            text_input.focus()


def on_select_all():
    if get_all_text() != '':
        text_input.tag_add(Tk.SEL, '1.0', Tk.END)
        text_input.mark_set(Tk.INSERT, '1.0')
        text_input.see(Tk.INSERT)


# SETTINGS MENU ACTIONS
def on_background_color():
    (rgb, hex) = tkColorChooser.askcolor(settings['background_color'])
    settings['background_color'] = hex
    text_input.config(bg=hex)


def on_text_color():
    (rgb, hex) = tkColorChooser.askcolor(settings['text_color'])
    settings['text_color'] = hex
    text_input.config(fg=hex)


# HELP MENU ACTIONS
def on_about():
    top = Tk.Toplevel(root)
    top.title("About")
    top.resizable(width=False, height=False)
    top.geometry('%dx%d+%d+%d' %
                 (200, 120, root.winfo_x() + 50, root.winfo_y() + 50))
    top.focus()

    about_message = "Simple Text Editor is a simple" \
                    " text editor made for educational purposes."

    top.update()
    msg = Tk.Message(top, text=about_message, pady=10, width=top.winfo_width())
    msg.pack()

    button = Tk.Button(top, text="OK", command=top.destroy, width=8)
    button.pack(side=Tk.BOTTOM, pady=10)


def load_settings():
    dictionary = {}
    try:
        f = open('settings.txt', 'r')
        for line in f:
            (key, val) = line.strip().split('=')
            dictionary[key] = val

        f.close()
        return dictionary

    except IOError:
        f = open('settings.txt', "w")
        f.write("background_color=" + "#000000\n")
        f.write("text_color=" + "#FFFFFFF\n")
        f.close()

        return {"background_color": "#FFFFFF",
                "text_color": "#000000"}


# KEYBOARD SHORTCUT HANDLER
def handle_shortcuts(event):
    functions = {'n': on_new,
                 'o': on_open,
                 's': on_save,
                 'q': on_exit,
                 'a': on_select_all,
                 'f': on_find}

    func = functions[event.keysym]
    func()


# HELPERS
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


def center_window():
    w = 400
    h = 400

    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()

    x = (sw - w) / 2
    y = (sh - h) / 2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))


root = Tk.Tk()
root.title("Simple Text Editor")
root.protocol('WM_DELETE_WINDOW', on_exit)  # Call custom exit method when exiting

path = ''

settings = load_settings()
center_window()

init_menubar()

# Create scrollbar
scrollbar = Tk.Scrollbar(orient=Tk.VERTICAL)
scrollbar.pack(side=Tk.RIGHT, fill=Tk.Y)

# Create text box
text_input = Tk.Text(yscrollcommand=scrollbar.set, height=100, width=80,
                     bg=settings['background_color'],
                     fg=settings['text_color'])
text_input.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)

scrollbar.config(command=text_input.yview)

init_shortcuts()

root.mainloop()
