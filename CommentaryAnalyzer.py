# -*- coding: utf-8 -*-
"""
Created on Mon May 14 21:00:51 2018

@author: Abhirup Sinha
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import warnings

warnings.filterwarnings("ignore")

players = pd.read_csv('cleaned-data.csv', skipinitialspace=True, usecols=['batsman', 'bowler', 'fielder'])
players = list(set(players['batsman']).union(set(players['bowler']).union(set(players['fielder']))))
players = list(set([name for player in players if isinstance(player, str) for name in player.split()]))

commentary = pd.read_csv('cleaned-data.csv')['comment']
commentary = [' '.join([word if word not in players else "" for word in comment.split()]) for comment in commentary]

vectorizer = TfidfVectorizer(decode_error='ignore', analyzer='word', stop_words='english', lowercase=True,
                             token_pattern='[a-z]{3,}')
weight_matrix = vectorizer.fit_transform(commentary)
dictionary = {i[1]: i[0] for i in vectorizer.vocabulary_.items()}
word_weights = [{dictionary[column]: value for (column, value) in zip(row.indices, row.data)} for row in weight_matrix]
#print(word_weights)