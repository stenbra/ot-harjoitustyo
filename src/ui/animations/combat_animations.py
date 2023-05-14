from ui.animations.character_anim_rescource import anim_resource
from mechanics.animations import Animation
from ui.animations.combat_comparison import image_appear
import pygame


class character_animation(Animation):
    def __init__(self,image_list, start=0, duration=1.3, sub_animations=[], on_animation_end=[],scale_list=[],position_list=[],frame_interval=0.05):
        super().__init__(start, duration, sub_animations, on_animation_end)
        self.scale_override=scale_list
        self.position_override = position_list
        self.images = image_list
        self.frame_interval = frame_interval
        self.duration = len(image_list) * frame_interval
        self.counter=0
        self.frame_interval= frame_interval
        self.clock=pygame.time.Clock()
        self.current_frame =0
        self.dt=0
    
    def render_image(self,screen,img,x=640,y=360,scale=1):
        imgWidth = img.get_width()
        imgHeight = img.get_height()
        image = pygame.transform.scale(
        img, (int(imgWidth)*scale, int(imgHeight)*scale))
        rect = image.get_rect()
        rect.center =(x,y)
        screen.blit(image, (rect.x, rect.y))
    
    def render(self, screen):
        self.counter += self.dt
        if self.counter >= self.frame_interval:
            self.current_frame += 1
            self.counter =0
        if self.current_frame <len(self.images):
            if self.position_override:
                if self.scale_override:
                    self.render_image(screen,self.images[self.current_frame],self.position_override[self.current_frame][0],self.position_override[self.current_frame][1],self.scale_override[self.current_frame],scale=self.scale_override[self.current_frame])   
                self.render_image(screen,self.images[self.current_frame],self.position_override[self.current_frame][0],self.position_override[self.current_frame][1])
            elif self.scale_override:
                self.render_image(screen,self.images[self.current_frame],scale=self.scale_override[self.current_frame])
            else:
                self.render_image(screen,self.images[self.current_frame])
        self.dt = self.clock.tick(60) /1000
        return super().render(screen)
    
    
        

class combat_animation_matcher(Animation):
    def __init__(self,data_dict, start=0, duration=1.3, sub_animations=[], on_animation_end=[]):
        super().__init__(start, duration, sub_animations, on_animation_end)
        d_guard = double_guard()
        self.sub_animations.append(d_guard)
        print("call")
        



class double_guard(Animation):
    def __init__(self, start=0, duration=5, sub_animations=[], on_animation_end=[]):
        super().__init__(start, duration, sub_animations, on_animation_end)
        scale=[4] * len(anim_resource.enemy_guard)
        scale_self=[7] * len(anim_resource.enemy_guard)
        enemy_guard = character_animation(anim_resource.enemy_guard,scale_list=scale)
        enemy_guard.play()
        self_guard = character_animation(anim_resource.self_guard,scale_list=scale_self)
        self.sub_animations.append(enemy_guard)
        self.sub_animations.append(self_guard)

        


