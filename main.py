import os
from tkinter import *
import tkinter
import customtkinter
from feature_extraction import pe_extract

customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()
root.title('PE malware classifier')
root.geometry('1000x750')


def start():
    global file_path
    if 'file_path' not in globals():
        my_text.insert('end', "Please specify the file path first\n")
    elif file_path == '':
        my_text.insert('end', "File path is empty. Please specify a valid file path\n")
    elif not os.path.exists(file_path):
        my_text.insert('end', f"File path '{file_path}' does not exist\n")
    else:
        my_text.insert('end', "Starting the classification...\n")
        try:
            result = pe_extract.pe_extract(file_path)
            my_text.insert('end', f"{file_path} is {'malicious' if result.res else 'legitimate'}!\n")
        except Exception as e:
            error_message = f"An error occurred: {str(e)}\n"
            my_text.insert('end', error_message)

def clear_text():
    my_text.delete(1.0, 'end')

def input():
    global file_path
    dialog = customtkinter.CTkInputDialog(text="Please enter the path to the PE file", title="File Path window",
        fg_color="white",
        button_fg_color="#2a97d4",
        button_hover_color="#083b5f",
        button_text_color="white",
        entry_fg_color="#2a97d4",
        entry_border_color="#083b5f",
        entry_text_color="black"
        )
    
    file_path = dialog.get_input()
    if file_path == None:
        file_path = ''
    if file_path == '':
        my_text.insert('end', f"Empty path is not a valid path.\n")
    elif not os.path.exists(file_path):
        my_text.insert('end', f"{file_path} is not a valid path.\n")
        file_path = ''
    else:
        my_text.insert('end', "got file path: %s\n" %(file_path))


top_bar = customtkinter.CTkFrame(root, corner_radius=0) 
top_bar.grid(row=0, column=0, columnspan=2, sticky="nsew")
top_bar.configure(height= 70, fg_color = "#083b5f")
top_bar.pack_propagate(0)

name_font = customtkinter.CTkFont(family="Kristen ITC", size=35, 
    weight="bold", slant="italic", underline=False, overstrike=False)

bg_image = PhotoImage(file="image14-1.png")

app_name_label = customtkinter.CTkLabel(master=top_bar, text="PE Malware Classifier", font=name_font)
app_name_label.pack(side="left")
app_name_label.configure(padx = 15, text_color = "#217B7E")

def show_help():
    my_text.insert('end', "Help: This is a classifier for malicious PE files\nTo run please specify the file path first and then press start\n")
    


help_button = customtkinter.CTkButton(master=top_bar, text="Help", command=show_help)
help_button.pack(side="right", padx=10)
help_button.configure(fg_color = "#217B7E", font= ("Kristen ITC", 20))

root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

my_text = customtkinter.CTkTextbox(root,
    width=600,
    height=200,
    corner_radius=15,
    border_width=5,
    border_color="#4cb1ff",
    border_spacing=2,
    fg_color="white", 
    text_color="#4C4C4C", 
    font=("Helvetica", 18),
    wrap="word",  # Char default, word, none
    activate_scrollbars=True,
    scrollbar_button_color="black",
    scrollbar_button_hover_color="#003660"
)

my_text.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

my_frame = customtkinter.CTkFrame(root)
my_frame.grid(row=1, column=1, padx=10, pady=20, sticky="nsew")

sniff_button = customtkinter.CTkButton(my_frame, text="Start", command=start)
sniff_button.grid(row=0, column=0, padx=10, pady=10)
sniff_button.configure(fg_color = "#2a97d4", font= ("aria", 17))

clear_button = customtkinter.CTkButton(my_frame, text="Clear Text", command=clear_text)
clear_button.grid(row=1, column=0, padx=10, pady=10)
clear_button.configure(fg_color = "#2a97d4", font= ("aria", 17))

enter_FilePath_button = customtkinter.CTkButton(my_frame, text="Enter File Path", command=input)
enter_FilePath_button.grid(row=2, column=0, padx=10, pady=10)
enter_FilePath_button.configure(fg_color = "#2a97d4", font= ("aria", 17))

root.mainloop()
