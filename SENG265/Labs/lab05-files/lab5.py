#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd

def main():
    #read files
    drivers_df: pd.DataFrame = pd.read_csv('drivers.csv')
    results_df: pd.DataFrame = pd.read_csv('results.csv')
    
    #make it so drivers_df has only driverid and nationality
    drivers_df.drop(['driverRef', 'number', 'code', 'forename','surname','dob', 'url'], inplace=True, axis=1)
    
    #make it so results_df has only resultid, driverId, and positionOrder
    results_df.drop(['raceId', 'constructorId', 'number', 'grid', 'position', 'positionText', 'points',
    'laps', 'time', 'milliseconds', 'fastestLap', 'rank', 'fastestLapTime', 'fastestLapSpeed', 'statusId'],
    inplace=True, axis=1)    
    
    #Only winners in first place
    results_df = results_df[results_df['positionOrder'] == 1]
    
    #merge drivers_df and results_df via the same driverId
    merged_df: pd.DataFrame = results_df.merge(drivers_df, on='driverId', how='left')
    
    #answer: a list of the top 10 nationalities with the most amount of wins
    answer: pd.DataFrame = merged_df.groupby(['nationality'],as_index=False).size().sort_values(by='size', ascending=False, ignore_index=True).head(10)
    print(answer)    

if __name__ == "__main__":
    main()
