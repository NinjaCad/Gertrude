import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import time
import random
def trigger_slap_event():
    # 1. Setup the main popup
    root = tk.Toplevel()
    root.title("SLAP!")
    root.geometry("400x500")
    root.configure(bg='white')
    img_url = "https://static.vecteezy.com/system/resources/previews/010/562/664/original/sticker-of-a-cartoon-slap-symbol-vector.jpg"
    response = requests.get(img_url)
    img_data = Image.open(BytesIO(response.content))
    img_data = img_data.resize((300, 300), Image.Resampling.LANCZOS)
    slap_img = ImageTk.PhotoImage(img_data)
    label = tk.Label(root, image=slap_img, bg='white')
    label.image = slap_img 
    label.pack(pady=20)
    status_text = tk.StringVar(value="SLAP DETECTED!")
    status_label = tk.Label(root, textvariable=status_text, font=("Arial", 18, "bold"), bg='white', fg='red')
    status_label.pack()
    def shake_window():
        orig_x = root.winfo_x()
        orig_y = root.winfo_y()
        for _ in range(10):
            root.geometry(f"+{orig_x + random.randint(-10, 10)}+{orig_y + random.randint(-10, 10)}")
            root.update()
            time.sleep(0.05)
        root.geometry(f"+{orig_x}+{orig_y}")
    def shuffle_sequence():
        shake_window()
        time.sleep(0.5)
        cards = ["|", "/", "-", "\\"]
        for i in range(12):
            status_text.set(f"Reshuffling Deck {cards[i % 4]}")
            root.update()
            time.sleep(0.15)
        status_text.set("READY!")
        root.update()
        time.sleep(1)
        root.destroy()
    root.after(100, shuffle_sequence)
    root.mainloop()
if __name__ == "__main__":
    main = tk.Tk()
    main.geometry("200x100")
    btn = tk.Button(main, text="Simulate Slap", command=trigger_slap_event)
    btn.pack(expand=True)
    main.mainloop()