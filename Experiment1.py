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
        box_width = max(200, txt_surface.get_width() + 10)
        input_box.w = box_width
        win.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
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

def instruction_screen():
    global win, width, height

    # Define colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Define font and size
    font = pygame.font.SysFont('Arial', 24)

    # Define texts
    instruction_text = "You will see a colored stickman appear on a football field background. Your task is to press the SPACE bar as soon as you see a stickman."
    participant_text = "Please enter your participant ID below:"
    age_text = "Please enter your age:"
    sports_experience_text = "Have you played in team sports? (yes/no)"
    thank_you_text = "Thank you! Press space to start the experiment."

    # Define input boxes for participant ID, age, and sports experience
    id_input_box = pygame.Rect(width // 2 - 70, height // 3, 140, 32)
    age_input_box = pygame.Rect(width // 2 - 70, id_input_box.bottom + 50, 140, 32)
    sports_input_box = pygame.Rect(width // 2 - 70, age_input_box.bottom + 50, 140, 32)

    # Set default input box properties
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active_box = None
    input_texts = ['', '', '']
    input_boxes = [id_input_box, age_input_box, sports_input_box]
    prompts = [participant_text, age_text, sports_experience_text]

    running = True
    current_box = 0

    while running:
        win.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for idx, box in enumerate(input_boxes):
                    if box.collidepoint(event.pos):
                        active_box = idx
                        color = color_active
                    else:
                        color = color_inactive
            if event.type == pygame.KEYDOWN:
                if active_box is not None:
                    if event.key == pygame.K_BACKSPACE:
                        input_texts[active_box] = input_texts[active_box][:-1]
                    elif event.key == pygame.K_RETURN:
                        current_box += 1
                        if current_box >= len(input_boxes):
                            running = False
                            break
                        active_box = current_box
                    else:
                        input_texts[active_box] += event.unicode

        # Render text
        win.blit(font.render(instruction_text, True, BLACK), (width // 2 - 350, height // 4))
        for idx, box in enumerate(input_boxes):
            txt_surface = font.render(input_texts[idx], True, BLACK)
            prompt_surface = font.render(prompts[idx], True, BLACK)
            win.blit(prompt_surface, (box.x - 50, box.y - 40))
            win.blit(txt_surface, (box.x + 5, box.y + 5))
            pygame.draw.rect(win, color if active_box == idx else color_inactive, box, 2)

        pygame.display.flip()
        clock.tick(30)

    participant_id = input_texts[0]
    participant_age = input_texts[1]
    sports_experience = input_texts[2]  # This can be 'yes' or 'no'

    # Display thank you text
    win.fill(WHITE)
    txt_surface = font.render(thank_you_text, True, BLACK)
    win.blit(txt_surface, (width // 2 - 70, height // 2 - txt_surface.get_height() // 2))
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

    return participant_id, participant_age, sports_experience


def spawn_objects(num_objects):
    win.blit(background, (0, 0))
    pygame.display.update()
    time.sleep(0.5)  # Brief delay to ensure background color is set before blocks appear

    existing_objects = []

    for i in range(num_objects):
        while True:
            random_image_filename = random.choice(image_filenames)
            base_sprite_path = os.path.join(image_path, random_image_filename)
            base_sprite = pygame.image.load(base_sprite_path)
            base_sprite = pygame.transform.scale(base_sprite, (200, 200))
            color = colors_extended.pop()
            colored_sprite = color_sprite(base_sprite, color)
            x = random.randint(50, 1000)
            y = random.randint(height / 2, height - 200)

            # Check if the new position is too close to existing objects
            if all((x - x0) ** 2 + (y - y0) ** 2 >= 50 ** 2 for x0, y0 in existing_objects):
                break

        existing_objects.append((x, y))
        win.blit(colored_sprite, (x, y))

    pygame.display.update()
    return color  # Add this line to return the color


def color_sprite(base_sprite, color):
    colored_sprite = base_sprite.copy()
    array = pygame.surfarray.pixels3d(colored_sprite)
    r, g, b = color
    is_white = (array[:, :, 0] == 255) & (array[:, :, 1] == 255) & (array[:, :, 2] == 255)
    array[is_white, 0] = r
    array[is_white, 1] = g
    array[is_white, 2] = b

    return colored_sprite


def create_results_directory():
    if not os.path.exists('results'):
        os.makedirs('results')


def attention_experiment(participant_id, participant_age, sports_experience):
    data = {'Participant_ID': [], 'Age': [], 'Sports_Experience': [], 'Reaction_Time': [], 'Color': []}

    for trial in range(60):
        running = True
        spawn_delay = random.randint(1, 5)
        time.sleep(spawn_delay)

        color = spawn_objects(1)

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
                        data['Age'].append(participant_age)
                        data['Sports_Experience'].append(sports_experience)
                        data['Reaction_Time'].append(reaction_time)
                        data['Color'].append(color)
                        print(f'Trial {trial + 1} - Reaction time: {reaction_time} seconds - Color: {color}')
                        # Background
                        win.blit(background, (0, 0))

                        pygame.display.update()
                        running = False
    create_results_directory()
    df = pd.DataFrame(data)
    file_path = os.path.join('results', f'experiment_data_{participant_id}.csv')
    df.to_csv(file_path, index=False)
    print(f'Data saved to: {file_path}')


# participant_id, participant_age, sports_experience = instruction_screen()
# time.sleep(5)
# mixer.music.play(-1)
# attention_experiment(participant_id, participant_age, sports_experience)
