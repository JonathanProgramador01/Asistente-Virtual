from tkinter import *
import pyttsx3
from difflib import get_close_matches





class AsistenteVirtual:

    def __init__(self):
        self.engine = pyttsx3.init()
        rate = self.engine.getProperty("rate")
        self.engine.setProperty("rate",rate-64)
        self.responses = {
            "saludame mi nombre es": "Holaa, ",
            "que es el deporte": "El deporte es una actividad física que se realiza de manera competitiva o recreativa, siguiendo un conjunto de reglas.",
            "cual es el deporte mas famoso": "El deporte más famoso del mundo es el fútbol.",
            "que es futbol": "El fútbol es un deporte en el que dos equipos intentan marcar goles al introducir una pelota en la portería del equipo contrario.",
            "que es basketball": "El baloncesto es un deporte en el que dos equipos intentan anotar puntos lanzando una pelota a través de un aro elevado.",
            "porque es bueno hacer deporte": "Hacer deporte es bueno porque mejora la salud física, aumenta la energía, reduce el estrés y promueve la socialización.",
            "que es futbol americano": "El fútbol americano es un deporte de equipo en el que dos equipos intentan avanzar con un balón ovalado hacia la zona de anotación del oponente.",
            "es malo si no hago deporte": "No hacer deporte puede tener efectos negativos en la salud física y mental, como aumento de peso y estrés.",
            "como podria empezar": "Puedes empezar haciendo caminatas, uniéndote a una clase de ejercicio o practicando un deporte que te guste.",
            "cuales son los beneficios del deporte": "Los beneficios del deporte incluyen una mejor salud cardiovascular, aumento de la fuerza muscular y mejor salud mental.",
            "que son los juegos olimpicos": "Los Juegos Olímpicos son un evento deportivo internacional que reúne a atletas de todo el mundo en diversas disciplinas.",
            "que es el entrenamiento de resistencia": "El entrenamiento de resistencia es una forma de ejercicio que utiliza la resistencia para mejorar la fuerza y la resistencia muscular.",
            "cual es la importancia del trabajo en equipo en el deporte": "El trabajo en equipo es crucial en muchos deportes, ya que fomenta la cooperación, la comunicación y la estrategia entre los jugadores.",
            "que es el yoga": "El yoga es una práctica que combina posturas físicas, respiración controlada y meditación para mejorar la salud física y mental.",
            "que es el tenis": "El tenis es un deporte en el que dos jugadores o dos equipos intentan golpear una pelota con una raqueta para que pase por encima de la red y aterrice en el campo del oponente.",
            "que es el atletismo": "El atletismo es un conjunto de deportes que incluyen carreras, saltos y lanzamientos, y se centra en las habilidades físicas fundamentales.",
            "que es la natacion": "La natación es un deporte en el que los atletas se desplazan en el agua usando técnicas como el estilo libre, mariposa, espalda y braza.",
            "que es el box": "El boxeo es un deporte de combate en el que dos participantes se enfrentan utilizando únicamente sus puños, con guantes, para golpear al oponente mientras intentan esquivar los golpes del contrario. El objetivo es ganar por puntos o por nocaut."
        }


    def talk(self,text):

        self.engine.say(",  "+text)
        self.engine.runAndWait()

    def matches(self,text):
        text = text.lower()
        text = (text.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").
        replace("ú","u").replace("ñ", "n"))

        if text in self.responses:
            return self.responses[text]


        best_match = get_close_matches(text,self.responses.keys())
        if best_match:
            return  self.responses[best_match[0]]
        else:
            return "Lo siento pero no cuento con esa informacion"
class Gui:
    def __init__(self, pantalla):

        self.asistentevirtual = AsistenteVirtual()
        self.window = pantalla
        self.window.title("Asistente Virtual De Deportes")
        self.window.geometry("720x650")
        self.canva = Canvas(self.window,highlightthickness=0, width=720, height=650)
        self.textoid = None
        self.entrada()
        self.crear_botones()


    def crear_fondo(self):
        ##Despues pongo esta imagen de fondo
        self.canva.create_text(360, 50, text="Asistente Virtual", font=("Elephant", 30, "bold"),
                          fill="#C7C3B4")  # Esto es para poner mi texto
        self.canva.pack()
        self.response = Text(fg="#C7C3B4", font=("Arial", 15, "bold"), width=58, height=17, bg="#0F0F0C")
        self.response.place(x=40, y=100)

    def procesador(self):
        text = self.data.get("1.0", END).strip()

        if text== "Escribe aquí..." or text == "":
            return
        response = self.asistentevirtual.matches(text)

        if response == "Holaa, ":
            temp =" ".join(text.split()[4:])
            response += temp

        self.put_text(response, text)
        self.window.update_idletasks()
        self.asistentevirtual.talk(response)


        self.data.delete("1.0", END)







    def put_text(self,asistente,ususario):

        self.response.tag_configure("padding", lmargin1=30, lmargin2=30, rmargin=30)
        text = f"Usuario: {ususario}\n"
        text2 = f"Asistente: {asistente}\n\n\n"
        self.response.insert(END, text)
        self.response.insert(END, text2)
        self.response.tag_add("padding", "1.0", "end")


        # Boton para saludar mi imagen
    def crear_botones(self):

        self.button_enviar = Button(text="Enviar", fg="#C7C3B4", font=("Arial", 15, "bold"), highlightthickness=0,
                               bg="#0F0F0C", width=9,command=self.procesador)
        self.button_enviar.place(y=605, x=600)
    def on_focus_in(self,event):
        if self.data.get("1.0", "end-1c") == "Escribe aquí...":
            self.data.delete("1.0", END)
            self.data.config(fg="#C7C3B4")
    def on_focus_out(self,event):
        if self.data.get("1.0", "end-1c") == "":
            self.data.insert("1.0", "Escribe aquí...")
            self.data.config(fg="#C7C3B4")
    def entrada(self):
        self.data = Text(fg="#C7C3B4", font=("Arial", 15, "bold"), width=66, height=5,bg="#0F0F0C")
        self.data.insert("1.0", "Escribe aquí...")
        self.data.bind("<FocusIn>", self.on_focus_in)
        self.data.bind("<FocusOut>", self.on_focus_out)
        self.data.place(x=0, y=550)








window = Tk()
gui = Gui(window)
background_image = PhotoImage(file="./image.png")
gui.canva.create_image(360, 325, image=background_image)
gui.crear_fondo()

window.mainloop()
