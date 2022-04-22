import pandas as pd 
import random as rnd
import numpy as np 
import matplotlib.pyplot as plt

from nba_api.stats.static import teams 
from nba_api.stats.endpoints import leaguegamefinder

team_dict = teams.get_teams()

def gameSim(team1_mean_pts, team1_std_pts, team1_mean_opp, team1_std_opp,
            team2_mean_pts, team2_std_pts, team2_mean_opp, team2_std_opp):
    while True:
        team1Score = (rnd.gauss(team1_mean_pts,team1_std_pts)+ rnd.gauss(team2_mean_opp,team2_std_opp))/2
        team2Score = (rnd.gauss(team2_mean_pts,team2_std_pts)+ rnd.gauss(team1_mean_opp,team1_std_opp))/2
        if int(round(team1Score)) > int(round(team2Score)):
            return 1
        elif int(round(team1Score)) < int(round(team2Score)):
            return -1
        
        
# Enter strings of full team names and what season the game is in
def gamesSim(team1, team2, season, ns):
    team1_df = [team for team in team_dict if team['full_name'] == team1][0]
    team1_id = team1_df['id']
    team1_games = leaguegamefinder.LeagueGameFinder(team_id_nullable=team1_id,season_nullable=season).get_data_frames()[0]
    team1_games['OPP_PTS'] = team1_games.PTS - team1_games.PLUS_MINUS
    
    team2_df = [team for team in team_dict if team['full_name'] == team2][0]
    team2_id = team2_df['id']
    team2_games = leaguegamefinder.LeagueGameFinder(team_id_nullable=team2_id,season_nullable=season).get_data_frames()[0]
    team2_games['OPP_PTS'] = team2_games.PTS - team2_games.PLUS_MINUS
    
    team1_mean_pts = team1_games.PTS.mean()
    team2_mean_pts = team2_games.PTS.mean()
    team1_std_pts = team1_games.PTS.std()
    team2_std_pts = team2_games.PTS.std()
    
    team1_mean_opp = team1_games.OPP_PTS.mean()
    team2_mean_opp = team2_games.OPP_PTS.mean()
    team1_std_opp = team1_games.OPP_PTS.std()
    team2_std_opp = team2_games.OPP_PTS.std()
    
    gamesout = []
    team1win = 0
    team2win = 0
    
    for i in range(ns):
        gm = gameSim(team1_mean_pts, team1_std_pts, team1_mean_opp, team1_std_opp,
                     team2_mean_pts, team2_std_pts, team2_mean_opp, team2_std_opp)
        gamesout.append(gm)
        if gm == 1:
            team1win +=1 
        elif gm == -1:
            team2win +=1
    print(team1, ' Win ', (team1win/(team1win+team2win))*100,'%')
    print(team2, ' Win ', (team2win/(team1win+team2win))*100,'%')
    return gamesout


# Use this if you don't want to use full season performance and just want to base it over the last n games
def gamesSimLastN(team1, team2, n, season, ns):
    team1_df = [team for team in team_dict if team['full_name'] == team1][0]
    team1_id = team1_df['id']
    team1_games = leaguegamefinder.LeagueGameFinder(team_id_nullable=team1_id,season_nullable=season).get_data_frames()[0]
    team1_games['OPP_PTS'] = team1_games.PTS - team1_games.PLUS_MINUS
    team1_games = team1_games.head(n)
    
    team2_df = [team for team in team_dict if team['full_name'] == team2][0]
    team2_id = team2_df['id']
    team2_games = leaguegamefinder.LeagueGameFinder(team_id_nullable=team2_id,season_nullable=season).get_data_frames()[0]
    team2_games['OPP_PTS'] = team2_games.PTS - team2_games.PLUS_MINUS
    team2_games = team2_games.head(n)
    
    team1_mean_pts = team1_games.PTS.mean()
    team2_mean_pts = team2_games.PTS.mean()
    team1_std_pts = team1_games.PTS.std()
    team2_std_pts = team2_games.PTS.std()
    
    team1_mean_opp = team1_games.OPP_PTS.mean()
    team2_mean_opp = team2_games.OPP_PTS.mean()
    team1_std_opp = team1_games.OPP_PTS.std()
    team2_std_opp = team2_games.OPP_PTS.std()
    
    gamesout = []
    team1win = 0
    team2win = 0
    
    for i in range(ns):
        gm = gameSim(team1_mean_pts, team1_std_pts, team1_mean_opp, team1_std_opp,
                     team2_mean_pts, team2_std_pts, team2_mean_opp, team2_std_opp)
        gamesout.append(gm)
        if gm == 1:
            team1win +=1 
        elif gm == -1:
            team2win +=1
    print(team1, ' Win ', (team1win/(team1win+team2win))*100,'%')
    print(team2, ' Win ', (team2win/(team1win+team2win))*100,'%')
    return gamesout




