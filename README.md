# Crime-Investigation

Crime investigation around Starbucks Stores in Seattle

This project's goal is to collect crime history data around certain starbucks stores in seattle area and categorize the level of crimes by their crime type and forecast the future crime rates and category in which each store falls and therfore take security measures at each store accordingly 

## Results
Crime severity is divided into 3 categories: Quality of Life(‘Drugs’, ‘Liquor’), Property('Property Crime',
'Theft', 'Theft of Vehicle', 'Theft from Vehicle'), Violent('Assault’, 'Robbery', 'Breaking & Entering')

Following are the forecasted crime values of stores around Seattle area for Feb 2018:

1. Quality of Life Crimes(Tier1)

![alt text](https://github.com/LalithaPalleti/Crime-Investigation/blob/master/Quality%20image.png)

2.Property Crimes(Tier2)

![alt text](https://github.com/LalithaPalleti/Crime-Investigation/blob/master/Property%20image.png)

3.Violent Crimes(Tier3)

![alt text](https://github.com/LalithaPalleti/Crime-Investigation/blob/master/Violence%20image.png)

Commands to deploy to heroku

heroku create --buildpack https://github.com/kennethreitz/conda-buildpack.git
git push heroku master
heroku ps:scale web=1
heroku open

Delete an App from heroku
heroku apps:destroy --app afternoon-fjord-61667
