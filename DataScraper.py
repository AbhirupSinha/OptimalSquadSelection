# -*- coding: utf-8 -*-
"""
Created on Mon May 14 18:22:50 2018

@author: Abhirup Sinha
"""

import requests, csv
import warnings

warnings.filterwarnings("ignore")
url = "http://site.api.espn.com/apis/site/v2/sports/cricket/8048/playbyplay"
data = {}

for year in range(2015, 2018):
    if year == 2015:
        start = 829705
        end = 829824
        step = 2
    elif year == 2016:
        start = 980901
        end = 981020
        step = 2
    elif year == 2017:
        start = 1082591
        end = 1082651
        step = 1

    for match in range(start, end, step):
        data[match] = {1: [], 2: []}
        for innings in range(1, 3):
            for page in range(1, 7):
                params = dict(
                    contentorigin='espn',
                    event=match,
                    page=page,
                    period=innings,
                    section='cricinfo'
                )
                r = requests.get(url=url, params=params)
                if 'commentary' in dict(r.json().items()).keys():
                    cp = dict(r.json().items())['commentary']['items']
                    if cp:
                        data[match][innings].extend(cp)
                else:
                    data.pop(match, None)

cleaneddata = []

for match in list(data.keys()):
    for inning in data[match]:
        for delivery in data[match][inning]:
            try:
                cleaneddata.append(dict(over=delivery['over']['actual'],
                                        batsman=delivery['batsman']['athlete']['name'],
                                        batsmanTeam=delivery['batsman']['team']['name'],
                                        strikeRate=100*delivery['batsman']['totalRuns'] / float(
                                            1 if delivery['batsman']['faced'] == 0 else delivery['batsman']['faced']),
                                        fours=delivery['batsman']['fours'],
                                        sixes=delivery['batsman']['sixes'],
                                        bowler=delivery['bowler']['athlete']['name'],
                                        bowlerTeam=delivery['bowler']['team']['name'],
                                        ballsBowled=delivery['bowler']['balls'],
                                        economy=delivery['bowler']['conceded'] / float(
                                            1 if delivery['bowler']['overs'] == 0 else delivery['bowler']['overs']),
                                        maidens=delivery['bowler']['maidens'],
                                        wickets=delivery['bowler']['wickets'],
                                        playType=delivery['playType']['description'],
                                        dismissal=delivery['dismissal']['dismissal'],
                                        dismissalType=delivery['dismissal']['type'],
                                        fielder=delivery['athletesInvolved'][0]['name'] if len(delivery['athletesInvolved']) == 3 else "",
                                        nonStriker=delivery['otherBatsman']['athlete']['name'],
                                        score=delivery['innings']['runs'],
                                        fallOfWickets=delivery['innings']['fallOfWickets'],
                                        runs=delivery['scoreValue'],
                                        runRate=delivery['innings']['runRate'],
                                        remainingBalls=delivery['innings']['remainingBalls'],
                                        comment=delivery['text'] if ('text' in delivery.keys()) else ''))
            except KeyError as err:
                print(err)

with open('cleaned-data.csv', 'w') as f:
    dict_writer = csv.DictWriter(f, cleaneddata[0].keys())
    dict_writer.writeheader()
    dict_writer.writerows(cleaneddata)
