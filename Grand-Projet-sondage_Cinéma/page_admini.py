from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox
import matplotlib.pyplot as pp
from PIL import Image, ImageTk
import pygame
import qrcode
import cv2 as cv
import smtplib
import ssl



def administration():
    fenetre2=Toplevel()
    fenetre2.title("Administration")
    fenetre2.geometry('480x320')
    fenetre2.config(bg='black')

    
    canvas = Canvas(fenetre2,height=0,width=0,)
    canvas.pack()
    img = PhotoImage(file="administration1.png")
    canvas.create_image(720, 480, image=img)
    label = Label(fenetre2, image=img)
    label.image = img
    label.pack()
    

    l0=Label(fenetre2,text="Administration",font=("Candara Light",21),bg="black",fg="white")
    l0.place(x=155,y=20)

    connect = sqlite3.connect("Cinema.db")
    cursor = connect.cursor()
        

    def liste():

        fenetre4 = Toplevel()
        fenetre4["bg"]="#021D42"
        fenetre4.title("Liste des sondés")


        
        nom1=""
        prenom1=""
        age1=""
        sexe1=""
        avec1=""
        cate1=""
        seance1=""
        film1=""

        cursor.execute("SELECT * FROM Cinema")
        l=cursor.fetchall()

        for i in range(len(l)):
            
            nom1 = nom1 + l[i][1]+"\n"
            prenom1 = prenom1 + l[i][2]+"\n"
            age1 = age1 + l[i][3]+"\n"
            sexe1 = sexe1 + (l[i][4])+"\n"
            avec1 = avec1 + str(l[i][5])+"\n"
            cate1 = cate1 + l[i][6]+"\n"
            seance1 = seance1 +(l[i][7])+"\n"
            film1 = film1 +(l[i][8])+"\n"
                

        



        l11=Label(fenetre4,text="Nom",font=("Candara Light",13),bg="#021D42",fg="white")
        l11.grid(row=2,column=0)
        l12=Label(fenetre4,text="Prénom",font=("Candara Light",13),bg="#021D42",fg="white")
        l12.grid(row=2,column=1)
        l13=Label(fenetre4,text="Age",font=("Candara Light",13),bg="#021D42",fg="white")
        l13.grid(row=2,column=2)
        l14=Label(fenetre4,text="Sexe",font=("Candara Light",13),bg="#021D42",fg="white")
        l14.grid(row=2,column=3)
        l15=Label(fenetre4,text="Avec qui ?",font=("Candara Light",13),bg="#021D42",fg="white")
        l15.grid(row=2,column=4)
        l16=Label(fenetre4,text="Catégorie de film",font=("Candara Light",13),bg="#021D42",fg="white")
        l16.grid(row=2,column=5)
        l17=Label(fenetre4,text="Type de séance",font=("Candara Light",13),bg="#021D42",fg="white")
        l17.grid(row=2,column=6)
        l18=Label(fenetre4,text="Film préféré",font=("Candara Light",13),bg="#021D42",fg="white")
        l18.grid(row=2,column=7)






        colonnenom1 = Text(fenetre4, height = 30, width = 16,font=("Courier",11),bg="#021D42",fg="red")
        colonnenom1.insert(END,nom1)
        colonnenom1.grid(row =3, column = 0)

        colonneprenom1 = Text(fenetre4, height = 30, width = 16,font=("Courier",11),bg="#021D42",fg="red")
        colonneprenom1.insert(END,prenom1)
        colonneprenom1.grid(row =3, column = 1)

        colonneage1 = Text(fenetre4, height = 30, width = 22,font=("Courier",11),bg="#021D42",fg="red")
        colonneage1.insert(END,age1)
        colonneage1.grid(row =3, column = 2)

        colonnesexe1 = Text(fenetre4, height = 30, width = 12,font=("Courier",11),bg="#021D42",fg="red")
        colonnesexe1.insert(END,sexe1)
        colonnesexe1.grid(row =3, column = 3)

        colonneseance1 = Text(fenetre4, height = 30, width = 18,font=("Courier",11),bg="#021D42",fg="red")
        colonneseance1.insert(END,avec1)
        colonneseance1.grid(row =3, column = 4)

        colonneavec1 = Text(fenetre4, height = 30, width = 18,font=("Courier",11),bg="#021D42",fg="red")
        colonneavec1.insert(END,cate1)
        colonneavec1.grid(row =3, column = 5)

        colonnecate1 = Text(fenetre4, height = 30, width = 15,font=("Courier",11),bg="#021D42",fg="red")
        colonnecate1.insert(END,seance1)
        colonnecate1.grid(row =3, column = 6)

        colonnefilm1 = Text(fenetre4, height = 30, width = 22,font=("Courier",11),bg="#021D42",fg="red")
        colonnefilm1.insert(END,film1)
        colonnefilm1.grid(row =3, column = 7)

        b1=Button(fenetre4,text="Quitter",font=("Candara Light",11),borderwidth=4,bg="red",command=fenetre4.destroy)
        b1.grid(row=0,column=7)

            

            
        fenetre4.mainloop()
        """
        im = Image.open("administration.jpg")
        resized1=im.resize((720,480), Image.ANTIALIAS)
        vac = ImageTk.PhotoImage(resized1)
        fond= Label(fenetre2,image=vac)
        fond.place(x=0,y=0)
        """

        
    def recherche():

        
        
        def save():


            
            colonnenom.delete(0.0,END)
            colonneprenom.delete(0.0,END)
            colonnesexe.delete(0.0,END)
            colonneage.delete(0.0,END)
            colonnefilm.delete(0.0,END)
            colonneseance.delete(0.0,END)
            colonnequi.delete(0.0,END)
            colonnecate.delete(0.0,END)
                           
            connect = sqlite3.connect("Cinema.db")
            cursor = connect.cursor()
                
                    
            
            nom=e.get()
            prenom=e1.get()
            sexe=""
            age=""
            film=""
            seance=""
            qui=""
            cate=""
                
                
            cursor.execute("SELECT * FROM Cinema WHERE Nom =(?) AND Prenom=(?)",(nom, prenom))
            connect.commit()
            liste=cursor.fetchall()
            
                              
            for i in range(len(liste)):
                
                nom =  (liste[0][1])+"\n"
                prenom = (liste[0][2])+"\n"
                sexe =  (liste[0][3])+"\n"
                age = (liste[0][4])+"\n"
                film =  ( liste[0][5])+"\n"
                seance = (liste[0][6])+"\n"
                qui =(liste[0][7])+"\n"
                cate =(liste[0][8])+"\n"
                    
            
            
            colonnenom.insert(END,nom)
            colonneprenom.insert(END,prenom)
            colonnesexe.insert(END,age)
            colonneage.insert(END,sexe)
            colonnefilm.insert(END,cate)
            colonneseance.insert(END,qui)
            colonnequi.insert(END,film)            
            colonnecate.insert(END,seance) 
            


        fenetre3=Tk()
        fenetre3.title("Rechercher/Supprimer un utilisateur")
        fenetre3.config(bg='#021D42')    


        
        l11=Label(fenetre3,text="Nom",font=("Candara Light",13),bg="#021D42",fg="white")
        l11.grid(row=2,column=0)
        l12=Label(fenetre3,text="Prénom",font=("Candara Light",13),bg="#021D42",fg="white")
        l12.grid(row=2,column=1)
        l13=Label(fenetre3,text="Sexe",font=("Candara Light",13),bg="#021D42",fg="white")
        l13.grid(row=2,column=2)
        l14=Label(fenetre3,text="Age",font=("Candara Light",13),bg="#021D42",fg="white")
        l14.grid(row=2,column=3)
        l15=Label(fenetre3,text="Film préferé ",font=("Candara Light",13),bg="#021D42",fg="white")
        l15.grid(row=2,column=4)
        l16=Label(fenetre3,text="Type de séance",font=("Candara Light",13),bg="#021D42",fg="white")
        l16.grid(row=2,column=5)
        l17=Label(fenetre3,text="Avec qui ?",font=("Candara Light",13),bg="#021D42",fg="white")
        l17.grid(row=2,column=6)
        l18=Label(fenetre3,text="Quelle catégorie",font=("Candara Light",13),bg="#021D42",fg="white")
        l18.grid(row=2,column=7)





        colonnenom = Text(fenetre3, height = 30, width = 14,font=("Courier",11),bg="#021D42",fg="red")
        colonnenom.grid(row =4, column = 0)

        colonneprenom = Text(fenetre3, height = 30, width = 14,font=("Courier",11),bg="#021D42",fg="red")
        colonneprenom.grid(row =4, column = 1)

        colonnesexe = Text(fenetre3, height = 30, width = 10,font=("Courier",11),bg="#021D42",fg="red")
        colonnesexe.grid(row =4, column = 2)

        colonneage = Text(fenetre3, height = 30, width = 20,font=("Courier",11),bg="#021D42",fg="red")
        colonneage.grid(row =4, column = 3)

        colonnefilm = Text(fenetre3, height = 30, width = 15,font=("Courier",11),bg="#021D42",fg="red")
        colonnefilm.grid(row =4, column = 4)

        colonneseance = Text(fenetre3, height = 30, width = 8,font=("Courier",11),bg="#021D42",fg="red")
        colonneseance.grid(row =4, column = 5)

        colonnequi = Text(fenetre3, height = 30, width = 15,font=("Courier",11),bg="#021D42",fg="red")
        colonnequi.grid(row =4, column = 6)
                
        colonnecate = Text(fenetre3, height = 30, width = 15,font=("Courier",11),bg="#021D42",fg="red")
        colonnecate.grid(row =4, column = 7)    


        b1=Button(fenetre3, text="Chercher",font=("Candara Light",12),borderwidth=4, bg="red", command=save)
        b1.grid(row=0,column=3)       

                    
        def supprimer():
            
            connect = sqlite3.connect("Cinema.db")
            cursor = connect.cursor()
                
            e0=e.get()
            e01=e1.get()
                
            req="DELETE FROM Cinema WHERE Nom=? AND Prenom=?"""
            cursor.execute(req, (e0, e01, ))
            connect.commit()
            e.delete(0,"end")
            e1.delete(0,"end")
            

            tk.messagebox.showinfo(title='Information', message='Ce sondé à bien été supprimé de la base de données')
            
               
                
        l=Label(fenetre3,bg="#021D42",fg="white",font=("Candara Light",15),text="Nom de l'utilisateur : ")
        l.grid(row=0,column=0)
        e=Entry(fenetre3)
        e.grid(row=0,column=1)
        l1=Label(fenetre3,bg="#021D42",fg="white",font=("Candara Light",15),text="Prénom de l'utilisateur : ")
        l1.grid(row=1,column=0)
        e1=Entry(fenetre3)
        e1.grid(row=1, column=1)



        b2=Button(fenetre3, text="Supprimer",font=("Candara Light",12),borderwidth=4, bg="red", command=supprimer)
        b2.grid(row=1,column=3)
        b3=Button(fenetre3,text="Quitter",font=("Candara Light",10),borderwidth=4,bg="red",command=fenetre3.destroy)
        b3.grid(row=0,column=7)
            
        
        
    b1=Button(fenetre2, bg="#021D42",fg="White",borderwidth=3,text="Liste des sondés",font=("Candara Light",17),command=liste)
    b1.place(x=150,y=200)
    b2=Button(fenetre2, bg="#021D42",fg="white",borderwidth=3,text="Rechercher / Supprimer un sondé",font=("Candara Light",17),command=recherche)
    b2.place(x=72,y=125)
    b3=Button(fenetre2,bg="black",fg="White",borderwidth=4, text="Quitter",font=("Candara Light",10),command=fenetre2.destroy)
    b3.place(x=25,y=275)

    
