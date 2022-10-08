CREATE TABLE african_power_plants AS 
(SELECT *
FROM power_plants_table
WHERE country_long IN('Djibouti','Seychelles','DR Congo','Comoros','Togo','Sierra Leone','Libya','Tanzania',
'South Africa','Cabo Verde','Congo','Kenya','Liberia','Central African Republic','Mauritania','Uganda','Algeria',
'Sudan','Morocco','Eritrea','Angola','Mozambique','Ghana','Madagascar','Cameroon','Côte DIvoire','Namibia',
'Niger','Gambia','Botswana','Gabon','Sao Tome & Principe','Lesotho','Burkina Faso','Nigeria','Mali',
'Guinea-Bissau','Malawi','Zambia','Senegal','Chad','Somalia','Zimbabwe','Equatorial Guinea','Guinea',
'Rwanda','Mauritius','Benin','Burundi','Tunisia','Eswatini','Ethiopia','South Sudan','Egypt'));

SELECT * FROM power_plants_table
					  WHERE country_long IN ('Equatorial Guinea');

					  
