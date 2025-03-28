#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 8 14:44:33 2024
Based on: https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023
Sample input: --filter="ARTIST" --value="Dua Lipa" --order_by="STREAMS" --order="ASC" --limit="6"'
@author: rivera
@author: Jay Robertson
"""
import pandas as pd
from pandas import DataFrame as df
import datetime as dt
import sys

DATA_INDEX:int = 1
ARGV_START:str = "--"
ARGV_END:str = "="
OUTPUT_FILE:str = "output.csv"

#dictionary of possible filters and their corresponding columns
FILTERS:dict = {"STREAMS":"streams", "ARTIST":"artist(s)_name", "YEAR":"released_year"}

#dictionary of possible orders and their corresponding columns
ORDERS:dict = {"STREAMS":"streams", "NO_SPOTIFY_PLAYLISTS":"in_spotify_playlists", "NO_APPLE_PLAYLISTS":"in_apple_playlists"}

#list of unused columns from a given csv file
NOT_USED:list = ['bpm','key','mode','danceability_%', "artist_count"]

def main() -> None:
    '''Main entry point of the program.'''
    arguments:dict = get_args()
    song_data:df = create_frame(arguments["data"])
    formatted_data:df = format_frame(song_data, arguments)
    
    #Write out to file without index nums
    formatted_data.to_csv(OUTPUT_FILE, index=False)

def get_args() -> dict:
    ''' 
    creates and returns a dictionary of arguments formatted as --key="val" 
    (ex.--value="Drake") passed from STDIN
            Parameters: NONE
            Returns: 
                  arg_dict (dict) - a dictionary of all valid arguments passed 
                                    to STDIN; formatted as {key:val,...}
    '''    
    arg_dict:dict = {} 
    
    for index in range(DATA_INDEX, len(sys.argv)): #range [first arg, last arg]
        cur_arg:str = sys.argv[index] 
        
        #get part of cur arg between -- and = (the key)
        cur_key:str = cur_arg[cur_arg.find(ARGV_START)+len(ARGV_START):cur_arg.find(ARGV_END)]
        
        #get part of cur arg between = and end (the val)
        cur_val:str = cur_arg[cur_arg.find(ARGV_END)+len(ARGV_END):]
        arg_dict[cur_key] = cur_val
        
    return arg_dict

def create_frame(name:str) -> df:
    ''' creates a pandas DataFrame song_data_df from a file named name
            Parameters: 
                  name (str) - the name of a file to read from
            Returns: 
                  song_data_df (pd.DataFrame) - a pandas DataFrame created
                                                from the file specified by name
    '''
    song_data_df:df = pd.read_csv(name)
    
    #remove unused columns
    song_data_df.drop(NOT_USED, inplace=True, axis=1)
    
    return song_data_df

def get_dateframe(row:df) -> str:
    ''' 
    creates a dataframe with rows of release dates from frame formatted as: 
    "Weekday:str, Month:str Day:int, Year:int" where the weekday is concatenated. 
    (Example: "Thu, May 25, 2023")
            Parameters: 
                  row (pd.DataFrame) - the row of a DataFrame with at least columns 
                                       "released_year", "released_month", and "released_day"
            Returns: 
                  formatted_dates (str) - a date string formatted as above
                 
    ''' 
    #get date info from cur row
    year:int = int(row["released_year"])
    month:int = int(row["released_month"])
    day:int = int(row["released_day"])
    
    #get datestr formatted as "Weekday:str, Month:str Day:int, Year:int"
    formatted_dates:str = dt.date(year, month, day).strftime("%a, %B %d, %Y")

    return formatted_dates

def format_frame(frame:df, args:dict) -> df:
    ''' 
    formats frame (filters, orders, limits, and slims) based on the 
    specifications in args
            Parameters: 
                  frame (pd.DataFrame) - a pandas DataFrame to format
                  args (dict) - a dictionary of specifications for filtering
                                containing at least "order_by" and "order"
            Returns: 
                  frame (pd.DataFrame) - a version offrame formatted by 
                                         specifications in args
    '''  
    by_what:str = ''
    
    #filter rows in a column if required
    if args.get("filter") != None:
        frame = filter_frame(frame, args.get("filter"), args.get("value"))
    
    #order rows in a column
    by_what, frame = order_frame(frame, args["order_by"], args["order"])
    
    #limit the number of rows if required
    if args.get("limit") != None:
        frame = frame.head(int(args["limit"]))
    
    #create new column called "released" with formatted dates
    frame["released"] = frame.apply(get_dateframe, axis=1) 
    
    #remove excess columns and order columns
    frame = frame[["released","track_name", "artist(s)_name", by_what]]
    
    return frame

def filter_frame(frame:df, filt:str, val:str) -> df:
    ''' 
    iterate through possible filters to determine what column to filter, then 
    filters frame based on a given a filt and val
            Parameters: 
                  frame (pd.DataFrame) - a pandas DataFrame to filter
                  filt (str) - a filter type corresponding to a column to filter; 
                               must be a key option in FILTERS (global constant) 
                  val (str) - a value to filter frame by; only values which either
                              contain or are the same as this (depending on filt)
                              will be kept                 
            Returns: 
                  frame (pd.DataFrame) - a filtered version of frame, with only 
                                         rows which contain/equal val in column
                                         corresponding to filt
    '''  
    for key in FILTERS: #each key in FILTERS corresponds to a column to filter
        if filt == key: 
            filter_by:str = FILTERS[key] 
            break;
          
    if filt == "ARTIST": 
        #if filtering by ARTIST, keep if val artist is one of artist in row
        frame = frame[frame[filter_by].str.contains(val)] 
    else:
        frame = frame[frame[filter_by] == int(val)]
    
    return frame

def order_frame(frame:df, order_by:str, order:str) -> df:
    ''' 
    iterate through possible orders to determine what column to order, then order
    in direction of order
            Parameters: 
                  frame (pd.DataFrame) - a pandas DataFrame to order
                  order_by (str) - an order type corresponding to a column to order; 
                                   must be a key option in ORDERS (global constant) 
                  order (str) - the order to list values in ordered column by;
                                either "DES" or "ASC"
            Returns: 
                  by_what (str) - name of the column that was ordered 
                  frame (pd.DataFrame) - a version of frame with column corresponding
                                         to order_by ordered in order given by order
    '''  
    for key in ORDERS: #each key in ORDERS corresponds to a column to order
        if order_by == key: 
            by_what:str = ORDERS[key]
            break;
    
    is_ascending:bool = (False if order == "DES" else True)
    frame = frame.sort_values(by=by_what, ascending=is_ascending, ignore_index = True, axis = 0)
    
    return by_what, frame


if __name__ == '__main__':
    main()

