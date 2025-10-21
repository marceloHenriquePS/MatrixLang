"""Minimal Tkinter UI for MatrixLang — only constructs the screen elements.

This file intentionally contains only the code that builds the window and its
main widgets (buttons, editor and output panes). All parsing/execution logic
has been removed.

Run: python ui/tk_ui.py
"""
import webbrowser
import tkinter as tk
from tkinter import ttk, messagebox, Toplevel,  scrolledtext

from . import controller

def main():
    root = tk.Tk()
    root.title("MatrixLang IDE")
    root.geometry("900x640")

    # Top frame with buttons (no commands)
    top = ttk.Frame(root, padding=(8, 8))
    top.pack(side=tk.TOP, fill=tk.X)

    run_btn = ttk.Button(top, text="Run")
    help_btn = ttk.Button(top, text="Help")
    run_btn.pack(side=tk.LEFT)
    help_btn.pack(side=tk.LEFT, padx=(8, 0))

    # Main panes: left editor, right output
    paned = ttk.Panedwindow(root, orient=tk.HORIZONTAL)
    paned.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

    # Editor frame
    editor_frame = ttk.Frame(paned)
    editor_label = ttk.Label(editor_frame, text="Code")
    editor_label.pack(anchor=tk.W)
    editor = tk.Text(editor_frame, wrap=tk.NONE)
    editor.pack(fill=tk.BOTH, expand=True)

    # Output frame
    output_frame = ttk.Frame(paned)
    output_label = ttk.Label(output_frame, text="Output")
    output_label.pack(anchor=tk.W)
    # Output should be view-only for the user. Use state='disabled'
    output = tk.Text(output_frame, wrap=tk.WORD, bg='white', state='disabled', takefocus=0)
    output.pack(fill=tk.BOTH, expand=True)

    # Helper to append text to the read-only output widget programmatically.
    def append_output(text: str) -> None:
        output.config(state='normal')
        output.insert(tk.END, text)
        output.see(tk.END)
        output.config(state='disabled')

    # Wire the Run and Help buttons to the controller functions.
    def on_run():
        txt = editor.get('1.0', tk.END)
        # clear previous output
        output.config(state='normal')
        output.delete('1.0', tk.END)
        output.config(state='disabled')
        controller.run_code(txt, append_output)

    def on_help():
        help_text = controller.get_help_text()

        win = Toplevel()
        win.title("MatrixLang Help")
        win.geometry("600x500")

        txt = scrolledtext.ScrolledText(win, wrap=tk.WORD)
        txt.insert(tk.END, help_text)
        txt.config(state=tk.DISABLED)
        txt.pack(fill=tk.BOTH, expand=True)

        btn = tk.Button(win, text="GitHub", command=lambda: webbrowser.open("https://github.com/marceloHenriquePS/MatrixLang.git"))
        btn.pack(pady=5)

    paned.add(editor_frame, weight=3)
    paned.add(output_frame, weight=2)

    run_btn.config(command=on_run)
    help_btn.config(command=on_help)

    root.mainloop()

if __name__ == "__main__":
    main()
