
#!/usr/bin/env python
from tkinter import*
import tkinter.messagebox as box#ok
from time import *
import datetime
import random

window=Tk()#ok
window.title('M I X U P')#okTITLE
dun=PhotoImage(file='dunce.gif')
small_dun=PhotoImage.subsample(dun,x=2,y=2)
win=PhotoImage(file='winner.gif')
small_win=PhotoImage.subsample(win,x=2,y=2)
img=PhotoImage(file='mixup.gif')#PIC
small_img=PhotoImage.subsample(img,x=2,y=2)#PIC
imgLb1=Label(window,relief=RAISED)#PIC
imgLb1.configure(image='')
label2=Label(window,relief=RAISED)   #
label=Label(window,relief=RAISED)   #var
label3=Label(window,relief=RAISED)#
label4=Label(window,relief=RAISED)#
label5=Label(window,relief=RAISED)#timed
label6=Label(window,relief=RAISED)#clock
label7=Label(window,text='**Your Score **',bg="yellow",relief=RAISED)
label8=Label(window,text='**Games Played**',bg="#c1d6d6",relief=RAISED)
label2.configure(text ='******',bg="#c1d6d6") #word to guess
label.configure( text = '...')#OK  intro & insrcts
label3.configure(text='...',bg="yellow")#player score
label4.configure(text ='...',bg="#c1d6d6")#games played
label5.configure(text='**Your Time***In Seconds**',bg="#ffaed6")#timed
label6.configure(text='*0  secs*',bg="#ffaed6")#  clock
frame=Frame(window)#ok

entryn = Entry(frame)#ok  name
entryw = Entry(frame, exportselection=0)#ok  word
player_score=0
count=0
guswor=['worsaa','worsbb','worsdd','worscc','worsee']
grets='\nWhat  Is  Your  Name  ?.\nType In Your Name And Pess Enter\n'#ok
wors='\nYou Have 800 Seconds To Guess 10 Words\n'#ok
words=['weasel','marten','badger','steady','forest','scored','stored','sorted','strand','dancer','chairs','choice','castor',
'curate','safety','tailor','softly','shogun','nougat','sacred','salted','dressy','endear','comedy','topics','spotty','flight',
'saturn','vulcan','future','trophy','tropic','coarse','scurge','facets','erupts','insect','orange','garden','turnip','magpie',
'yellow','python','escape','banana','forget','global','mirror','window','debug','script','editor','figure','system','output',
'reason','driver','matter','proper','browse','camera','button','bottom','change','either','unique','prefix','remove']
a='worsaa'
b='worsbb'
d='worsdd'
c='worscc'
e='worsee'

label.configure(text=grets)#  first  intro
label4.configure(text=count)#0
label3.configure(text=player_score)#0
imgLb1.configure(image=small_img)

def pick_a_word():
    word_position=random.randint(0, len(words)-1)
    return words[word_position]
def pick_a_mix():
    word_position=random.randint(0, len(guswor)-1)
    return guswor[word_position]
            
start_timer=time()
def play():    
    if entryw.get()==word_a:
        box.showinfo('***MIXUP ***','Well Done, You Are Correct : '+entryn.get())
        global player_score
        player_score+=1
        label3.configure(text=player_score)
        global count
        count+=1
    else:
        box.showinfo('***MIXUP***','Sorry, You Are Incorrect,\nBad Luck : '+entryn.get())#4
        global count
        count +=1      
    label4.configure(text=count)
    label3.configure(text=player_score)
    
    end_timer=time()#time
    struct=localtime(end_timer) #?
    difference=round(end_timer - start_timer)#time
    #print('\ntime:',difference,'secs') 
    label6.configure(text=difference)      #time
    if player_score==10 and difference <700:
        label6.configure(text='**Well Done ,You Must Have Had The Easey Words**')
        imgLb1.configure(image=small_win)
    if player_score==10 and difference >700 and difference <800:
        label6.configure(text=' **Well  Done ,You Have A Good Time**')
        imgLb1.configure(image=small_win)
    if player_score==10 and difference >800 and difference <900:
        label6.configure(text='**You Have 10  Rigth But You Have Run Out Of Time**')
        imgLb1.configure(image=small_dun)
    if player_score==10 and difference >900:
        label6.configure(text="**You Ran Out Of Time, Your To slow,\nYou Will Have To Be Faster Next Time.")
        imgLb1.configure(image=small_dun)
    label2.configure(text='******')
button=Button(frame,text='**ENTER   WORD**',bg="cyan",cursor="mouse",command=play)#7

def playw():
    global word_a
    word_a=pick_a_word()[0: 6]
    word_b=pick_a_mix()[0: 6]
    #print(word_a)
    worsaa= (word_a[1],word_a[2],word_a[0],word_a[5],word_a[4],word_a[3])
    worsbb= (word_a[5],word_a[1],word_a[3],word_a[0],word_a[4],word_a[2])
    worsdd= (word_a[3],word_a[4],word_a[5],word_a[0],word_a[2],word_a[1])
    worscc= (word_a[3],word_a[0],word_a[5],word_a[2],word_a[1],word_a[4])
    worsee= (word_a[5],word_a[1],word_a[3],word_a[2],word_a[4],word_a[0])
    if a==word_b:
        print('1')
        label2.configure(text=worsaa,bg="#c1d6d6")        
    if b==word_b:
        print('2')
        label2.configure(text=worsbb,bg="#c1d6d6")        
    if d==word_b:
        print('3')
        label2.configure(text=worsdd,bg="#c1d6d6")        
    if c==word_b:
        print('4')
        label2.configure(text=worscc,bg="#c1d6d6")
    if e==word_b:
        label2.configure(text=worsee,bg="#c1d6d6")
    
    struct=localtime(start_timer)#time
    strftime('%X',struct)     #time
button2=Button(frame,text='**NEXT   WORD**',bg="#c1d6d6",cursor="watch",command=playw ) # 1 
 
def dialog():  #ok
    label.configure( text =wors)  #first word intro 1   
    box.showinfo('***MIXUP**','Hello , Welcome To Mixup ,:'+entryn.get()) 
btn=Button(frame,text='**ENTER NAME**',cursor="heart",command=dialog)#ok   1

frame.pack(padx=50,pady=10)#ok    1
btn.pack()#ok                     1
entryn.pack()#ok                 1
button.pack()#ok
entryw.pack()

frame.pack()#ok
label2.pack()

label.pack(padx=50,pady=20)#ok
button2.pack(padx=50,pady=20)
label7.pack()
label3.pack()
label8.pack()
label4.pack()

label5.pack()
label6.pack()
imgLb1.pack()
window.mainloop()#ok
 
 
 
