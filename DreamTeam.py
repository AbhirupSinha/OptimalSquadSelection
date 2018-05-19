import WeighPlayers
import pandas as pd
from collections import defaultdict
import prediction
import math
import warnings

warnings.filterwarnings("ignore")
playing_team = []
reserve_team = []
expected_runs = 0
expected_stumps = 0
expected_wickets = 0

crushers_dict = {}
crushers_dataset = WeighPlayers.crushers
crushers_dataset = crushers_dataset.reset_index()
max_match = crushers_dataset.max()['matchCount']
max_four = crushers_dataset.max()['fours']
max_six = crushers_dataset.max()['sixes']
for i in range(0, len(crushers_dataset)):
    score = ((crushers_dataset.iloc[i]['matchCount'] / max_match) * crushers_dataset.iloc[i]['commentWeight'] *
             (crushers_dataset.iloc[i]['strikeRate'] / 100) * 
             ((crushers_dataset.iloc[i]['fours'] / max_four) + (crushers_dataset.iloc[i]['sixes'] / max_six)))
    crushers_dict[crushers_dataset.iloc[i]['batsman']] = score
crushers_val=[]
d1 = defaultdict(float)
for key in crushers_dict.keys():
    d1[key] = crushers_dict[key]
for w in sorted(d1, key = d1.get, reverse = True):
    crushers_val.append([w,d1[w]])   
for i in range(0, len(crushers_val)):
    if crushers_val[i][0] not in playing_team:
        playing_team.append(crushers_val[i][0])
        expected_runs += math.floor(prediction.crusher_prediction_bat(crushers_val[i][0]))
        break
    
delacquerers_dict = {}
delacquerers_dataset = WeighPlayers.delacquerers
delacquerers_dataset = delacquerers_dataset.reset_index()
max_match = delacquerers_dataset.max()['matchCount']
max_four = delacquerers_dataset.max()['fours']
max_six = delacquerers_dataset.max()['sixes']
for i in range(0, len(delacquerers_dataset)):
    score = ((delacquerers_dataset.iloc[i]['matchCount'] / max_match) * 
             (delacquerers_dataset.iloc[i]['batsmanRuns']) * delacquerers_dataset.iloc[i]['commentWeight'] *
             ((delacquerers_dataset.iloc[i]['fours'] / max_four) + (delacquerers_dataset.iloc[i]['sixes'] / max_six)))
    delacquerers_dict[delacquerers_dataset.iloc[i]['batsman']] = score
delacquerers_val=[]
d2 = defaultdict(float)
for key in delacquerers_dict.keys():
    d2[key] = delacquerers_dict[key]
for w in sorted(d2, key = d2.get, reverse = True):
    delacquerers_val.append([w,d2[w]])    
for i in range(0, len(delacquerers_val)):
    if delacquerers_val[i][0] not in playing_team:
        playing_team.append(delacquerers_val[i][0])
        expected_runs += math.floor(prediction.delacquerers_prediction_bat(delacquerers_val[i][0]))
        break

cultured_batsmen_dict = {}
cultured_batsmen_dataset = WeighPlayers.cultured_batsmen
cultured_batsmen_dataset = cultured_batsmen_dataset.reset_index()
max_match = cultured_batsmen_dataset.max()['matchCount']
max_four = cultured_batsmen_dataset.max()['fours']
max_six = cultured_batsmen_dataset.max()['sixes']
for i in range(0, len(cultured_batsmen_dataset)):
    score = ((cultured_batsmen_dataset.iloc[i]['matchCount'] / max_match) * 
             (cultured_batsmen_dataset.iloc[i]['batsmanRuns']) * cultured_batsmen_dataset.iloc[i]['commentWeight'] *
             ((cultured_batsmen_dataset.iloc[i]['fours'] / max_four) + (cultured_batsmen_dataset.iloc[i]['sixes'] / max_six)))
    cultured_batsmen_dict[cultured_batsmen_dataset.iloc[i]['batsman']] = score
cultured_batsmen_val=[]
d3 = defaultdict(float)
for key in cultured_batsmen_dict.keys():
    d3[key] = cultured_batsmen_dict[key]
for w in sorted(d3, key = d3.get, reverse = True):
    cultured_batsmen_val.append([w,d3[w]]) 
for i in range(0, len(cultured_batsmen_val)):
    if cultured_batsmen_val[i][0] not in playing_team:
        playing_team.append(cultured_batsmen_val[i][0])
        expected_runs += math.floor(prediction.culturedbatsmen_prediction_bat(cultured_batsmen_val[i][0]))
        break
    
hard_hitter1_dict = {}
hard_hitter1_dataset = WeighPlayers.hard_hitters
hard_hitter1_dataset = hard_hitter1_dataset.reset_index()
max_match = hard_hitter1_dataset.max()['matchCount']
max_four = hard_hitter1_dataset.max()['fours']
max_six = hard_hitter1_dataset.max()['sixes']
for i in range(0, len(hard_hitter1_dataset)):
    score = ((hard_hitter1_dataset.iloc[i]['matchCount'] / max_match) * 
             (hard_hitter1_dataset.iloc[i]['batsmanRuns']) * hard_hitter1_dataset.iloc[i]['commentWeight'] *
             ((hard_hitter1_dataset.iloc[i]['fours'] / max_four) + (hard_hitter1_dataset.iloc[i]['sixes'] / max_six)))
    hard_hitter1_dict[hard_hitter1_dataset.iloc[i]['batsman']] = score
