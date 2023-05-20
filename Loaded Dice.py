import numpy as np
import math
import matplotlib.pyplot as plt


### Numbers of rolls
roll = 10

def dice(roll):
    return np.random.randint(1, high=7, size=roll)

def loaded_dice(roll):
    faces = [4,5,5,6,6,6]
    position = np.random.randint(1, high=7, size=roll)

    out = np.zeros(roll, dtype=int)
    for i in range(roll):
        out[i] = faces[position[i]-1]
    return out

def difference(num1,num2):
    return math.sqrt(num1**2 + num2**2)

### Define dices

dice1 = dice(roll)
dice2 = dice(roll)

### Mean

dice1_mean = np.mean(dice1)
dice2_mean = np.mean(dice2)
mean_difference = difference(dice1_mean, dice2_mean).__round__(3)
print(f'Old values of means:\n#rolls = {roll}\nDice 1 mean = {dice1_mean}'
      f'\nDice 2 mean = {dice2_mean}\nMean difference = {mean_difference}')


### Increasing number of rolls -> means became similar
new_roll = 100

dice1_new = dice(new_roll)
dice2_new = dice(new_roll)
dice1_new_mean = np.mean(dice1_new)
dice2_new_mean = np.mean(dice2_new)
mean_difference = difference(dice1_new_mean, dice2_new_mean).__round__(3)

print(f'\nNew values of means:\n#rolls = {new_roll}\nDice 1 mean = {dice1_new_mean}'
      f'\nDice 2 mean = {dice2_new_mean}\nMean difference = {mean_difference}')

### Plotting Mean/Standard Deviation vs #Rolls

roll_array = np.arange(start=1, stop = 1000+1, dtype=int)
diff_array = []

for i in range(1,len(roll_array)+1):
    diff_array.append(difference(np.mean(dice(i)),np.mean(loaded_dice(i))))

### Standard Deviation

std_array = []

for i in range(1,len(roll_array)+1):
    std_array.append(difference(np.std(dice(i)),np.std(loaded_dice(i))))

fig,ax = plt.subplots()
plt.plot(roll_array, std_array, label = 'Standard Deviation')
plt.plot(roll_array, diff_array, label = 'Mean')
plt.grid()
plt.legend()
plt.xlabel('Number of Roll')
plt.ylabel('Standard Deviation')
plt.title('Statistical Values vs Number of Roll')
plt.savefig('Statistical Values vs Number of Roll -- Loaded Dice')
plt.show()

