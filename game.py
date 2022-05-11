import pygame,sys
def ball_animation():
    global ball_speed_x,ball_speed_y,player,player_speed,opponent_speed,opponent      
    ball.x +=ball_speed_x
    ball.y +=ball_speed_y

    if ball.top<= 0 or ball.bottom>=screen_height:
        ball_speed_y*=-1
    if ball.left<=0 or ball.right>=screen_width:
        ball_speed_x*=-1
    if ball.colliderect(player):
    
        ball_speed_x*=-1
    if ball.colliderect(opponent):
        ball_speed_y*=-1
        ball_speed_x=-1

    if ball.colliderect(opponent) and ball_speed_y>0:
        if abs(ball.left-opponent.right)<10:
            ball_speed_x*=-10
        elif abs(ball.bottom-opponent.top)<10 and ball_speed_y<0:
            ball_speed_y*=-1
        elif abs(ball.top-opponent.bottom)<10 and ball_speed_y <0:
            ball_speed_y *=-1

def player_animation():
    player.y+=player_speed
    if player.top<=0:
        player.top=0
    if player.bottom>=screen_height:
        player.bottom=screen_height


def opponent_ai():
	if opponent.top < ball.y:
		opponent.y += opponent_speed
	if opponent.bottom > ball.y:
		opponent.y -= opponent_speed

	if opponent.top <= 0:
		opponent.top = 0
	if opponent.bottom >= screen_height:
		opponent.bottom = screen_height
    
    
pygame.init()
clock=pygame.time.Clock()
#main window dimensions
screen_width=600
screen_height=660
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Ping')

#game rectangles

ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10,140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10,140)
bg_color=pygame.Color('blue')
light_grey=(0,255,255)
blek=pygame.Color('black')

ball_speed_x=7
ball_speed_y=7
player_speed=0
opponent_speed=7
while True :
    #Handling input
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                player_speed+=7
            if event.key==pygame.K_UP:
                player_speed-=7
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_DOWN :
                player_speed-=7
            if event.key==pygame.K_UP:
                player_speed+=7




    ball_animation()
    player_animation()
    opponent_ai()
    # visuals

    screen.fill(bg_color)
    pygame.draw.rect(screen,light_grey,player)
    pygame.draw.rect(screen,light_grey,opponent)
    pygame.draw.ellipse(screen,light_grey,ball)
    pygame.draw.aaline(screen,light_grey,(screen_width / 2, 0),(screen_width/2,screen_height))
    # pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0),(screen_width / 2, screen_height))


    #Updating the window
    pygame.display.flip()
    clock.tick(60)
