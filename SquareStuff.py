import pygame

pygame.init()

ScreenX, ScreenY = 800, 800
Clock = pygame.time.Clock()
Screen = pygame.display.set_mode((ScreenX, ScreenY))
Name = "SquareStuff"
Running = True

pygame.display.set_caption(Name)

# Settings 

BackgroundColour = (0, 0, 0)
Fps = 60
Stop = 4
Big_Size = int(800 / 3) + 1

Squares = []

# Main

def Generate(Stop, Big_Size, List : list):

    Rect = pygame.Rect(0, 0, Big_Size, Big_Size)
    Rect.center = (400, 400)

    List.append(Rect)

    def Repeat(Position, NewSize, Depth):

        if Depth > Stop:
            return
        
        Depth += 1
        
        for x in range(1, 4):
            for y in range(1, 4):
                if x == 2 and y == 2:
                    continue

                Rect = pygame.Rect(0, 0, NewSize / 2, NewSize / 2)
                Rect.center = (Position[0] + int((x * NewSize) - (NewSize / 2)), Position[1] + int((y * NewSize) - (NewSize / 2)))
                List.append(Rect)
    
    Repeat((0,0), Big_Size / 1, 0)
    Repeat((200, 75), Big_Size / 2, 1)

Generate(Stop, Big_Size, Squares)

while Running:

    # Control

    for Event in pygame.event.get():
        if Event.type == pygame.QUIT:
            Running = False

    Keys = pygame.key.get_pressed()

    # Render

    Screen.fill(BackgroundColour)

    for Square in Squares:
        pygame.draw.rect(Screen, (255, 255, 255), Square)

    pygame.display.flip()
    Clock.tick(Fps)

pygame.quit()