class Menu:
    def __init__(self):
        self.options = [
            "Launch the game",
            "Add a Pokémon",
            "Quit"
        ]
        self.button_rects = []

    def display_menu(self):
        print("\nWelcome to Pokémon Game!")
        print("\n=== Menu ===")
        for i, option in enumerate(self.options, 1):
            print(f"{i}. {option}")

    def draw(self):
        screen.fill((50, 50, 50))
        y = 200
        self.button_rects.clear()
        
        for option in self.options:
            text = font.render(option, True, (255, 255, 255))
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, y))
            screen.blit(text, text_rect)
            self.button_rects.append(text_rect)
            y += 80

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for i, text_rect in enumerate(self.button_rects):
                if text_rect.collidepoint(mouse_pos):
                    return i
        return None
