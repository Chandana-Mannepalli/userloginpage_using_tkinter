import tkinter as tk
from tkinter import filedialog
import csv
import mysql.connector
from tkinter import messagebox
conn=mysql.connector.connect(
       user='root',
       password='@Chandana67',
       host='localhost',
       database='tkinter_db'
)
print(conn.is_connected())
cursor=conn.cursor()


def file_open():
      file=filedialog.askopenfilename(filetypes=[('csvfiles','*.csv')])
      with open(file,'r') as f:
            reader=csv.reader(f)
            print(next(reader))
              
            for row in reader:
                     cursor.execute(
                            '''INSERT INTO STUDENTS(NAME,CLASS,GRADE)
                            VALUES(%s,%s,%s)
                            ''',
                            tuple(row)
                        )
            conn.commit()           
            messagebox.showinfo('info','data saved to db')
def fill_textbox():
      txt_box.configure(state='normal')
      txt_box.delete('1.0',tk.END)
      cursor.execute('Select * from students')
      for row in cursor.fetchall():
             txt_box.insert(tk.END,f'ID:{row[0]},Name:{row[1]},Class:{row[2]},Grade:{row[3]}\n')
      txt_box.configure(state='disabled')
def add_record():
      name=name_entry.get()
      class_=class_entry.get()
      grade=grade_entry.get()
      cursor.execute('''INSERT INTO STUDENTS(NAME,CLASS,GRADE)
                            VALUES(%s,%s,%s)
                            ''',
                            (name,class_,grade)
                        )
      conn.commit()
      messagebox.showinfo('Info','record added')
      fill_textbox()
      

def update_record():
       id=id_entry.get()
       name=name_entry.get()
       class_=class_entry.get()
       grade=grade_entry.get()
       cursor.execute('''UPDATE STUDENTS SET NAME= %s Where Id=%s
                            ''',
                            (name,id)
                        )
       conn.commit() 
       cursor.execute('''UPDATE STUDENTS SET Class= %s Where Id=%s
                            ''',
                            (class_,id)
                        )
       conn.commit()
       messagebox.showinfo('Info','record updated')
       fill_textbox()

def delete_record():
       id=id_entry.get()
       cursor.execute(''' delete from students where id=%s
       ''',(id,))
       conn.commit()
       messagebox.showinfo('Info','record deleted')
       fill_textbox()

root=tk.Tk()
root.geometry('500x500')
tk.Button(root,text='UPLOAD CSV',command=file_open).pack(pady=10)
txt_box=tk.Text(root,height=5,width=50)
txt_box.pack(pady=20)
fill_textbox()
action_frame=tk.Frame(root)
action_frame.pack()
tk.Label(action_frame,text='ID').grid(row=0,column=0)
id_entry=tk.Entry(action_frame,width=4)
id_entry.grid(row=0,column=1)
tk.Label(action_frame,text='NAME').grid(row=0,column=2)
name_entry=tk.Entry(action_frame)
name_entry.grid(row=0,column=3)
tk.Label(action_frame,text='CLASS').grid(row=0,column=4)
class_entry=tk.Entry(action_frame,width=2)
class_entry.grid(row=0,column=5)
tk.Label(action_frame,text='GRADE').grid(row=0,column=6)
grade_entry=tk.Entry(action_frame,width=2)
grade_entry.grid(row=0,column=7) 

tk.Button(action_frame,text='ADD',command=add_record).grid(row=1,column=1,padx=10)
tk.Button(action_frame,text='UPDATE',command=update_record).grid(row=1,column=2,padx=10)
tk.Button(action_frame,text='DELETE',command=delete_record).grid(row=1,column=3,padx=10)



root.mainloop()