from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

#root = Tk()
root = customtkinter.CTk()

root.title('PE Network Sniffer')
root.geometry('700x300')


def start_sniffing():
	my_text.insert('end', "starting to sniff the network\n")


my_text = customtkinter.CTkTextbox(root,
	width=600,
	height=200,
	corner_radius=15,
	border_width=5,
	border_color="#003660",
	border_spacing=2,
	fg_color="silver",
	text_color="black",
	font=("Helvetica", 18),
	wrap="word", # Char default, word, none
	activate_scrollbars = True,
	scrollbar_button_color="black",
	scrollbar_button_hover_color="#003660",

	)
my_text.pack(pady=20)


my_frame = customtkinter.CTkFrame(root)
my_frame.pack(pady=10)

sniff_button = customtkinter.CTkButton(my_frame, text="Start Sniffing", command=start_sniffing)


sniff_button.grid(row=0, column=0)


root.mainloop()