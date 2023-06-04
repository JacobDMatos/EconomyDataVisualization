-- Create/Alter a view that displays each country's highest unemployment rate, and the year that rate was recorded

CREATE OR ALTER VIEW HighestUnemploymentPercentage AS
	-- Join data set and subset such that each country only displays its highest unemployment rate and the respective year

	SELECT
		up.Country,
		up.Year,
		up.Unemployment_Percentage as Highest_Unemployment_Percentage
	FROM 
		EconomyData..UnemploymentPercentage up
	INNER JOIN (
		SELECT
			Country,
			MAX(cast(Unemployment_Percentage as float)) max
		FROM 
			EconomyData..UnemploymentPercentage
		GROUP BY 
			Country
	) sub ON up.Country = sub.Country AND up.Unemployment_Percentage = sub.max