import pygame
import random
class Audio_resource:
    def __init__(self) -> None:
        self.active_anouncer_index = 0
    def Initialize(self,url="src/gamedata/audio/"):
        self.url = url
        self.anouncers = []
        announcer_death=[]
        announcer_death.append(pygame.mixer.Sound(self.url+"announcer_edgy/death_1.wav"))
        announcer_death.append(pygame.mixer.Sound(self.url+"announcer_edgy/death_2.wav"))
        announcer_death.append(pygame.mixer.Sound(self.url+"announcer_edgy/death_3.wav"))
        announcer_death.append(pygame.mixer.Sound(self.url+"announcer_edgy/death_4.wav"))

        announcer_2_death=[]
        announcer_2_death.append(pygame.mixer.Sound(self.url+"announcer_old/death_1.wav"))
        announcer_2_death.append(pygame.mixer.Sound(self.url+"announcer_old/death_2.wav"))
        announcer_2_death.append(pygame.mixer.Sound(self.url+"announcer_old/death_3.wav"))

        announcer_name=[]
        announcer_name.append(pygame.mixer.Sound(self.url+"announcer_edgy/name_1.wav"))
        announcer_name.append(pygame.mixer.Sound(self.url+"announcer_edgy/name_2.wav"))
        announcer_name.append(pygame.mixer.Sound(self.url+"announcer_edgy/name_3.wav"))

        announcer_2_name=[]
        announcer_2_name.append(pygame.mixer.Sound(self.url+"announcer_old/name_1.wav"))
        announcer_2_name.append(pygame.mixer.Sound(self.url+"announcer_old/name_2.wav"))
        announcer_2_name.append(pygame.mixer.Sound(self.url+"announcer_old/name_3.wav"))

        announcer_new=[]
        announcer_new.append(pygame.mixer.Sound(self.url+"announcer_edgy/new_1.wav")
                             )
        announcer_2_new=[]
        announcer_2_new.append(pygame.mixer.Sound(self.url+"announcer_old/new_1.wav"))

        announcer_round=[]
        announcer_round.append(pygame.mixer.Sound(self.url+"announcer_edgy/round_1.wav"))
        announcer_round.append(pygame.mixer.Sound(self.url+"announcer_edgy/round_2.wav"))
        announcer_round.append(pygame.mixer.Sound(self.url+"announcer_edgy/round_3.wav"))

        announcer_2_round=[]
        announcer_2_round.append(pygame.mixer.Sound(self.url+"announcer_old/round_1.wav"))
        announcer_2_round.append(pygame.mixer.Sound(self.url+"announcer_old/round_2.wav"))
        announcer_2_round.append(pygame.mixer.Sound(self.url+"announcer_old/round_3.wav"))

        announcer_dict ={}
        announcer_dict["DEATH"] = announcer_death
        announcer_dict["NAME"] = announcer_name
        announcer_dict["NEW"] = announcer_new
        announcer_dict["ROUND"] = announcer_round

        announcer_2_dict ={}
        announcer_2_dict["DEATH"] =announcer_2_death
        announcer_2_dict["NAME"] = announcer_2_name
        announcer_2_dict["NEW"] = announcer_2_new
        announcer_2_dict["ROUND"] = announcer_2_round 

        self.anouncers.append(announcer_dict)
        self.anouncers.append(announcer_2_dict)

        self.clinks =[]
        self.clinks.append(pygame.mixer.Sound(self.url+"clink/clink_1.wav"))
        self.clinks.append(pygame.mixer.Sound(self.url+"clink/clink_2.wav"))
        self.clinks.append(pygame.mixer.Sound(self.url+"clink/clink_3.wav"))
        self.clinks.append(pygame.mixer.Sound(self.url+"clink/clink_4.wav"))
        self.clinks.append(pygame.mixer.Sound(self.url+"clink/clink_5.wav"))
        self.button_sound = pygame.mixer.Sound(self.url+"menu_button/click.wav")

        pygame.mixer.music.load(self.url+"music/cave.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.pause()

    def set_random_anouncer(self):
        self.active_anouncer_index = random.randint(0,len(self.anouncers)-1)

    def play_anouncer_sound(self,sound):
       if pygame.mixer.Channel(0).get_busy() == True:
           return
       soundlist= self.anouncers[self.active_anouncer_index][sound]
       soundlist[(random.randint(0,len(soundlist)-1))].play()

    def play_clink(self):
        self.clinks[(random.randint(0,len(self.clinks)-1))].play()



audio_resource= Audio_resource()        