import pygame
import serial
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect(300, 250, 50, 50)

# Replace 'COMx' with the correct serial port where Arduino is connected
ser = serial.Serial('COM7', 9600)

trying = True

while trying:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            trying = False

    # Read joystick values from Arduino
    try:
        joystick_data = ser.readline().decode().strip().split(',')
        if len(joystick_data) == 2:
            joystickX, joystickY = map(int, joystick_data)
            # Map joystick values to rectangle movement
            player.x += int((joystickX - 500) / 10)  # Adjust scaling factor
            player.y += int((joystickY - 500) / 10)  # Adjust scaling factor

            # Keep the player rectangle within the screen bounds
            player.x = max(0, min(player.x, SCREEN_WIDTH - player.width))
            player.y = max(0, min(player.y, SCREEN_HEIGHT - player.height))

            screen.fill((0, 0, 0))
            pygame.draw.rect(screen, (255, 255, 255), player)
            pygame.display.update()
    except (ValueError, UnicodeDecodeError):
        pass

pygame.quit()
