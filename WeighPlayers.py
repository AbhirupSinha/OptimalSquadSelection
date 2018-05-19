import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore")

data = pd.read_csv('cleaned-data.csv', skipinitialspace=True)
# players = list(set(data['batsman']).union(set(data['bowler']).union(set(data['fielder']))))

match_score = data.groupby(['matchID', 'inningsID']).agg({'score': np.max, 'fallOfWickets': np.max})
# print(match_score)

crushers = data.query("25 <= batsmanRuns and over < 4").groupby(['batsman', 'matchID', 'inningsID']).\
    agg({'over': np.mean, 'strikeRate': np.mean, 'ballsFaced': np.mean, 'commentWeight': np.mean, 'batsmanRuns': np.max, 'fours': np.max, 'sixes': np.max}).\
    groupby(['batsman']).agg({'over': np.size, 'strikeRate': np.mean, 'ballsFaced': np.mean, 'commentWeight': np.mean,'batsmanRuns':np.mean, 'fours': np.mean, 'sixes': np.mean}).\
    sort_values('over', ascending=False).rename(columns={'over': 'matchCount','batsmanRuns':'averageRunsScored'})
#print(crushers)

pre_delacquerers = data.query("over < 7 and batsmanRuns >= 25").groupby(['batsman', 'matchID', 'inningsID']).\
    agg({'over': np.max, 'batsmanRuns': np.max, 'ballsFaced': np.max, 'commentWeight': np.mean}).\
    query("batsmanRuns/ballsFaced > 1")
players = pre_delacquerers['over'].keys().levels[0]
matches = pre_delacquerers['over'].keys().levels[1]
delacquerers = data.query("over > 7 and batsman in @players and matchID in @matches").groupby(['batsman', 'matchID', 'inningsID']).\
    agg({'over': np.max, 'ballsFaced': np.max, 'commentWeight': np.mean, 'batsmanRuns': np.max, 'fours': np.max, 'sixes': np.max}).\
    query("batsmanRuns/ballsFaced > 1.5").groupby(['batsman']).\
    agg({'over': np.size, 'ballsFaced': np.mean, 'commentWeight': np.mean, 'batsmanRuns': np.mean, 'fours': np.mean, 'sixes': np.mean}).\
    sort_values('over', ascending=False).rename(columns={'over': 'matchCount'})
#print(delacquerers)

cultured_batsmen = data.query("batsmanRuns >= 40 and ballsFaced/(fours+sixes) <= 6").groupby(['batsman', 'matchID', 'inningsID']).\
    agg({'over': np.max, 'batsmanRuns': np.max, 'ballsFaced': np.max, 'commentWeight': np.mean, 'fours': np.max, 'sixes': np.max}).\
    query("batsmanRuns/ballsFaced > 1.35").groupby(['batsman']).\
    agg({'over': np.size, 'ballsFaced': np.mean, 'commentWeight': np.mean, 'batsmanRuns': np.mean, 'fours': np.mean, 'sixes': np.mean}).\
    sort_values('over', ascending=False).rename(columns={'over': 'matchCount'})
#print(cultured_batsmen)

hard_hitters = data.query("batsmanRuns >= 30").groupby(['batsman', 'matchID', 'inningsID']).\
    agg({'over': np.max, 'batsmanRuns': np.max, 'ballsFaced': np.max, 'commentWeight': np.mean, 'fours': np.max, 'sixes': np.max}).\
    query("batsmanRuns/ballsFaced > 1.5").groupby(['batsman']).\
    agg({'over': np.size, 'ballsFaced': np.mean, 'commentWeight': np.mean, 'batsmanRuns': np.mean, 'fours': np.mean, 'sixes': np.mean}).\
    sort_values('over', ascending=False).rename(columns={'over': 'matchCount'})
#print(hard_hitters)

bat_hitters2 = data.query("batsmanRuns >= 30").groupby(['batsman', 'matchID', 'inningsID']).\
    agg({'over': np.max, 'batsmanRuns': np.max, 'ballsFaced': np.max, 'commentWeight': np.mean, 'batsman': 'first', 'fours': np.max, 'sixes': np.max}).\
    query("batsmanRuns/ballsFaced > 1.2").groupby(['batsman']).\
    agg({'over': np.size, 'ballsFaced': np.mean, 'commentWeight': np.mean, 'batsman': 'first', 'batsmanRuns': np.mean, 'fours': np.mean, 'sixes': np.mean}).\
    sort_values('over', ascending=False).rename(columns={'over': 'matchCount'})
