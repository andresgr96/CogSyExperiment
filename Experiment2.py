import sys
import pygame
import random
import time
import pandas as pd
from pygame import mixer
import os
# from Experiment1 import create_results_directory

pygame.init()

# Set the dimensions of the window
infoObject = pygame.display.Info()
width, height = infoObject.current_w, infoObject.current_h
win = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
clock = pygame.time.Clock()

# Set the background 
# field_color = (0, 255, 0)
background = pygame.image.load('./stadium_pictures/net1.jpg')
background = pygame.transform.scale(background, (2040, 1280))

# Player

# Declare Folder with Images of Players
image_path = './pictures_football'
image_filenames = os.listdir(image_path)

# Set background sound
mixer.music.load('./stadium_sounds/stadium3.mp3')
mixer.music.set_volume(0.15)

# Define colors
colors = [
    # Red Channel
    (110, 123, 50),
    (135, 123, 50),
    (161, 123, 50),

    # Green Channel
    (84, 149, 50),
    (84, 174, 50),
    (84, 200, 50),

    # Blue Channel
    (84, 123, 76),
    (84, 123, 101),
    (84, 123, 127),

    # All Channels
    (110, 149, 76),
    (135, 174, 101),
    (161, 200, 127),

    # Red & Blue Channel
    (110, 123, 76),
    (135, 123, 101),
    (161, 123, 127)
]

colors_extended = colors * 4
random.shuffle(colors_extended)


font = pygame.font.Font(None, 74)
arial_font = pygame.font.SysFont('Arial', 50)

