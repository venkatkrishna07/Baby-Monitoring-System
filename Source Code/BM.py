import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time
import os.path



window=tkinter.Tk()
window.geometry("1212x776+325+103")
window.title('Baby Monitor')
window.resizable(0, 0)
window.focus_force()


window.configure(bg="#1f1f1f")


notifyimage=tkinter.PhotoImage(file="C:/Users/Venkat Krishna/Google Drive/Object Tracking/tensorflow_object_counting_api/icons/rsz_notify_page.png")
allownoti=tkinter.PhotoImage(file="C:/Users/Venkat Krishna/Google Drive/Object Tracking/tensorflow_object_counting_api/icons/rsz_allownot.png")
mobilenot=tkinter.PhotoImage(file="C:/Users/Venkat Krishna/Google Drive/Object Tracking/tensorflow_object_counting_api/icons/mobile.png")
qrimage=tkinter.PhotoImage(file="C:/Users/Venkat Krishna/Google Drive/Object Tracking/tensorflow_object_counting_api/icons/defaultimage.png")
logoimg=tkinter.PhotoImage(file="C:/Users/Venkat Krishna/Google Drive/Object Tracking/tensorflow_object_counting_api/icons/baby.png")
def detect():
            import tensorflow as tf

            from utils import backbone
            from api import object_counting_api

            detection_graph, category_index = backbone.set_model('custom_frozen_inference_graph', 'label_map.pbtxt')

            is_color_recognition_enabled = 0

            object_counting_api.detect_baby(detection_graph, category_index, is_color_recognition_enabled)

def qr(link):
    import qrcode
    img = qrcode.make(link)
    print(type(img))
    print(img.size)
    img.save('QR/qrcode.png')
    qrimage=tkinter.PhotoImage(file="C:/Users/Venkat Krishna/Google Drive/Object Tracking/tensorflow_object_counting_api/QR/qrcode.png")
    
def clipboardc(link):
    r=tkinter.Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(link)
    r.update() 
    r.destroy()
def qrwindow():
            qrwin=tkinter.Toplevel(window,bd=1,highlightthickness=1,relief='ridge',bg="#ffffff")
            qrwin.geometry("435x409+1469+578")
            qrwin.resizable(0, 0)   
            
            qrimage=tkinter.PhotoImage(file="C:/Users/Venkat Krishna/Google Drive/Object Tracking/tensorflow_object_counting_api/QR/qrcode.png")
          
            labelqr=tkinter.Label(qrwin,image=qrimage)
            labelqr.image=qrimage
            labelqr.place(relx=0.029,rely=0.014)
