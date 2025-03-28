import pandas as pd

def main():
    #read the files
    drivers_df: pd.DataFrame = pd.read_csv('drivers.csv')
    results_df: pd.DataFrame = pd.read_csv('results.csv')
    
    #remove uncecessary columns in drivers.csv
    drivers_df.drop(['driverRef', 'number', 'code', 'dob', 'nationality', 'url'], inplace=True, axis=1)
    
    #remove unnecessary columns in results.csv
    results_df.drop(['raceId', 'constructorId', 'number', 'grid', 'position', 'positionText', 'points',
    'laps', 'time', 'milliseconds', 'fastestLap', 'rank', 'fastestLapTime', 'fastestLapSpeed', 'statusId'],
    inplace=True, axis=1)    
     
    print(drivers_df.head())
    #prints resultID, driverID, and positionOrder
    
    #filtering rows
    results_df = results_df[results_df['positionOrder'] == 1]
    
    print(results_df)
    #only prints rows with the positionOrder "1" (the ones in first)
    
    merged_df: pd.DataFrame = results_df.merge(drivers_df, on='driverId', how='left')
    #merges two different data frames
    #whenever you find similar data in driverId, add the correponding data from driver_df to merged_df
    
    #grouping
    answer: pd.DataFrame = merged_df.groupby(['driverId', 'forename', 'surname'],as_index=False).size().sort_values(by='size', ascending=False).head(20)
    print(answer)
    #Create a column called size that tracks the amount of times a driver appears
    #in merged_df and creates a new DataFrame with each name only once
    
    #ASSIGNMENT: filter data so we only get nationality
    #merge with results
    #group results and count
    #select top 10
    
    if __name__ == "__main__":
        main()    