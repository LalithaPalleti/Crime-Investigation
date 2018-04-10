# Crime-Investigation

Crime investigation around Starbucks Stores in Seattle

This project's goal is to collect crime history data around certain starbucks stores in seattle area and categorize the level of crimes by their crime type and forecast the future crime rates and category in which each store falls and therfore take security measures at each store accordingly 

Commands to deploy to heroku

heroku create --buildpack https://github.com/kennethreitz/conda-buildpack.git
git push heroku master
heroku ps:scale web=1
heroku open

Delete an App from heroku
heroku apps:destroy --app afternoon-fjord-61667
