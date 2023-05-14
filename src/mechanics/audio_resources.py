import pygame
import random
class Audio_resource:
    """singleton which contains all audiofiles for easy access across the project

    Attrubutes:
        announcers: list of dictionaries containing all voicelines for announcers
        active_anouncer_index: The index of which anouncer that is currently in use in the announcers list
        url: relative path to the audiofiles
        button_sound: the universal buttonsound that is used through out the project
        clinks: weapon clink -sound list
    """
    def __init__(self) -> None:
        self.active_anouncer_index = 0
    def Initialize(self,url="src/gamedata/audio/"):
        """loads all the sounds and puts them in a easy to find structure, also initializes the menu music
        """
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
        """randomly configuers the active_anouncer_index to be one of the announcers in the anouncers lis
        """
        self.active_anouncer_index = random.randint(0,len(self.anouncers)-1)

    def play_anouncer_sound(self,sound):
       """plays a random sound from list in the dictionary<string,List[]> that is at the current index of the anouncers list
       """
       if pygame.mixer.Channel(0).get_busy() == True:
           return
       soundlist= self.anouncers[self.active_anouncer_index][sound]
       soundlist[(random.randint(0,len(soundlist)-1))].play()

    def play_clink(self):
        """plays a random sound from the clinks list
        """
        self.clinks[(random.randint(0,len(self.clinks)-1))].play()



audio_resource= Audio_resource()        