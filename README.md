# EconomyDataVisualization
This repository displays graphs showing different economic statistics across different nations. This was accomplished using SQL and Python. In Microsoft SSMS, I set up a local SQL Server and used it to format the imported economic data CSVs into several views. These views were then exported into CSVs. Those exported CSVs were then imported into Python via Pandas, where I used Matplotlib to create graphs from the imported data. I am currently working to create similar graphs on dashboards using Microsoft Power BI.

All data used in this project was obtained from the Organization for Economic Co-operation and Development's public database, found at this link under Economic Projections/OECD Economic Outlook/OECD Economic Outlook latest edition/ Economic Outlook No. 112 - November 2022./EO By Subject(GDP, Unemployment...): https://stats.oecd.org/Index.aspx?DataSetCode=DP_LIVE

# What I Have Learned So Far
- Data analysis
  - Preparing data
  - Modeling data
  - Visualizing data
- Setting up a local SQL database using Microsoft's SQL Server Management Studio (SSMS)
- Importing/Exporting files using SSMS
- SQL programming
  - Selecting data
  - Performing aggregate functions
  - Creating CTEs
  - Joining multiple data sets together
  - Creating views
  - Extrapolating data by grouping
- Python programming through Matplotlib and Pandas
  - Reading CSVs
  - Plotting different types of graphs (line, bar, horizontal bar)
  - Setting graph and axis titles
  - Creating custom legends
  - Displaying multiple legends
  - Altering graph line/bar appearance using optional parameters (color and linestyle)
  - Altering legend appearance using optional parameters (title, loc, borderpad, labelspacing, ncol)
- Power BI
  - Transforming data in Power Query
  - Setting relationships between CSVs in the Model View
  - Displaying data using various visualizations and filters in the Report View
