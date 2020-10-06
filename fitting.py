from tkinter import filedialog
import tkinter as tkinter
import matplotlib.pyplot as plt
import numpy as np
from PIL import ImageTk, Image
import os


def plot_experimental_and_fitted(depth, depth_loading, load_experimental, load_fitted,filename):
	plt.figure()
	depth_in_nanometers = [element * 1E9 for element in depth]
	load_experimental_in_milinewtons = [element * 1E3 for element in load_experimental]
	depth_loading_in_nanometers = [element * 1E9 for element in depth_loading]
	load_fitted_in_milinewtons = [element * 1E3 for element in load_fitted]
	plt.plot(depth_in_nanometers, load_experimental_in_milinewtons, 'o', color = "blue", label = "experimental data")
	plt.plot(depth_loading_in_nanometers, load_fitted_in_milinewtons, '-', color = "red", linewidth=2.2, label = "fitted data")
	plt.ylabel("Load (mN)")
	plt.xlabel("Depth (nm)")
	plt.title(str(filename.split("/")[-1]) + "\n" + "R = " + str(np.round(R*1E9,2)) + ' nm', size = 10 )
	plt.legend()
	plt.savefig(str(filename.split(".txt")[0])+"curve.png")
	plt.close()



def fitting_R(depth,depth_loading, load_experimental, Er, filename, hmax):
	global R, load_fitted
	load_fitted = []
	R = 9/16 *((max(load_experimental)**2)/((Er**2) *(hmax **3))) #Here I put the equation 2
	for a in range (0, len(depth_loading)):
		load = (4/3)*Er*np.sqrt(R*(depth_loading[a]**3)) #Here I put the equation 1
		load_fitted.append(load)
	return load_fitted, R


def Get_Measurement_data(initial_data_line,final_data_line, filename):
	global depth, load_experimental
	depth = []
	load_experimental = []
	file2 = open(filename, 'r+', encoding = "windows-1252")
	line_number2 = 0 
	for line2 in file2:
		line_number2 +=1
		if line_number2 in range(initial_data_line, final_data_line+1):
			depth.append(float((line2.split())[1].replace(',', '.'))*(10**(-9))) #nanometers to meters, saving as SI unit
			load_experimental.append(float((line2.split())[2].replace(',', '.'))*(10**(-3)))#milinewtons to newtons, saving as SI unit 
	file2.close()
	return depth, load_experimental
	

   


def Get_Er_hmax_and_Measurement_lines(filename):
	global initial_data_line, final_data_line, Er, hmax
	file = open(filename, 'r+', encoding = "windows-1252")
	line_number = 0
	for line in file:
		line_number += 1
		if "Er" in line:
			Er = float((line.split())[1].replace(',', '.'))*(10**(9)) #reduced modullus Oliver-Pharr, gigapascal to Pa, saving as SI unit 
		if "hmax" in line:
			hmax = float((line.split())[1].replace(',', '.'))*(10**(-9)) #from nanometers to meters, saving as SI unit 
		if "Measured values" in line:
			initial_data_line = line_number+4
	final_data_line = line_number
	file.close()
	return initial_data_line, final_data_line, Er, hmax



def Define_adjust_depth_range(depth):
	global depth_loading
	depth_loading = []
	for element in depth:
		if element <= max(depth):
			depth_loading.append(element)
	return depth_loading

def plot_dispersion_and_Mean_R(R_list):
	R_mean = []
	x_mean_axis = []
	for i in range (0, len(R_list)):
		R_mean.append(np.mean(R_list))
		x_mean_axis.append(i)
	plt.plot(R_list ,'o')
	plt.plot(x_mean_axis, R_mean, '-', color = "red")
	plt.title("R dispersion" + " \n "+ "mean  = " + str(np.round(np.mean(R_list),2))+ " nm")
	plt.ylabel("R (nanometers)")
	plt.tick_params(axis = "x", which = "both", bottom = False, top = False, labelbottom=False)
	plt.savefig("dispersion_of_R.png", dpi = 300)
	plt.close()	

def main():

	R_list = []
	print("Analyzing " + str(len(list_of_files))+ " files.")
	for index in range(0, len(list_of_files)):
		filename = list_of_files[index]

		Get_Er_hmax_and_Measurement_lines(filename)
		Get_Measurement_data(initial_data_line,final_data_line, filename)
		Define_adjust_depth_range(depth)
		fitting_R(depth,depth_loading, load_experimental, Er, filename, hmax)
		plot_experimental_and_fitted(depth, depth_loading, load_experimental, load_fitted,filename)
		R_list.append(R*1E9)# nanometers to plot
		print("File number " + str(index+1)+ " already analyzed.")

	plot_dispersion_and_Mean_R(R_list)



def Read_Files():
	global list_of_files, root
	root = tkinter.Tk()
	root.geometry("550x500+300+150")
	root.resizable(width=True, height=True)
	img = ImageTk.PhotoImage(Image.open("pythonimage.png"))
	panel = tkinter.Label(root, image = img)
	panel.pack(side = "bottom", fill = "both", expand = "yes")
	filez = filedialog.askopenfilenames(parent=root,title='Select the text files', filetypes = [("test files", "*.txt")])
	list_of_files = list(filez)
	main()
	root.mainloop()

Read_Files()