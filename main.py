from tkinter import *
import pyttsx3
import difflib


class AsistenteVirtual:
    def __init__(self):
        self.responses = {
           
    "que es el deporte": "El deporte es una actividad física que se realiza de manera competitiva o recreativa, siguiendo un conjunto de reglas.",
    "cual es el deporte mas famoso": "El deporte más famoso del mundo es el fútbol.",
    "que es el futbol": "El fútbol es un deporte en el que dos equipos intentan marcar goles al introducir una pelota en la portería del equipo contrario.",
    "que es basketball": "El baloncesto es un deporte en el que dos equipos intentan anotar puntos lanzando una pelota a través de un aro elevado.",
    "porque es bueno hacer deporte": "Hacer deporte es bueno porque mejora la salud física, aumenta la energía, reduce el estrés y promueve la socialización.",
    "que es el futbol americano": "El fútbol americano es un deporte de equipo en el que dos equipos intentan avanzar con un balón ovalado hacia la zona de anotación del oponente.",
    "es malo si no hago deporte": "No hacer deporte puede tener efectos negativos en la salud física y mental, como aumento de peso y estrés.",
    "como podria empezar": "Puedes empezar haciendo caminatas, uniéndote a una clase de ejercicio o practicando un deporte que te guste.",
    "cuales son los beneficios del deporte": "Los beneficios del deporte incluyen una mejor salud cardiovascular, aumento de la fuerza muscular y mejor salud mental.",
    "que son los juegos olimpicos": "Los Juegos Olímpicos son un evento deportivo internacional que reúne a atletas de todo el mundo en diversas disciplinas.",
    "que es el entrenamiento de resistencia": "El entrenamiento de resistencia es una forma de ejercicio que utiliza la resistencia para mejorar la fuerza y la resistencia muscular.",
    "cual es la importancia del trabajo en equipo en el deporte": "El trabajo en equipo es crucial en muchos deportes, ya que fomenta la cooperación, la comunicación y la estrategia entre los jugadores."



        }
        self.engine = pyttsx3.init()
        self.set_voice()

    def set_voice(self, voice_name="spanish-latin-am"):
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if voice_name in voice.id:
                self.engine.setProperty('voice', voice.id)
                break
    def get_response(self, user_input):
        user_input = user_input.lower()  # Convertir a minúsculas
        user_input = user_input.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú",
                                                                                                                "u").replace(
            "ñ", "n")

        if user_input in self.responses:
            return self.responses[user_input]

        closest_matches = difflib.get_close_matches(user_input, self.responses.keys(), n=1, cutoff=0.5)
        if closest_matches:
            return self.responses[closest_matches[0]]
        else:
            return "No tengo una respuesta exacta para eso, pero estoy aquí para ayudar en lo que pueda."

    def speak_response(self, response):
        self.engine.say(response)
        self.engine.runAndWait()










def on_focus_in(event):
    if data.get("1.0", "end-1c") == "Escribe aquí...":
        data.delete("1.0", END)
        data.config(fg="#6D1A12")
def on_focus_out(event):
    if data.get("1.0", "end-1c") == "":
        data.insert("1.0", "Escribe aquí...")
        data.config(fg="grey")
def get_data(data):
    print(data.get("1.0", END))

window = Tk()
engine = pyttsx3.init()
rate = engine.getProperty("rate")
engine.setProperty("rate",rate-95)



window.geometry("500x650")

canva = Canvas(window, width=500, height=700)
canva.create_text(90, 30, text="Asistente Virtual", font=("Arial", 20, "bold"), anchor="w")
canva.pack()

chat_image = PhotoImage(file="chatbot_image.png")
canva.create_image(50, 30, image=chat_image)

data = Text(fg="grey", font=("Arial", 20, "bold"), width=33, height=3)
data.insert("1.0", "Escribe aquí...")
data.bind("<FocusIn>", on_focus_in)
data.bind("<FocusOut>", on_focus_out)
data.place(x=0, y=550)


button = Button(text="Enviar", font=("Arial", 15, "bold"), highlightthickness=0,command=lambda: get_data(data))
button.place(x=422, y=610)












window.mainloop()
