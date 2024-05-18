import pygame
import math

pygame.init()

ScreenX, ScreenY = 800, 800
Clock = pygame.time.Clock()
Screen = pygame.display.set_mode((ScreenX, ScreenY))
Name = "Fractal Tree"
Running = True

pygame.display.set_caption(Name)

# Settings 

BackgroundColour = (0, 0, 0)
BranchColour = (255, 255, 255)
BranchSize = 5
Start = (400, 700)
Start_Length = 55
Stop = 10

Fps = 60
Angle = 25
Multi = 0.9 # Faster The Branches Get Smaller, From 0, 1

# Main

Branches = []

def GenerateBranches(Branches : list, Stop : int):

    def CalculatePoint(Position, Radius, Angle):
        
        x = Position[0] + Radius * math.cos(math.radians(Angle))
        y = Position[1] + Radius * math.sin(math.radians(Angle))
        
        return (x, y)
    
    def Branch(Branch_Position, Branch_Length, Branch_Angle, Depth):

        if Depth >= Stop:
            return

        EndPosition = CalculatePoint(Branch_Position, Branch_Length, Branch_Angle)
        Branches.append({
            
            "StartPosition" : Branch_Position,
            "EndPosition" : EndPosition,
            
        })
        
        Branch(EndPosition, Branch_Length * Multi, Branch_Angle + Angle, Depth + 1)
        Branch(EndPosition, Branch_Length * Multi, Branch_Angle - Angle, Depth + 1)

    Branch(Start, Start_Length, -90, 0)

GenerateBranches(Branches, Stop)

while Running:

    # Control

    for Event in pygame.event.get():
        if Event.type == pygame.QUIT:
            Running = False

    Keys = pygame.key.get_pressed()

    # Render

    Screen.fill(BackgroundColour)

    for Branch in Branches:
        
        pygame.draw.line(Screen, BranchColour, Branch["StartPosition"], Branch["EndPosition"], BranchSize)

    pygame.display.flip()
    Clock.tick(Fps)

pygame.quit()