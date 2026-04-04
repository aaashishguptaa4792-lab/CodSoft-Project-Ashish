import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json, os

CONTACT_FILE = "contacts.json"

# Load contacts
def load_contacts():
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, "r") as f:
            return json.load(f)
    return {}

# Save contacts
def save_contacts():
    with open(CONTACT_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

# Add contact
def add_contact():
    name = simpledialog.askstring("Add Contact", "Enter Name:")
    if not name: return
    phone = simpledialog.askstring("Add Contact", "Enter Phone Number:")
    email = simpledialog.askstring("Add Contact", "Enter Email:")
    address = simpledialog.askstring("Add Contact", "Enter Address:")

    contacts[name] = {"phone": phone, "email": email, "address": address}
    save_contacts()
    refresh_list()
    messagebox.showinfo("Success", f"Contact '{name}' added successfully!")

# Refresh list
def refresh_list():
    listbox.delete(0, tk.END)
    for name, details in contacts.items():
        listbox.insert(tk.END, f"{name} - {details['phone']}")

# Search contact
def search_contact():
    query = simpledialog.askstring("Search Contact", "Enter Name or Phone:")
    if not query: return
    results = [f"{n} - {d['phone']}" for n, d in contacts.items()
               if query.lower() in n.lower() or query in d['phone']]
    if results:
        messagebox.showinfo("Search Results", "\n".join(results))
    else:
        messagebox.showwarning("Not Found", "No matching contact found.")

# Update contact
def update_contact():
    name = simpledialog.askstring("Update Contact", "Enter Name to Update:")
    if name in contacts:
        phone = simpledialog.askstring("Update Contact", "Enter New Phone:", initialvalue=contacts[name]["phone"])
        email = simpledialog.askstring("Update Contact", "Enter New Email:", initialvalue=contacts[name]["email"])
        address = simpledialog.askstring("Update Contact", "Enter New Address:", initialvalue=contacts[name]["address"])
        contacts[name] = {"phone": phone, "email": email, "address": address}
        save_contacts()
        refresh_list()
        messagebox.showinfo("Success", f"Contact '{name}' updated successfully!")
    else:
        messagebox.showwarning("Not Found", "Contact not found.")

# Delete contact
def delete_contact():
    name = simpledialog.askstring("Delete Contact", "Enter Name to Delete:")
    if name in contacts:
        if messagebox.askyesno("Confirm Delete", f"Delete '{name}'?"):
            del contacts[name]
            save_contacts()
            refresh_list()
            messagebox.showinfo("Deleted", f"Contact '{name}' deleted successfully!")
    else:
        messagebox.showwarning("Not Found", "Contact not found.")

# Show details
def show_details(event):
    selection = listbox.curselection()
    if selection:
        name = listbox.get(selection[0]).split(" - ")[0]
        d = contacts[name]
        messagebox.showinfo("Contact Details",
                            f"Name: {name}\nPhone: {d['phone']}\nEmail: {d['email']}\nAddress: {d['address']}")

# Main window
root = tk.Tk()
root.title("📒 Modern Contact Book")
root.geometry("550x500")
root.configure(bg="#f0f8ff")

# Apply ttk theme
style = ttk.Style(root)
style.theme_use("clam")

# Custom button style
style.configure("Accent.TButton",
                font=("Segoe UI", 11, "bold"),
                foreground="white",
                background="#0078D7",
                padding=8)
style.map("Accent.TButton",
          background=[("active", "#005A9E")])

contacts = load_contacts()

# Title
title_label = tk.Label(root, text="📒 Contact Book", font=("Segoe UI", 20, "bold"),
                       fg="#005A9E", bg="#f0f8ff")
title_label.pack(pady=15)

btn_frame = ttk.Frame(root)
btn_frame.pack(pady=10)

ttk.Button(btn_frame, text="➕ Add", style="Accent.TButton", command=add_contact).grid(row=0, column=0, padx=8)
ttk.Button(btn_frame, text="🔍 Search", style="Accent.TButton", command=search_contact).grid(row=0, column=1, padx=8)
ttk.Button(btn_frame, text="✏️ Update", style="Accent.TButton", command=update_contact).grid(row=0, column=2, padx=8)
ttk.Button(btn_frame, text="❌ Delete", style="Accent.TButton", command=delete_contact).grid(row=0, column=3, padx=8)

# Contact list
listbox = tk.Listbox(root, width=60, height=15, bg="#ffffff", fg="#333",
                     font=("Segoe UI", 12), selectbackground="#0078D7", selectforeground="white")
listbox.pack(pady=15)
listbox.bind("<Double-1>", show_details)

refresh_list()
root.mainloop()
