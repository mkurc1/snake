from snake.snake import Snake

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def main():
    snake = Snake(SCREEN_WIDTH, SCREEN_HEIGHT)
    snake.play()


if __name__ == '__main__':
    main()
