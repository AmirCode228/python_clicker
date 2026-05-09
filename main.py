import tkinter as tk

root = tk.Tk()
root.geometry('300x350')
root.title('Clicker')
root.resizable(False, False)

with open('score.txt', 'r', encoding='utf-8') as file:
    content = int(file.read())

score = content

def on_click():
    global score
    score += 1
    with open('score.txt', 'w', encoding='utf-8') as file:
        content = str(score)
        file.write(content)
    score_label.config(text=f'Score: {score}')
def del_score():
    global score
    score = 0
    with open('score.txt', 'w', encoding='utf-8') as file:
        content = str(score)
        file.write(content)
    score_label.config(text='Score: 0')

score_label = tk.Label(root, text=f'Score: {score}', font=('Arial', 12))
score_label.pack(pady=20)

button = tk.Button(root, text='Click me!', font=('Arial', 12), command=on_click)
button.pack(pady=30)

del_score_btn = tk.Button(root, text='Delete score', font=('Arial', 12), command=del_score)
del_score_btn.pack(pady=20)

root.mainloop()