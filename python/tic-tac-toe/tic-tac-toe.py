from tkinter import *
from tkinter.ttk import Combobox

# create window
window = Tk()
window.title("Крестики-Нолики")
window.geometry('400x250')

# who make next move
next_move ="X"
# amount of move need for define "DRAW"
move_count = 0
#function
#event NEW GAME
# смотрим на комбобокс
# press new game
def new_game():
    global move_count, next_move
    # define button style
    btn1.config(text="",state=NORMAL, bg="white")
    btn2.config(text="",state=NORMAL, bg="white")
    btn3.config(text="",state=NORMAL, bg="white")
    btn4.config(text="",state=NORMAL, bg="white")
    btn5.config(text="",state=NORMAL, bg="white")
    btn6.config(text="",state=NORMAL, bg="white")
    btn7.config(text="",state=NORMAL, bg="white")
    btn8.config(text="",state=NORMAL, bg="white")
    btn9.config(text="",state=NORMAL, bg="white")
    # set global variable
    move_count = 0
    lbl.config(text="Ходит: крестик")
    next_move = "X"
# Checking fields, try find winner
def iswin():
    global next_move
    is_win = False
    # check all win combination
    if btn1.cget('text')==btn2.cget('text')==btn3.cget('text')!="":
        is_win = True
        btn1.config(bg="#00FA9A")
        btn2.config(bg="#00FA9A")
        btn3.config(bg="#00FA9A")
    if btn4.cget('text')==btn5.cget('text')==btn6.cget('text')!="":
        is_win = True
        btn4.config(bg="#00FA9A")
        btn5.config(bg="#00FA9A")
        btn6.config(bg="#00FA9A")
    if btn7.cget('text')==btn8.cget('text')==btn9.cget('text')!="":
        is_win = True
        btn7.config(bg="#00FA9A")
        btn8.config(bg="#00FA9A")
        btn9.config(bg="#00FA9A")
    if btn1.cget('text')==btn4.cget('text')==btn7.cget('text')!="":
        is_win = True
        btn1.config(bg="#00FA9A")
        btn4.config(bg="#00FA9A")
        btn7.config(bg="#00FA9A")
    if btn2.cget('text')==btn5.cget('text')==btn8.cget('text')!="":
        is_win = True
        btn2.config(bg="#00FA9A")
        btn5.config(bg="#00FA9A")
        btn8.config(bg="#00FA9A")
    if btn3.cget('text')==btn6.cget('text')==btn9.cget('text')!="":
        is_win = True
        btn3.config(bg="#00FA9A")
        btn6.config(bg="#00FA9A")
        btn9.config(bg="#00FA9A")
    if btn1.cget('text')==btn5.cget('text')==btn9.cget('text')!="":
        is_win = True
        btn1.config(bg="#00FA9A")
        btn5.config(bg="#00FA9A")
        btn9.config(bg="#00FA9A")
    if btn3.cget('text')==btn5.cget('text')==btn7.cget('text')!="":
        is_win = True
        btn3.config(bg="#00FA9A")
        btn5.config(bg="#00FA9A")
        btn7.config(bg="#00FA9A")
    # if win combination exists or all moves made
    if is_win or move_count == 9 :
        #is_win = True
        if next_move == 'X':
            lbl.config(text="ПОБЕДИЛ: крестик")
        else:
            lbl.config(text="ПОБЕДИЛ: нолик")

        btn1.config( state=DISABLED)
        btn2.config( state=DISABLED)
        btn3.config( state=DISABLED)
        btn4.config( state=DISABLED)
        btn5.config( state=DISABLED)
        btn6.config( state=DISABLED)
        btn7.config( state=DISABLED)
        btn8.config( state=DISABLED)
        btn9.config( state=DISABLED)
    return is_win
# return value for button-text
def get_sign():
    global next_move
    if next_move == "X":
        return '╳'
    else:
        return '◯'


# after each move change sign of player
def switch_mode():
    global next_move
    global move_count
    if iswin() :##возвращать стопер
        None
    else:
        move_count =move_count +1
        if move_count != 9:
            if next_move == "X":
                next_move = '0'
                lbl.config(text="Ходит: нолик")
            else:
                next_move = 'X'
                lbl.config(text="Ходит: крестик")
        else:
            #draw ничья
            next_move = '-'
            lbl.config(text="Ничья")
