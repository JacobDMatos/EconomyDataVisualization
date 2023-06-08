import copy
import pandas as ps
from matplotlib import pyplot as pt
from matplotlib.lines import Line2D

# Set window size for graph
pt.rcParams["figure.figsize"] = [16, 8]

# Import the CSV file
table = ps.read_csv('CalculatedUnemploymentPercentage.csv', encoding='Latin1')

# Store target data columns on variables
years = table['Year']
calc_data_points = table['Calculated_Unemployment_Percentage']
real_data_points = table['Real_Unemployment_Percentage']

# Define a function which takes in a target data column,
# and organize the data by country in a nested array
def organize_data(list):
    # Variables required in for loop
    index = 0
    output = []
    temp_list = []

    # Iterate through every element in the data list
    for element in list:
        # Deep copy the temp list into the output list every 9 elements,
        # then clear the temp list
        if ((index != 0) and (index % 9 == 0)):
            output.append(copy.deepcopy(temp_list))
            temp_list.clear()

        # Add the element to the temp list
        temp_list.append(element)

        # Increase the index by 1 until we get to the end of the list
        if (index != len(list) - 1):
            index += 1
            continue

        # Deep copy temp list into the output once reaching the end of the loop
        output.append(copy.deepcopy(temp_list))
    
    # Return the output list
    return output

# Store the output from the above function onto variables
organized_years = organize_data(years)
organized_calc_data_points = organize_data(calc_data_points)
organzied_real_data_points = organize_data(real_data_points)

# Store the country names onto a variable
countries = table['Country']

# Iterate through all country names,
# and store only one of each name
name_index = 0
country_names = []
for element in years:
    # Store the country name at index 0
    if (name_index == 0):
        country_names.append(countries[name_index])
    # Afterwards, store a country name every 9 elements
    elif ((name_index != 0) and (name_index % 9 == 0)):
        country_names.append(countries[name_index])

    # Increase the index by 1
    name_index += 1

# Set colors for use in legend
colors = ['black', 'silver', 'brown', 'red', 'chocolate', 'darkorange',
          'goldenrod', 'darkkhaki', 'olive', 'olivedrab', 'yellowgreen',
          'lawngreen', 'darkseagreen', 'green', 'mediumaquamarine', 'turquoise',
          'teal', 'cyan', 'deepskyblue', 'steelblue', 'cornflowerblue',
          'darkblue', 'blue', 'slateblue', 'mediumslateblue', 'mediumpurple',
          'rebeccapurple', 'blueviolet', 'mediumorchid', 'plum', 'violet',
          'darkmagenta', 'magenta', 'hotpink']

# Plot all calculated and real unemployment percentages
# Color code each line to indicate different countries
plot_index = 0
for element in organized_years:
    # Plot calculated unemployment percentages as solid lines
    pt.plot(organized_years[plot_index], 
            organized_calc_data_points[plot_index], 
            color = colors[plot_index])
    
    # Plot real unemployment percentages as dashed lines
    pt.plot(organized_years[plot_index], 
            organzied_real_data_points[plot_index], 
            color = colors[plot_index], 
            linestyle = 'dashed')
    
    # Increase the index by 1
    plot_index += 1

# Set colors for lines in the legend
legend_colors = []
for element in colors:
    legend_colors.append(Line2D([0], [0], color = element, lw=3))

# Create a legend for the country names,
# and store it on a variable
country_legend = pt.legend(legend_colors, country_names, ncol = 5, 
                           title = "Country", 
                           loc = 1, 
                           borderpad = 0.5, 
                           labelspacing = 0.25)

# Set line types for the line legend
legend_lines = [Line2D([0], [0], color = 'black', lw = 3),
                Line2D([0], [0], color = 'black', lw = 3, linestyle = 'dotted')]

# Set labels for line types in the line legend
legend_labels = ['Calculated Unemployment', 'Real Unemployment']

# Create a legend to show the difference between the solid and dashed lines
pt.legend(legend_lines, legend_labels, loc = 2)

# Add the country name legend back in
pt.gca().add_artist(country_legend)

# Set graph title and axis labels
pt.title('Calculated and Real Unemployment Percentages For Various Countries')
pt.xlabel('Year')
pt.ylabel('Unemployment Percentage')

# Show the graph
pt.show()