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
        self.frame_interval = duration /len(image_list)
        #self.duration = len(image_list) * frame_interval
        self.counter=0
        self.frame_interval= frame_interval
        self.clock=pygame.time.Clock()
        self.current_frame =0
        self.dt=0
        print("call")
    
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
            if self.position_override and self.current_frame <len(self.position_override):
                if self.scale_override and self.current_frame <len(self.scale_override):
                    self.render_image(screen,self.images[self.current_frame],self.position_override[self.current_frame][0],self.position_override[self.current_frame][1],scale=self.scale_override[self.current_frame])
                else:
                    self.render_image(screen,self.images[self.current_frame],self.position_override[self.current_frame][0],self.position_override[self.current_frame][1])
            elif self.scale_override and self.current_frame <len(self.scale_override):
                self.render_image(screen,self.images[self.current_frame],scale=self.scale_override[self.current_frame])
            else:
                self.render_image(screen,self.images[self.current_frame])
        self.dt = self.clock.tick(60) /1000
        return super().render(screen)
    
    
        

class combat_animation_matcher(Animation):
    def __init__(self,data_dict, start=0, duration=1.3, sub_animations=[], on_animation_end=[]):
        super().__init__(start, duration, sub_animations, on_animation_end)
        
        players = list(data_dict)
        action_1=str(data_dict[players[0]][0])
        action_2 =str(data_dict[players[1]][0])
        self.faster=None
        if data_dict["FASTER"] == players[0]:
            self.faster = 1
        if data_dict["FASTER"] == players[1]:
            self.faster = 2

        if action_1 == "DODGE":
            anim = self_dodge(action_2,duration=duration)
            self.sub_animations.append(anim)
            return
        elif self.faster==None and action_1 == "ATTACK" and action_2 == "ATTACK" or self.faster==None and action_1 == "GUARDBREAK" and action_2 == "GUARDBREAK":
            anim = attack_vs_attack(duration=duration)
            self.sub_animations.append(anim)
            return
        elif self.faster==2 and action_1 == "ATTACK" and action_2=="GUARD":
            anim = block_vs_attack(duration=duration)
            self.sub_animations.append(anim)
            return
        elif self.faster==1 and action_2 == "ATTACK" and action_1=="GUARD":
            anim = attack_vs_block(duration=duration)
            self.sub_animations.append(anim)
            return
        
        if action_2 =="ATTACK":
            if self.faster==1 and action_1  =="ATTACK" or self.faster==1 and action_1  =="POKE"or self.faster==1 and action_1  =="GUARDBREAK":
                anim = enemy_attack_guarded(duration=duration)
                self.sub_animations.append(anim)
            else:
                anim = enemy_attack(duration=duration)
                self.sub_animations.append(anim)
        if action_2 =="GUARD":
            anim = enemy_guard(duration=duration)
            self.sub_animations.append(anim)
        if action_2 =="GUARDBREAK":
            if self.faster==1 and action_1  =="ATTACK" or self.faster==1 and action_1  =="POKE"or self.faster==1 and action_1  =="GUARDBREAK":
                anim = enemy_attack_guarded(duration=duration)
                self.sub_animations.append(anim)
            else:
                anim = enemy_guardbreak(duration=duration)
                self.sub_animations.append(anim)
        if action_2 =="POKE":
            anim = enemy_poke(duration=duration)
            self.sub_animations.append(anim)
        if action_2 =="DODGE":
            anim = enemy_dodge(duration=duration)
            self.sub_animations.append(anim)

        if action_1 =="ATTACK":
            if self.faster==2 and action_2  =="ATTACK" or self.faster==2 and action_2  =="POKE"or self.faster==2 and action_2  =="GUARDBREAK":
                anim = self_attack_guarded(duration=duration)
                self.sub_animations.append(anim)
            else:
                anim = self_attack(duration=duration)
                self.sub_animations.append(anim)
        if action_1 =="GUARD":
            anim = self_guard(duration=duration)
            self.sub_animations.append(anim)
        if action_1 =="GUARDBREAK":
            if self.faster==2 and action_2  =="ATTACK" or self.faster==2 and action_2  =="POKE"or self.faster==2 and action_2  =="GUARDBREAK":
                anim = self_attack_guarded(duration=duration)
                self.sub_animations.append(anim)
            else:
                anim = self_guardbreak(duration=duration)
                self.sub_animations.append(anim)
        if action_1 =="POKE":
            anim = self_poke(duration=duration)
            self.sub_animations.append(anim)
        


class attack_vs_block(Animation):
    def __init__(self, start=0, duration=3, sub_animations=[], on_animation_end=[]):
        super().__init__(start, duration, sub_animations, on_animation_end)
        scale=[4] * len(anim_resource.enemy_attack_guarded)
        scale_self=[6] * len(anim_resource.self_guard)
        enemy_guard = character_animation(anim_resource.enemy_attack_guarded,scale_list=scale,duration=duration)
        self_guard = character_animation(anim_resource.self_guard,scale_list=scale_self,duration=duration)
        self.sub_animations.append(enemy_guard)
        self.sub_animations.append(self_guard)

