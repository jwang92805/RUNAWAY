from gamelib import *

game=Game(800,600,"RUNAWAY")
game.setMusic("sounds\\MarioTheme.wav")

cabin=Image("images\\cabin (1).png",game)
cabin.resizeBy(-40)
cabin.moveTo(1200,350)
cabin.setSpeed(2,90)

boy=Animation("images\\kid.png",8,game,108,140,5)
boy.moveTo(100,490)
boy.resizeBy(-10)
boy.stop()

heart=[]
for times in range(10):
    heart.append(Image("images\\heart.png",game))

for h in heart:
    x=randint(700,10000)
    y=460
    s=2
    h.moveTo(x,y)
    h.setSpeed(s,90)
    h.visible=True
    h.resizeBy(-95)

jumping = False #Used to check to see if you are jumping
landed = False #Used to check to see if you have landed on the ground
factor = 1 #Used for a slowing effect of the jumping
bushcount = 0
trashcount = 0
carcount = 0
cactuscount = 0
rockcount = 0
gorillacount = 0
magmacount = 0


bk1=Image("images\\neighborhood.jpg",game)
bk1.resizeBy(30)

bk2=Image("images\\city.jpg",game)
bk2.resizeBy(85)

bk3=Image("images\\desert2.jpg",game)
bk3.resizeBy(40)

bk4=Image("images\\bk6.png",game)
bk4.resizeTo(game.width, game.height)

bk5=Image("images\\mountain.png",game)
bk5.resizeBy(40)

bk6=Image("images\\jungle.gif",game)
bk6.resizeBy(50)

bk7=Image("images\\volcano2.png",game)
bk7.resizeTo(game.width, game.height)

bk8=Image("images\\forest.jpg",game)

trash=[]
for times in range(15):
    trash.append(Image("images\\trash.png",game))

for t in trash:
    x=randint(700,10000)
    y=495
    s=2
    t.moveTo(x,y)
    t.setSpeed(s,90)
    t.resizeBy(-30)
    t.visible=True

bush=[]
for times in range(30):
    bush.append(Image("images\\bush.png",game))

for bu in bush:
    x=randint(700,10000)
    y=480
    s=randint(2,5)
    bu.moveTo(x,y)
    bu.setSpeed(s,90)
    bu.resizeBy(-80)
    bu.visible=True

cars=[]
for times in range(10):
    cars.append(Image("images\\car.png",game))

for c in cars:
    x=randint(700,10000)
    y=510
    s=3.5
    c.moveTo(x,y)
    c.setSpeed(s,90)
    c.resizeBy(-60)
    c.visible=True

cacti=[]
for times in range(30):
    cacti.append(Image("images\\cactus.png",game))

for ca in cacti:
    x=randint(700,10000)
    y=randint(450,475)
    s=2
    ca.moveTo(x,y)
    ca.setSpeed(s,90)
    ca.resizeBy(-90)
    ca.visible=True

rocks=[]
for times in range(45):
    rocks.append(Image("images\\rock2.png",game))

for r in rocks:
    x=randint(700,10000)
    y=randint(450,480)
    s=randint(2,5)
    r.moveTo(x,y)
    r.setSpeed(s,90)
    r.resizeBy(-87)
    r.visible=True
    
gorilla=[]
for times in range(50):
    gorilla.append(Image("images\\gorilla.png",game))

for g in gorilla:
    x=randint(700,10000)
    y=420
    s=randint(3,5)
    g.moveTo(x,y)
    g.setSpeed(s,90)
    g.resizeBy(-77)
    g.visible=True

branch=[] #Empty List
for times in range(30):
    branch.append(Image("images\\branch.png",game))

for b in branch:
    x = randint(100,700)
    y = -randint(100,5000)#places the objects off the screen on the top side from a range of (-100)-(-5000)
    s = randint(1,2)#speed 1-3
    b.moveTo(x,y)
    b.setSpeed(s,180)
    b.resizeBy(-89)

magma=[]
for times in range(30):
    magma.append(Image("images\\volcanic wolf.png",game))

for m in magma:
    x=randint(700,10000)
    y=randint(495,515)
    s=randint(2,5)
    size=randint(-70,-50)
    m.moveTo(x,y)
    m.setSpeed(s,90)
    m.resizeBy(size)
    m.visible=True

bScreen=Image("images\\bScreen.png",game)#creates the title screen
bScreen.resizeTo(game.width,game.height)
bScreen.draw()#draws the title image
game.update(1)#updates the game
game.wait(K_SPACE)#game starts when space bar is pressed

cScreen=Image("images\\cScreen.png",game)#creates the title screen
cScreen.resizeTo(game.width,game.height)
cScreen.draw()#draws the title image
game.drawText("PRESS [RIGHT ->] TO START",10,5)
game.update(1)#updates the game
game.wait(K_RIGHT)#game starts when space bar is pressed

