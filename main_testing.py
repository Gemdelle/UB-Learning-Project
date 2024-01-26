import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import pygame
import sys


class ConsoleRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, message):
        self.text_widget.insert(tk.END, message)
        self.text_widget.see(tk.END)


def run_code():
    code = code_text.get("1.0", tk.END)
    try:
        # Redirect sys.stdout to the text widget
        sys.stdout = ConsoleRedirector(output_text)

        # Execute the code
        exec(code)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{str(e)}")
    finally:
        # Reset sys.stdout to the original value
        sys.stdout = sys.__stdout__


# Initialize Pygame
pygame.init()

# Set up Pygame window
pygame.display.set_caption("Python Code Editor")
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)

# Create the main Tkinter window
root = tk.Tk()
root.title("Python Code Editor")

# Create a scrolled text area for code input
code_text = scrolledtext.ScrolledText(root, width=50, height=20)
code_text.pack(padx=10, pady=10)

# Create a scrolled text area for console output
output_text = scrolledtext.ScrolledText(root, width=50, height=10)
output_text.pack(padx=10, pady=10)

# Create a button to run the code
run_button = tk.Button(root, text="Run Code", command=run_code)
run_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()

# Quit Pygame
pygame.quit()