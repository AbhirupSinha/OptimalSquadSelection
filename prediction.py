# -*- coding: utf-8 -*-
"""
Created on Wed May 16 21:55:30 2018

@author: Abhirup Sinha
"""

"""
for batsmen: we predict expected run he can score
for bowlers: we predict expected no. of wickets he can take
for wicketkeepers: we predict expected no. of stumps
"""

import WeighPlayers
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
import warnings

warnings.filterwarnings("ignore")

def crusher_prediction_bat(name):
    crushers_dataset = WeighPlayers.crushers
    crushers_dataset = crushers_dataset.reset_index()
    
    X = crushers_dataset.loc[:, ['batsman','matchCount','strikeRate','ballsFaced','commentWeight']]
    #X = X.drop(labels = 'matchCount', axis = 1)
    X = X.drop(labels = 'batsman', axis = 1)
    X_val = X.values
    Y = crushers_dataset.loc[:, ['averageRunsScored']]
    Y_val = Y.values
    
    #X_train, X_test, Y_train, Y_test = train_test_split(X_val, Y_val, test_size = 0.1, random_state = 0)
    X_train, X_test, Y_train, Y_test = train_test_split(X_val, Y_val, test_size = 0.3)
     
    regressor = LinearRegression()
    regressor.fit(X_train, Y_train)
    
    x_pred = crushers_dataset.loc[crushers_dataset['batsman'] == name].drop(labels = 'batsman', axis = 1)
    x_pred = x_pred.loc[:,['matchCount','strikeRate','ballsFaced','commentWeight']]
    y_pred = regressor.predict(x_pred.values)
    #print("Crusher Score:" + str(regressor.score(X_test, Y_test)))
    return y_pred[0][0]
    
def delacquerers_prediction_bat(name):
    delacquerers_dataset = WeighPlayers.delacquerers
    delacquerers_dataset = delacquerers_dataset.reset_index()
    
    X = delacquerers_dataset.loc[:, ['batsman','matchCount','ballsFaced','commentWeight']]
    #X = X.drop(labels = ['matchCount'], axis = 1)
    X = X.drop(labels = 'batsman', axis = 1)
    X_val = X.values
    Y = delacquerers_dataset.loc[:, ['batsmanRuns']]
    Y_val = Y.values
    
    #X_train, X_test, Y_train, Y_test = train_test_split(X_val, Y_val, test_size = 0.15, random_state = 0)
    X_train, X_test, Y_train, Y_test = train_test_split(X_val, Y_val, test_size = 0.15)
    
    regressor = LinearRegression()
    regressor.fit(X_train, Y_train)
    
    x_pred = delacquerers_dataset.loc[delacquerers_dataset['batsman'] == name].drop(labels = 'batsman', axis = 1)
    x_pred = x_pred.loc[:,['matchCount','ballsFaced','commentWeight']]
    y_pred = regressor.predict(x_pred.values)
    #print("Delacquer Score:" + str(regressor.score(X_test, Y_test)))
    return y_pred[0][0]
    
def culturedbatsmen_prediction_bat(name):
    culturedbatsmen_dataset = WeighPlayers.cultured_batsmen
    culturedbatsmen_dataset = culturedbatsmen_dataset.reset_index()
    
    X = culturedbatsmen_dataset.loc[:, ['batsman','matchCount','ballsFaced','commentWeight']]
    X = X.drop(labels = ['matchCount', 'batsman'], axis = 1)
    #X = pd.get_dummies(X, columns = ['batsman'])
    X_val = X.values
    Y = culturedbatsmen_dataset.loc[:, ['batsmanRuns']]
    Y_val = Y.values
    
    X_train, X_test, Y_train, Y_test = train_test_split(X_val, Y_val, test_size = 0.1, random_state = 7)
    
    #regressor = RandomForestRegressor(random_state = 16, criterion = 'mae',n_estimators = 9)
    regressor = LinearRegression()
    regressor.fit(X_train, Y_train)
    
    x_pred = culturedbatsmen_dataset.loc[culturedbatsmen_dataset['batsman'] == name].drop(labels = 'batsman', axis = 1)
    x_pred = x_pred.loc[:,['ballsFaced','commentWeight']]
    y_pred = regressor.predict(x_pred.values)
    #print("Cultured Batsman Score:" + str(regressor.score(X_test, Y_test)))
    return y_pred[0]
    """
    parameters = [{'n_estimators':[5,7,10],'criterion':['mse','mae'], 'warm_start':[True,False],
                   'max_features':['auto','sqrt','log2'],'random_state':[10,15,20],
                   'min_samples_split':[2,4,8],'min_samples_leaf':[2,4,8]}]
    grid_search = GridSearchCV(estimator = regressor, param_grid = parameters, cv = 5)
    grid_search = grid_search.fit(X_train, Y_train)
    print(grid_search.best_score_)
    print(grid_search.best_params_)
    """
    