hard_hitter1_val=[]
d4 = defaultdict(float)
for key in hard_hitter1_dict.keys():
    d4[key] = hard_hitter1_dict[key]
for w in sorted(d4, key = d4.get, reverse = True):
    hard_hitter1_val.append([w,d4[w]])
for i in range(0, len(hard_hitter1_val)):
    if hard_hitter1_val[i][0] not in playing_team:
        playing_team.append(hard_hitter1_val[i][0])
        expected_runs += math.floor(prediction.hardhitters1_prediction_bat(hard_hitter1_val[i][0]))
        break
    
hard_hitter2_dict = {}
hard_hitter2_dataset = WeighPlayers.hard_hitters2
max_match = hard_hitter2_dataset.max()['matchCount_x']
max_four = hard_hitter2_dataset.max()['fours']
max_six = hard_hitter2_dataset.max()['sixes']
max_wicket = hard_hitter2_dataset.max()['wickets']
for i in range(0, len(hard_hitter2_dataset)):
    score = ((hard_hitter2_dataset.iloc[i]['matchCount_x'] / max_match) * (hard_hitter2_dataset.iloc[i]['wickets'] / max_wicket) *
             (hard_hitter2_dataset.iloc[i]['batsmanRuns']) * (hard_hitter2_dataset.iloc[i]['commentWeight_x'] + hard_hitter2_dataset.iloc[i]['commentWeight_y']) *
             ((hard_hitter2_dataset.iloc[i]['fours'] / max_four) + (hard_hitter2_dataset.iloc[i]['sixes'] / max_six))) / hard_hitter2_dataset.iloc[i]['economy']
    hard_hitter2_dict[hard_hitter2_dataset.iloc[i]['batsman']] = score     
hard_hitter2_val=[]
d5 = defaultdict(float)
for key in hard_hitter2_dict.keys():
    d5[key] = hard_hitter2_dict[key]
for w in sorted(d5, key = d5.get, reverse = True):
    hard_hitter2_val.append([w,d5[w]]) 
for i in range(0, len(hard_hitter2_val)):
    if hard_hitter2_val[i][0] not in playing_team:
        playing_team.append(hard_hitter2_val[i][0])
        expected_runs += math.floor(prediction.hardhitters2_prediction_bat(hard_hitter2_val[i][0]))
        break
    
wk_dict = {}
wk_dataset = WeighPlayers.wicket_keeper  
max_match = wk_dataset.max()['matchCount']
max_four = wk_dataset.max()['fours']
max_six = wk_dataset.max()['sixes']
max_stumps = wk_dataset.max()['stumps']
for i in range(0, len(wk_dataset)):
    score = ((wk_dataset.iloc[i]['matchCount'] / max_match) * (wk_dataset.iloc[i]['stumps'] / max_stumps) *
             (wk_dataset.iloc[i]['batsmanRuns']) * (wk_dataset.iloc[i]['commentWeight_x'] + wk_dataset.iloc[i]['commentWeight_y']) *
             ((wk_dataset.iloc[i]['fours'] / max_four) + (wk_dataset.iloc[i]['sixes'] / max_six)))
    wk_dict[wk_dataset.iloc[i]['batsman']] = score 
wk_val=[]
d6 = defaultdict(float)
for key in wk_dict.keys():
    d6[key] = wk_dict[key]
for w in sorted(d6, key = d6.get, reverse = True):
    wk_val.append([w,d6[w]])    
for i in range(0, len(wk_val)):
    if wk_val[i][0] not in playing_team:
        playing_team.append(wk_val[i][0])
        runs, stumps = prediction.wk_bat_stumps(wk_val[i][0])
        #expected_runs += runs
        expected_stumps = stumps
        break
    
bowl_allrounder_dict = {}
bowl_allrounder_dataset = WeighPlayers.allRounder
max_match_y = bowl_allrounder_dataset.max()['matchCount_y']
max_match_x = bowl_allrounder_dataset.max()['matchCount_x']
max_four = bowl_allrounder_dataset.max()['fours']
max_six = bowl_allrounder_dataset.max()['sixes']
max_wickets = bowl_allrounder_dataset.max()['wickets']
for i in range(0, len(bowl_allrounder_dataset)):
    score = (((bowl_allrounder_dataset.iloc[i]['matchCount_y'] / max_match_y) + (bowl_allrounder_dataset.iloc[i]['matchCount_x'] / max_match_x)) * 
             (bowl_allrounder_dataset.iloc[i]['batsmanRuns']) * (bowl_allrounder_dataset.iloc[i]['ballsBowled']) *
             (bowl_allrounder_dataset.iloc[i]['commentWeight_x'] + bowl_allrounder_dataset.iloc[i]['commentWeight_y']) *
             ((bowl_allrounder_dataset.iloc[i]['fours'] / max_four) + (bowl_allrounder_dataset.iloc[i]['sixes'] / max_six)) *
             (bowl_allrounder_dataset.iloc[i]['wickets'] / max_wickets)) / bowl_allrounder_dataset.iloc[i]['economy']
    bowl_allrounder_dict[bowl_allrounder_dataset.iloc[i]['bowler']] = score
