
import pandas as pd
import numpy as np


filename = '2019-20_pbp.csv'

df = pd.read_csv(filename)

print(df)

# Removing violations:
df = df.loc[df['ViolationType'].isna()]

# Removing free throws:
df = df.loc[df['FreeThrowNum'].isna()]

# Removing turnovers:
df = df.loc[df['TurnoverType'].isna()]

# Dropping unnecessary columns:
colNames = ['URL', 'ViolationPlayer', 'ViolationType', 'TimeoutTeam', 'FreeThrowShooter', 
        'FreeThrowOutcome', 'FreeThrowNum', 'EnterGame', 'LeaveGame', 'TurnoverPlayer', 
        'TurnoverType', 'TurnoverCause', 'TurnoverCauser', 'JumpballAwayPlayer', 
        'JumpballHomePlayer', 'JumpballPoss']

df = df.drop(colNames, axis=1)

print(df)

df.to_csv('2019-20_pbp_data.csv', index=False)