def hardhitters1_prediction_bat(name):
    hardhitters1_dataset = WeighPlayers.hard_hitters
    hardhitters1_dataset = hardhitters1_dataset.reset_index()
    
    X = hardhitters1_dataset.loc[:, ['batsman','matchCount','ballsFaced','commentWeight']]
    #X = X.drop(labels = ['matchCount'], axis = 1)
    #X = pd.get_dummies(X, columns = ['batsman'])
    X = X.drop(labels = 'batsman', axis = 1)
    X_val = X.values
    Y = hardhitters1_dataset.loc[:, ['batsmanRuns']]
    Y_val = Y.values
    
    #X_train, X_test, Y_train, Y_test = train_test_split(X_val, Y_val, test_size = 0.2, random_state = 0)
    X_train, X_test, Y_train, Y_test = train_test_split(X_val, Y_val, test_size = 0.1)
    
    regressor = LinearRegression()
    regressor.fit(X_train, Y_train)
    
    x_pred = hardhitters1_dataset.loc[hardhitters1_dataset['batsman'] == name].drop(labels = 'batsman', axis = 1)
    x_pred = x_pred.loc[:,['matchCount','ballsFaced','commentWeight']]
    y_pred = regressor.predict(x_pred.values)
    #print("Hard Hitter 1 Score:" + str(regressor.score(X_test, Y_test)))
    return y_pred[0][0]
    
def hardhitters2_prediction_bat(name):
    hardhitters2_dataset = WeighPlayers.hard_hitters2
    
    X_bat = hardhitters2_dataset.loc[:, ['batsman','matchCount_x','ballsFaced','commentWeight_x']]
    #X_bat = pd.get_dummies(X_bat, columns = ['batsman'])
    X_bat = X_bat.drop(labels = 'batsman', axis = 1)
    X_bat_val = X_bat.values
    Y_bat = hardhitters2_dataset.loc[:, ['batsmanRuns']]
    Y_bat_val = Y_bat.values
    
    #X_bat_train, X_bat_test, Y_bat_train, Y_bat_test = train_test_split(X_bat_val, Y_bat_val, test_size = 0.1, random_state = 0)
    X_bat_train, X_bat_test, Y_bat_train, Y_bat_test = train_test_split(X_bat_val, Y_bat_val, test_size = 0.1)
       
    #regressor_bat = RandomForestRegressor(random_state = 12, n_estimators = 5)
    regressor_bat = RandomForestRegressor()
    regressor_bat.fit(X_bat_train, Y_bat_train)
    
    x_pred = hardhitters2_dataset.loc[hardhitters2_dataset['batsman'] == name].drop(labels = 'batsman', axis = 1)
    x_pred = x_pred.loc[:,['matchCount_x','ballsFaced','commentWeight_x']]
    y_pred = regressor_bat.predict(x_pred.values)
    #print("Hard Hitter 2 Score (bat):" + str(regressor_bat.score(X_bat_test, Y_bat_test)))
    return y_pred[0]
    """
    parameters = [{'n_estimators':[5,10,15],'criterion':['mse','mae'], 'warm_start':[True,False],
                   'max_features':['auto','sqrt','log2'],'random_state':[0,10,15],
                   'min_samples_split':[2,4,8],'min_samples_leaf':[1,2,4,8]}]
    grid_search = GridSearchCV(estimator = regressor_bat, param_grid = parameters, cv = 5)
    grid_search = grid_search.fit(X_bat_train, Y_bat_train)
    print(grid_search.best_score_)
    print(grid_search.best_params_)"""
    """
    #bowling prediction for wicket taking is of no good
    X_bowl = hardhitters2_dataset.iloc[:, ['bowler','matchCount_y','economy','commentWeight_y']]
    X_bowl = X_bowl.drop(labels = ['bowler'], axis = 1)
    X_bowl_val = X_bowl.values
    Y_bowl = hardhitters2_dataset.iloc[:, ['wickets']]
    Y_bowl_val = Y_bowl.values
    
    from sklearn.cross_validation import train_test_split
    X_bowl_train, X_bowl_test, Y_bowl_train, Y_bowl_test = train_test_split(X_bowl_val, Y_bowl_val, test_size = 0.1, random_state = 0)
    
    regressor_bowl = DecisionTreeRegressor(random_state = 0)
    regressor_bowl.fit(X_bowl_train, Y_bowl_train)
    
    y_bowl_pred = regressor_bowl.predict(X_bowl_test)
    print("Hard Hitter 2 Score (bowl):" + str(regressor_bowl.score(X_bowl_test, Y_bowl_test)))
    """