class attack_vs_attack(Animation):
    def __init__(self, start=0, duration=3, sub_animations=[], on_animation_end=[]):
        super().__init__(start, duration, sub_animations, on_animation_end)
        scale=[4] * len(anim_resource.enemy_attack_guarded)
        scale_self=[6] * len(anim_resource.self_attack_guarded)
        enemy_guard = character_animation(anim_resource.enemy_attack_guarded,scale_list=scale,duration=duration)
        self_guard = character_animation(anim_resource.self_attack_guarded,scale_list=scale_self,duration=duration)
        self.sub_animations.append(enemy_guard)
        self.sub_animations.append(self_guard)


class block_vs_attack(Animation):
    def __init__(self, start=0, duration=3, sub_animations=[], on_animation_end=[]):
        super().__init__(start, duration, sub_animations, on_animation_end)
        scale=[4] * len(anim_resource.enemy_guard)
        scale_self=[6] * len(anim_resource.self_attack_guarded)
        enemy_guard = character_animation(anim_resource.enemy_guard,scale_list=scale,duration=duration)
        self_guard = character_animation(anim_resource.self_attack_guarded,scale_list=scale_self,duration=duration)
        self.sub_animations.append(enemy_guard)
        self.sub_animations.append(self_guard)

class double_guard(Animation):
    def __init__(self, start=0, duration=3, sub_animations=[], on_animation_end=[]):
        super().__init__(start, duration, sub_animations, on_animation_end)
        scale=[4] * len(anim_resource.enemy_guard)
        scale_self=[6] * len(anim_resource.self_guard)
        enemy_guard = character_animation(anim_resource.enemy_guard,scale_list=scale,duration=duration)
        self_guard = character_animation(anim_resource.self_guard,scale_list=scale_self,duration=duration)
        self.sub_animations.append(enemy_guard)
        self.sub_animations.append(self_guard)

class self_dodge(Animation):
    def __init__(self,action, start=0, duration=3, sub_animations=[], on_animation_end=[]):
        super().__init__(start, duration, sub_animations, on_animation_end)
        if action =="ATTACK":
            anim = enemy_attack(move_offset=anim_resource.self_dodge_pos_offset,duration=duration)
            self.sub_animations.append(anim)
        if action =="GUARD":
            anim = enemy_guard(move_offset=anim_resource.self_dodge_pos_offset,duration=duration)
            self.sub_animations.append(anim)
        if action =="GUARDBREAK":
            anim = enemy_guardbreak(move_offset=anim_resource.self_dodge_pos_offset,duration=duration)
            self.sub_animations.append(anim)
        if action =="POKE":
            anim = enemy_poke(move_offset=anim_resource.self_dodge_pos_offset,duration=duration)
            self.sub_animations.append(anim)
        if action =="DODGE":
            anim = enemy_dodge(move_offset=anim_resource.self_dodge_pos_offset,duration=duration)
            self.sub_animations.append(anim)

class enemy_guard(Animation):
    def __init__(self, start=0, duration=3, sub_animations=[], on_animation_end=[],move_offset=[]):
        super().__init__(start, duration, sub_animations, on_animation_end)
        scale=[4] * len(anim_resource.enemy_guard)
        pos=[]
        for i in range(len(anim_resource.enemy_guard)):
            if i<len(move_offset):
                pos.append([640+move_offset[i][0],360+move_offset[i][0]])
        enemy_guard = character_animation(anim_resource.enemy_guard,position_list=pos,scale_list=scale,duration=duration)
        self.sub_animations.append(enemy_guard)

class self_guard(Animation):
    def __init__(self, start=0, duration=3, sub_animations=[], on_animation_end=[]):
        super().__init__(start, duration, sub_animations, on_animation_end)
        scale_self=[6] * len(anim_resource.self_guard)
        self_guard = character_animation(anim_resource.self_guard,scale_list=scale_self,duration=duration)
        self.sub_animations.append(self_guard)


class enemy_attack(Animation):
    def __init__(self, start=0, duration=3, sub_animations=[], on_animation_end=[],move_offset=[]):
        super().__init__(start, duration, sub_animations, on_animation_end)
        scale=[4] * len(anim_resource.enemy_attack)
        pos=[]
        for i in range(len(anim_resource.enemy_attack)):
            if i<len(move_offset):
                pos.append([640+move_offset[i][0],360+move_offset[i][1]])
            else:
                pos.append([640,360])
        enemy_guard = character_animation(anim_resource.enemy_attack,position_list=pos,scale_list=scale,duration=duration)
        self.sub_animations.append(enemy_guard)

