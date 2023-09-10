
from tkinter import * 					# imports the Tkinter lib
root = Tk()								# create the root object
root.wm_title("Welcome to AIOITS")		# sets title of the window
root.configure(bg="#00A0F3")			# change the background color 
root.geometry("1280x800")
#root.attributes("-fullscreen", True) 	# set to fullscreen

#update the text in the label_1
def saldo():
	label_1 ["text"] = "" 
	label_2 ["text"] = ""
	label_3 ["text"] = "Selamat Datang"
	label_4 ["text"] = "TIARA ASA"
	label_5 ["text"] = "Saldo"
	label_6 ["text"] = "Rp128.122,45" 		
	label_7 ["text"] = "Sisa Subsidi"
	label_8 ["text"] = "23 Liter"
	btnkonifr = Button(root, text="Honda Vario 125 \n L 1150 CC",font="Poppins 20", command = konfirmasi )
	btnkonifr.place(relx = 0.80,
                   rely = 0.45,
                   anchor = 'sw')
	btnkonifr = Button(root, text="Honda Supra GTR 150 \n L 1490 CC",font="Poppins 20", command = konfirmasi )
	btnkonifr.place(relx = 0.745,
                   rely = 0.72,
                   anchor = 'sw')
#def jenispengisian():
#	label_1.config(text="JENIS PENGISIAN") 
#	label_1.place(relx = 0.5,
#                   rely = 0.14,
#                   anchor = 'center')
#	btnkonifr.config ( text="SUBSIDI",font="Poppins 20 bold", command = jenispengisian )
#	btnkonifr.place(relx = 0.80,
#                   rely = 0.45,
#                   anchor = 'sw')
#	btnkonifr.config ( text="NON-SUBSIDI",font="Poppins 20 bold", command = jenispengisian )
#	btnkonifr.place(relx = 0.745,
#                   rely = 0.72,
#                   anchor = 'sw')
def konfirmasi():
	label_1.config(text="KONFIRMASI") 
	label_1.place(relx = 0.5,
                   rely = 0.14,
                   anchor = 'center')
	#label_2 ["text"] = "Kendaraan"
	label_2.config(text="Kendaraan", font="Poppins 18",
			fg="#FFFFFF",
			bg="#4895EF")
	label_2.place(relx = 0.02,
                   rely = 0.34,
                   anchor = 'sw')
	#label_3 ["text"] = "Honda Vario 125 \n L 1150 CC"
	label_3.config(text="Honda Vario 125 \n L 1150 CC", font="Poppins 21 bold",
			fg="#FFFFFF",
			bg="#4895EF")
	label_3.place(relx = 0.2,
                   rely = 0.37,
                   anchor = 'sw')
	
	label_4.config(text="Jenis BBM", font="Poppins 18",
			fg="#FFFFFF",
			bg="#4895EF")
	label_4.place(relx = 0.023,
                   rely = 0.44,
                   anchor = 'sw')
	label_5.config(text="PERTALITE", font="Poppins 21 bold",
			fg="#FFFFFF",
			bg="#4895EF")
	label_5.place(relx = 0.2,
                   rely = 0.44,
                   anchor = 'sw')
	
	label_6.config(text="Skema", font="Poppins 18",
			fg="#FFFFFF",
			bg="#4895EF")
	label_6.place(relx = 0.023,
                   rely = 0.51,
                   anchor = 'sw')
	label_7.config(text="SUBSIDI", font="Poppins 21 bold",
			fg="#FFFFFF",
			bg="#4895EF")
	label_7.place(relx = 0.2,
                   rely = 0.51,
                   anchor = 'sw')
	
	label_8.config(text="Harga/Liter", font="Poppins 18",
			fg="#FFFFFF",
			bg="#4895EF")
	label_8.place(relx = 0.023,
                   rely = 0.58,
                   anchor = 'sw')
	label_9.config(text="Rp10.000/Liter", font="Poppins 21 bold",
			fg="#FFFFFF",
			bg="#4895EF")
	label_9.place(relx = 0.2,
                   rely = 0.58,
                   anchor = 'sw')
	
	label_10.config(text="Jumlah", font="Poppins 18",
			fg="#FFFFFF",
			bg="#4895EF")
	label_10.place(relx = 0.023,
                   rely = 0.65,
                   anchor = 'sw')
	label_11.config(text="5 Liter", font="Poppins 21 bold",
			fg="#FFFFFF",
			bg="#4895EF")
	label_11.place(relx = 0.2,
                   rely = 0.65,
                   anchor = 'sw')
	
	label_12.config(text="Total", font="Poppins 18",
			fg="#FFFFFF",
			bg="#4895EF")
	label_12.place(relx = 0.023,
                   rely = 0.72,
                   anchor = 'sw')
	label_13.config(text="Rp50.000", font="Poppins 21 bold",
			fg="#FFFFFF",
			bg="#4895EF")
	label_13.place(relx = 0.2,
                   rely = 0.72,
                   anchor = 'sw')
	btnkonifr = Button(root, text="Tempel kartu untuk konfirmasi",font="Poppins 18", command = jenispengisian )
	btnkonifr.place(relx = 0.5,
                   rely = 0.8,
                   anchor = 'center')
	btn.destroy()
	btnkonifr.destroy()


	


