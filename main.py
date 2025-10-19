import pygame
from game.game_engine import GameEngine

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong - Pygame Edition")

# Clock
clock = pygame.time.Clock()
FPS = 60

def main():
    running = True
    engine = GameEngine(WIDTH, HEIGHT)
    in_menu = False

    while running:
        SCREEN.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Replay menu options
            if in_menu and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:
                    engine.winning_score = 2  # best of 3
                    engine.reset_game()
                    in_menu = False
                elif event.key == pygame.K_5:
                    engine.winning_score = 3  # best of 5
                    engine.reset_game()
                    in_menu = False
                elif event.key == pygame.K_7:
                    engine.winning_score = 4  # best of 7
                    engine.reset_game()
                    in_menu = False
                elif event.key == pygame.K_ESCAPE:
                    running = False

        # Game update
        if not engine.game_over:
            engine.handle_input()
            engine.update()
        else:
            # Wait 2 seconds after showing winner, then show menu
            if engine.showing_winner:
                engine.render(SCREEN)
                if pygame.time.get_ticks() - engine.winner_display_time > 2000:
                    engine.showing_winner = False
                    in_menu = True
            elif in_menu:
                engine.render_replay_menu(SCREEN)
            else:
                engine.render(SCREEN)

        if not in_menu:
            engine.render(SCREEN)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
