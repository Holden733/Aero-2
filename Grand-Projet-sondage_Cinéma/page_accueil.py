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
from page_admini import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


fenetre = Tk()
fenetre.title("Accueil")
fenetre.geometry("720x480")
fenetre.config(bg="black")


#Photo de fond d'écran

im = Image.open("salle-de-cinema.gif")
resized1=im.resize((720,480), Image.ANTIALIAS)
vac = ImageTk.PhotoImage(resized1)
fond= Label(fenetre,image=vac)
fond.place(x=-2,y=0)



#création du module musique

pygame.mixer.init()
musique= pygame.mixer.Sound("Disney.mp3")
musique.set_volume(1)
musique.play()
def son():
    musique.set_volume(1)
   

def off():
    musique.set_volume(0)

image1=PhotoImage(file="sonoff.png").subsample(3)    
image2=PhotoImage(file="sonon.png").subsample(3)
b00=Button(fenetre,width= 25, height=25,bg="#861F09",borderwidth=4,image=image1,command=off)
b00.place(x=670,y=55)
b01=Button(fenetre, width= 25, height=25,bg="#861F09",borderwidth=4,image=image2,command=son)
b01.place(x=670,y=105)



#création boutons/entrées


image3=PhotoImage(file="quitter.png").subsample(3)
image4=PhotoImage(file="mail.png").subsample(3)

l0=Label(fenetre, text="Veuillez saisir vos informations personnelles", font=("Candara Light",18),bg="black",fg="red")
l0.place(x=140, y = 50)

l1=Label(fenetre,text="Nom :",font=("Candara Light",11),bg="#861F09",fg="white")
l1.place(x=210,y=122)
e1=Entry(fenetre)
e1.place(x=171,y=156)


l2=Label(fenetre,text="Prénom :",font=("Candara Light",11),bg="#861F09",fg="white")
l2.place(x=452,y=122)
e2=Entry(fenetre)
e2.place(x=419,y=156)
    

l3=Label(fenetre,text="Genre :",font=("Candara Light",11),bg="#861F09",fg="white")
l3.place(x=202,y=235)

s3 = ttk.Combobox(fenetre,values=["Homme", "Femme", "Autre"])
s3.place(x=160,y=269)
s3.current(0)
    

l4=Label(fenetre,text="Catégorie d'âge :",font=("Candara Light",11),bg="#861F09",fg="white")
l4.place(x=427,y=235)

s4 = ttk.Combobox(fenetre,values=["Mineur (0 à 17ans)", "Adulte (18 à 59ans)", "Senior (après 59ans)"])
s4.place(x=408, y=269)
s4.current(0)

l5=Label(fenetre,text="Adresse mail :",font=("Candara Light",11),bg="black",fg="white")
l5.place(x=210,y=433)
e5=Entry(fenetre)
e5.place(x=325,y=435)  



