from dotenv import load_dotenv
import openai
import os
import tkinter as tk
from PIL import Image, ImageTk

load_dotenv()
API_KEY = os.getenv("api_key")
openai.api_key = API_KEY

def generate_text(prompt):
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=1,
    )
    message = response.choices[0].text
    return message



class ChatWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chat Window")
        self.geometry("500x700")
        self.configure(bg='#282828')

        self.chat_log = tk.Text(self, bg='#282828', fg='white', font=("Consolas", 12), wrap="word")
        self.chat_log.pack(expand=True, fill="both")

        self.input_frame = tk.Frame(self, bg='#282828')
        self.input_frame.pack(fill="x")

        self.entry = tk.Entry(self.input_frame, bg='black', fg='white',width = 45, font = ("Consolas", 12))
        self.entry.pack(side = "left",padx=5)
        self.entry.bind('<Return>', self.send_message)
        self.entry.focus()

        self.icon = Image.open("image/send.png")
        self.icon_resize = self.icon.resize((25,30))
        self.arrow_icon = ImageTk.PhotoImage(self.icon_resize)

        self.send_button = tk.Button(self.input_frame, image=self.arrow_icon, command=self.send_message, bg='#282828', fg='white', font=("Consolas", 12))
        self.send_button.pack(side = "right",padx=5)
        
    def send_message(self, event=None):
        message = self.entry.get()
        if message.strip():
            response = generate_text(message)
            self.chat_log.insert("end", f"You: {message}\n")
            self.chat_log.insert("end", f"ChatGPT: {response}\n")
            self.entry.delete(0, "end")
        else:
            self.entry.delete(0, "end")
        
        
        
if __name__ == "__main__":
    chat_window = ChatWindow()
    chat_window.mainloop()





