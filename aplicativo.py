import tkinter as tk
import chatbot as cb

app = tk.Tk()

app.title("Aplicativo")
app.geometry("500x500")

try:
    texto = open("conversa.txt", "r", encoding="utf-8").read()
except FileNotFoundError:
    texto = ""

conversa = tk.Text(app, height=20, width=50)
conversa.grid(column=0, row=0, sticky=tk.NSEW)
if texto:
    conversa.insert(tk.END, texto)
conversa.configure(state=tk.DISABLED)

inferior = tk.Label(app)
inferior.grid(column=0, row=1, sticky=tk.EW)

entrada = tk.Entry(inferior)
entrada.grid(column=0, row=0, sticky=tk.EW)


def executar():
    global texto
    prompt = entrada.get().strip()
    conversa.configure(state=tk.NORMAL)
    conversa.insert(tk.END, "usuario: " + prompt + "\n")
    conversa.configure(state=tk.DISABLED)
    prompt_completo = cb.contexto + texto + "assistente:"
    resposta = cb.executar(prompt_completo).strip()
    texto += "usuario: " + prompt + "\n"
    texto += "assistente: " + resposta + "\n"
    conversa.configure(state=tk.NORMAL)
    conversa.insert(tk.END, "assistente: " + resposta + "\n")
    conversa.configure(state=tk.DISABLED)
    entrada.delete(0, tk.END)
    open("conversa.txt", "w", encoding="utf-8").write(texto)


enviar = tk.Button(inferior, text="Enviar", command=executar)
enviar.grid(column=1, row=0)

app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)
inferior.grid_columnconfigure(0, weight=1)

app.mainloop()
