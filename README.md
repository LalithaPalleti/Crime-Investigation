# Crime-Investigation

Crime investigation around Starbucks Stores in Seattle

This project's goal is to collect crime history data around certain starbucks stores in seattle area and categorize the level of crimes by their crime type and forecast the future crime rates and category in which each store falls and therfore take security measures at each store accordingly 


I have categorized crime severity into 3 tiers: Tier1(‘Drugs’, ‘Liquor’), Tier2('Property Crime',
'Theft', 'Theft of Vehicle', 'Theft from Vehicle'), Tier3('Assault’, 'Robbery', 'Breaking & Entering')
Following are the forecasted crime values of stores neighborhood for Feb 2018:


SNO | Store | Tier1 | Tier2 | Tier3 | 
--- | --- | --- | --- |--- |
1 | 1912 Pike Place Seattle, WA 98101 | Approximately 0 | Between 0 and 2 | Between 0 and 10 |
2 | 4634 26th Avenue NE Seattle, WA 98105 | Approximately 0 | Between 0 and 2 | Between 0 and 5 |
1 | 10002 Aurora Avenue North Seattle, WA 98133 | Approximately 0 | Between 0 and 2 | Between 0 and 5 |
1 | 3300 W. McGraw St. Seattle, WA 98119 | Approximately 0 | Between 0 and 2 | Between 0 and 5 |
1 | 1125 4th Avenue Seattle, WA 98101 | Approximately 0 | Between 0 and 2 | Between 0 and 10 |

As observed from the above figures all the stores mostly fall in Tier3 and some pat in Tier2,so they need
security from crimes mostly 'Assault’, 'Robbery', 'Breaking & Entering', so they should be taking security
measures such as installing security euipment that monitors the store 24hours such as Security
Cameras,frequent cash pickups,ask the customers to pay mostly through Credit card.For the 1st
store(1912 Pike Place Seattle, WA 98101) and 5th store(1125 4th Avenue Seattle, WA 98101) there is
more chance of tier3 crimes,so it would be better if they have on premise security persons





Commands to deploy to heroku

heroku create --buildpack https://github.com/kennethreitz/conda-buildpack.git
git push heroku master
heroku ps:scale web=1
heroku open

Delete an App from heroku
heroku apps:destroy --app afternoon-fjord-61667