game.setBackground(bk1)
game.playMusic()
    
while not game.over:
    game.processInput()

    game.scrollBackground("left",3)
    
    if boy.y >= 475:
        landed = True
        #475 is the floor.  Decision can be replaced with a more complex condition based on game
   
    if jumping:
        boy.y -= 30 * factor
        #Make the character go up.  Factor creates a slowing effect to the jump
        factor *= .95
        landed = False
        #Since you are jumping you are no longer staying on land
        if factor < .18:
            jumping = False
            #Stop jumping once the slowing effect finishes
            factor = 1
            
    if keys.Pressed[K_SPACE] and landed and not jumping:
            #If you landed on the floor and are not jumping and press the SpaceBar then jump
            jumping = True

    if not landed:
        boy.y += 9
        #If you haven't landed then you are in the air, so you should fall.

    if keys.Pressed[K_LEFT]:
        boy.prevFrame()
        boy.x -= 8
    elif keys.Pressed[K_RIGHT]:
        boy.nextFrame()
        boy.x += 8
    else:
        boy.draw()

    for t in trash:
        t.move()
        if t.collidedWith(boy):
            t.visible=False
            boy.health-=10
            trashcount+=1
        if t.isOffScreen("left"):
            x=randint(700,10000)
            y=495
            s=2
            t.moveTo(x,y)
            t.setSpeed(s,90)
            trashcount+=1

    if trashcount == 5:
        game.over=True
        #trashcount.visible=False
        
    if boy.health<10:
        game.over=True

    game.drawText("Health: " + str(boy.health),10,5)
    game.drawText("Trash Count: " + str(trashcount),150,5)
    game.update(60)
game.over=False



game.setBackground(bk2)

while not game.over:
    game.processInput()

    game.scrollBackground("left",3)
    
    if boy.y >= 510:
        landed = True
        #475 is the floor.  Decision can be replaced with a more complex condition based on game
   
    if jumping:
        boy.y -= 30 * factor
        #Make the character go up.  Factor creates a slowing effect to the jump
        factor *= .95
        landed = False
        #Since you are jumping you are no longer staying on land
        if factor < .18:
            jumping = False
            #Stop jumping once the slowing effect finishes
            factor = 1
            
    if keys.Pressed[K_SPACE] and landed and not jumping:
            #If you landed on the floor and are not jumping and press the SpaceBar then jump
            jumping = True

    if not landed:
        boy.y += 9
        #If you haven't landed then you are in the air, so you should fall.

    if keys.Pressed[K_LEFT]:
        boy.prevFrame()
        boy.x -= 8
    elif keys.Pressed[K_RIGHT]:
        boy.nextFrame()
        boy.x += 8
    else:
        boy.draw()

    for c in cars:
        c.move()
        if c.collidedWith(boy):
            c.visible=False
            boy.health-=10
            carcount+=1
        if c.isOffScreen("left"):
            x=randint(700,10000)
            y=510
            speed=3.5
            c.moveTo(x,y)
            c.setSpeed(speed,90)
            carcount+=1

    for h in heart:
        h.move()
        if h.collidedWith(boy):
            h.visible=False
            boy.health+=20

    if carcount == 20:
        game.over=True

    if boy.health < 10:
        game.over=True

    game.drawText("Health: " + str(boy.health),10,5)
    game.drawText("Car Count: " + str(carcount),150,5) 

    game.update(60)
game.over=False


game.setBackground(bk3)

while not game.over:
    game.processInput()

    game.scrollBackground("left",3)
    
    if boy.y >= 475:
        landed = True
        #475 is the floor.  Decision can be replaced with a more complex condition based on game
   
    if jumping:
        boy.y -= 30 * factor
        #Make the character go up.  Factor creates a slowing effect to the jump
        factor *= .95
        landed = False
        #Since you are jumping you are no longer staying on land
        if factor < .18:
            jumping = False
            #Stop jumping once the slowing effect finishes
            factor = 1
            
    if keys.Pressed[K_SPACE] and landed and not jumping:
            #If you landed on the floor and are not jumping and press the SpaceBar then jump
            jumping = True

    if not landed:
        boy.y += 9
        #If you haven't landed then you are in the air, so you should fall.

    if keys.Pressed[K_LEFT]:
        boy.prevFrame()
        boy.x -= 8
    elif keys.Pressed[K_RIGHT]:
        boy.nextFrame()
        boy.x += 8
    else:
        boy.draw()

    for ca in cacti:
        ca.move()
        if ca.collidedWith(boy):
            ca.visible=False
            boy.health-=10
            cactuscount+=1
        if ca.isOffScreen("left"):
            x=randint(700,10000)
            y=475
            s=2
            ca.moveTo(x,y)
            ca.setSpeed(s,90)
            cactuscount+=1

    for h in heart:
        h.move()
        if h.collidedWith(boy):
            h.visible=False
            boy.health+=20

    if cactuscount == 30:
        game.over=True

    if boy.health < 10:
        game.over=True

    game.drawText("Health: " + str(boy.health),10,5)
    game.drawText("Cactus Count: " + str(cactuscount),150,5)
    
    game.update(60)
