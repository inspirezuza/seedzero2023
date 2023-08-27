import pygame
from player import Player

pygame.init()
screen = pygame.display.set_mode((800, 600))

player_image = pygame.image.load("block.png")
player_image = pygame.transform.scale(player_image, (50, 50))
clock = pygame.time.Clock()


def main():
    font = pygame.font.SysFont("", 32)
    text = font.render("", True, (255, 0, 0))
    time_left = 10
    player1 = Player(width=10, height=10, screen=screen, speed=5)
    player2 = Player(width=50, height=50, pos_x=400, pos_y=400, screen=screen, speed=5)
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player1.update_player_speed_y(-1)
                if event.key == pygame.K_s:
                    player1.update_player_speed_y(1)
                if event.key == pygame.K_a:
                    player1.update_player_speed_x(-1)
                if event.key == pygame.K_d:
                    player1.update_player_speed_x(1)

                if event.key == pygame.K_UP:
                    player2.update_player_speed_y(-1)
                if event.key == pygame.K_DOWN:
                    player2.update_player_speed_y(1)
                if event.key == pygame.K_LEFT:
                    player2.update_player_speed_x(-1)
                if event.key == pygame.K_RIGHT:
                    player2.update_player_speed_x(1)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player1.update_player_speed_y(1)
                if event.key == pygame.K_s:
                    player1.update_player_speed_y(-1)
                if event.key == pygame.K_a:
                    player1.update_player_speed_x(1)
                if event.key == pygame.K_d:
                    player1.update_player_speed_x(-1)

                if event.key == pygame.K_UP:
                    player2.update_player_speed_y(1)
                if event.key == pygame.K_DOWN:
                    player2.update_player_speed_y(-1)
                if event.key == pygame.K_LEFT:
                    player2.update_player_speed_x(1)
                if event.key == pygame.K_RIGHT:
                    player2.update_player_speed_x(-1)

        screen.fill("white")
        time_left -= 1 / 60
        text = font.render(f"Time left: {time_left:.2f}", True, "black")
        text_rect = text.get_rect()

        if time_left <= 0:
            text = font.render("Time out", True, "black")
            is_running = False

        if (
            player1.pos_x <= player2.pos_x + player2.width
            and player1.pos_x + player1.width >= player2.pos_x
            and player1.pos_y <= player2.pos_y + player2.height
            and player1.pos_y + player1.height >= player2.pos_y
        ):
            text = font.render("Collision!", True, (255, 0, 0))

        player1.update_player_pos()
        player2.update_player_pos()
        player1.render()
        player2.render()
        screen.blit(
            text,
            (
                screen.get_width() / 2 - text_rect.width / 2,
                screen.get_height() / 2 - text_rect.height / 2,
            ),
        )
        pygame.display.update()


if __name__ == "__main__":
    main()
