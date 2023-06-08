import pandas as ps
from matplotlib import pyplot as pt
from matplotlib.lines import Line2D

# Set window size for graph
pt.rcParams["figure.figsize"] = [16, 8]

# Import the CSV file
table = ps.read_csv("HighestUnemploymentPercentage.csv", encoding = 'Latin1')

# Store target data columns on variables
xAxis = table['Country']
yAxis = table['Highest_Unemployment_Percentage']
years = table['Year']

# Set colors for use in bars and legend
colors = ['red', 'orange', 'gold', 'green', 'lime', 
          'cyan', 'blue', 'blueviolet', 'magenta']

# Set the color of each bar, based on the year
bar_color = []
for year in years:
    match year:
        case 2016:
            bar_color.append(colors[0])
        case 2017:
            bar_color.append(colors[1])
        case 2018:
            bar_color.append(colors[2])
        case 2019:
            bar_color.append(colors[3])
        case 2020:
            bar_color.append(colors[4])
        case 2021:
            bar_color.append(colors[5])
        case 2022:
            bar_color.append(colors[6])
        case 2023:
            bar_color.append(colors[7])
        case 2024:
            bar_color.append(colors[8])

# Plot a horizontal bar graph
pt.barh(xAxis, yAxis, color = bar_color)

# Set graph title and axis labels
pt.title('Highest Unemployment Percentages For Various Countries')
pt.xlabel('Highest Unemployment Percentage')
pt.ylabel('Country')

# Set colors for lines in the legend
legend_colors = []
for element in colors:
    legend_colors.append(Line2D([0], [0], color = element, lw=5))

# Set years in legend
legend_years = ['2016', '2017', '2018', '2019', '2020', 
                '2021', '2022', '2023', '2024']

# Create a legend for the recorded years
pt.legend(legend_colors, legend_years, title = "Recorded Year")

# Show the graph
pt.show()