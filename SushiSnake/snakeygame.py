
from graphics import *
makeGraphicsWindow(1000, 700)

import random
# this function is called once to initialize your new world
 
def startWorld(world):
    #Define the image of sushi
    #I drew the image myself on Photoshop
    world.unagi=loadImage("unagi.png", scale=0.05)
    world.unagiX=400
    world.unagiY=360
    world.unagiwidth=getImageWidth(world.unagi)
    world.unagiheight=getImageHeight(world.unagi)
    #Red square character start coordinates
    world.rectangleX=0
    world.rectangleY=670
    #Lowest horizontal barrier
    world.rectangle2X=200
    world.rectangle2Y=600
    world.rectangle2velocity=10
    #Second horizontal barrier
    world.rectangle3X=0
    world.rectangle3Y=500
    world.rectangle3velocity=10
    #Third horizontal barrier
    world.rectangle4X=200
    world.rectangle4Y=400
    world.rectangle4velocity=13
    #Fourth horizontal barrier
    world.rectangle5X=0
    world.rectangle5Y=300
    world.rectangle5velocity=14
    #Fifth horizontal barrier
    world.rectangle6X=250
    world.rectangle6Y=200
    world.rectangle6velocity=18
    #Sixth horizontal barrier
    world.rectangle7X=300
    world.rectangle7Y=100
    world.rectangle7velocity=20
    #First vertical barrier
    world.rectangle8X=100
    world.rectangle8Y=0
    world.rectangle8velocity=15
    #Second vertical barrier
    world.rectangle9X=300
    world.rectangle9Y=0
    world.rectangle9velocity=20
    #Third vertical barrier
    world.rectangle10X=500
    world.rectangle10Y=0
    world.rectangle10velocity=15
    #Fourth vertical barrier
    world.rectangle11X=700
    world.rectangle11Y=0
    world.rectangle11velocity=20
    #Fifth vertical barrier
    world.rectangle12X=880
    world.rectangle12Y=0
    world.rectangle12velocity=22
    #Background color
    setBackground("black")
    #Whether there are instructions or not
    world.instructions=True
    #Instructions page disappearance
    onKeyPress(startgame, "enter")
    #Game over
    world.gameover=False
    #Displaying score
    world.score=0
    #Restart game
    onKeyPress(startWorld, "space")
    
#what to display at the start of the game
#should display the instructions page and not the "you died" page
def startgame(world):
    if world.instructions==True:
        world.instructions=False
        world.gameover=False
        
# this function is called every frame to update your world    
def updateWorld(world):  
    #Check for game over
    if world.gameover==True:
        return
    
    #Red block controls
    if isKeyPressed("right"):
        world.rectangleX=world.rectangleX+10
    if isKeyPressed("left"):
        world.rectangleX=world.rectangleX-10
    if isKeyPressed("up"):
        world.rectangleY=world.rectangleY-10
    if isKeyPressed("down"):
        world.rectangleY=world.rectangleY+10
        
    #Red rectangle wrap-around
    if world.rectangleX<0:
        world.rectangleX=1000
    if world.rectangleX>1000:
        world.rectangleX=0
    if world.rectangleY<0:
        world.rectangleY=700
    if world.rectangleY>700:
        world.rectangleY=0
        
    #Horizontal barriers motions
    world.rectangle2X=world.rectangle2X + world.rectangle2velocity
    if world.rectangle2X+800>1000:
        world.rectangle2velocity= -10
    if world.rectangle2X<0:
        world.rectangle2velocity=10
    world.rectangle3X=world.rectangle3X + world.rectangle3velocity
    if world.rectangle3X+750>1000:
        world.rectangle3velocity=-10
    if world.rectangle3X<0:
        world.rectangle3velocity=10
    world.rectangle4X=world.rectangle4X + world.rectangle4velocity
    if world.rectangle4X+800>1000:
        world.rectangle4velocity=-13
    if world.rectangle4X<0:
        world.rectangle4velocity=13
    world.rectangle5X=world.rectangle5X + world.rectangle5velocity
    if world.rectangle5X+800>1000:
        world.rectangle5velocity=-14
    if world.rectangle5X<0:
        world.rectangle5velocity=14
    world.rectangle6X=world.rectangle6X + world.rectangle6velocity
    if world.rectangle6X+750>1000:
        world.rectangle6velocity=-18
    if world.rectangle6X<0:
        world.rectangle6velocity=18
    world.rectangle7X=world.rectangle7X + world.rectangle7velocity
    if world.rectangle7X+600>1000:
        world.rectangle7velocity=-20
    if world.rectangle7X<0:
        world.rectangle7velocity=20
        
    #Vertical rectangles motions
    world.rectangle8Y=world.rectangle8Y + world.rectangle8velocity
    if world.rectangle8Y<0:
        world.rectangle8velocity=15
    if world.rectangle8Y+100>700:
        world.rectangle8velocity=-15
    world.rectangle9Y=world.rectangle9Y + world.rectangle9velocity
    if world.rectangle9Y<0:
        world.rectangle9velocity=20
    if world.rectangle9Y+100>700:
        world.rectangle9velocity=-20
    world.rectangle10Y=world.rectangle10Y + world.rectangle10velocity
    if world.rectangle10Y<0:
        world.rectangle10velocity=15
    if world.rectangle10Y+100>700:
        world.rectangle10velocity=-15
    world.rectangle11Y=world.rectangle11Y + world.rectangle11velocity
    if world.rectangle11Y<0:
        world.rectangle11velocity=20
    if world.rectangle11Y+100>700:
        world.rectangle11velocity=-20
    world.rectangle12Y=world.rectangle12Y + world.rectangle12velocity
    if world.rectangle12Y<0:
        world.rectangle12velocity=22
    if world.rectangle12Y+100>700:
        world.rectangle12velocity=-22
        
    #check for overlap between red square and white rectangles
    if collision(world.rectangleX, world.rectangleY, 30, 30, world.rectangle2X, world.rectangle2Y, 800, 30):
        world.gameover=True
    if collision(world.rectangleX, world.rectangleY, 30, 30, world.rectangle3X, world.rectangle3Y, 750, 30):
        world.gameover=True    
    if collision(world.rectangleX, world.rectangleY, 30, 30, world.rectangle4X, world.rectangle4Y, 800, 30):
        world.gameover=True        
    if collision(world.rectangleX, world.rectangleY, 30, 30, world.rectangle5X, world.rectangle5Y, 800, 30):
        world.gameover=True       
    if collision(world.rectangleX, world.rectangleY, 30, 30, world.rectangle6X, world.rectangle6Y, 750, 30):
        world.gameover=True       
    if collision(world.rectangleX, world.rectangleY, 30, 30, world.rectangle7X, world.rectangle7Y, 600, 30):
        world.gameover=True       
    if collision(world.rectangleX, world.rectangleY, 30, 30, world.rectangle8X, world.rectangle8Y, 20, 100):
        world.gameover=True   
    if collision(world.rectangleX, world.rectangleY, 30, 30, world.rectangle8X, world.rectangle8Y, 20, 100):
        world.gameover=True      
    if collision(world.rectangleX, world.rectangleY, 30, 30, world.rectangle9X, world.rectangle9Y, 20, 100):
        world.gameover=True      
    if collision(world.rectangleX, world.rectangleY, 30, 30, world.rectangle10X, world.rectangle10Y, 20, 100):
        world.gameover=True      
    if collision(world.rectangleX, world.rectangleY, 30, 30, world.rectangle11X, world.rectangle11Y, 20, 100):
        world.gameover=True      
    if collision(world.rectangleX, world.rectangleY, 30, 30, world.rectangle12X, world.rectangle12Y, 20, 100):
        world.gameover=True      
        
    #check for overlap between sushi and red square\
    #upper left corner
    if collision(world.rectangleX, world.rectangleY, 30, 30, world.unagiX-(world.unagiwidth/2), world.unagiY-(world.unagiheight/2), world.unagiwidth, world.unagiheight):
        world.score=world.score+1
        world.unagiX=random.choice([650, 550, 450, 350, 250, 150, 50, 950, 850, 750])
        world.unagiY=random.choice([50, 150, 250, 350, 450, 550, 650])
        
