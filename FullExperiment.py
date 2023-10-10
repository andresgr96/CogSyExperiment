from Experiment1 import instruction_screen, attention_experiment
from Experiment2 import instruction_screen_exp_2, memory_experiment
import time
import pygame
from pygame import mixer

def pre_load():
    mixer.music.load('./stadium_sounds/stadium3.mp3')
    mixer.music.set_volume(0.15)

def go():
    pre_load()
    participant_id = instruction_screen()
    # Play music continuously
    time.sleep(5)
    mixer.music.play(-1)
    attention_experiment(participant_id)
    time.sleep(2)
    participant_id_2 = instruction_screen_exp_2()
    time.sleep(5)
    mixer.music.play(-1)
    memory_experiment(participant_id_2)

go()
