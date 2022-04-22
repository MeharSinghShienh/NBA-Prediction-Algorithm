# NBA-Prediction-Algorithm
This is a program that uses a Teams data for the season to predict the percentage chance they have of winning a specific matchup. It has approximately a 70% accuracy
rate, a spreadsheet is attached with a 2 month log that was taken during the 2021-22 season to track the results of the algorithm

The program takes a teams data for their 'points scored' along with their 'opponent points allowed' and creates a normal distribution of them, which it takes a 
random sample from to simulate what they would score in that game. It does this score simulation for each team in a matchup and compares the scores to decide who wins the
game.

## Setup Requirements
This program was written in **Python 3.9**, to run it make sure you have **Python**, along with the **pandas**, **numpy**, **matplotlib** modules installed on the Python environment you are 
using to run the code.

Additionally, this program uses the nba_api to access the needed data for its functions. Please ensure you have the **nba_api** module installed within your Python
environment, details found here https://github.com/swar/nba_api 

## Available Functions
### gamesSim(team1, team2, season, ns)
gamesSim takes two teams, a season, and a number. It then runs the simulation game between the two teams the given number of times and returns the percentage of the
simulations that each team won, which is used as the percentage chance that team has to win that game based off their data for the given season. Below is an example
use of the function:
#### gamesSim('Toronto Raptors', 'Milwaukee Bucks', '2021-22', 100000)
The above function predicts the percentage chance the Raptors and Bucks have to win a game against each other based of their data for the 2021-22 season and with 100000
simulations run.

### gamesSimLastN(team1, team2, n, season, ns)
gamesSimLastN takes two teams, a season, and two number. It then runs the simulation game between the two teams the 'ns' times and returns the percentage of the
simulations that each team won, which is used as the percentage chance that team has to win that game based off their data for the last 'n' games in the given season.
Below is an example use of the function:
#### gamesSimLastN('Toronto Raptors', 'Milwaukee Bucks', 15, '2021-22', 100000)
The above function predicts the percentage chance the Raptors and Bucks have to win a game against each other based of their data for their last 15 games in the 
2021-22 season and with 100000 simulations run.

### todayGamesSim()
todayGamesSim is used to automate the prediction process, it automatically fetches the games that are happening the day the function is run and outputs the predictions
for each of them

### todayGamesSimLastN(n)
todayGamesSimLastN provides the same function of todayGamesSim, the only difference is that it makes its predictions based off the data from the teams last 'n' games
