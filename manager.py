from tkinter import *
import os
from tkinter import filedialog

root = Tk()
root["bg"] = "gray22"
name_entry = None
password_entry = None

def check_login():
    global name_entry, password_entry
    if name_entry.get() == 'a' and password_entry.get() == '1':
        welcome_window = Toplevel(root)
        welcome_window.geometry('1280x1024+0+0')
        welcome_label_nadpis_for_main_panel = Label(welcome_window, text='Основная панель управления',
                                                    font=('Arial', 20), fg='black', bg='gray22')
        def create_folder():
            folder_path = filedialog.askdirectory(initialdir='C:/Users/', title='Выберите папку')
            os.makedirs(folder_path + '/Новая папка')

        def delete_file():
            file_path = filedialog.askopenfilename(initialdir='C:/Users/', title='Выберите файл')
            os.remove(file_path)

        def open_file():
            file_path = filedialog.askopenfilename(initialdir='C:/Users/', title='Выберите файл')
            os.startfile(file_path)

        def edit_file():
            file_path = filedialog.askopenfilename(initialdir='C:/Users/', title='Выберите файл')
            os.system('notepad.exe ' + file_path)

        button1 = Button(welcome_window, text='Создать новый файл/папку', font=('Segoe UI', 14, "bold"),
                         bg='#0078d7', command=create_folder, relief='flat', bd=0, )
        button1.grid(row=1, column=0, pady=10, padx=10)
        button1.config(height=2, width=31)

        button2 = Button(welcome_window, text='Удалить файл', font=('Segoe UI', 14, "bold"),
                         bg='#0078d7', command=delete_file, bd=0,)
        button2.grid(row=2, column=0, pady=10, padx=10)
        button2.config(height=2, width=31)

        button3 = Button(welcome_window, text='Открыть файл', font=('Segoe UI', 14, "bold"),
                         bg='#0078d7', command=open_file, bd=0,)
        button3.grid(row=3, column=0, pady=10, padx=10)
        button3.config(height=2, width=31)

        button4 = Button(welcome_window, text='Редактировать файл', font=('Segoe UI', 14, "bold"),
                         bg='#0078d7', command=edit_file, bd=0,)
        button4.grid(row=4, column=0, pady=10, padx=10)
        button4.config(height=2, width=31)

        def move_file():
            file_path = filedialog.askopenfilename(initialdir='C:/Users/', title='Выберите файл')
            new_path = filedialog.askdirectory(initialdir='C:/Users/', title='Выберите папку')
            os.replace(file_path, new_path)

        # Добавляем новую кнопку

        button5 = Button(welcome_window, text='Переместить файл', font=('Segoe UI', 14, "bold"),
                         bg='#0078d7', command=move_file)
        button5.grid(row=5, column=0, pady=10, padx=10)
        button5.config(height=2, width=31)
        button5.config(relief='flat')

        # Копируем дизайн других кнопок для новой кнопки

        button5.config(activebackground='#0078d7', activeforeground='white', bd=0, fg='black', font=('Segoe UI', 14, "bold"),
                       highlightbackground='#0078d7', highlightcolor='#0078d7')

        welcome_label_nadpis_for_main_panel.grid(row=0, column=1, padx=10, pady=50)

        welcome_window["bg"] = "gray22"
    else:
        error_label = Label(root, text='Неправильное имя пользователя или пароль', font=('Arial', 16), fg='black', bg='#0078d7')
        error_label.grid(row=3, column=0, columnspan=2)

root.geometry('527x400+100+100')
label_1 = Label(root, text='Name', font=('Segoe UI', 16), pady=-1, padx=11,  bg='#0078d7', relief='flat')
label_2 = Label(root, text='Password', font=('Segoe UI', 16), pady=-1, padx=11,  bg='#0078d7', relief='flat')
name_entry = Entry(root, font=('Segoe UI', 16),  bg='#0078d7', width=30, relief='flat')
password_entry = Entry(root, font=('Segoe UI', 16), show='*',  bg='#0078d7', width=30, relief='flat')
submit_button = Button(root, text='Submit', font=('Segoe UI', 16), command=check_login,  bg='#0078d7', relief='flat')
label_1.grid(row=0, column=0, sticky='E', padx=20, pady=10)
name_entry.grid(row=0, column=1, padx=20, pady=10)
label_2.grid(row=1, column=0, sticky='E', padx=20, pady=20)
password_entry.grid(row=1, column=1, padx=20, pady=20)
submit_button.grid(row=2, column=1, pady=10)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