def wk_bat_stumps(name):
    wk_dataset = WeighPlayers.wicket_keeper
    X_bat = wk_dataset.loc[:, ['matchCount','ballsFaced','commentWeight_y','batsman']]
    Y_bat = wk_dataset.loc[:, ['batsmanRuns']]
    X_bat = X_bat.drop(labels = ['batsman'], axis = 1)
    X_bat_val = X_bat.values
    Y_bat_val = Y_bat.values
    
    #X_bat_train, X_bat_test, Y_bat_train, Y_bat_test = train_test_split(X_bat_val, Y_bat_val, test_size = 0.12, random_state = 0)
    X_bat_train, X_bat_test, Y_bat_train, Y_bat_test = train_test_split(X_bat_val, Y_bat_val, test_size = 0.1)
    
    regressor_bat = LinearRegression()
    regressor_bat.fit(X_bat_train, Y_bat_train)
    
    x_bat_pred = wk_dataset.loc[wk_dataset['batsman'] == name].drop(labels = 'batsman', axis = 1)
    x_bat_pred = x_bat_pred.loc[:,['matchCount','ballsFaced','commentWeight_y']]
    y_bat_pred = regressor_bat.predict(x_bat_pred.values)
    #print("WK Score (bat):" + str(regressor_bat.score(X_bat_test, Y_bat_test)))
    
    X_stumps = wk_dataset.loc[:, ['fielder','commentWeight_x','matchCount']]
    Y_stumps = wk_dataset.loc[:, ['stumps']]
    X_stumps = X_stumps.drop(labels =['fielder'], axis = 1)
    X_stumps_val = X_stumps.values
    Y_stumps_val = Y_stumps.values
    
    X_stumps_train, X_stumps_test, Y_stumps_train, Y_stumps_test = train_test_split(X_stumps_val, Y_stumps_val, test_size = 0.1, random_state = 0)
    
    regressor_stumps = DecisionTreeRegressor(random_state = 4) 
    #if min_samples_split = 3 or min_samples_leaf = 2 then R^2 = 1.0, so keeping the default values 2 & 1 respectively
    regressor_stumps.fit(X_stumps_train, Y_stumps_train)
    
    x_stumps_pred = wk_dataset.loc[wk_dataset['fielder'] == name].drop(labels = 'fielder', axis = 1)
    x_stumps_pred = x_stumps_pred.loc[:,['matchCount','commentWeight_x']]
    y_stumps_pred = regressor_stumps.predict(x_stumps_pred.values)
    #print("WK Score (Stumps):" + str(regressor_stumps.score(X_stumps_test, Y_stumps_test)))
    return y_bat_pred[0], y_stumps_pred[0]
    
def do_specialist_bowl(name):
    do_dataset = WeighPlayers.do_specialist
    do_dataset = do_dataset.reset_index()
    
    X = do_dataset.loc[:,['bowler','matchCount','economy','ballsBowled','commentWeight','bowlStrikeRate']]
    X = X.drop(labels = ['bowler'], axis = 1)
    #X = pd.get_dummies(X, columns = ['bowler'])
    Y = do_dataset.loc[:, ['wickets']]
    X_val = X.values
    Y_val = Y.values
    
    X_train, X_test, Y_train, Y_test = train_test_split(X_val, Y_val, test_size = 0.15, random_state = 0)
    
    regressor = LinearRegression()
    regressor.fit(X_train, Y_train)
    
    x_pred = do_dataset.loc[do_dataset['bowler'] == name].drop(labels = 'bowler', axis = 1)
    x_pred = x_pred.loc[:,['matchCount','economy','ballsBowled','commentWeight','bowlStrikeRate']]
    y_pred = regressor.predict(x_pred)
    #print("Death Over Bowlers Score:" + str(regressor.score(X_test, Y_test)))
    return y_pred[0][0]
    
