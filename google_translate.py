import asyncio
from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def change(text="type", src="English", dest="Urdu"):
    async def async_translate():
        lang_dict = {v.title(): k for k, v in LANGUAGES.items()}
        src_code = lang_dict.get(src.title())
        dest_code = lang_dict.get(dest.title())
        if not src_code or not dest_code:
            return "Invalid language selection"

        translator = Translator()
        translation = await translator.translate(text=text, src=src_code, dest=dest_code)
        return translation.text

    try:
        return asyncio.run(async_translate())
    except Exception as e:
        return f"Translation Error: {str(e)}"

def data():
    s=combo_sor.get()
    d=combo_dest.get()
    mess=sor_txt.get(1.0,END)
    text_get=change(text=mess,src=s,dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,text_get)



root=Tk()
root.title("Language Translator")
root.geometry("520x800")
root.config(bg="Red")
label_txt=Label(root,text="Language Translator",font=("Times New Roman",30,"bold"))
label_txt.place(x=10,y=40,height=50,width=500)
frame=Frame(root).pack(side=BOTTOM)
label_txt=Label(root,text="Source Text",font=("Times New Roman",20),fg="white",bg="Red")
label_txt.place(x=10,y=100,height=50,width=500)
sor_txt = Text(frame,font=("Times New Roman",15),wrap=WORD)
sor_txt.place(x=10,y=150,height=200,width=500)


list_text=list(LANGUAGES.values())
combo_sor=ttk.Combobox(frame,value=list_text)
combo_sor.place(x=10,y=360,height=40,width=150)
combo_sor.set("english")

button_change=Button(frame,text="Translate", relief=RAISED,command=data)
button_change.place(x=170,y=360,height=40,width=180)

combo_dest=ttk.Combobox(frame,value=list_text)
combo_dest.place(x=360,y=360,height=40,width=150)
combo_dest.set("english")

label_txt=Label(root,text="Destination Text",font=("Times New Roman",20),fg="white",bg="Red")
label_txt.place(x=10,y=400,height=50,width=500)
dest_txt = Text(frame,font=("Times New Roman",15),wrap=WORD)
dest_txt.place(x=10,y=450,height=200,width=500)




root.mainloop()