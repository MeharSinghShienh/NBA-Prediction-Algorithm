from GameSimulator import *

import pandas as pd 
import random as rnd
import numpy as np 
import matplotlib.pyplot as plt

from nba_api.live.nba.endpoints import scoreboard

board = scoreboard.ScoreBoard()
games = board.games.get_dict()


# Finds all the games happening on the day its run and makes a simulation for each 
def todayGamesSim():
    for game in games:
        home_tm = [team for team in team_dict if team['id'] == game['homeTeam']['teamId']][0]
        away_tm = [team for team in team_dict if team['id'] == game['awayTeam']['teamId']][0]  
        gamesSim(home_tm['full_name'], away_tm['full_name'], '2021-22', 100000)
        
# Finds all the games happening on the day its run and makes a simulation for each based of date from last n games
def todayGamesSimLastN(n):
    for game in games: 
        home_tm = [team for team in team_dict if team['id'] == game['homeTeam']['teamId']][0]
        away_tm = [team for team in team_dict if team['id'] == game['awayTeam']['teamId']][0]  
        gamesSimLastN(home_tm['full_name'], away_tm['full_name'], n, '2021-22', 100000)