import sys, pygame
import time
pygame.init()
size = width, height = 1920, 1080
speed = [2, 2]
red = 141, 9, 9
screen = pygame.display.set_mode(size)
pygame.time.Clock()
pygame.display.set_caption('Super Slaughter House Escape(DUPER HARD CONTROLS)')
sprite = pygame.image.load("slaughter.gif.png")
spriterect = sprite.get_rect()
monster = pygame.image.load("monster.png")
monsterect = monster.get_rect()
bg_image = pygame.image.load("untitled.png").convert()
pygame.mixer.init()
pygame.mixer.music.load("SlaughterHouse.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)
stuff = pygame.image.load('stuff.png')
show = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    spriterect = spriterect.move(speed)
    keys = pygame.key.get_pressed()
    spriterect.clamp_ip((0, 0, width, height))
    spriterect.x += (keys[pygame.K_d] - keys[pygame.K_a]) * 8
    spriterect.y += (keys[pygame.K_s] - keys[pygame.K_w]) * 8
    spriterect.x
    with open("LOG.txt", "w") as f:
        print("Player Moved", file=f)
    spriterect.y
    if keys[pygame.K_a]:
        if spriterect.left:
            speed[1] = -speed[1]
            with open("LOG.txt", "a") as f:
                print("LOG:Sprite Move Left", file=f)
    if spriterect.top < 0 or spriterect.bottom > height or width or width and height:
        speed[1] = -speed[1]
        with open("LOG.txt", "a") as f:
            print('LOG:Sprite Top/Bottom Stabilized', file=f)
    if spriterect.left or spriterect.right > width:
        speed[0] = -speed[0]
        with open("LOG.txt", "a") as f:
            print('LOG:Prevented Sprite From Going Out Of Bounds', file=f)
    dir_vec = pygame.math.Vector2(spriterect.center) - monsterect.center
    if dir_vec.length() > 0: monsterect.center += dir_vec.normalize() * 4
    ms =  pygame.time.get_ticks()
    seconds = ms / 1000.0
    if seconds > 3 and spriterect.colliderect(monsterect):
        pygame.mixer.music.stop()
        screen.fill(red)
        time.sleep(1)
        with open("LOG.txt", "a") as f:
            print('LOG:Sprite Has Collided ):', file=f)
        sys.exit()
    bg_image = pygame.transform.scale(bg_image, (width, height))
    screen.blit(bg_image, (0, 0))
    screen.blit(sprite, spriterect)
    screen.blit(monster, monsterect)
    if seconds > 30:
        pygame.mixer.music.stop()
        win = pygame.image.load('win.png')
        with open("LOG.txt", "a") as f:
            print('LOG:LOADED "win.png"', file=f)
        winscale = pygame.transform.scale(win, (width, height))
        screen.blit(winscale, (0, 0))
    pygame.display.flip()
