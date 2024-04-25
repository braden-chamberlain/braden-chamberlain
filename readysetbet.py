import numpy as np
from numpy.random import randint


def roll_dice(num_dice=2, sides=6):
    return sum([randint(1,sides+1) for _ in range(num_dice)])


class Horse:
    
    def __init__(self, numbers=[2,3], bonus=3, position=None):
        if position:
            self.position = position
        else:
            self.position = 0
        self.position_history = [(0, self.position)]
        self.movement_history = [(0, 0)]
        self.numbers = numbers # if these numbers are rolled move
        self.bonus = bonus # bonus if rolled twice in a row
        self.won = False
        self.placed = False
        self.showed = False
        
    def move(self, n, current_step=None):
        self.position = np.min([self.position + n, MAX_POSITION])
        if not current_step:
            current_step = self.position_history[-1][0] + 1 # Use the step number of the last recorded step in history + 1
        self.position_history.append((current_step, self.position))
        self.movement_history.append((current_step, n))


class Stable:
    
    def __init__(self, horses, positions=None): # takes a dict of 'name':horse pairs
        self.horses = horses
        self.positions = {name:horse.position for name, horse in self.horses.items()}
        self.step = 0
        
    def update(self, roll): 
        self.step += 1
        for name, horse in self.horses.items():
            if roll in horse.numbers:
                num2move = 1
                if horse.movement_history[-1][1] == 1: # If it also moved last time exactly 1 (no back to back bonus moves)
                    num2move += horse.bonus
                horse.move(num2move, self.step)
            else:
                horse.move(0, self.step)
        self.positions = {name:horse.position for name,horse in self.horses.items()} # Don't forget to keep positions helper variable updated!
        
    def check_over(self):
        for _, horse in self.horses.items():
            if horse.position >= MAX_POSITION:
                return True
        return False


class ReadySetBetGame:
    
    def __init__(self, stable=None):
        if stable:
            self.stable = stable
            self.step = self.stable.step
        else:
            self.stable = Stable({
                '23': Horse(numbers=[2,3], bonus=3),
                '4': Horse(numbers=[4], bonus=3),
                '5': Horse(numbers=[5], bonus=2),
                '6': Horse(numbers=[6], bonus=1),
                '7': Horse(numbers=[7], bonus=0),
                '8': Horse(numbers=[8], bonus=1),
                '9': Horse(numbers=[9], bonus=2),
                '10': Horse(numbers=[10], bonus=3),
                '1112': Horse(numbers=[11,12], bonus=3),
            })

        self.step = 0
        self.over = False
        self.placement = {}
        self.won = None
        self.placed = None
        self.showed = None
        self.roll_history = []
        self.finish_step = 15
        self.race_data = []
        global MAX_POSITION, RED_LINE_POSITION
        MAX_POSITION = self.finish_step                            
        RED_LINE_POSITION = 10
        
    def play_step(self):
        self.step += 1
        roll = roll_dice()
        self.roll_history.append(roll)
        self.stable.update(roll)
        
        # Collect race data
        race_step_data = {
            'step': self.step,
            'roll': roll,
            'positions': self.stable.positions.copy(),
            'bonus': {name: horse.movement_history[-1][1] == 1 for name, horse in self.stable.horses.items()},
        }
        self.race_data.append(race_step_data)
    
    def determine_placement(self):
        positions = self.stable.positions
        current_rank = 1
        self.placement = {}
        self.finish_order = {}
        self.won = []
        self.placed = []
        self.showed = []
        for i in range(MAX_POSITION,-1,-1):
            horses_at_this_position = [name for name, position in positions.items() if position==i]
            
            if horses_at_this_position:
                self.finish_order[current_rank] = horses_at_this_position
                if current_rank == 1: # Win
                    self.won.extend(horses_at_this_position)
                    self.placed.extend(horses_at_this_position)
                    self.showed.extend(horses_at_this_position)
                    for name in horses_at_this_position:
                        self.stable.horses[name].won = True
                elif current_rank == 2: # Place)
                    self.placed.extend(horses_at_this_position)
                    self.showed.extend(horses_at_this_position)
                    for name in horses_at_this_position:
                        self.stable.horses[name].placed = True
                elif current_rank == 3: # Show)
                    self.showed.extend(horses_at_this_position)
                    for name in horses_at_this_position:
                        self.stable.horses[name].showed = True
                current_rank += len(horses_at_this_position)
        
        for place, horse_names in self.finish_order.items():
            for name in horse_names:
                self.placement[name] = place

    def get_stable(self):
        return self.stable
    
    def play_game(self):
        while not self.over:
            self.play_step()
            
            # Check if any horse has reached space 15
            for horse in self.stable.horses.values():
                if horse.position >= 15:
                    self.over = True
                    break  # Exit the loop once a horse reaches space 15
        
        self.determine_placement()

    def get_race_data(self):
        return self.race_data
