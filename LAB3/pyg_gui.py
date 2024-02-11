import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WIDTH, HEIGHT = 780, 600
FONT_SIZE = 30

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock, Paper, Scissors")

# Set up fonts
font = pygame.font.Font(None, FONT_SIZE)

# Load and scale images
def load_image(name, size=(200, 200)):
    try:
        image = pygame.image.load(name).convert_alpha()
        return pygame.transform.scale(image, size)
    except pygame.error as e:
        print(f"Failed to load image '{name}': {e}")
        sys.exit(1)

rock = load_image("rock.jpg")
paper = load_image("paper.jpg")
scissors = load_image("scissors.jpg")

# Function to draw text on the screen
def draw_text(message, color, x, y):
    text = font.render(message, True, color)
    screen.blit(text, (x, y))

# Function to create buttons
def create_button(msg, color, x, y, w, h):
    button_rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, color, button_rect)
    draw_text(msg, BLACK, x + 10, y + 5)
    return button_rect

# Function to get the player's choice
def get_user_choice():
    screen.fill(WHITE)
    draw_text("Choose rock, paper, or scissors:", RED, 100, 100)

    # Draw the images on the screen
    rock_rect = screen.blit(rock, (65, 100))
    paper_rect = screen.blit(paper, (260, 100))
    scissors_rect = screen.blit(scissors, (460, 100))
    pygame.display.update()

    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if rock_rect.collidepoint(mouse_pos):
                return "rock"
            elif paper_rect.collidepoint(mouse_pos):
                return "paper"
            elif scissors_rect.collidepoint(mouse_pos):
                return "scissors"

# Determine the winner
def determine_winner(user_choice, opponent_choice):
    if user_choice == opponent_choice:
        return "It's a tie!"
    if (user_choice == "rock" and opponent_choice == "scissors" or
        user_choice == "paper" and opponent_choice == "rock" or
        user_choice == "scissors" and opponent_choice == "paper"):
        return "You win!"
    return "You lose!"

# Main function where the game loop runs
def main():
    running = True
    while running:
        # Get user's choice
        user_choice = get_user_choice()
        opponent_choice = random.choice(["rock", "paper", "scissors"])
        winner_text = determine_winner(user_choice, opponent_choice)

        # Display the choices and the result
        screen.fill(WHITE)
        draw_text(f"You chose {user_choice}", BLACK, 50, 150)
        draw_text(f"The opponent chose {opponent_choice}", BLACK, 50, 250)
        draw_text(winner_text, RED if winner_text == "You lose!" else BLACK, 50, 350)

        # Create 'Quit' and 'Play Again' buttons
        quit_button = create_button("Quit", RED, 50, 500, 200, 50)
        play_again_button = create_button("Play Again", RED, 550, 500, 200, 50)
        pygame.display.update()

        # Process button clicks
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if quit_button.collidepoint(event.pos):
                    running = False
                    break
                elif play_again_button.collidepoint(event.pos):
                    # Reset the screen for a new game
                    break  # Break out of the inner loop to start a new game

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
