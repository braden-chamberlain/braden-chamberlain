from readysetbet import ReadySetBetGame
import pandas as pd
import numpy as np


def create_race_dataframe(all_race_data):
    race_dataframe_list = []
    
    for race_id, race in enumerate(all_race_data, start=1):
        roll_number = 0  # Initialize roll number for each race
        for step_data in race:
            step_data['race_id'] = race_id
            
            # Transform positions dictionary into separate columns
            for horse, position in step_data['positions'].items():
                step_data[f'horse_{horse.replace("/", "_")}'] = position
            
            # Convert bonus dictionary to single column and bonus_value
            bonus_horses = [horse for horse, bonus in step_data['bonus'].items() if bonus]
            bonus_horse = bonus_horses[0] if bonus_horses else '0'
            step_data['bonus'] = bonus_horse
            step_data['bonus_value'] = game.stable.horses[bonus_horse].bonus if bonus_horse != '0' else 0
            
            # Convert bonus column to numeric
            if bonus_horse == '2/3':
                step_data['bonus'] = 3
            elif bonus_horse == '11/12':
                step_data['bonus'] = 11
            else:
                step_data['bonus'] = int(bonus_horse)
            
            roll_number += 1  # Increment roll number for each step
            step_data['roll_number'] = roll_number  # Add roll_number column
            
            race_dataframe_list.append(step_data)
    
    race_dataframe = pd.DataFrame(race_dataframe_list)
    
    # Reorganize columns as per the specified order
    columns_order = ['race_id', 'step', 'roll', 'roll_number'] + [f'horse_{horse.replace("/", "_")}' for horse in game.stable.horses.keys()] + ['bonus', 'bonus_value']
    race_dataframe = race_dataframe[columns_order]
    
    return race_dataframe

# Run multiple races
num_races = 10
all_race_data = []
count = 0 

for _ in range(num_races):
    game = ReadySetBetGame()
    count += 1
    game.play_game()
    all_race_data.append(game.get_race_data())
    print(f"game({count}) over")


# Create DataFrame from all race data
df = create_race_dataframe(all_race_data)

print(df.head())