def gen_bowl(name):
    gen_bowl_dataset = WeighPlayers.general_bowlers
    gen_bowl_dataset = gen_bowl_dataset.reset_index()
    
    X = gen_bowl_dataset.loc[:,['bowler','matchCount','economy','ballsBowled','commentWeight','bowlStrikeRate']]
    X = X.drop(labels = ['bowler'], axis = 1)
    #X = pd.get_dummies(X, columns = ['bowler'])
    Y = gen_bowl_dataset.loc[:, ['wickets']]
    X_val = X.values
    Y_val = Y.values
       
    X_train, X_test, Y_train, Y_test = train_test_split(X_val, Y_val, test_size = 0.15, random_state = 0)
    
    regressor = LinearRegression()
    regressor.fit(X_train, Y_train)
    
    x_pred = gen_bowl_dataset.loc[gen_bowl_dataset['bowler'] == name].drop(labels = 'bowler', axis = 1)
    x_pred = x_pred.loc[:,['matchCount','economy','ballsBowled','commentWeight','bowlStrikeRate']]
    y_pred = regressor.predict(x_pred)
    #print("General Bowlers Score:" + str(regressor.score(X_test, Y_test)))
    return y_pred[0][0]
    
def all_rounder_bat_bowl(name):
    all_rounder_dataset = WeighPlayers.allRounder
    
    all_rounder_bat_dataset = all_rounder_dataset.loc[:, ['matchCount_x','batsmanRuns','ballsFaced','commentWeight_x','batsman']]
    all_rounder_bat_dataset = all_rounder_bat_dataset.drop(labels = ['batsman'], axis = 1)
    X_bat = all_rounder_bat_dataset.loc[:, ['matchCount_x','ballsFaced','commentWeight_x']]
    X_bat_val = X_bat.values
    Y_bat = all_rounder_bat_dataset.loc[:, ['batsmanRuns']]
    Y_bat_val = Y_bat.values
    
    X_bat_train, X_bat_test, Y_bat_train, Y_bat_test = train_test_split(X_bat_val, Y_bat_val, test_size = 0.15, random_state = 0)
    
    regressor_bat = LinearRegression()
    regressor_bat.fit(X_bat_train, Y_bat_train)
    
    x_bat_pred = all_rounder_dataset.loc[all_rounder_dataset['batsman'] == name].drop(labels = 'batsman', axis = 1)
    x_bat_pred = x_bat_pred.loc[:,['matchCount_x','ballsFaced','commentWeight_x']]
    y_bat_pred = regressor_bat.predict(x_bat_pred.values)
    #print("Bowling All Rounder Score (bat):" + str(regressor_bat.score(X_bat_test, Y_bat_test)))
    
    all_rounder_bowl_dataset = all_rounder_dataset.loc[:, ['matchCount_y','economy','commentWeight_y','bowler','wickets','ballsBowled']]
    all_rounder_bowl_dataset = all_rounder_bowl_dataset.drop(labels = ['bowler'], axis = 1)
    X_bowl = all_rounder_dataset.loc[:, ['matchCount_y','economy','commentWeight_y']]
    X_bowl_val = X_bowl.values
    Y_bowl = all_rounder_dataset.loc[:, ['wickets']]
    Y_bowl_val = Y_bowl.values
    
    X_bowl_train, X_bowl_test, Y_bowl_train, Y_bowl_test = train_test_split(X_bowl_val, Y_bowl_val, test_size = 0.15, random_state = 0)
    
    regressor_bowl = DecisionTreeRegressor(random_state = 9)
    regressor_bowl.fit(X_bowl_train, Y_bowl_train)
    
    x_bowl_pred = all_rounder_dataset.loc[all_rounder_dataset['bowler'] == name].drop(labels = 'bowler', axis = 1)
    x_bowl_pred = x_bowl_pred.loc[:,['matchCount_y','economy','commentWeight_y']]
    y_bowl_pred = regressor_bowl.predict(x_bowl_pred)
    #print("Bowling All Rounder Score (bowl):" + str(regressor_bowl.score(X_bowl_test, Y_bowl_test)))
    return y_bat_pred[0], y_bowl_pred[0]
"""    
crusher_prediction_bat() 
delacquerers_prediction_bat()
culturedbatsmen_prediction_bat()
hardhitters1_prediction_bat()
hardhitters2_prediction_bat()
wk_bat_stumps()
all_rounder_bat_bowl()
gen_bowl()
do_specialist_bowl()
"""