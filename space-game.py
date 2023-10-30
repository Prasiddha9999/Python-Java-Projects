import pygame
pygame.init()

FPS = 60
Width, Height = 800, 680
Win = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('Space wars')
space_ship = pygame.image.load('spaceship1_1.png')
warship = pygame.transform.scale(space_ship, (54, 64))
warship1 = pygame.transform.rotate(warship, 90 )
warship2 = pygame.transform.rotate(warship, 270)
bg = pygame.image.load('bg.png')

class Spaceship():
    def __init__(self, width, height):
        self.width = width
        self.height = height


class ship1(Spaceship):
    def __init__(self, x, y, width, height):
        super().__init__(width, height)
        self.x = x
        self.y = y
        self.right = True
        self.left = False
        self.up = False
        self.down = False
        self.vel = 5
        self.health = 20
        self.visible = True
        self.Rect = (self.x, self.y, self.width, self.height-10)

    def draw(self):
        Win.blit(warship1, (self.x, self.y))
        self.Rect = (self.x-2, self.y-3, self.width, self.height - 10)
        #pygame.draw.rect(Win ,(255,0,0), self.Rect, 1)

    def hit(self):
        if self.health > 0 :
            self.health -= 1
        else:
            self.visible = False
        
        
        
    
class ship2(Spaceship):
    def __init__(self, x, y, width, height):
        super().__init__(width, height)
        self.x = x
        self.y = y
        self.right = True
        self.left = False
        self.up = False
        self.down = False
        self.vel = 5
        self.health = 20
        self.visible = True
        self.Rect = (self.x, self.y, self.width, self.height - 10)

    def draw(self):
        Win.blit(warship2, (self.x, self.y))
        self.Rect = (self.x-2, self.y-3, self.width, self.height - 10)
        #pygame.draw.rect(Win ,(255,0,0), self.Rect, 1)

    def hit(self):
        if self.health > 0 :
            self.health -= 1
        else:
            self.visible = False
class projectile:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = 10 
        self.color = color

    def draw(self, Win):
        pygame.draw.circle(Win, self.color, (self.x, self.y), 8 )
        
        

def DrawWindow():
    #Win.fill((0, 255, 0))
    Win.blit(bg, (0, 0))
    pygame.draw.rect(Win, (0, 0, 244), (round(800/2 - 10 ), 0,  20, 680))
    text1 = font.render('Score '+ str(score1) , 1, (0,0,0))
    Win.blit(text1, (40, 10))
    text2 = font.render('Score ' + str(score2), 1, (0,0,0))
    Win.blit(text2, (650, 10))
    if ship11.visible:
        ship11.draw()
    if ship22.visible:
        ship22.draw()
    if ship11.visible:
        for bullet in bullet_of_P1:
            bullet.draw(Win)
    if ship22.visible:
        for bullets in bullet_of_P2:
            bullets.draw(Win)
    pygame.display.update()


font = pygame.font.SysFont('comicsans', 40 , True)
mainship = Spaceship(64, 64)
ship11 = ship1(20, 20, 64, 64)
ship22 = ship2(720, 20, 64, 64)
bullet_of_P1 = []
bullet_of_P2 = []


def main():
    clock = pygame.time.Clock()
    run = True
    shootc1 = 0
    shootc2 = 0
    global score1
    global score2
    score1 = 0
    score2 = 0
    while run:
        DrawWindow()
        clock.tick(FPS)

        print(bullet_of_P1)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if ship11.visible:
            for bullet in bullet_of_P1:
                if bullet.x + bullet.speed > ship11.x  and bullet.x + bullet.speed < Width:
                    bullet.x += bullet.speed
                else:
                    bullet_of_P1.remove(bullet)
                if bullet.y + bullet.radius > ship22.Rect[1] and bullet.y - bullet.radius < ship22.Rect[3] + ship22.Rect[1] and ship22.visible == True:
                    if bullet.x + bullet.radius > ship22.Rect[0] and bullet.x - bullet.radius < ship22.Rect[2] + ship22.Rect[0]:
                        ship22.hit()
                        print("got hit")
                        score1 += 1
                        bullet_of_P1.remove(bullet)
        if ship22.visible:
            for bullets in bullet_of_P2:
                if bullets.x - bullets.speed < ship22.x and bullets.x - bullets.speed > 0:
                    bullets.x -= bullets.speed
                else:
                    bullet_of_P2.remove(bullets)
                    
                if bullets.y + bullets.radius > ship11.Rect[1] and bullets.y - bullets.radius < ship11.Rect[3] + ship11.Rect[1] and ship11.visible == True:
                    if bullets.x + bullets.radius > ship11.Rect[0] and bullets.x - bullets.radius < ship11.Rect[2] + ship11.Rect[0]:
                        ship11.hit()
                        print('got hit')
                        score2 += 1
                        bullet_of_P2.remove(bullets)

        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and ship22.y > 30:
            ship22.y -= ship22.vel
            ship22.up = True
            ship22.down = False
        
            
            
        if keys[pygame.K_DOWN] and ship22.y <= Height - ship22.height - ship22.vel:
            ship22.y += ship22.vel
            ship22.down = True
            ship22.up = False
            
            
            
        if keys[pygame.K_RIGHT] and ship22.x < Width - ship22.width - ship22.vel:
            ship22.x += ship22.vel
            ship22.right = True
            ship22.left = False
            
            
            
        if keys[pygame.K_LEFT] and ship22.x > round(800/2 + 20) :
            ship22.x -= ship22.vel
            ship22.left = True
            ship22.right = False

        if keys[pygame.K_SPACE] and shootc1 == 0 :
            if len(bullet_of_P1) < 5:
                bullet_of_P1.append(projectile(ship11.x + ship11.width + 3, ship11.y + ship11.height//2 - 5, 8, (255, 0, 0)))
            
        if keys[pygame.K_w] and ship11.y > 30:
            ship11.y -= ship11.vel
            ship11.up = True
            ship11.down = False
        
            
            
        if keys[pygame.K_s] and ship11.y <= Height - ship11.height - ship11.vel:
            ship11.y += ship11.vel
            ship11.down = True
            ship11.up = False
            
            
            
        if keys[pygame.K_d] and ship11.x < round(800/2 - 80):
            ship11.x += ship11.vel
            ship11.right = True
            ship11.left = False
            
            
            
        if keys[pygame.K_a] and ship11.x > 10:
            ship11.x -= ship11.vel
            ship11.left = True
            ship11.right = False

        if keys[pygame.K_RCTRL] and shootc2 == 0:
            if len(bullet_of_P2) < 5:
                bullet_of_P2.append(projectile(ship22.x - 4, ship22.y + ship22.height//2 -5 , 8, (255, 255, 88)))


        if keys[pygame.K_SPACE]:
            shootc1 += 1
            if shootc1 > 15:
                shootc1 = 0
            
        
        if keys[pygame.K_RCTRL]:
            shootc2 += 1
            if shootc2 > 15:
                shootc2 = 0
            
    pygame.quit()

    

    

if __name__== '__main__':
    main()
      
