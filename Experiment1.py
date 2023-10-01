import sys
import pygame
import random
import time
import pandas as pd
from pygame import mixer
import os

pygame.init()

# Set the dimensions of the window
infoObject = pygame.display.Info()
width, height = infoObject.current_w, infoObject.current_h
win = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
clock = pygame.time.Clock()

# Set the background 
# field_color = (0, 255, 0)
background = pygame.image.load('./pictures_football/net2.jpg')
background = pygame.transform.scale(background, (2040, 1280))

# Player

# player = pygame.image.load('./pictures_football/right1.png')
image_path = './pictures_football/image_filenames'
image_filenames = os.listdir(image_path)

# Set background sound

mixer.music.load('./stadium_sounds/stadium1.mp3')
mixer.music.set_volume(0.15)
# Define colors
colors = [
    (0, 255, 100),
    (0, 255, 150),
    (0, 0, 255),
    (255, 0, 0),
]

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


def welcome_screen():
    win.fill((255, 255, 255))  # Set background color to white
    arial_font = pygame.font.SysFont('Arial', 30)

    # Display welcome message
    welcome_message = arial_font.render('Welcome to the Experiment', True, (0, 0, 0))
    win.blit(welcome_message, (50, 50))  # Adjusted y-coordinate

    # Display instruction to enter participant ID
    instruction_message = arial_font.render('Please enter your participant ID:', True, (0, 0, 0))
    win.blit(instruction_message, (50, 100))  # Adjusted y-coordinate

    pygame.display.update()

    # Call the input box function to get the participant ID
    participant_id = input_box(200)  # Adjusted y-offset to avoid overlapping with the texts

    # Display thank you message with the participant ID
    win.fill((255, 255, 255))
    thank_you_message = arial_font.render('Thank you, Participant: ' + participant_id, True, (0, 0, 0))
    win.blit(thank_you_message, (50, 150))  # Set a fixed margin for the text

    pygame.display.update()
    time.sleep(2)
    return participant_id


def instruction_screen():
    global win, width, height

    # Define colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Define font and size
    font = pygame.font.SysFont('Arial', 24)

    # Define texts
    instruction_text = "You will see colored blocks appear on a field background. Your task is to press the SPACE bar as soon as you see a block."
    submit_text = "Please enter your participant ID below:"
    thank_you_text = "Thank you! Press space to start the experiment."

    # Define input box
    input_box = pygame.Rect(width // 2 - 70, height // 2 - 10, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    txt_surface = font.render(text, True, color)

    # Define button
    button = pygame.Rect(width // 2 - 40, height // 2 + 40, 140, 32)
    button_text = font.render('Submit', True, WHITE)

    running = True
    while running:
        win.fill(WHITE)
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
                if button.collidepoint(event.pos):
                    participant_id = text
                    running = False
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                    txt_surface = font.render(text, True, color)

        # Render text
        txt_surface = font.render(text, True, color)

        # Resize input box if text is too long
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width

        # Display instructions
        ins_txt_surface = font.render(instruction_text, True, BLACK)
        win.blit(ins_txt_surface, (input_box.x - 450, height // 4))
        sub_txt_surface = font.render(submit_text, True, BLACK)
        win.blit(sub_txt_surface, (input_box.x - 50, input_box.y - 50))

        # Draw input box and text
        pygame.draw.rect(win, color, input_box, 2)
        win.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

        # Display button
        pygame.draw.rect(win, BLACK, button)
        win.blit(button_text, (button.x + button.width // 2 - button_text.get_width() // 2,
                               button.y + button.height // 2 - button_text.get_height() // 2))

        pygame.display.flip()
        clock.tick(30)

    # Display thank you text
    win.fill(WHITE)
    txt_surface = font.render(thank_you_text, True, BLACK)
    win.blit(txt_surface, (input_box.x - 70, height // 2 - txt_surface.get_height() // 2))
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

    return participant_id

def spawn_objects(num_objects, color):
    # Background
    win.blit(background, (0, 0))
    # win.fill(field_color)
    pygame.display.update()
    time.sleep(0.5)  # Brief delay to ensure background color is set before blocks appear

    existing_objects = []

    for i in range(num_objects):
        while True:
            x = random.randint(50, 1000)
            y = random.randint(50, height - 50)

            # Check if the new position is too close to existing objects
            if all((x - x0) ** 2 + (y - y0) ** 2 >= 50 ** 2 for x0, y0 in existing_objects):
                break

        existing_objects.append((x, y))
        pygame.draw.rect(win, color, (x, y, 100, 100))
        # win.blit(player, color, (x, y, 100, 100))

    pygame.display.update()

def attention_experiment(participant_id):
    data = {'Participant_ID': [], 'Reaction_Time': [], 'Color': []}
    
    for trial in range(40):
        running = True
        spawn_delay = random.randint(1, 5)
        time.sleep(spawn_delay)

        color = random.choice(colors)
        spawn_objects(2, color)

        start_time = time.time()
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        reaction_time = time.time() - start_time
                        data['Participant_ID'].append(participant_id)
                        data['Reaction_Time'].append(reaction_time)
                        data['Color'].append(color)
                        print(f'Trial {trial + 1} - Reaction time: {reaction_time} seconds- Color: {color}')
                        print(color)
                        # Background
                        win.blit(background, (0, 0))
                        
                        # win.fill(field_color)
                        pygame.display.update()
                        running = False

    df = pd.DataFrame(data)
    df.to_csv(f'experiment_data_{participant_id}.csv', index=False)

participant_id = instruction_screen()
# Play music continuously
time.sleep(5)
mixer.music.play(-1)
attention_experiment(participant_id)