# check for overlapping rectangles
# arguments: rect1 x, rect1 y, rect1 w, rect1 h, rect2 x, rect2 y, rect2 w, rect2 h
# return: boolean true when 2 rectangles overlap, false when 2 rectangles don't overlap
def collision(rect1x, rect1y, rect1w, rect1h, rect2x, rect2y, rect2w, rect2h):
    #upper left of rect1
    if rect1x>rect2x and rect1x<rect2x+rect2w and rect1y>rect2y and rect1y<rect2y+rect2h:
        return True
    #upper right of rect1
    elif rect1x+rect1w>rect2x and rect1x+rect1w<rect2x+rect2w and rect1y>rect2y and rect1y<rect2y+rect2h:
        return True
    #lower left of rect1
    elif rect1x>rect2x and rect1x<rect2x+rect2w and rect1y+rect1h>rect2y and rect1y+rect1h<rect2y+rect2h:
        return True
    #lower right of rect1
    elif rect1x+rect1w>rect2x and rect1x+rect1w<rect2x+rect2w and rect1y+rect1h>rect2y and rect1y+rect1h<rect2y+rect2h:
        return True
    #no overlap
    else:
        return False



# this function is called every frame to draw your world
 
def drawWorld(world):
    #Instructions page
    if world.instructions==True:
        drawString("Welcome to SushiSnake!", 320, 100, 40, "red")
        drawString("The objective of the game is to collect as much sushi as possible", 170, 150, color="white")
        drawString("Use the arrow keys to move", 360, 200, color="white")
        drawString("If you hit any of the moving rectangles, you die", 270, 250, color="white")
        drawString("Press enter/return to start the game. Good luck!", 270, 300, color="white")
    else:
        #Sushi
        drawImage(world.unagi, world.unagiX, world.unagiY)
        #Horizontal rectangles
        fillRectangle(world.rectangleX, world.rectangleY, 30, 30, "red")
        fillRectangle(world.rectangle2X, world.rectangle2Y, 800, 30, "white")
        fillRectangle(world.rectangle3X, world.rectangle3Y, 750, 30, "white")
        fillRectangle(world.rectangle4X, world.rectangle4Y, 800, 30, "white")
        fillRectangle(world.rectangle5X, world.rectangle5Y, 800, 30, "white")
        fillRectangle(world.rectangle6X, world.rectangle6Y, 750, 30, "white")
        fillRectangle(world.rectangle7X, world.rectangle7Y, 600, 30, "white")
        #Vertical rectangles
        fillRectangle(world.rectangle8X, world.rectangle8Y, 20, 100, "white")
        fillRectangle(world.rectangle9X, world.rectangle9Y, 20, 100, "white")
        fillRectangle(world.rectangle10X, world.rectangle10Y, 20, 100, "white")
        fillRectangle(world.rectangle11X, world.rectangle11Y, 20, 100, "white")
        fillRectangle(world.rectangle12X, world.rectangle12Y, 20, 100, "white")  
        #Score
        drawString("Score:"+str(world.score), 850, 20, color="red")
    #Game over
    if world.gameover==True:
        drawString("YOU DIED!", 350, 200, 80, "red")
        drawString("Press space to restart", 390, 260, color="white")
 
runGraphics(startWorld, updateWorld, drawWorld)