def display_message(message, y_offset, font):
    text = font.render(message, True, (0, 0, 0))
    text_rect = text.get_rect(center=(width // 2, height // 2 - y_offset))
    win.blit(text, text_rect)
    pygame.display.update()

def input_box(y_offset):
    active = False
    text = ''
    arial_font = pygame.font.SysFont('Arial', 50)
    input_box = pygame.Rect(width // 2 - 70, height // 2 - y_offset, 140, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    clock = pygame.time.Clock()

    while True:
        win.fill((255, 255, 255))  # Set the background color to white
        txt_surface = arial_font.render(text, True, (0, 0, 0))  # Set the text color to black
        box_width = max(200, txt_surface.get_width()+10)
        input_box.w = box_width
        win.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(win, color, input_box, 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        pygame.display.flip()
        clock.tick(30)

def create_results_directory():
    if not os.path.exists('results'):
        os.makedirs('results')

def display_thank_you_message():
    # Display thank you text
    win.fill(WHITE)
    txt_surface = font.render("Thank you!", True, BLACK)
    win.blit(txt_surface, (width // 2 - txt_surface.get_width() // 2, height // 2 - txt_surface.get_height() // 2))
    pygame.display.flip()

    # Wait for space key press
    waiting_for_space = True
    while waiting_for_space:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting_for_space = False




def instruction_screen_exp_2():
    global win, width, height

    # Define colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Define font and size
    font = pygame.font.SysFont('Arial', 24)

    # Define texts
    instruction_text = Now, You will see one to five (1-5) colored stickman appear on the football field background."
    instruction_text_2 = "Additionally, You will see some RED stickman appear, make sure to ignore these when counting."
    instruction_text_3 = "Your task is to recall the number of non-red stickman shown by pressing the correct number on your keyboard."
    start_exp_text = "When you are ready, press space to start the experiment."

    running = True

    while running:
        win.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False

        # Render text
        win.blit(font.render(instruction_text, True, BLACK), (width // 2 - 350, height // 4))
        win.blit(font.render(instruction_text_2, True, BLACK), (width // 2 - 350, height // 4 + 50))
        win.blit(font.render(instruction_text_3, True, BLACK), (width // 2 - 350, height // 4 + 100))
        win.blit(font.render(start_exp_text, True, BLACK), (width // 2 - 350, height // 4 + 200))

        pygame.display.flip()
        # clock.tick(30)


def goodbye_screen():
    global win, width, height

    # Define colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Define font and size
    font = pygame.font.SysFont('Arial', 24)

    # Define texts
    goodbye_text = "Thats it! Thanks for Participating in our experiment."
    goodbye_text_2 = "Press space to close this screen."


    running = True

    while running:
        win.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    sys.exit()

        # Render text
        win.blit(font.render(goodbye_text, True, BLACK), (width // 2 - 350, height // 4))
        win.blit(font.render(goodbye_text_2, True, BLACK), (width // 2 - 300, height // 4 + 50))

        pygame.display.flip()

def spawn_objects_memory(num_objects, color):
    win.blit(background, (0, 0))
    pygame.display.update()
    time.sleep(0.5)
    existing_objects =spawn_distractors()

    for i in range(num_objects):
        while True:
            random_image_filename = random.choice(image_filenames)
            base_sprite_path = os.path.join(image_path, random_image_filename)
            base_sprite = pygame.image.load(base_sprite_path)
            base_sprite = pygame.transform.scale(base_sprite, (200, 200))
            colored_sprite = color_sprite(base_sprite, color)
            x = random.randint(50, 1000)
            y = random.randint(height / 2, height - 200)

            if all((x - x0) ** 2 + (y - y0) ** 2 >= 50 ** 2 for x0, y0 in existing_objects):
                break

        existing_objects.append((x, y))
        win.blit(colored_sprite, (x, y))

    pygame.display.update()
    time.sleep(0.5)  # Show the stickman for 0.5 seconds
    win.blit(background, (0, 0))  # Clear the screen
    pygame.display.update()


def spawn_distractors():
    num_distractors = random.randint(1, 3)
    red_color = (255, 0, 0)
    existing_objects = []
    for i in range(num_distractors):
        while True:
            random_image_filename = random.choice(image_filenames)
            base_sprite_path = os.path.join(image_path, random_image_filename)
            base_sprite = pygame.image.load(base_sprite_path)
            base_sprite = pygame.transform.scale(base_sprite, (200, 200))
            colored_sprite = color_sprite(base_sprite, red_color)
            x = random.randint(50, 1000)
            y = random.randint(height / 2, height - 200)

            if all((x - x0) ** 2 + (y - y0) ** 2 >= 50 ** 2 for x0, y0 in existing_objects):
                break

        existing_objects.append((x, y))
        win.blit(colored_sprite, (x, y))

    return existing_objects

def get_user_input():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5]:
                    return int(event.unicode)


def color_sprite(base_sprite, color):
    colored_sprite = base_sprite.copy()
    array = pygame.surfarray.pixels3d(colored_sprite)
    r, g, b = color
    is_white = (array[:, :, 0] == 255) & (array[:, :, 1] == 255) & (array[:, :, 2] == 255)
    array[is_white, 0] = r
    array[is_white, 1] = g
    array[is_white, 2] = b

    return colored_sprite

def is_safe_distance(x, y, existing_objects, min_distance=50):
    "Check if the (x, y) is a safe distance from all existing objects"
    return all((x - x0) ** 2 + (y - y0) ** 2 >= min_distance ** 2 for x0, y0 in existing_objects)

def memory_experiment(participant_id, age, sports_experience):
    data = {'Participant_ID': [], 'Age': [], 'Sports_Experience': [], 'Correct': [],'Number_Shown': [],'User Input':[], 'Color': []}

    for trial in range(5):
        num_stickman = random.randint(1, 5)
        color = colors_extended.pop()

        spawn_objects_memory(num_stickman, color)

        user_input = get_user_input()

        is_correct = user_input == num_stickman
        data['Participant_ID'].append(participant_id)
        data['Age'].append(age)
        data['Sports_Experience'].append(sports_experience)
        data['Correct'].append(is_correct)
        data['Number_Shown'].append(num_stickman)
        data['User Input'].append(user_input)
        data['Color'].append(color)

        print(f'Trial {trial + 1} - Correct: {is_correct} - User Input: {user_input} - Number Shown: {num_stickman} - Color: {color}')

        # Adding a random delay between 1.5 to 3 seconds before the next iteration
        time.sleep(random.uniform(1.5, 3))
    create_results_directory()
    df = pd.DataFrame(data)
    file_path =os.path.join('results', f'memory_experiment_data_{participant_id}.csv')
    df.to_csv(file_path, index=False)
    print(f'Data saved to: {file_path}')


# # participant_id, age, sports_experience = instruction_screen_exp_2()
# time.sleep(5)
# mixer.music.play(-1)
# memory_experiment(participant_id, age, sports_experience)

