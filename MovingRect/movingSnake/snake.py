import pygame
import sys
import serial

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Snake attributes
snake_size = 20
snake_speed = 10
snake_color = (255, 255, 255)
max_snake_length = 10

# Initial snake position with fixed length
snake = [{'x': SCREEN_WIDTH // 2 - i * snake_size, 'y': SCREEN_HEIGHT // 2} for i in range(max_snake_length)]

# Replace 'COMx' with the correct serial port where Arduino is connected
ser = serial.Serial('COM7', 9600)

last_movement = (0, 0)

def move_snake(x, y):
    new_head = {'x': snake[0]['x'] + x, 'y': snake[0]['y'] + y}
    snake.insert(0, new_head)
    
    # Ensure the snake has a fixed length
    if len(snake) > max_snake_length:
        snake.pop()

def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, snake_color, pygame.Rect(segment['x'], segment['y'], snake_size, snake_size))

def main():
    trying = True

    while trying:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                trying = False

        try:
            joystick_data = ser.readline().decode().strip().split(',')
            if len(joystick_data) == 2:
                joystickX, joystickY = map(int, joystick_data)
                
                # Map joystick values to snake movement
                x_movement = int((joystickX - 512) / 50)
                y_movement = int((joystickY - 512) / 50)

                # Move the snake
                move_snake(x_movement, y_movement)

                # Fill the screen with black to clear traces
                screen.fill((0, 0, 0))

                # Draw the snake
                draw_snake()

                # Update the display
                pygame.display.flip()

                # Control the snake's speed
                clock.tick(snake_speed)
                
                # Save the last movement direction
                last_movement = (x_movement, y_movement)
            else:
                # If no joystick data, keep moving in the last direction
                move_snake(last_movement[0], last_movement[1])
                
                # Fill the screen with black to clear traces
                screen.fill((0, 0, 0))

                # Draw the snake
                draw_snake()

                # Update the display
                pygame.display.flip()

                # Control the snake's speed
                clock.tick(snake_speed)

        except (ValueError, UnicodeDecodeError):
            pass

    pygame.quit()

if __name__ == "__main__":
    main()