bowl_allrounder_val=[]
d7 = defaultdict(float)
for key in bowl_allrounder_dict.keys():
    d7[key] = bowl_allrounder_dict[key]
for w in sorted(d7, key = d7.get, reverse = True):
    bowl_allrounder_val.append([w,d7[w]])
for i in range(0, len(bowl_allrounder_val)):
    if bowl_allrounder_val[i][0] not in playing_team:
        playing_team.append(bowl_allrounder_val[i][0])
        runs , wickets = prediction.all_rounder_bat_bowl(bowl_allrounder_val[i][0])
        #expected_runs += runs
        expected_wickets += wickets
        break
        
gen_bowl_dict = {}
gen_bowl_dataset = WeighPlayers.general_bowlers
gen_bowl_dataset = gen_bowl_dataset.reset_index()
max_match = gen_bowl_dataset.max()['matchCount']
max_wicket = gen_bowl_dataset.max()['wickets']
for i in range(0,len(gen_bowl_dataset)):
    score = ((gen_bowl_dataset.iloc[i]['matchCount'] / max_match) * (gen_bowl_dataset.iloc[i]['wickets'] / max_wicket) *
            (gen_bowl_dataset.iloc[i]['commentWeight']) * (gen_bowl_dataset.iloc[i]['bowlStrikeRate'])) / gen_bowl_dataset.iloc[i]['economy']
    gen_bowl_dict[gen_bowl_dataset.iloc[i]['bowler']] = score
gen_bowl_val=[]
d8 = defaultdict(float)
for key in gen_bowl_dict.keys():
    d8[key] = gen_bowl_dict[key]
for w in sorted(d8, key = d8.get, reverse = True):
    gen_bowl_val.append([w,d8[w]])
for k in range(0,2):
    for i in range(0, len(gen_bowl_val)):
        if gen_bowl_val[i][0] not in playing_team:
            playing_team.append(gen_bowl_val[i][0])
            expected_wickets += prediction.gen_bowl(gen_bowl_val[i][0])
            break
        
do_bowl_dict = {}
do_bowl_dataset = WeighPlayers.do_specialist
do_bowl_dataset = do_bowl_dataset.reset_index()
max_match = gen_bowl_dataset.max()['matchCount']
max_wicket = gen_bowl_dataset.max()['wickets']
for i in range(0,len(do_bowl_dataset)):
    score = ((do_bowl_dataset.iloc[i]['matchCount'] / max_match) * (do_bowl_dataset.iloc[i]['wickets'] / max_wicket) *
            (do_bowl_dataset.iloc[i]['commentWeight']) * (do_bowl_dataset.iloc[i]['bowlStrikeRate'])) / do_bowl_dataset.iloc[i]['economy']
    do_bowl_dict[do_bowl_dataset.iloc[i]['bowler']] = score
do_bowl_val=[]
d9 = defaultdict(float)
for key in do_bowl_dict.keys():
    d9[key] = do_bowl_dict[key]
for w in sorted(d9, key = d9.get, reverse = True):
    do_bowl_val.append([w,d9[w]])
for k in range(0,2):
    for i in range(0, len(do_bowl_val)):
        if do_bowl_val[i][0] not in playing_team:
            playing_team.append(do_bowl_val[i][0])
            expected_wickets += prediction.gen_bowl(do_bowl_val[i][0])
            break
        
for i in range(0, len(cultured_batsmen_val)):
    if (cultured_batsmen_val[i][0] not in playing_team) and (cultured_batsmen_val[i][0] not in reserve_team):
        reserve_team.append(cultured_batsmen_val[i][0])
        break
for i in range(0, len(hard_hitter1_val)):
    if (hard_hitter1_val[i][0] not in playing_team) and (hard_hitter1_val[i][0] not in reserve_team):
        reserve_team.append(hard_hitter1_val[i][0])
        break
for i in range(0, len(bowl_allrounder_val)):
    if (bowl_allrounder_val[i][0] not in playing_team) and (bowl_allrounder_val[i][0] not in reserve_team):
        reserve_team.append(bowl_allrounder_val[i][0])
        break
for i in range(0, len(do_bowl_val)):
    if (do_bowl_val[i][0] not in playing_team) and (do_bowl_val[i][0] not in reserve_team):
        reserve_team.append(do_bowl_val[i][0])
        break
    
#print(playing_team)
#print(reserve_team)
dream_team = playing_team + reserve_team
print(dream_team)
print(math.floor(expected_runs))
print(math.floor(expected_wickets))
print(math.floor(expected_stumps))