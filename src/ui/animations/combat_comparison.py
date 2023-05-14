import pygame
import random
from mechanics.animations import Animation
class backround_box_move(Animation):
    def __init__(self, start=0, duration=1, sub_animations=[], on_animation_end=[],text=""):
        super().__init__(start, duration, sub_animations, on_animation_end)
        self.x_pos = 0
        self.y_pos = 0
        self.back_ground_color = (230,50,30)
        self.color = (230,170,10)
        self.text= text

    def setup(self):
        self.sub_animations=[]
        self.x_pos = 1280
        self.y_pos = 250
        round_text_appear =text_appear(0.3,0.75,text=self.text,shadow=True)
        round_text_appear.play()
        self.sub_animations.append(round_text_appear)

    def render(self, screen):
        pygame.draw.rect(screen, self.back_ground_color,
                         (self.x_pos+100, self.y_pos, 4000, 220))
        pygame.draw.rect(screen, self.color,
                         (self.x_pos, self.y_pos+35, 4200, 150))
        self.x_pos -=3

class backround_box_move_random_color(Animation):
    def __init__(self, start=0, duration=1, sub_animations=[], on_animation_end=[],text="",rgb_lower=60,rgb_upper=245):
        super().__init__(start, duration, sub_animations, on_animation_end)
        self.x_pos = 0
        self.y_pos = 0
        self.back_ground_color = (random.randint(rgb_lower,rgb_upper),random.randint(rgb_lower,rgb_upper),random.randint(rgb_lower,rgb_upper))
        self.color = (random.randint(rgb_lower,rgb_upper),random.randint(rgb_lower,rgb_upper),random.randint(rgb_lower,rgb_upper))
        self.text= text

    def setup(self):
        self.sub_animations=[]
        self.x_pos = 1280
        self.y_pos = 250
        round_text_appear =text_appear(0.3,0.75,text=self.text,shadow=True)
        round_text_appear.play()
        self.sub_animations.append(round_text_appear)

    def render(self, screen):
        pygame.draw.rect(screen, self.back_ground_color,
                         (self.x_pos+100, self.y_pos, 4000, 220))
        pygame.draw.rect(screen, self.color,
                         (self.x_pos, self.y_pos+35, 4200, 150))
        self.x_pos -=3

class text_appear(Animation):
    def __init__(self, start=1, duration=1, sub_animations=[], on_animation_end=[],text="",fontsize=78,x_pos=640,y_pos=360,shadow=False):
        super().__init__(start, duration, sub_animations, on_animation_end)
        self.text_font = pygame.font.Font('freesansbold.ttf', fontsize)
        self.text = self.text_font.render(text, True, (0, 0, 0))
        self.text_shadow = self.text_font.render(text, True, (50, 50, 50))
        self.text_rect = self.text.get_rect()
        self.text_shadow_rect = self.text_shadow.get_rect()
        self.x_pos=x_pos
        self.y_pos=y_pos
        self.shadow= shadow

    def render(self, screen):
        self.text_rect.center = (self.x_pos,self.y_pos)
        self.text_shadow_rect.center = (self.x_pos+5,self.y_pos+2)
        if self.shadow:
            screen.blit(self.text_shadow, (self.text_shadow_rect.x, self.text_shadow_rect.y))
        screen.blit(self.text, (self.text_rect.x, self.text_rect.y))

