# -*- coding: utf-8 -*-

import tkinter as Tk
from tkinter import filedialog, simpledialog, colorchooser


# An implementation with many features using OOP

class TextEditor(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)

        self.path = ''
        self.settings = self.load_settings()
        self.parent = parent

        self.parent.title("Simple Text Editor")
        self.pack(fill=Tk.BOTH)
        self.center_window()

        self.init_menubar()

        # Create scrollbar
        scrollbar = Tk.Scrollbar(self, orient=Tk.VERTICAL)
        scrollbar.pack(side=Tk.RIGHT, fill=Tk.Y)

        # Create text box
        self.text_input = Tk.Text(self, yscrollcommand=scrollbar.set, height=100, width=80,
                                  bg=self.settings['background_color'],
                                  fg=self.settings['text_color'])
        self.text_input.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)

        scrollbar.config(command=self.text_input.yview)

        self.init_shortcuts()

        self.load_settings()

        self.parent.protocol('WM_DELETE_WINDOW', self.on_exit)

    def init_menubar(self):
        # Create menubar
        menubar = Tk.Menu(self)

        # Set menubar as menu for parent
        self.parent.config(menu=menubar)

        # Fill menubar with "File" menu
        filemenu = Tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.on_new, accelerator="Ctrl+N")
        filemenu.add_command(label="Open...", command=self.on_open, accelerator="Ctrl+O")
        filemenu.add_command(label="Save", command=self.on_save, accelerator="Ctrl+S")
        filemenu.add_command(label="Save as...", command=self.on_save_as)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.on_exit, accelerator="Ctrl+Q")
        menubar.add_cascade(label="File", menu=filemenu)

        # Fill menubar with "Edit" menu
        editmenu = Tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Find", command=self.on_find, accelerator="Ctrl+F")
        editmenu.add_command(label="Select all", command=self.on_select_all, accelerator="Ctrl+A")
        menubar.add_cascade(label="Edit", menu=editmenu)

        # Fill menubar with "Settings" menu
        settingsmenu = Tk.Menu(menubar, tearoff=0)
        settingsmenu.add_command(label="Text color...", command=self.on_text_color)
        settingsmenu.add_command(label="Background color...", command=self.on_background_color)
        menubar.add_cascade(label="Settings", menu=settingsmenu)

        # Fill menubar with "Help" menu
        helpmenu = Tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.on_about)
        menubar.add_cascade(label="Help", menu=helpmenu)

    def init_shortcuts(self):
        self.bind_all('<Control-n>', self.handle_shortcuts)
        self.bind_all('<Control-o>', self.handle_shortcuts)
        self.bind_all('<Control-s>', self.handle_shortcuts)
        self.bind_all('<Control-q>', self.handle_shortcuts)
        self.bind_all('<Control-a>', self.handle_shortcuts)
        self.bind_all('<Control-f>', self.handle_shortcuts)

    # FILE MENU ACTIONS
    def on_new(self):
        self.path = ''
        self.delete_all_text()

    def on_open(self):
        dialog = filedialog.Open()
        path = dialog.show()

        if path != '':
            text = self.read_file(path)
            self.delete_all_text()
            self.text_input.insert('1.0', text)
            self.path = path

    def on_save(self):
        path = self.path

        if path == '':
            dialog = filedialog.SaveAs(defaultextension='txt')
            path = dialog.show()

        if path:
            self.path = path
            text = self.get_all_text()
            self.save_file(self.path, text)

    def on_save_as(self):
        dialog = filedialog.SaveAs(defaultextension='txt')
        path = dialog.show()

        if path:
            self.path = path
            text = self.get_all_text()
            self.save_file(path, text)

    def on_exit(self):

        f = open("settings.txt", 'w')
        f.write("background_color=" + self.settings['background_color'] + "\n")
        f.write("text_color=" + self.settings['text_color'] + "\n")
        f.close()

        self.quit()

    # EDIT MENU ACTIONS
    def on_find(self):
        target = simpledialog.askstring("Simple Text Editor", "Search for:")
        if target:
            index = self.text_input.search(target, Tk.INSERT, Tk.END)
            if not index:
                index = self.text_input.search(target, '1.0', Tk.END)
            if index:
                length = index + ('+%dc' % len(target))
                self.text_input.tag_add(Tk.SEL, index, length)
                self.text_input.mark_set(Tk.INSERT, length)
                self.text_input.see(Tk.INSERT)
                self.text_input.focus()

    def on_select_all(self):
        if self.get_all_text() != '':
            self.text_input.tag_add(Tk.SEL, '1.0', Tk.END)
            self.text_input.mark_set(Tk.INSERT, '1.0')
            self.text_input.see(Tk.INSERT)

    # SETTINGS MENU ACTIONS
    def on_background_color(self):
        (rgb, hex) = colorchooser.askcolor(self.settings['background_color'])
        self.settings['background_color'] = hex
        self.text_input.config(bg=hex)

    def on_text_color(self):
        (rgb, hex) = colorchooser.askcolor(self.settings['text_color'])
        self.settings['text_color'] = hex
        self.text_input.config(fg=hex)

    # HELP MENU ACTIONS
    def on_about(self):
        top = Tk.Toplevel(self.parent)
        top.title("About")
        top.resizable(width=False, height=False)
        top.geometry('%dx%d+%d+%d' %
                     (200, 120, self.parent.winfo_x() + 50, self.parent.winfo_y() + 50))
        top.focus()

        about_message = "Simple Text Editor is a simple" \
                        " text editor made for educational purposes."

        top.update()
        msg = Tk.Message(top, text=about_message, pady=10, width=top.winfo_width())
        msg.pack()

        button = Tk.Button(top, text="OK", command=top.destroy, width=8)
        button.pack(side=Tk.BOTTOM, pady=10)

    def load_settings(self):
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
    def handle_shortcuts(self, event):
        functions = {'n': self.on_new,
                     'o': self.on_open,
                     's': self.on_save,
                     'q': self.on_exit,
                     'a': self.on_select_all,
                     'f': self.on_find}

        func = functions[event.keysym]
        func()

    # HELPERS
    def get_all_text(self):
        return self.text_input.get('1.0', 'end-1c')

    def delete_all_text(self):
        self.text_input.delete('1.0', Tk.END)

    def save_file(self, path, text):
        file_to_save = open(path, 'w')
        file_to_save.write(text)
        file_to_save.close()

    def read_file(self, path):
        file_content = open(path, 'r')
        text = file_content.read()
        return text

    def center_window(self):
        w = 400
        h = 400

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))


def main():
    root = Tk.Tk()
    TextEditor(root)
    root.mainloop()


if __name__ == '__main__':
    main()
