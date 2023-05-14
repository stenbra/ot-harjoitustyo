class Scene:
    """ class, that makes scene handling easy by having scenes derive from this class
    
    Attributes:
        name: the name of the scene
        scenemanager: the scenemanager managing this scene
    """
    def __init__(self, name, scenemanager=None):
        self.name = name
        if scenemanager is not None:
            scenemanager.add_scene(self)
        self.scenemanager = scenemanager

    def update(self):
        """updates scene"""
        pass

    def get_scene_name(self):
        """Returns: scenen name"""
        return self.name
    def on_activate(self):
        """called when scene is set to the active scene"""
        pass