game.over=False


game.setBackground(bk4)

while not game.over:
    game.processInput()

    game.scrollBackground("left",3)
    
    if boy.y >= 470:
        landed = True
        #475 is the floor.  Decision can be replaced with a more complex condition based on game
   
    if jumping:
        boy.y -= 30 * factor
        #Make the character go up.  Factor creates a slowing effect to the jump
        factor *= .95
        landed = False
        #Since you are jumping you are no longer staying on land
        if factor < .18:
            jumping = False
            #Stop jumping once the slowing effect finishes
            factor = 1
            
    if keys.Pressed[K_SPACE] and landed and not jumping:
            #If you landed on the floor and are not jumping and press the SpaceBar then jump
            jumping = True

    if not landed:
        boy.y += 9
        #If you haven't landed then you are in the air, so you should fall.

    if keys.Pressed[K_LEFT]:
        boy.prevFrame()
        boy.x -= 8
    elif keys.Pressed[K_RIGHT]:
        boy.nextFrame()
        boy.x += 8
    else:
        boy.draw()

    for bu in bush:
        bu.move()
        if bu.collidedWith(boy):
            bu.visible=False
            boy.health-=10
            bushcount+=1
        if bu.isOffScreen("left"):
            x=randint(700,10000)
            y=480
            s=randint(2,5)
            bu.moveTo(x,y)
            bu.setSpeed(s,90)
            bushcount+=1

    for h in heart:
        h.move()
        if h.collidedWith(boy):
            h.visible=False
            boy.health+=20

    if bushcount == 35:
        game.over=True

    if boy.health < 10:
        game.over=True

    game.drawText("Health: " + str(boy.health),10,5)
    game.drawText("Bush Count: " + str(bushcount),150,5)
    
    game.update(60)
game.over=False


game.setBackground(bk5)

while not game.over:
    game.processInput()

    game.scrollBackground("left",3)
    
    if boy.y >= 475:
        landed = True
        #475 is the floor.  Decision can be replaced with a more complex condition based on game
   
    if jumping:
        boy.y -= 30 * factor
        #Make the character go up.  Factor creates a slowing effect to the jump
        factor *= .95
        landed = False
        #Since you are jumping you are no longer staying on land
        if factor < .18:
            jumping = False
            #Stop jumping once the slowing effect finishes
            factor = 1
            
    if keys.Pressed[K_SPACE] and landed and not jumping:
            #If you landed on the floor and are not jumping and press the SpaceBar then jump
            jumping = True

    if not landed:
        boy.y += 9
        #If you haven't landed then you are in the air, so you should fall.

    if keys.Pressed[K_LEFT]:
        boy.prevFrame()
        boy.x -= 8
    elif keys.Pressed[K_RIGHT]:
        boy.nextFrame()
        boy.x += 8
    else:
        boy.draw()

    for r in rocks:
        r.move()
        if r.collidedWith(boy):
            r.visible=False
            boy.health-=10
            rockcount+=1
        if r.isOffScreen("left"):
            x=randint(700,10000)
            y=randint(450,480)
            s=randint(2,5)
            r.moveTo(x,y)
            r.setSpeed(s,90)
            rockcount+=1

    for h in heart:
        h.move()
        if h.collidedWith(boy):
            h.visible=False
            boy.health+=20

    if rockcount == 40:
        game.over=True

    if boy.health < 10:
        game.over=True

    game.drawText("Health: " + str(boy.health),10,5)
    game.drawText("Rock Count: " + str(rockcount),150,5)
    
    game.update(60)
game.over=False


game.setBackground(bk6)

