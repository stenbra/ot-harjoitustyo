import pygame
import time

class AnimationHandler:
    """Class, which controlls a queue of animations

    Attributes:
        screen: The screen/surface to render animations on
        animation_queue: A list of animations to play
        playing_animation: The animation currently being played, None if there is no animation
        clicked: controlls The mouse click so it only triggers once per button down press
        started_this_fram: A check for if the animation was started this frame (used to not skip the animation on the startframe by accident)
    """
    def __init__(self,screen):
        self.screen = screen
        self.animation_queue=[]
        self.playing_animation = None
        self.clicked = False
        self.started_this_frame = False

    def play_next_from_queue(self):
        """Stops the current playing animation if there is one.
            Tries to play the next animation from animation_queue it there is one
        """
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
        """Stops any current playing animations, clears the animation queue, puts the given animation into the queue.

        Args:
            animation: The animation to be put into the queue
        """
        self.stop_and_empty_queue()
        if not animation:
            return
        self.add_to_animation_queue(animation)
    
    def stop_and_empty_queue(self):
        """Stops any current playing animations, clears the animation queue
        """
        self.animation_queue = []
        if self.playing_animation is not None:
            self.playing_animation.stop()
        self.playing_animation = None

    def update(self):
        """Is called to update any animations playing, checks if the animation has ended or if nothing is playing,
            In that case it will try to play the next animation from queue if there is one.

            Handles click events to see if animation should be skipped
        """
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
        """ Checks if there currently is a playing animation.
            Returns: True if there is, returns False if there is not one
        """
        if self.playing_animation is None:
            return False
        return True
    
    def is_not_running_and_empty_queue(self):
        """ Checks if there currently is no playing animation and also if the animation queue is empty
            Returns: True if that is the case, returns False otherwise
        """
        if self.playing_animation is None and len(self.animation_queue)==0:
            return True
        return False
    
    def add_to_animation_queue(self,animation):
        """ Adds animation to animation_queue

        Args:
            animation: the anmimation to be added
        """
        self.animation_queue.append(animation)

class Animation:
    """Class, from which all animations derive, has preset methods that can be overriden,
    this class holds the functionality of animations, so the AnimationHandler can easily controll animations

    Attributes:
        sub_animations: List of children animations that can will also be played/updated/stopped when the main one is played/updated/stopped
        start: controllable delay of when the animation should start updating
        duration: The duration of the animation
        start_time: the system time when the animations should start updating
        stop_time: the system time when the animations should stop updating
        on_animation_end: list of funtions to call when the animation is over
        end_call: checks if the animation already has called the on_animation_end functions
    """
    def __init__(self,start=0,duration=1,sub_animations=[],on_animation_end=[]):
        self.sub_animations = sub_animations
        self.start= start
        self.duration = duration
        self.start_time = 0
        self.stop_time=0
        self.on_animation_end = on_animation_end
        self.end_call = False

    def setup(self):
        """overriden if there is a special setup for the animation before it is played and after it is initialized
        """
        pass

    def play(self):
        """Sets the start and stop time for the animation does this recursively for its sub_animations
        """
        self.start_time = time.time() + self.start
        self.stop_time = self.start_time + self.duration
        self.end_call = False
        for i in self.sub_animations:
            i.play()
        self.setup()

    def stop(self):
        """stops the animation and all its sub animation
            calls all the funtions in on_animation_end
            removes it self when done
        """
        self.timer = self.duration +1
        if len(list(self.on_animation_end))==0:
            return
        for i in self.sub_animations:
            over = i.stop()
        if not self.end_call:
            self.end_call = True
            for function in self.on_animation_end:
                function.call()
        self.sub_animations ={}
        del self

    def render(self,screen):
        """overriden to enter the things to render in the animaton"""
        pass

    def update(self,screen):
        """updates the amation time, checks if it should start/stop also calls render on every update"""
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