players = bat_hitters2['batsman'].keys()
bowl_hitters2 = data.query("bowler in @players").groupby(['bowler', 'matchID', 'inningsID']).\
    agg({'over': np.max, 'economy': np.mean, 'commentWeight': np.mean, 'bowler': 'first', 'wickets': np.max}).\
    query("economy < 9").groupby(['bowler']).\
    agg({'over': np.size, 'economy': np.mean, 'commentWeight': np.mean, 'bowler': 'first', 'wickets': np.mean}).\
    sort_values('over', ascending=False).rename(columns={'over': 'matchCount'})
hard_hitters2 = pd.merge(bat_hitters2, bowl_hitters2, left_on=['batsman'], right_on=['bowler'])
#print(hard_hitters2)

wicket_keeper_stump = data.query("dismissalType == 'stumped'").groupby(['fielder']). \
    agg({'fielder': 'first', 'commentWeight': np.mean, 'over': np.size}).\
    sort_values('over', ascending=False).rename(columns={'over': 'stumps'})
players = wicket_keeper_stump['fielder'].keys()
wicket_keeper_bat = data.query("batsman in @players").groupby(['batsman', 'matchID', 'inningsID']).\
    agg({'over': np.max, 'batsmanRuns': np.max, 'ballsFaced': np.max, 'commentWeight': np.mean, 'batsman': 'first', 'fours': np.max, 'sixes': np.max}).\
    query("batsmanRuns/ballsFaced > 1").groupby(['batsman']).\
    agg({'over': np.size, 'ballsFaced': np.mean, 'commentWeight': np.mean, 'batsman': 'first', 'batsmanRuns': np.mean, 'fours': np.mean, 'sixes': np.mean}).\
    rename(columns={'over': 'matchCount'})
wicket_keeper = pd.merge(wicket_keeper_stump, wicket_keeper_bat, left_on=['fielder'], right_on=['batsman'])
#print(wicket_keeper)

bat_allRounder = data.groupby(['batsman', 'matchID', 'inningsID']).\
    agg({'over': np.max, 'batsmanRuns': np.max, 'ballsFaced': np.max, 'commentWeight': np.mean, 'batsman': 'first', 'fours': np.max, 'sixes': np.max}).\
    query("batsmanRuns/ballsFaced > 1.4").groupby(['batsman']).\
    agg({'over': np.size, 'batsmanRuns': np.mean, 'ballsFaced': np.mean, 'commentWeight': np.mean, 'batsman': 'first', 'fours': np.mean, 'sixes': np.mean}).\
    sort_values('over', ascending=False).rename(columns={'over': 'matchCount'})
players = bat_allRounder['batsman'].keys()
bowl_allRounder = data.query("bowler in @players").groupby(['bowler', 'matchID', 'inningsID']).\
    agg({'over': np.max, 'economy': np.mean, 'commentWeight': np.mean, 'bowler': 'first', 'wickets': np.max, 'ballsBowled': np.max}).\
    query("economy < 9").groupby(['bowler']).\
    agg({'over': np.size, 'economy': np.mean, 'commentWeight': np.mean, 'bowler': 'first', 'wickets': np.mean, 'ballsBowled': np.mean}).\
    sort_values('over', ascending=False).rename(columns={'over': 'matchCount'})
#bowl_allRounder['bowlStrikeRate'] = bowl_allRounder.apply(lambda row: row['ballsBowled']/row['wickets'], axis=1)
allRounder = pd.merge(bat_allRounder, bowl_allRounder, left_on=['batsman'], right_on=['bowler'])
#print(allRounder)

general_bowlers = data.query("4 < over < 16").groupby(['bowler', 'matchID', 'inningsID']).\
    agg({'over': np.max, 'economy': np.mean, 'ballsBowled': np.max, 'wickets': np.max, 'commentWeight': np.mean}).\
    query("ballsBowled/wickets < 25").groupby(['bowler']).\
    agg({'over': np.size, 'economy': np.mean, 'ballsBowled': np.mean, 'wickets': np.mean, 'commentWeight': np.mean}). \
    query("10 <= over").rename(columns={'over': 'matchCount'}).sort_values('matchCount', ascending=False)
general_bowlers['bowlStrikeRate'] = general_bowlers.apply(lambda row: row['ballsBowled']/row['wickets'], axis=1)
#print(general_bowlers)

do_specialist = data.query("16 <= over").groupby(['bowler', 'matchID', 'inningsID']).\
    agg({'over': np.max, 'economy': np.mean, 'ballsBowled': np.max, 'wickets': np.max, 'commentWeight': np.mean}).\
    query("ballsBowled/wickets < 15").groupby(['bowler']).\
    agg({'over': np.size, 'economy': np.mean, 'ballsBowled': np.mean, 'wickets': np.mean, 'commentWeight': np.mean}). \
    query("4 <= over").rename(columns={'over': 'matchCount'}).sort_values('matchCount', ascending=False)
do_specialist['bowlStrikeRate'] = do_specialist.apply(lambda row: row['ballsBowled']/row['wickets'], axis=1)
#print(do_specialist)
