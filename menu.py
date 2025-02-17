import pygame

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pokémon Game")

# Set font and clock
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# Define colors
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
DARK_GRAY = (50, 50, 50)
BLUE = (0, 122, 255)

class Menu:
    def __init__(self):
        # Menu options
        self.options = [
            "Launch the game",
            "Add a Pokémon",
            "Quit"
        ]
        # List to store button rectangles
        self.button_rects = []

    # Draw the menu on the screen
    def draw(self):
        screen.fill(DARK_GRAY)  # Fill background with dark gray
        y = 200  # Starting position for the first button
        self.button_rects.clear()  # Clear previous button rectangles
        
        for option in self.options:
            # Render text
            text_surface = font.render(option, True, WHITE)
            text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, y))
            
            # Create a button rectangle around the text
            button_rect = pygame.Rect(text_rect.x - 20, text_rect.y - 10, text_rect.width + 40, text_rect.height + 20)
            
            # Draw the button and text on the screen
            pygame.draw.rect(screen, BLUE, button_rect, border_radius=10)
            screen.blit(text_surface, text_rect)
            
            # Store button rectangle for event handling
            self.button_rects.append(button_rect)
            y += 100  # Move down for the next button

    # Handle user input (mouse click)
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()  # Get mouse position
            for i, button_rect in enumerate(self.button_rects):
                if button_rect.collidepoint(mouse_pos):  # Check if a button was clicked
                    return i  # Return the index of the clicked button
        return None  # Return None if no button was clicked
