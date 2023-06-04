-- Create a view that compares a calculated unemployment percentage to the real value from UnemploymentPercentage

CREATE OR ALTER VIEW CalculatedUnemploymentPercentage AS
	-- Store joining of LabourForce and TotalEmployedPeople as CTE for calculations

	WITH
		LFandTEP(Country, Year, People_in_Labour_Force, Total_Employed_People)
	AS (
		SELECT
			lf.Country,
			lf.Year,
			lf.People_in_Labour_Force,
			tep.Total_Employed_People
		FROM
			EconomyData..LabourForce lf
		INNER JOIN 
			EconomyData..TotalEmployedPeople tep
		ON 
			lf.Country = tep.Country AND lf.Year = tep.Year
	)

	-- Display CTE contents
	-- Calculate and display total number of unemployed people in each country per year
	-- Calculate and display mathematical unemployment percentage
	-- Display real unemployment percentage from UnemploymentPercentage for comparison
	-- Calculate and display percent difference between these two unemployment percentages

	SELECT
		comb.Country,
		comb.Year,
		comb.People_in_Labour_Force,
		comb.Total_Employed_People,
		(cast(People_in_Labour_Force as float) - cast(Total_Employed_People as float)) as Total_Unemployed_People,
		(cast(People_in_Labour_Force as float) - cast(Total_Employed_People as float)) / cast(People_in_Labour_Force as float) * 100 as Calculated_Unemployment_Percentage,
		up.Unemployment_Percentage as Real_Unemployment_Percentage,
		((cast(People_in_Labour_Force as float) - cast(Total_Employed_People as float)) / cast(People_in_Labour_Force as float) * 100) - cast(up.Unemployment_Percentage as float) as Percent_Difference
	FROM
		LFandTEP comb
	INNER JOIN
		EconomyData..UnemploymentPercentage up
	ON
		comb.Country = up.Country AND comb.year = up.Year