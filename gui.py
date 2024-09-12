import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import subprocess

def start_scraping():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Input Error", "URL cannot be empty")
        return
    
    csv_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                           filetypes=[("CSV files", "*.csv")])
    if not csv_path:
        return
    
    try:
        subprocess.run(['python', 'scraper.py', url, csv_path], check=True)
        messagebox.showinfo("Success", f"Data successfully saved to {csv_path}")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "An error occurred during scraping")

# Set up the GUI
root = tk.Tk()
root.title("Product Scraper")

tk.Label(root, text="Enter URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

tk.Button(root, text="Start Scraping", command=start_scraping).pack(pady=20)

root.mainloop()