class image_appear(Animation):
    def __init__(self,image , start=1, duration=1, sub_animations=[], on_animation_end=[],x_pos=640,y_pos=360,scale=1):
        super().__init__(start, duration, sub_animations, on_animation_end)

        self.img = image
        self.imgWidth = self.img.get_width()
        self.imgHeight = self.img.get_height()
        self.image = pygame.transform.scale(
        self.img, (int(self.imgWidth)*scale, int(self.imgHeight)*scale))
        self.rect = self.image.get_rect()
        self.rect.center =(x_pos,y_pos)

    def render(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def stop(self):
        self.rect.center =(-2000,-2000)
        return super().setup()


class game_over(Animation):
    def __init__(self, start=0, duration=1, sub_animations=[], on_animation_end=[],text=""):
        super().__init__(start, duration, sub_animations, on_animation_end)
        self.x_pos = 0
        self.y_pos = 0
        self.back_ground_color = (255,40,150)
        self.color = (255,0,0)
        self.text= text
        self.alpha=0
        

    def setup(self):
        self.sub_animations=[]
        self.x_pos = 1280
        self.y_pos = 250
        self.alpha=0
        round_text_appear =text_appear(0.3,0.75,text=self.text,shadow=True)
        round_text_appear.play()
        self.sub_animations.append(round_text_appear)

    def render(self, screen):
        pygame.draw.rect(screen, (0,0,0,self.alpha),
                         (0, 0, 4000, 4000))
        pygame.draw.rect(screen, self.back_ground_color,
                         (self.x_pos+100, self.y_pos, 4000, 220))
        pygame.draw.rect(screen, self.color,
                         (self.x_pos, self.y_pos+35, 4200, 150))
        self.x_pos -=3
        self.alpha +=0.1
        if self.alpha > 255:
            self.alpha = 255

class combat_time(Animation):
    def __init__(self,data_dict,cardPool, start=0, duration=1, sub_animations=[], on_animation_end=[]):
        super().__init__(start, duration, sub_animations, on_animation_end)
        self.x_pos = 0
        self.y_pos = 0
        self.back_ground_color = (255,0,0)
        self.color = (255,235,10)

        #player data
        players = list(data_dict)
        self.player1_name = players[0].name
        self.player2_name = players[1].name

        self.player1_advantage = "ADV: -" +str(players[0].get_advantage())+"s"
        self.player2_advantage = "ADV: -" +str(players[1].get_advantage())+"s"
        
        #card data
        self.card1_img = cardPool.card_visuals[data_dict[players[0]][0]]["IMAGE"]
        self.card2_img = cardPool.card_visuals[data_dict[players[1]][0]]["IMAGE"]
        
        self.card1_title_text = str(data_dict[players[0]][0])
        self.card2_title_text = str(data_dict[players[1]][0])
        self.faster=None
        if data_dict["FASTER"] == players[0]:
            self.faster = 1
        if data_dict["FASTER"] == players[1]:
            self.faster = 2



    def setup(self):
        self.sub_animations=[]
        self.x_pos = 1280
        self.y_pos = 200
        p1_name_font_size = max(min(28,int(28*(14/len(self.player1_name)))),12)
        p2_name_font_size = max(min(28,int(28*(14/len(self.player2_name)))),12)
        p1_name_text_appear =text_appear(0.4,5.7,text=self.player1_name,x_pos=140,fontsize=p1_name_font_size)
        p1_name_text_appear.play()
        p2_name_text_appear =text_appear(0.9,5,text=self.player2_name,x_pos=1140,fontsize=p2_name_font_size)
        p2_name_text_appear.play()
        p1_adv_text_appear =text_appear(0.4,5.7,text=self.player1_advantage,x_pos=80,y_pos=400,fontsize=15)
        p1_adv_text_appear.play()
        p2_adv_text_appear =text_appear(0.9,5,text=self.player2_advantage,x_pos=1200,y_pos=400,fontsize=15)
        p2_adv_text_appear.play()
        vs_text_appear =text_appear(0.6,5.3,text="VS")
        vs_text_appear.play()
        card1_image_appear = image_appear(self.card1_img,duration=4.9,x_pos=450,y_pos=340,scale=1.7)
        card1_image_appear.play()
        card2_image_appear = image_appear(self.card2_img,duration=4.9,x_pos=830,y_pos=340,scale=1.7)
        card2_image_appear.play()
        p1_card_text_appear =text_appear(start=1,duration=4.9,text=self.card1_title_text,x_pos=450,y_pos=470,fontsize=24)
        p1_card_text_appear.play()
        p2_card_text_appear =text_appear(start=1,duration=4.9,text=self.card2_title_text,x_pos=830,y_pos=470,fontsize=24)
        p2_card_text_appear.play()
        
        self.sub_animations.append(vs_text_appear)
        self.sub_animations.append(p1_name_text_appear)
        self.sub_animations.append(p2_name_text_appear)
        self.sub_animations.append(p1_adv_text_appear)
        self.sub_animations.append(p2_adv_text_appear)
        self.sub_animations.append(card1_image_appear)
        self.sub_animations.append(card2_image_appear)
        self.sub_animations.append(p1_card_text_appear)
        self.sub_animations.append(p2_card_text_appear)
        if self.faster ==1:
            faster_text_appear =text_appear(1.2,4.7,text="FASTER >>",x_pos=300,y_pos=280,fontsize=20)
            faster_text_appear.play()
            self.sub_animations.append(faster_text_appear)
        if self.faster ==2:
            faster_text_appear =text_appear(1.2,4.7,text="<< FASTER",x_pos=980,y_pos=280,fontsize=20)
            faster_text_appear.play()
            self.sub_animations.append(faster_text_appear)
        


    def render(self, screen):
        pygame.draw.rect(screen, self.back_ground_color,
                         (self.x_pos+100, self.y_pos, 20600, 320))
        pygame.draw.rect(screen, self.color,
                         (self.x_pos, self.y_pos+30, 20800, 260))
        self.x_pos -=3
