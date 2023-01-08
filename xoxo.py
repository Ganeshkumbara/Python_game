from tkinter import *
from tkinter import messagebox

window = Tk()
# # window.geometry("300x250+1000+100")
window.title("Python GUI App")
# window.configure(bg='black')
#  # buttons clicked



clicked = True
count = 0 

No_winner = True

def draw():
   if count == 9 and No_winner :
      messagebox.showinfo('Draw','unlucky Fellowz : Go for one more round')


def winner_validator():
   buttons = [B1,B2,B3,B4,B5,B6,B7,B8,B9]

   # check if x wins

   if B1['text'] =='X' and B2['text'] == 'X' and B3["text"] == "X":
      B1['bg'] = 'green'
      B2['bg'] = 'green'   
      B3['bg'] = 'green'
      messagebox.showinfo('win','Hurry X won')
      for button in buttons:
         button["state"] = DISABLED
   
   if B4['text'] =='X' and B5['text'] == 'X' and B6["text"] == "X":
      B4['bg'] = 'green'
      B5['bg'] = 'green'   
      B6['bg'] = 'green'
      messagebox.showinfo('win','Hurry X won')
      for button in buttons:
         button["state"] = DISABLED
         
   if B7['text'] =='X' and B8['text'] == 'X' and B9["text"] == "X":
      B7['bg'] = 'green'
      B8['bg'] = 'green'   
      B9['bg'] = 'green'
      messagebox.showinfo('win','Hurry X won')
      for button in buttons:
         button["state"] = DISABLED
   if B1['text'] =='X' and B4['text'] == 'X' and B7["text"] == "X":
      B1['bg'] = 'green'
      B4['bg'] = 'green'   
      B7['bg'] = 'green'
      messagebox.showinfo('win','Hurry X won')
      for button in buttons:
         button["state"] = DISABLED
   if B2['text'] =='X' and B5['text'] == 'X' and B8["text"] == "X":
      B2['bg'] = 'green'
      B5['bg'] = 'green'   
      B8['bg'] = 'green'
      messagebox.showinfo('win','Hurry X won')
      for button in buttons:
         button["state"] = DISABLED
   if B3['text'] =='X' and B6['text'] == 'X' and B9["text"] == "X":
      B3['bg'] = 'green'
      B6['bg'] = 'green'   
      B9['bg'] = 'green'
      messagebox.showinfo('win','Hurry X won')
      for button in buttons:
         button["state"] = DISABLED

   if B1['text'] =='X' and B5['text'] == 'X' and B9["text"] == "X":
      B1['bg'] = 'green'
      B5['bg'] = 'green'   
      B9['bg'] = 'green'
      messagebox.showinfo('win','Hurry X won')
      for button in buttons:
         button["state"] = DISABLED
   if B3['text'] =='X' and B5['text'] == 'X' and B7["text"] == "X":
      B3['bg'] = 'green'
      B5['bg'] = 'green'   
      B7['bg'] = 'green'
      messagebox.showinfo('win','Hurry X won')
      for button in buttons:
         button["state"] = DISABLED

   #check if 0 wins
   if B1['text'] =='O' and B2['text'] == 'O' and B3["text"] == "O":
      B1['bg'] = 'green'
      B2['bg'] = 'green'   
      B3['bg'] = 'green'
      messagebox.showinfo('win','Hurry O won')
      for button in buttons:
         button["state"] = DISABLED

   if B4['text'] =='O' and B5['text'] == 'O' and B6["text"] == "O":
      B4['bg'] = 'green'
      B5['bg'] = 'green'   
      B6['bg'] = 'green'
      messagebox.showinfo('win','Hurry O won')
      for button in buttons:
         button["state"] = DISABLED
         
   if B7['text'] =='O' and B8['text'] == 'O' and B9["text"] == "O":
      B7['bg'] = 'green'
      B8['bg'] = 'green'   
      B9['bg'] = 'green'
      messagebox.showinfo('win','Hurry O won')
      for button in buttons:
         button["state"] = DISABLED
   if B1['text'] =='O' and B4['text'] == 'O' and B7["text"] == "O":
      B1['bg'] = 'green'
      B4['bg'] = 'green'   
      B7['bg'] = 'green'
      messagebox.showinfo('win','Hurry O won')
      for button in buttons:
         button["state"] = DISABLED
   if B2['text'] =='O' and B5['text'] == 'O' and B8["text"] == "O":
      B2['bg'] = 'green'
      B5['bg'] = 'green'   
      B8['bg'] = 'green'
      messagebox.showinfo('win','Hurry X won')
      for button in buttons:
         button["state"] = DISABLED
   if B3['text'] =='O' and B6['text'] == 'O' and B9["text"] == "O":
      B3['bg'] = 'green'
      B6['bg'] = 'green'   
      B9['bg'] = 'green'
      messagebox.showinfo('win','Hurry X won')
      for button in buttons:
         button["state"] = DISABLED
   if B1['text'] =='O' and B5['text'] == 'O' and B9["text"] == "O":
      B1['bg'] = 'green'
      B5['bg'] = 'green'   
      B9['bg'] = 'green'
      messagebox.showinfo('win','Hurry O won')
      for button in buttons:
         button["state"] = DISABLED
   if B3['text'] =='O' and B5['text'] == 'O' and B7["text"] == "O":
      B3['bg'] = 'green'
      B5['bg'] = 'green'   
      B7['bg'] = 'green'
      messagebox.showinfo('win','Hurry O won')
      for button in buttons:
         button["state"] = DISABLED
   


