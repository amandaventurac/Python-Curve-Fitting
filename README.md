# Python
 
 <b>What is this repository for?</b>

It's basically an automated fitting python app.

It works with nanoindentation experimental files, but it can be modified to other needs depending on the data to be fitted.

 <b>About its creation</b>
 
I had to fit a lot of experimental curves, and perfom some statistical analysis with them.
It was always the same process of searching for some values in a text file, and use them into some equation to get a parameter. Then,  I usually have to see how this important parameter changes from one measurement to another. 

 <b>What does this repository comprise?</b>

- fitting.py (the app itself)
- an image used in GUI 
- example text files with experimental data to be fitted

<b>The equation to be fitted:</b>
The main equation that describes this essay is the following Hertz equation.
Equation1:

![eq1](https://user-images.githubusercontent.com/41547014/95214976-d72e8000-07c6-11eb-9a45-8f0beced9a29.gif)

Where R is the tip radius and Er is the Reduced Young Modullus.
The R value can present some small variation from one experiment to another. The Er value is a sample constant.

The R value can be extracted from the maximum load and depth. 
Equation2:

![eq2](https://user-images.githubusercontent.com/41547014/95215234-24125680-07c7-11eb-9255-937ef01b5a73.gif)



<b>The Scritpt process:</b> 
 
Get_Er_hmax_and_Measurement_lines(filename):
Search the Er and hmax values, they are unique values on each text file. In addition, this function can also identify which lines present the Load x Depth           essay data.
 Returns initial_data_line, final_data_line, Er, hmax(depth_max)

Get_Measurement_data(initial_data_line,final_data_line, filename):
This function can extract two lists with experimental depths and load data from each text file, depending on initial and final data lines returned from previous function.
 Returns depth, load_experimental

Define_adjust_depth_range(depth):
We want to plot only the loading part of the curve, so this funcion make a list with only the depth values on the loading part of the curve.
 Returns depth_loading

fitting_R(depth,depth_loading,load_experimental, Er, filename, hmax):
This fuction calculates the R value based on maximum forces and depth (equation 2), and uses it to calculate the theoretical F for Pd values. This process is called Hertz fitting. The R value is returned to a list called R_list.
 Returns load_fitted, R 
 
plot_experimental_and_fitted(depth, depth_loading, load_experimental, load_fitted,filename):
This function plots the experimental and fitted curves, and saves the result as png files, where the R value is displayed for each curve.

plot_dispersion_and_Mean_R(R_list):
Finally, we can see the R dispersion and mean. 

main() and def Read_Files():
They are functions contructed to call the other functions.



