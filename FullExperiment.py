from Experiment1 import instruction_screen, attention_experiment
from Experiment2 import instruction_screen_exp_2, memory_experiment, goodbye_screen
import time
import pygame
from pygame import mixer

def pre_load():
    mixer.music.load('./stadium_sounds/stadium3.mp3')
    mixer.music.set_volume(0.15)

def go():
    pre_load()

    #Exp1
    participant_id, participant_age, sports_experience = instruction_screen()
    # Play music continuously
    time.sleep(5)
    mixer.music.play(-1)
    attention_experiment(participant_id, participant_age, sports_experience)

    #Exp2
    time.sleep(2)
    instruction_screen_exp_2()
    time.sleep(5)
    mixer.music.play(-1)
    memory_experiment(participant_id, participant_age, sports_experience)
    goodbye_screen()

go()
