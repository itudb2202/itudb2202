import pandas as pd
    


#       ----------STATS---------
data = pd.read_csv("Basic_Stats.csv")
for inr in data.index:
    row = data.iloc[inr]
    insertValues = ""
    column_index = 0
    for column_name in data.columns:
        if (column_index != len(data.columns) - 1):
            insertValues = insertValues + str(row[column_name])+","
        else:
            insertValues = insertValues + str(row[column_name])
        column_index = column_index + 1
    statement = "INSERT INTO basic_stats VALUES (%s)" % insertValues
    
#       ---------DEFENSIVE---------
data = pd.read_csv("Career_Stats_Defensive.csv")
column_names = ["Player Id", "Year", "Team", "Games Played", "Total Tackles", "Solo Tackles",
                "Assisted Tackles","Passes Defended","Ints","Yards Per Int"]
for data_column in data.columns:
    if data_column not in column_names:
        data.drop(data_column, inplace = True, axis=1)
for inr in data.index:
    row = data.iloc[inr]
    insertValues = ""
    column_index = 0
    for column_name in column_names:
        if (column_index != len(column_names) - 1):
            insertValues = insertValues + str(row[column_name])+","
        else:
            insertValues = insertValues + str(row[column_name])
        column_index = column_index + 1
    statement = "INSERT INTO career_stats_defensive VALUES (%s)" % insertValues

#       ----------RECEIVING---------
data = pd.read_csv("Career_Stats_Receiving.csv")
column_names = ["Player Id", "Year", "Team", "Games Played", "Receptions", "Receiving Yards",
                "Yards Per Reception","Yards Per Game"]
for data_column in data.columns:
    if data_column not in column_names:
        data.drop(data_column, inplace = True, axis=1)
for inr in data.index:
    row = data.iloc[inr]
    insertValues = ""
    column_index = 0
    for column_name in column_names:
        if (column_index != len(column_names) - 1):
            insertValues = insertValues + str(row[column_name])+","
        else:
            insertValues = insertValues + str(row[column_name])
        column_index = column_index + 1
    statement = "INSERT INTO career_stats_receiving VALUES (%s)" % insertValues

#       ----------PUNTING---------
data = pd.read_csv("Career_Stats_Punting.csv")
column_names = ["Player Id", "Year", "Team", "Games Played", "Punts", "Gross Punting Yards",
                "Longest Punt","Fair Catches"]
for data_column in data.columns:
    if data_column not in column_names:
        data.drop(data_column, inplace = True, axis=1)
for inr in data.index:
    row = data.iloc[inr]
    insertValues = ""
    column_index = 0
    for column_name in column_names:
        if (column_index != len(column_names) - 1):
            insertValues = insertValues + str(row[column_name])+","
        else:
            insertValues = insertValues + str(row[column_name])
        column_index = column_index + 1
    statement = "INSERT INTO career_stats_punting VALUES (%s)" % insertValues
    


   