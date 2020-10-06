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
The nanoindentation curve is constructed when a very small tip presses the sample surface. The Load versus Depth curve is described by the Hertz equation:

<img src="https://render.githubusercontent.com/render/math?math= load = \frac{4}{3}* E_{r}*\sqrt{R*{depth}^{3}}">  equation1


<b>The Scritpt process:</b> 
 
Get_Er_hmax_and_Measurement_lines(filename):
 search the Er and hmax values, they are unique values on each text file. In addition, this function can also identify which lines present the Pd x Force           essay data.
 Returns initial_data_line, final_data_line, Er, hmax

Get_Measurement_data(initial_data_line,final_data_line, filename):
 this function can extract two lists with experimental Pd and Force data from each text file, depending on initial and final data lines returned from previous function.
 Returns Pd, F_experimental

Define_adjust_depth_range(Pd):
 we want to plot only the loading part of the curve, so this funcion make a list with only the Pd values on the loading part of the curve.
 Returns Pd_loading

fitting_R(Pd,Pd_small_range, F_experimental, Er, filename, hmax):
 this fuction calculates the R value based on maximum forces and depth (equation 2), and uses it to calculate the theoretical F for Pd values. This process is called Hertz fitting. The R value is returned to a list called R_list.
Returns F_fitted, R 
 
plot_experimental_and_fitted(Pd, Pd_loading, F_experimental, F_fitted,filename):
This function plots the experimental and fitted curves, and saves the result as png files, where the R value is displayed for each curve.

plot_dispersion_and_Mean_R(R_list)
Finally, we can see the R dispersion and mean. It should not present a variation larger than 10% of mean value, as we can see. The graph is saved.





 
 
 

 
 
 
 
