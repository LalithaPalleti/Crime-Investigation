# Crime-Investigation
## Introduction
Crime investigation around Starbucks Stores in Seattle

This project's goal is to collect crime history data around certain starbucks stores in seattle area and categorize the level of crimes by their crime type and forecast the future crime rates and category in which each store falls and therfore take security measures at each store accordingly 

## Model
Crime data in seattle area is extracted from   https://www.crimereports.com/

Used Facebook's Prophet model to forecast crime rates around starbucks stores in seattle area

First I have trained the Prophet model using the crime data in the seattle area.
Then I forecasted for future 6 months of data using prophet's predict method.

## Results
Crime severity is divided into 3 categories: Quality of Life(‘Drugs’, ‘Liquor’), Property('Property Crime',
'Theft', 'Theft of Vehicle', 'Theft from Vehicle'), Violent('Assault’, 'Robbery', 'Breaking & Entering')

Forecasted crime rates in all 3 categories for a strabucks store in seattle.

Following are the forecasted crime rate trends (monthly,yearly,weekly and daily trends) for that store:

1. Quality of Life Crimes

![alt text](https://github.com/LalithaPalleti/Crime-Investigation/blob/master/Quality%201.PNG)
![alt text](https://github.com/LalithaPalleti/Crime-Investigation/blob/master/Quality%203.PNG)
![alt text](https://github.com/LalithaPalleti/Crime-Investigation/blob/master/Quality2%20Png.PNG)

2.Property Crimes

![alt text](https://github.com/LalithaPalleti/Crime-Investigation/blob/master/Property1.PNG)
![alt text](https://github.com/LalithaPalleti/Crime-Investigation/blob/master/Property3.PNG)
![alt text](https://github.com/LalithaPalleti/Crime-Investigation/blob/master/Property2.PNG)

3.Violent Crimes

![alt text](https://github.com/LalithaPalleti/Crime-Investigation/blob/master/Violent1.PNG)
![alt text](https://github.com/LalithaPalleti/Crime-Investigation/blob/master/Violent3.PNG)
![alt text](https://github.com/LalithaPalleti/Crime-Investigation/blob/master/Violent2.PNG)

