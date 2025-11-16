import pandas as pd
df= pd.read_csv('C:/Users/Lenovo/OneDrive/Desktop/DAY-2/Mini Project/ipl-matches.csv')
#display
#print(df)

#display the first 5 rows
#print(df.head())
#show no.of rows and cols
#print(df.shape)

#task2

#list all unique seasons and teams
#print(df['Season'].unique())
#print(df['Team1'].unique())

#how many matches were played per season?
#print(df['Season'].value_counts())

#Which team has won the most matches?
#print(df['WinningTeam'].value_counts().head(1))

#Show matches where Mumbai Indians were the winner
#print(df['WinningTeam'][df['WinningTeam']=='Mumbai Indians'])

#Show all the matches were there have been a super over
print(df[df['SuperOver']=='Y'])

#show matches held at "Eden Garden"
print(df[df['Venue']=='Eden Gardens'])

#show many super over finishes have occured
#check if toss winner is match winner in percentage
print((df[(df['TossWinner'])==(df['WinningTeam'])]).shape[0]/(df.shape[0])*100)