# we can exit when we press the escape key
def end_fullscreen(event):
	root.attributes("-fullscreen", False)

name = StringVar() 						#store a string from the Entry widget input

label_1 = Label(root, text="Silahkan", font="Poppins 40 bold",
			fg="#FFFFFF",
			bg="#4895EF")
label_2 = Label(root, text="TAP DISINI", font="Poppins 25",
			fg="#FFFFFF",
			bg="#4895EF")
label_3 = Label(root, text="", font="Poppins 32",
			fg="#FFFFFF",
			bg="#4895EF")
label_4 = Label(root, text="", font="Poppins 29 bold",
			fg="#FFFFFF",
			bg="#4895EF")
label_5 = Label(root, text="", font="Poppins 25",
			fg="#FFFFFF",
			bg="#4895EF")
label_6 = Label(root, text="", font="Poppins 27 bold",
			fg="#FFFFFF",
			bg="#4895EF")
label_7 = Label(root, text="", font="Poppins 25",
			fg="#FFFFFF",
			bg="#4895EF")
label_8 = Label(root, text="", font="Poppins 27 bold",
			fg="#FFFFFF",
			bg="#4895EF")
label_9 = Label(root, text="", font="Poppins 27 bold",
			fg="#FFFFFF",
			bg="#4895EF")
label_10 = Label(root, text="", font="Poppins 27 bold",
			fg="#FFFFFF",
			bg="#4895EF")
label_11 = Label(root, text="", font="Poppins 27 bold",
			fg="#FFFFFF",
			bg="#4895EF")
label_12 = Label(root, text="", font="Poppins 27 bold",
			fg="#FFFFFF",
			bg="#4895EF")
label_13 = Label(root, text="", font="Poppins 27 bold",
			fg="#FFFFFF",
			bg="#4895EF")
#entry_1 = Entry(root, textvariable = name)

btn = Button(root, text="Selanjutnya", activeforeground = "white",activebackground = "blue",font="Poppins 20", command = saldo ) #Add a button inside the window
btn.pack()


label_1.place(relx = 0.5,
                   rely = 0.4,
                   anchor = 'center')
label_2.place(relx = 0.5,
                   rely = 0.5,
                   anchor = 'center')
btn.place(relx = 0.85,
                   rely = 0.95,
                   anchor = 'sw')
label_3.place(relx = 0.023,
                   rely = 0.2,
                   anchor = 'sw')
label_4.place(relx = 0.023,
                   rely = 0.265,
                   anchor = 'sw')
label_5.place(relx = 0.023,
                   rely = 0.4,
                   anchor = 'sw')
label_6.place(relx = 0.023,
                   rely = 0.47,
                   anchor = 'sw')
label_7.place(relx = 0.023,
                   rely = 0.637,
                   anchor = 'sw')
label_8.place(relx = 0.023,
                   rely = 0.692,
                   anchor = 'sw')

root.bind("<Escape>", end_fullscreen)
root.mainloop()				# starts the GUI loop