class enemy_attack_guarded(Animation):
    def __init__(self, start=0, duration=3, sub_animations=[], on_animation_end=[],move_offset=[]):
        super().__init__(start, duration, sub_animations, on_animation_end)
        scale=[4] * len(anim_resource.enemy_attack_guarded)
        pos=[]
        for i in range(len(anim_resource.enemy_attack_guarded)):
            if i<len(move_offset):
                pos.append([640+move_offset[i][0],360+move_offset[i][1]])
            else:
                pos.append([640,360])
        enemy_guard = character_animation(anim_resource.enemy_attack_guarded,position_list=pos,scale_list=scale,duration=duration)
        self.sub_animations.append(enemy_guard)

class self_attack(Animation):
    def __init__(self, start=0, duration=3, sub_animations=[], on_animation_end=[]):
        super().__init__(start, duration, sub_animations, on_animation_end)
        scale_self=[6] * len(anim_resource.self_attack)
        self_guard = character_animation(anim_resource.self_attack,scale_list=scale_self,duration=duration)
        self.sub_animations.append(self_guard)
        
class self_attack_guarded(Animation):
    def __init__(self, start=0, duration=3, sub_animations=[], on_animation_end=[]):
        super().__init__(start, duration, sub_animations, on_animation_end)
        scale_self=[6] * len(anim_resource.self_attack_guarded)
        self_guard = character_animation(anim_resource.self_attack_guarded,scale_list=scale_self,duration=duration)
        self.sub_animations.append(self_guard)
        
class enemy_guardbreak(Animation):
    def __init__(self, start=0, duration=3, sub_animations=[], on_animation_end=[],move_offset=[]):
        super().__init__(start, duration, sub_animations, on_animation_end)
        scale=[4] * len(anim_resource.enemy_guardbreak)
        pos=[]
        for i in range(len(anim_resource.enemy_guardbreak)):
            if i<len(move_offset):
                pos.append([640+move_offset[i][0],360+move_offset[i][1]])
            else:
                pos.append([640,360])
        print(pos)
        enemy_guard = character_animation(anim_resource.enemy_guardbreak,position_list=pos,scale_list=scale,duration=duration)
        self.sub_animations.append(enemy_guard)

class self_guardbreak(Animation):
    def __init__(self, start=0, duration=3, sub_animations=[], on_animation_end=[]):
        super().__init__(start, duration, sub_animations, on_animation_end)
        scale_self=[6] * len(anim_resource.self_guardbreak)
        self_guard = character_animation(anim_resource.self_guardbreak,scale_list=scale_self,duration=duration)
        self.sub_animations.append(self_guard)

class enemy_poke(Animation):
    def __init__(self, start=0, duration=3, sub_animations=[], on_animation_end=[],move_offset=[]):
        super().__init__(start, duration, sub_animations, on_animation_end)
        scale=[4] * len(anim_resource.enemy_poke)
        enemy_guard = character_animation(anim_resource.enemy_poke,scale_list=scale,duration=duration)
        self.sub_animations.append(enemy_guard)

class self_poke(Animation):
    def __init__(self, start=0, duration=3, sub_animations=[], on_animation_end=[]):
        super().__init__(start, duration, sub_animations, on_animation_end)
        scale_self=[6] * len(anim_resource.self_poke)
        
        self_guard = character_animation(anim_resource.self_poke,scale_list=scale_self,duration=duration)
        self.sub_animations.append(self_guard)

class enemy_dodge(Animation):
    def __init__(self, start=0, duration=3, sub_animations=[], on_animation_end=[],move_offset=[]):
        super().__init__(start, duration, sub_animations, on_animation_end)
        scale=[4] * len(anim_resource.enemy_dodge)
        pos=[]
        for i in range(len(anim_resource.enemy_dodge)):
            if i<len(move_offset):
                pos.append([640+anim_resource.enemy_dodge_pos_offset[i][0]+move_offset[i][0],360+anim_resource.enemy_dodge_pos_offset[i][1]+move_offset[i][1]])
            elif i < len(anim_resource.enemy_dodge_pos_offset):
                pos.append([640+anim_resource.enemy_dodge_pos_offset[i][0],360+anim_resource.enemy_dodge_pos_offset[i][1]])
            else:
                pos.append([640,360])
        enemy_guard = character_animation(anim_resource.enemy_dodge,position_list=pos,scale_list=scale,duration=duration)
        self.sub_animations.append(enemy_guard)

class enemy_die(Animation):
    def __init__(self, start=0, duration=3, sub_animations=[], on_animation_end=[]):
        super().__init__(start, duration, sub_animations, on_animation_end)
        scale=[4] * len(anim_resource.enemy_die)
        enemy_guard = character_animation(anim_resource.enemy_die,scale_list=scale,duration=duration)
        self.sub_animations.append(enemy_guard)