def seance():

    fenetre1=Toplevel()
    fenetre1.title("Cinéma")
    fenetre1.geometry('720x480')
    fenetre1.config(bg='black')


    #Photo fond d'écran 2nde page
    canvas = Canvas(fenetre1,height=0,width=0,)
    canvas.pack()

    img = PhotoImage(file="universal.png")
    canvas.create_image(720, 480, image=img)
    label = Label(fenetre1, image=img)
    label.image = img

    label.pack()

    #Création Combobox/entrées


    l0=Label(fenetre1,text="Choisissez votre séance idéale au cinéma",font=("Candara Light",21),bg="#021D42",fg="white")
    l0.place(x=135,y=5)
        
        
    l1=Label(fenetre1,text="Votre film préféré :",font=("Candara Light",13),bg="#021D42",fg="white")
    l1.place(x=447, y=200)
    s1 = ttk.Combobox(fenetre1,values=["Boite Noire", "Seul sur Mars","Effeil","Mourir peut attendre","Barbaque","Dune","Aline","Venom","Last Night in Soho","Autre"])
    s1.place ( x=445,y=240)
    s1.current(0)

    l5=Label(fenetre1,text="(Si votre film préféré \n ne figure pas sur la liste,\n veuillez l'inscrire dans la case)",font=("courier",8),bg="#861F09",fg="white")
    l5.place(x=395,y=267)


    l2=Label(fenetre1,text="Type de séance :",font=("Candara Light",13),bg="#021D42",fg="white")
    l2.place(x=145,y=200)
    s5 = ttk.Combobox(fenetre1,values=["4K","3D","4DX","VOSTFR","VF"])
    s5.place(x=135, y=240)
    s5.current(0)

        
    l3=Label(fenetre1,text="Je préfère y aller avec qui ?",font=("Candara Light",13),bg="#021D42",fg="white")
    l3.place(x=110,y=90)
    s6 = ttk.Combobox(fenetre1,values=["En famille", "En amoureux", "Avec des amis"])
    s6.place ( x=135,y=130)
    s6.current(0)

        
    l4=Label(fenetre1,text="Catégorie de film préférée ?",font=("Candara Light",13),bg="#021D42",fg="white")
    l4.place(x=420,y=90)
    s7 = ttk.Combobox(fenetre1,values=["Action", "Aventure", "Comédie","Drame","Fantastique","Guerre","Policier","Horreur","Western","Science-fiction","Documentaire","Dessin animé"])
    s7.place ( x=445,y=130)
    s7.current(0)






    def enregistrer():

        tk.messagebox.showinfo(title='Information', message='les choix ont bien été enregistrés')
                
                
        connexion = sqlite3.connect('Cinema.db')
        cursor = connexion.cursor()

                
        E1=e1.get()
        E2=e2.get()
        E3=s1.get()
        E4=s4.get()
        E5=s5.get()  
        E6=s3.get()
        E7=s6.get()
        E8=s7.get()
                

        cursor.execute('INSERT INTO Cinema(Nom, Prenom, Age, Sexe, Avec, Categorie, Seance, Film) VALUES (?,?,?,?,?,?,?,?)',(E1,E2,E4,E6,E7,E8,E5,E3))
        connexion.commit()  # mise à jour et enregistrement
                
        connexion.close()


   

           

    def stats_genre():
        E1=e1.get()
        E2=e2.get()
        E3=s1.get()
        E4=s4.get()
        E5=s5.get()  
        E6=s3.get()
        E7=s6.get()
        E8=s7.get()
                   
        connexion = sqlite3.connect('Cinema.db')
        cursor = connexion.cursor()
                    
        connexion.close()
            #figure 2

        pp.figure("Diagramme sur les genres",facecolor="blanchedalmond", figsize=(6, 4))
        pp.suptitle("Statistiques sur les genres", fontsize=20, style= "oblique", x=0.5, y=0.95)
                    
          
            #graph1
            
        pp.subplot(111)
        name_genre = ["Homme","Femme","Autre"]
        con = sqlite3.connect("Cinema.db")
        cur = con.cursor()
        cur.execute("SELECT COUNT (Sexe) FROM Cinema WHERE Sexe= 'Homme'")
        homme=cur.fetchone()[0]
        con.commit()
        cur.execute("SELECT COUNT (Sexe) FROM Cinema WHERE Sexe= 'Femme'")
        femme=cur.fetchone()[0]
        con.commit()
        cur.execute("SELECT COUNT (Sexe) FROM Cinema WHERE Sexe= 'Autre'")
        autre=cur.fetchone()[0]
        con.commit()
        con.close()

        genr= [homme,femme,autre]
        pp.pie(genr, labels=name_genre,autopct='%1.2f%%')

        pp.savefig("diagramme1.png")



        pp.show()
        

    b6=Button(fenetre1,bg="black",fg="red",borderwidth=2, relief=GROOVE,text="Statistiques sur les genres",font=("Candara Light",12),command=stats_genre)
    b6.place(x=75,y=370)   

            #graph2

    def stats_age():
        
        pp.figure("Diagramme sur les âges",facecolor="papayawhip", figsize=(6, 4))
        pp.suptitle("Statistiques sur les âges", fontsize=20, style= "oblique", x=0.5, y=0.95)
        

        pp.subplot(111)
        name_age = ["Mineur (0 à 17ans)","Adulte (18 à 59ans)","Senior (après 59ans)"]
        con = sqlite3.connect("Cinema.db")
        cur = con.cursor()
        cur.execute("SELECT COUNT (Age) FROM Cinema WHERE Age= 'Mineur (0 à 17ans)'")
        mineur=cur.fetchone()[0]
        con.commit()
        cur.execute("SELECT COUNT (Age) FROM Cinema WHERE Age= 'Adulte (18 à 59ans)'")
        adulte=cur.fetchone()[0]
        con.commit()
        cur.execute("SELECT COUNT (Age) FROM Cinema WHERE Age= 'Senior (après 59ans)'")
        senior=cur.fetchone()[0]
        con.commit()
        con.close()

        age= [mineur,adulte,senior]
        pp.pie(age, labels=name_age,autopct='%1.2f%%')

        pp.savefig("diagramme2.png")


            
        pp.show()

    
    b3=Button(fenetre1,bg="black",fg="red",borderwidth=2,relief=GROOVE, text="Statistiques sur les âges",font=("Candara Light",12),command=stats_age)
    b3.place(x=82,y=405)
        

    def statistiques1():

          


            #figure1

        pp.figure("Diagrammes sur vos choix de séance", facecolor="blanchedalmond",figsize=(12, 10))
        pp.suptitle("Statistiques sur les séances choisies", fontsize=30, style= "oblique", x=0.5, y=0.95)

            #graph1

        pp.subplot(221)
        name_carac = ["4K","3D","4DX","VOSTFR","VF"]
        con = sqlite3.connect("Cinema.db")
        cur = con.cursor()
        cur.execute("SELECT COUNT (Seance) FROM Cinema WHERE Seance= '4K'")
        quatreK=cur.fetchone()[0]
        con.commit()
        cur.execute("SELECT COUNT (Seance) FROM Cinema WHERE Seance= '3D'")
        troisD=cur.fetchone()[0]
        con.commit()
        cur.execute("SELECT COUNT (Seance) FROM Cinema WHERE Seance= '4DX'")
        quatreDX=cur.fetchone()[0]
        con.commit()
        cur.execute("SELECT COUNT (Seance) FROM Cinema WHERE Seance= 'VOSTFR'")
        vostfr=cur.fetchone()[0]
        con.commit()
        cur.execute("SELECT COUNT (Seance) FROM Cinema WHERE Seance= 'VF'")
        vf=cur.fetchone()[0]
        con.commit()
        con.close()

        typ= [quatreK,troisD,quatreDX,vostfr,vf]
        pp.pie(typ, labels=name_carac,autopct='%1.2f%%')
                

                
            #graph2

        pp.subplot(212)
        name_avec = ["En famille","En amoureux","Avec des amis"]
        con = sqlite3.connect("Cinema.db")
        cur = con.cursor()
        cur.execute("SELECT COUNT (Avec) FROM Cinema WHERE Avec= 'En famille'")
        famille=cur.fetchone()[0]
        con.commit()
        cur.execute("SELECT COUNT (Avec) FROM Cinema WHERE Avec= 'En amoureux'")
        amoureux=cur.fetchone()[0]
        con.commit()
        cur.execute("SELECT COUNT (Avec) FROM Cinema WHERE Avec= 'Avec des amis'")
        amis=cur.fetchone()[0]
        con.commit()
        con.close()
                
        avec= [famille,amoureux,amis]
        pp.pie(avec, labels=name_avec,autopct='%1.2f%%')

                
                
            #graph3

        pp.subplot(222)
        name_cate = ["Action", "Aventure", "Comédie","Drame","Fantastique","Guerre","Policier","Horreur","Western","Science-fiction","Documentaire","Dessin animé"]
        con = sqlite3.connect("Cinema.db")
        cur = con.cursor()
        cur.execute("SELECT COUNT (Categorie) FROM Cinema WHERE Categorie= 'Action'")
        action=cur.fetchone()[0]
        con.commit()
        cur.execute("SELECT COUNT (Categorie) FROM Cinema WHERE Categorie= 'Aventure'")
        aventure=cur.fetchone()[0]
        con.commit()
        cur.execute("SELECT COUNT (Categorie) FROM Cinema WHERE Categorie= 'Comédie'")
        comed=cur.fetchone()[0]
        con.commit()
        cur.execute("SELECT COUNT (Categorie) FROM Cinema WHERE Categorie= 'Drame'")
        drame=cur.fetchone()[0]
        con.commit()
        cur.execute("SELECT COUNT (Categorie) FROM Cinema WHERE Categorie= 'Fantastique'")
        fantastique=cur.fetchone()[0]
        con.commit()
        cur.execute("SELECT COUNT (Categorie) FROM Cinema WHERE Categorie= 'Guerre'")
        guerre=cur.fetchone()[0]
        con.commit()
        cur.execute("SELECT COUNT (Categorie) FROM Cinema WHERE Categorie= 'Policier'")
        policier=cur.fetchone()[0]
        con.commit()
        cur.execute("SELECT COUNT (Categorie) FROM Cinema WHERE Categorie= 'Horreur'")
        horreur=cur.fetchone()[0]
        con.commit()
        cur.execute("SELECT COUNT (Categorie) FROM Cinema WHERE Categorie= 'Western'")
        western=cur.fetchone()[0]
        con.commit()
        cur.execute("SELECT COUNT (Categorie) FROM Cinema WHERE Categorie= 'Science-fiction'")
        SF=cur.fetchone()[0]
        con.commit()
        cur.execute("SELECT COUNT (Categorie) FROM Cinema WHERE Categorie= 'Documentaire'")
        docu=cur.fetchone()[0]
        con.commit()
        cur.execute("SELECT COUNT (Categorie) FROM Cinema WHERE Categorie= 'Dessin animé'")
        dess=cur.fetchone()[0]
        con.commit()
                    
        con.close()
                 
        catego= [action, aventure,comed, drame, fantastique, guerre, policier, horreur, western, SF, docu, dess]
        pp.pie(catego, labels=name_cate, autopct='%1.2f%%')
                    
                    
                    
        pp.show()               
        
        
    #Creation du QR code
    def make_qrcode():

        tk.messagebox.showinfo(title="Information", message="Vous allez recevoir un QRCODE")


        qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4,)


        E1=e1.get()
        E2=e2.get()
        E3=s1.get()
        E5=s5.get()  
        E8=s7.get()

        data=  'Nom :',E1 ,'Prénom :',E2 , 'Type de séance préférée :', E5, 'Film préféré :', E3, 'Catégorie preférée:', E8
        qr.add_data(data)
        qr.make(fit=True)


        img = qr.make_image(fill_color="red", back_color="black").convert('RGB')
        img.save("Qr_code.png")



        #creation de la fenetre d'affichage


        fenetre5=Toplevel()
        fenetre5.title("QRcode")
        fenetre5.config(bg="black")
        fenetre5.geometry('780x780')

        canvas = Canvas(fenetre5,height=0,width=0,)

        canvas.pack()

        img = PhotoImage(file="QR_code.png")
        canvas.create_image(680, 680, image=img)

        label = Label(fenetre5, image=img)
        label.image = img ## Association de l'image au widget
        label.pack()

        e1.delete(0,END)
        e2.delete(0,END)

        smtp_address = "smtp.gmail.com"
        smtp_port = 465
        address = "votreseanceidealeaucinema@gmail.com"
        password = "seanceideale"
        receiver = e5.get()



        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_address, smtp_port, context = context) as server :
            server.login(address, password)
            server.sendmail(address, receiver, "Bonjour utilisateur ! \n\n      Nous vous remercions de nous avoir accorde de votre temps pour reponde a ce questionnaire. \n\n      Afin de garder une trace de ce questionnaire, nous vous invitons a cliquer sur l'icone e-mail present sur la 2eme fenetre de notre application afin de recevoir par mail certaines statistiques !\n\nCordialement, \n\nQuentin Delpeuch & Ghislain Lecouillard")
            



        tk.messagebox.showinfo("Information", "Un mail automatique vous à été envoyé")


        #création mail


    def mail():
        smtp_address = "smtp.gmail.com"
        smtp_port = 465
            
        address = "votreseanceidealeaucinema@gmail.com"
        password = "seanceideale"
        receiver = e5.get()
        message=MIMEMultipart()
        message['subject']= "Merci de votre participation au sondage"
        

        with open ("diagramme1.png",'rb')as f:
            image=MIMEImage(f.read())
            image.add_header('Content-Disposition','attachment',filename="diagramme1.png")
            message.attach(image)
        with open ("diagramme2.png",'rb')as f:
            image1=MIMEImage(f.read())
            image1.add_header('Content-Disposition','attachment',filename="diagramme2.png")
            message.attach(image1)



        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_address, smtp_port, context = context) as server :
            server.login(address, password)            
            txt=message.as_string().encode('utf-8')           
            server.sendmail(address, receiver, txt)



        tk.messagebox.showinfo("Envoie E-mail", "Un mail contenant certaines statistiques vous a été envoyé")

        e5.delete(0,END)

    b001=Button(fenetre1, width= 30, height=30,bg="#861F09",borderwidth=4,image=image4,command=mail)
    b001.place(x=333,y=440)

        
          

        

    
    #Création boutons 2eme fenetre

    b1=Button(fenetre1,bg="#021D42",fg="white",borderwidth=4, relief=GROOVE,text="Enregistrer votre choix",font=("Candara Light",16),command=enregistrer)
    b1.place(x=240,y=318)
    b2=Button(fenetre1,bg="black",fg="red",borderwidth=2, relief=GROOVE,text="Statistiques sur vos choix",font=("Candara Light",12),command=statistiques1)
    b2.place(x=438,y=387)
    b4=Button(fenetre1,bg="#021D42",fg="white",borderwidth=3, relief=GROOVE,text="Valider",font=("Candara Light",14),command=make_qrcode)
    b4.place(x=316,y=387)
    b5=Button(fenetre1,bg="blanchedalmond",image=image3,command=fenetre1.destroy)
    b5.place(x=15,y=15)


  



    

   

#Boutons 1ere fenetre

b1=Button(fenetre, bg="black",fg="red",borderwidth=4, relief=GROOVE, text="Quelle est votre séance de cinéma idéale ?",font=("Candara Light",16),command=seance)
b1.place(x=160,y=340)       
b2=Button(fenetre,bg="black",fg="red",borderwidth=4, relief=GROOVE, text="Administratif",font=("Candara Light",10),command=administration)
b2.place(x=605,y=430)
b4=Button(fenetre,bg="blanchedalmond",image=image3,command=fenetre.destroy)
b4.place(x=15,y=430)


fenetre.mainloop()
