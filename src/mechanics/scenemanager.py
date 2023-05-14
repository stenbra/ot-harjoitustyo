from mechanics.scene import Scene


class Scenemanager:
    """class, that manages wich scene to render and update
    
    Attributes:
        scene: a dictionary of all scenes to manage
        active_scene: the currently active scene
        screen: the screen/surface to draw/render on
        events: pygame input events (since the game lags if you check for them multiple times scenes use them from here)
    """
    def __init__(self, scene_list, screen):
        self.scenes = {}
        for i in scene_list:
            self.scenes[i.get_scene_name()] = i
            i.scenemanager = self
        self.active_scene = None
        self.screen = screen
        self.events =[]

    def update(self,events=[]):
        """updates the active scene and the events list"""
        self.events = events
        self.active_scene.update()

    def add_scene(self, scene):
        """adds a new scene to the manager

        Args:
            scene: the scene to be added
        """
        if scene.get_scene_name() in self.scenes:
            return
        self.scenes[scene.get_scene_name()] = scene
        scene.scenemanager = self

    def get_scene_by_name(self,name):
        """Gets scene from scenes dictionary using its name
        Args:
            name: the name of the scene to get
        Returns: a scene present in the scenes dictionary based on name
        """
        if name in self.scenes:
            return self.scenes[name]

    def set_active_scene(self, scene_name):
        """Sets the active scene to the scene with the same name
        
        Args:
            scene_name: the name of the scene to set as the active scene 
        """
        if scene_name in self.scenes:
            self.active_scene = self.scenes[scene_name]
            self.active_scene.on_activate()
