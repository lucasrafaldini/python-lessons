import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 700, 700
FPS = 24

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("LOAB is here with you")

clock = pygame.time.Clock()

# Load the character image
character_image = pygame.image.load("loab.png")
character_rect = character_image.get_rect()

# Set the initial position of the character
character_rect.center = (WIDTH // 2, HEIGHT // 2)

# Filter functions
def apply_grayscale(image):
    grayscale_image = pygame.Surface(image.get_size())
    grayscale_image.blit(image, (0, 0))
    grayscale_image = grayscale_image.convert()
    pygame.draw.rect(grayscale_image, (0, 0, 0), grayscale_image.get_rect(), 0)
    return grayscale_image

def apply_sepia(image):
    sepia_image = pygame.Surface(image.get_size())
    sepia_image.blit(image, (0, 0))
    sepia_image = sepia_image.convert()
    
    for x in range(sepia_image.get_width()):
        for y in range(sepia_image.get_height()):
            r, g, b, _ = sepia_image.get_at((x, y))
            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)
            tr, tg, tb = min(tr, 255), min(tg, 255), min(tb, 255)
            sepia_image.set_at((x, y), (tr, tg, tb))

    return sepia_image

def apply_invert(image):
    inverted_image = pygame.Surface(image.get_size())
    inverted_image.blit(image, (0, 0))
    inverted_image = inverted_image.convert()
    
    for x in range(inverted_image.get_width()):
        for y in range(inverted_image.get_height()):
            r, g, b, a = inverted_image.get_at((x, y))
            inverted_image.set_at((x, y), (255 - r, 255 - g, 255 - b, a))

    return inverted_image

# Filter modes
filters = {
    "Normal": lambda img: img,
    "Grayscale": apply_grayscale,
    "Sepia": apply_sepia,
    "Invert": apply_invert,
}
current_filter = "Normal"

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Cycle through filters on click
            filter_keys = list(filters.keys())
            current_index = filter_keys.index(current_filter)
            next_index = (current_index + 1) % len(filter_keys)
            current_filter = filter_keys[next_index]

    # Clear the screen
    screen.fill((255, 255, 255))

    # Apply the selected filter to the character image
    filtered_image = filters[current_filter](character_image)

    # Draw the filtered character image on the screen
    screen.blit(filtered_image, character_rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()