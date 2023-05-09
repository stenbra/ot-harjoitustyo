import pygame
import time

class AnimationHandler:
    def __init__(self,screen):
        self.screen = screen
        self.animation_queue=[]
        self.playing_animation = None
        self.clicked = False
        self.started_this_frame = False

    def play_next_from_queue(self):
        if self.playing_animation is not None:
            self.playing_animation.stop()
            self.playing_animation = None
        if len(self.animation_queue) == 0:
            return
        next_animation = self.animation_queue.pop(0)
        if not next_animation:
            return
        self.playing_animation = next_animation
        self.playing_animation.play()
        self.started_this_frame = True
        self.clicked = True

    def force_animation(self, animation):
        self.stop_and_empty_queue()
        if not animation:
            return
        self.add_to_animation_queue(animation)
    
    def stop_and_empty_queue(self):
        self.animation_queue = []
        if self.playing_animation is not None:
            self.playing_animation.stop()
        self.playing_animation = None

    def update(self):
        if not self.is_running():
            if len(self.animation_queue)==0:
                return
            self.play_next_from_queue()
        over = self.playing_animation.update(self.screen)
        
        if self.started_this_frame:
            self.started_this_frame = False
            return
        if over or pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.play_next_from_queue()
                self.clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

    def is_running(self):
        if self.playing_animation is None:
            return False
        return True
    
    def is_not_running_and_empty_queue(self):
        if self.playing_animation is None and len(self.animation_queue)==0:
            return True
        return False
    
    def add_to_animation_queue(self,animation):
        self.animation_queue.append(animation)

class Animation:
    def __init__(self,start=0,duration=1,sub_animations=[],on_animation_end=[]):
        self.sub_animations = sub_animations
        self.start= start
        self.duration = duration
        self.start_time = 0
        self.stop_time=0
        self.on_animation_end = on_animation_end
        self.end_call = False

    def setup(self):
        pass

    def play(self):
        self.start_time = time.time() + self.start
        self.stop_time = self.start_time + self.duration
        self.end_call = False
        for i in self.sub_animations:
            i.play()
        self.setup()

    def stop(self):
        self.timer = self.duration +1
        if len(list(self.on_animation_end))==0:
            return
        for i in self.sub_animations:
            over = i.stop()
        if not self.end_call:
            self.end_call = True
            for function in self.on_animation_end:
                function.call()

    def render(self,screen):
        pass

    def update(self,screen):
        timer= time.time()
        if timer< self.start_time:
            return False
        if timer >= self.stop_time:
            return True
        self.render(screen)
        for i in self.sub_animations:
            over = i.update(screen)
            if over:
                i.stop()
        return False