def notifywin():
    def closewin():
        notwin.destroy()
    
    

    notwin=tkinter.Toplevel(window,bd=1,highlightthickness=1,relief='ridge')
    notwin.geometry("929x687+475+182")
    notwin.resizable(0, 0)
    notwin.focus_force()
    notwin.overrideredirect(True)
    
    notwin.configure(bg="#1f1f1f")
    closeb=tkinter.Button(notwin,text='Back',bg="#4C8BF5",fg='white',border=0,command=closewin)
    closeb.place(relx=0.017,rely=0.022,width=87,height=27)
    
    
    labelnotify=tkinter.Label(notwin,image=notifyimage)
    labelnotify.image=notifyimage
    labelnotify.place(relx=0.052,rely=0.467)
    
    labelallow=tkinter.Label(notwin,image=allownoti)
    labelallow.image=allownoti
    labelallow.place(relx=0.582,rely=0.466)
    
    labelmobile=tkinter.Label(notwin,image=mobilenot)
    labelmobile.image=mobilenot
    labelmobile.place(relx=0.582,rely=0.711)
    
    
    def add_device():
         
            file1 = open("notify/notification.txt","r") 
            contents=file1.read()
            if(contents!=0):
                   file2=open("C:/Users/Venkat Krishna/.config/notify-run","r")
                   contents2=file2.read()
                   temp=contents2.replace("[","")
                   temp2=temp.replace("]","")
                   temp3=temp2.replace("endpoint","url")
                   temp4=temp3.replace("{","").replace("}","")
                   link=temp4
                   clink=link.split(' ')[1]
                   flink=clink.replace('"','')
                   
                   urlt=tkinter.Text(canvas1,bg="#363636",fg='white',border=0)
                   urlt.tag_configure("center", justify='center')
                 
                   urlt.insert("1.0",link)
                   urlt.tag_add("center", "1.0", "end")
                   urlt.place(relx=0.291,rely=0.389,height=35,width=367)
                   note=tkinter.Label(notwin,text="Note: Please enter the url in the browser and follow the steps given below",bg="#363636",fg='white',border=0)
                   note.place(relx=0.052,rely=0.415,height=23,width=438)   
                   copyb=tkinter.Button(canvas1,width=32,height=32,bg='#363636',command=clipboardc(flink))
                   copyb.place(relx=0.925,rely=0.079)
                   photo_location = os.path.join("C:/Users/Venkat Krishna/Google Drive/Object Tracking/tensorflow_object_counting_api/icons/copy2.png")
                   global _img0
                   _img0 = tkinter.PhotoImage(file=photo_location)
                   copyb.configure(image=_img0)

                   import qrcode
                   img = qrcode.make(flink)
                   print(type(img))
                   print(img.size)
                   img.save('QR/qrcode.png')
                   qrb=tkinter.Button(notwin,bg='#363636',command=qrwindow())
                   qrb.place(relx=0.905,rely=0.179,width=0,height=0)

                   
                  
                   file2.close()
            file1.close()
            

    def new_reg():
            import subprocess
            import os
           
            def subprocess_cmd(command):
                process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
                proc_stdout = process.communicate()[0].strip()
                #print (proc_stdout)

            subprocess_cmd('notify-run register')
            file3=open("C:/Users/Venkat Krishna/.config/notify-run","r")
            contents2=file3.read()
            temp=contents2.replace("[","")
            temp2=temp.replace("]","")
            temp3=temp2.replace("endpoint","url")
            temp4=temp3.replace("{","").replace("}","")
            link=temp4
            clink=link.split(' ')[1]
            flink=clink.replace('"','')
            buttonnew1=tkinter.Button(canvas1,text='New Registration',bg="#363636",state=tkinter.DISABLED)
            buttonnew1.place(relx=0.084,rely=0.183,height=38,width=105)
            urlt=tkinter.Text(canvas1,bg="#363636",fg='white',border=0)
            urlt.tag_configure("center", justify='center')
            urlt.insert("1.0",link)
            urlt.tag_add("center", "1.0", "end")
            urlt.place(relx=0.291,rely=0.389,height=35,width=367)
            note=tkinter.Label(notwin,text="Note: Please enter the url in the browser and follow the steps given below",bg="#363636",fg='white',border=0)
            note.place(relx=0.052,rely=0.415,height=23,width=438)   
            copyb=tkinter.Button(canvas1,width=32,height=32,bg='#363636',command=clipboardc(flink))
            copyb.place(relx=0.925,rely=0.379)
            photo_location = os.path.join("C:/Users/Venkat Krishna/Google Drive/Object Tracking/tensorflow_object_counting_api/icons/copy2.png")
            global _img0
            _img0 = tkinter.PhotoImage(file=photo_location)
            copyb.configure(image=_img0)
            file3.close()
            import qrcode
            img = qrcode.make(flink)
            print(type(img))
            print(img.size)
            img.save('QR/qrcode.png')
            qrb=tkinter.Button(notwin,bg='#363636',command=qrwindow())
            qrb.place(relx=0.905,rely=0.179,width=0,height=0)

            
            
            
    if os.path.isfile("C:/Users/Venkat Krishna/.config/notify-run"):
        canvas1=tkinter.Canvas(notwin,bg="#1f1f1f",bd=2,highlightthickness=1, relief='flat')
        canvas1.place(relx=0.184,rely=0.103,height=180,width=593)
        buttonnew=tkinter.Button(canvas1,text='New Registration',bg="#363636",fg='white',border=0,state=tkinter.DISABLED,relief='flat',bd=1,highlightthickness=1)
        buttonnew.place(relx=0.084,rely=0.183,height=38,width=105)
        buttonnew=tkinter.Button(canvas1,text='Add Device',bg="#363636",fg='white',border=1,command=add_device,relief='flat',bd=1,highlightthickness=1)
        buttonnew.place(relx=0.084,rely=0.556,height=38,width=105)
        
               
    else:
        canvas1=tkinter.Canvas(notwin,bg="#1f1f1f",bd=2,highlightthickness=1, relief='flat')
        canvas1.place(relx=0.184,rely=0.103,height=180,width=593)
        buttonnew=tkinter.Button(canvas1,text='New Registration',bg="#363636",fg='white',border=0,command=new_reg,relief='flat',bd=1,highlightthickness=1)
        buttonnew.place(relx=0.084,rely=0.183,height=38,width=105)
        buttonnew=tkinter.Button(canvas1,text='Add Device',bg="#363636",fg='white',border=1,state=tkinter.DISABLED,relief='flat',bd=1,highlightthickness=1)
        buttonnew.place(relx=0.084,rely=0.556,height=38,width=105)

mlabel=tkinter.Label(window,text="Baby Monitoring System",bd=0,fg="white",bg="#1f1f1f",justify="left")
mlabel.config(font=("sans", 33)) 
mlabel.place(relx=0,rely=0,height=65,width=1229)

Button2 = tkinter.Button(window,text='Start',bg="#4285F4",fg='white',border=0,highlightbackground='white',command=detect)
Button2.place(relx=0.305, rely=0.764, height=48, width=160)

Button1 = tkinter.Button(window,text='Notifications',bg="#4285F4",fg='white',border=0,command=notifywin)
Button1.place(relx=0.561, rely=0.764, height=48, width=160)

labellogo=tkinter.Label(window,image=logoimg)
labellogo.image=logoimg
labellogo.place(relx=0.328,rely=0.162)

labelkey=tkinter.Label(window,bg="#1f1f1f",fg='white',text='Key Mapping:')
labelkey.place(relx=0.8,rely=0.315)

labelkey1=tkinter.Label(window,bg="#1f1f1f",fg='white',text='Q : Stop the Process')
labelkey1.place(relx=0.8,rely=0.355)

labelkey2=tkinter.Label(window,bg="#1f1f1f",fg='white',text='N : Toggle Notifications')
labelkey2.place(relx=0.8,rely=0.395)

labelkey3=tkinter.Label(window,bg="#1f1f1f",fg='white',text='R : Check Connectivity')
labelkey3.place(relx=0.8,rely=0.435)


window.mainloop()