def b_click(b):
   global clicked, count
   if b['text'] == '' and clicked == True :
      b['text'] = 'X'
      b['bg'] = '#4B8BBE'
      b['fg'] = '#e5e4e2'
      clicked = False
      count += 1
      if winner_validator():
         No_winner = False
      else:
         draw()
      

   elif b['text'] == '' and clicked == False:
      b['text'] = 'O'
      b['bg'] = '#FFE873'
      b['fg'] = '#e5e4e2'
      clicked = True
      count += 1
      if winner_validator():
         No_winner = False
      else:
         draw()

   else:
      messagebox.showerror('kabzzz','Slot Issue: Hey click on empty solts ')
   



# Buttons configur

B1 = Button(window, text='', font=('Cavergiz', 20), height=3, width=6, bg='SystemButtonFace',command=lambda:b_click(B1))
B2 = Button(window, text='', font=('Cavergiz', 20), height=3, width=6, bg='SystemButtonFace',command=lambda:b_click(B2))
B3 = Button(window, text='', font=('Cavergiz', 20), height=3, width=6, bg='SystemButtonFace',command=lambda:b_click(B3))
B4 = Button(window, text='', font=('Cavergiz', 20), height=3, width=6, bg='SystemButtonFace',command=lambda:b_click(B4))
B5 = Button(window, text='', font=('Cavergiz', 20), height=3, width=6, bg='SystemButtonFace',command=lambda:b_click(B5))
B6 = Button(window, text='', font=('Cavergiz', 20), height=3, width=6, bg='SystemButtonFace',command=lambda:b_click(B6))
B7 = Button(window, text='', font=('Cavergiz', 20), height=3, width=6, bg='SystemButtonFace',command=lambda:b_click(B7))
B8 = Button(window, text='', font=('Cavergiz', 20), height=3, width=6, bg='SystemButtonFace',command=lambda:b_click(B8))
B9 = Button(window, text='', font=('Cavergiz', 20), height=3, width=6, bg='SystemButtonFace',command=lambda:b_click(B9))
 
# Grid bottons

B1.grid(row=0, column=0)
B2.grid(row=0, column=1)
B3.grid(row=0, column=2)

B4.grid(row=1, column=0)
B5.grid(row=1, column=1)
B6.grid(row=1, column=2)

B7.grid(row=2, column=0)
B8.grid(row=2, column=1)
B9.grid(row=2, column=2)

start = window.mainloop()
 
