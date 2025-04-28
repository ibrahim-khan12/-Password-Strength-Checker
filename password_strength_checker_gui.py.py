"""
Password Strength Checker - GUI Version
Name : Muhammad Ibrahim
Description: A Python Tkinter application to evaluate password strength and provide improvement suggestions.
"""





import re
import tkinter as tk
from tkinter import messagebox

def check_password_strength(password: str) -> tuple[str, list[str]]:
    """
    Evaluate the strength of a given password and suggest improvements.
    """
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters (A-Z).")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters (a-z).")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Include numeric digits (0-9).")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Include special characters (!@#$%^&* etc.).")

    if score >= 4:
        return "Strong", []
    elif score == 3:
        return "Moderate", suggestions
    else:
        return "Weak", suggestions

def evaluate_password():
    """
    Called when the user clicks the "Check Strength" button.
    """
    password = entry_password.get().strip()

    if not password:
        messagebox.showwarning("Warning", "Password cannot be empty.")
        return

    strength, suggestions = check_password_strength(password)
    result_var.set(f"Password Strength: {strength}")

    if suggestions:
        suggestions_text = "\n".join(f"- {s}" for s in suggestions)
        suggestion_var.set(f"Suggestions:\n{suggestions_text}")
    else:
        suggestion_var.set("")

def toggle_password_visibility():
    """
    Toggle the visibility of the password input.
    """
    if entry_password.cget('show') == '':
        entry_password.config(show='*')
        button_toggle.config(text="Show Password")
    else:
        entry_password.config(show='')
        button_toggle.config(text="Hide Password")

# --- GUI Setup ---
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("450x350")
root.resizable(False, False)

# Styling
root.configure(bg="#e6f0fa")

# Title
label_title = tk.Label(root, text="🔐 Password Strength Checker", font=("Helvetica", 18, "bold"), bg="#e6f0fa", fg="#2e4053")
label_title.pack(pady=15)

# Password Entry Frame
frame_entry = tk.Frame(root, bg="#e6f0fa")
frame_entry.pack(pady=5)

entry_password = tk.Entry(frame_entry, show="*", font=("Helvetica", 14), width=25)
entry_password.pack(side="left", padx=5)

button_toggle = tk.Button(frame_entry, text="Show Password", command=toggle_password_visibility, font=("Helvetica", 10), bg="#5dade2", fg="white")
button_toggle.pack(side="left", padx=5)

# Check Button
button_check = tk.Button(root, text="Check Strength", command=evaluate_password, font=("Helvetica", 13, "bold"), bg="#28b463", fg="white", padx=10, pady=5)
button_check.pack(pady=15)

# Result
result_var = tk.StringVar()
label_result = tk.Label(root, textvariable=result_var, font=("Helvetica", 14, "bold"), bg="#e6f0fa", fg="#154360")
label_result.pack(pady=5)

# Suggestions
suggestion_var = tk.StringVar()
label_suggestion = tk.Label(root, textvariable=suggestion_var, font=("Helvetica", 11), bg="#e6f0fa", justify="left")
label_suggestion.pack(pady=5)

# Run the app
root.mainloop()