while not game.over:
    game.processInput()

    game.scrollBackground("left",3)
    
    if boy.y >= 445:
        landed = True
        #475 is the floor.  Decision can be replaced with a more complex condition based on game
   
    if jumping:
        boy.y -= 30 * factor
        #Make the character go up.  Factor creates a slowing effect to the jump
        factor *= .95
        landed = False
        #Since you are jumping you are no longer staying on land
        if factor < .18:
            jumping = False
            #Stop jumping once the slowing effect finishes
            factor = 1
            
    if keys.Pressed[K_SPACE] and landed and not jumping:
            #If you landed on the floor and are not jumping and press the SpaceBar then jump
            jumping = True

    if not landed:
        boy.y += 9
        #If you haven't landed then you are in the air, so you should fall.

    if keys.Pressed[K_LEFT]:
        boy.prevFrame()
        boy.x -= 8
    elif keys.Pressed[K_RIGHT]:
        boy.nextFrame()
        boy.x += 8
    else:
        boy.draw()

    for g in gorilla:
        g.move()
        if g.collidedWith(boy):
            g.visible=False
            boy.health-=10
            gorillacount+=1
        if g.isOffScreen("left"):
            x=randint(700,10000)
            y=420
            s=randint(2,5)
            g.moveTo(x,y)
            g.setSpeed(s,90)
            gorillacount+=1

    for b in branch:
        b.move()
        if b.collidedWith(boy):
            b.visible=False
            boy.health-=10
        if b.y >= 445:
            b.visible=False

    for h in heart:
        h.move()
        if h.collidedWith(boy):
            h.visible=False
            boy.health+=20
        if g.isOffScreen("left"):
            x=randint(700,7000)
            y=450
            s=randint(3,5)
            g.moveTo(x,y)
            g.setSpeed(s,90)
        

    if gorillacount == 40:
        game.over=True

    if boy.health < 10:
        game.over=True

    game.drawText("Health: " + str(boy.health),10,5)
    game.drawText("Gorilla Count: " + str(gorillacount),150,5)
    
    game.update(60)
game.over=False


game.setBackground(bk7)

while not game.over:
    game.processInput()

    game.scrollBackground("left",3)
    
    if boy.y >= 515:
        landed = True
        #475 is the floor.  Decision can be replaced with a more complex condition based on game
   
    if jumping:
        boy.y -= 30 * factor
        #Make the character go up.  Factor creates a slowing effect to the jump
        factor *= .95
        landed = False
        #Since you are jumping you are no longer staying on land
        if factor < .18:
            jumping = False
            #Stop jumping once the slowing effect finishes
            factor = 1
            
    if keys.Pressed[K_SPACE] and landed and not jumping:
            #If you landed on the floor and are not jumping and press the SpaceBar then jump
            jumping = True

    if not landed:
        boy.y += 9
        #If you haven't landed then you are in the air, so you should fall.

    if keys.Pressed[K_LEFT]:
        boy.prevFrame()
        boy.x -= 8
    elif keys.Pressed[K_RIGHT]:
        boy.nextFrame()
        boy.x += 8
    else:
        boy.draw()

    for m in magma:
        m.move()
        if m.collidedWith(boy):
            m.visible=False
            boy.health-=20
            magmacount+=1
        if m.isOffScreen("left"):
            x=randint(700,10000)
            y=randint(495,515)
            s=randint(2,5)
            size=randint(-70,-50)
            m.resizeBy(size)
            m.moveTo(x,y)
            m.setSpeed(s,90)
            magmacount+=1

    for h in heart:
        h.move()
        if h.collidedWith(boy):
            h.visible=False
            boy.health+=20
        

    if magmacount == 40:
        game.over=True

    if boy.health < 10:
        game.over=True

    game.drawText("Health: " + str(boy.health),10,5)
    game.drawText("Magma Wolf Count: " + str(magmacount),150,5)
    
    game.update(60)
game.over=False


game.setBackground(bk8)

while not game.over:
    game.processInput()

    game.scrollBackground("left",3)

    cabin.move()
    
    if boy.y >= 455:
        landed = True
        #475 is the floor.  Decision can be replaced with a more complex condition based on game
   
    if jumping:
        boy.y -= 30 * factor
        #Make the character go up.  Factor creates a slowing effect to the jump
        factor *= .95
        landed = False
        #Since you are jumping you are no longer staying on land
        if factor < .18:
            jumping = False
            #Stop jumping once the slowing effect finishes
            factor = 1
            
    if keys.Pressed[K_SPACE] and landed and not jumping:
            #If you landed on the floor and are not jumping and press the SpaceBar then jump
            jumping = True

    if not landed:
        boy.y += 9
        #If you haven't landed then you are in the air, so you should fall.

    if keys.Pressed[K_LEFT]:
        boy.prevFrame()
        boy.x -= 8
    elif keys.Pressed[K_RIGHT]:
        boy.nextFrame()
        boy.x += 8
    else:
        boy.draw()

    if boy.collidedWith(cabin):
        game.over=True

    if boy.health < 10:
        game.over=True
    
    game.drawText("Health: " + str(boy.health),10,5)
    
    game.update(60)
eScreen=Image("images\\eScreen.png",game)#creates the title screen
eScreen.resizeTo(game.width,game.height)
eScreen.draw()#draws the title image
game.drawText("Health: " + str(boy.health),600,48)
game.update(1)#updates the game
game.wait(K_ESCAPE)#game starts when space bar is pressed
game.quit()