# не удалось найти рабочего решения, для объявления одного действия на все кнопки
# поэтому пришлось прописать 9 схожих функций, на каждую кнопку
def btn_click1():
    if btn1.cget('text') != "":
        print( btn1.cget('text') )
    else:
        btn1.config(text=get_sign())
    btn1.config(state=DISABLED, bg="#BEBEBE")
    switch_mode()


def btn_click2():
    if btn2.cget('text') != "":
        print( btn2.cget('text') )
    else:
        btn2.config(text=get_sign())
    btn2.config(state=DISABLED, bg="#BEBEBE")
    switch_mode()

def btn_click3():
    if btn3.cget('text') != "":
        print( btn3.cget('text') )
    else:
        btn3.config(text=get_sign())
    btn3.config(state=DISABLED , bg="#BEBEBE")
    switch_mode()
def btn_click4():
    if btn4.cget('text') != "":
        print( btn4.cget('text') )
    else:
        btn4.config(text=get_sign())
    btn4.config(state=DISABLED, bg="#BEBEBE")
    switch_mode()
def btn_click5():
    if btn5.cget('text') != "":
        print( btn5.cget('text') )
    else:
        btn5.config(text=get_sign())
    btn5.config(state=DISABLED, bg="#BEBEBE")
    switch_mode()
def btn_click6():
    if btn6.cget('text') != "":
        print( btn6.cget('text') )
    else:
        btn6.config(text=get_sign())
    btn6.config(state=DISABLED, bg="#BEBEBE")
    switch_mode()
def btn_click7():
    if btn7.cget('text') != "":
        print( btn7.cget('text') )
    else:
        btn7.config(text=get_sign())
    btn7.config(state=DISABLED, bg="#BEBEBE")
    switch_mode()
def btn_click8():
    if btn8.cget('text') != "":
        print( btn8.cget('text') )
    else:
        btn8.config(text=get_sign())
    btn8.config(state=DISABLED, bg="#BEBEBE")
    switch_mode()
def btn_click9():
    if btn9.cget('text') != "":
        print( btn9.cget('text') )
    else:
        btn9.config(text=get_sign())
    btn9.config(state=DISABLED, bg="#BEBEBE")
    switch_mode()

# инициируем кнопки, хаодно проверяя отображение
btn1 = Button(window, text="╳", width=4, height=2,comman=btn_click1 , bg='white', state=DISABLED)
btn2 = Button(window, text="╳", width=4, height=2,comman=btn_click2, bg='white', state=DISABLED)
btn3 = Button(window, text="╳", width=4, height=2,comman=btn_click3, bg='white', state=DISABLED)
btn4 = Button(window, text="◯", width=4, height=2,comman=btn_click4, bg='white', state=DISABLED)
btn5 = Button(window, text="◯", width=4, height=2,comman=btn_click5, bg='white', state=DISABLED)
btn6 = Button(window, text="◯", width=4, height=2,comman=btn_click6, bg='white', state=DISABLED)
btn7 = Button(window, text="?", width=4, height=2,comman=btn_click7, bg='white', state=DISABLED)
btn8 = Button(window, text="", width=4, height=2,comman=btn_click8, bg='white', state=DISABLED)
btn9 = Button(window, text="—", width=4, height=2,comman=btn_click9, bg='white', state=DISABLED)



btn1.grid(column=2, row=2 )
btn2.grid(column=3, row=2)
btn3.grid(column=4, row=2)
btn4.grid(column=2, row=3)
btn5.grid(column=3, row=3)
btn6.grid(column=4, row=3)
btn7.grid(column=2, row=4)
btn8.grid(column=3, row=4)
btn9.grid(column=4, row=4)
# режим
combo = Combobox(window, state=DISABLED)
combo['values'] = ("1 игрок","2 игрока")
combo.current(1)  # установим вариант по умолчанию
combo.grid(column=0, row=1)

# new game
btnnew = Button(window, text="Новая игра", command=new_game)
btnnew.grid(column=0, row=2 )
#info табло с подсказками
lbl = Label(window, text="Ходит: крестик", font=("Arial Bold", 30))
lbl.place(x=1 , y=150)

window.mainloop()