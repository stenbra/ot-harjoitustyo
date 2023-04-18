class Scene:
    def __init__(self, name, scenemanager=None):
        self.name = name
        if scenemanager is not None:
            scenemanager.add_scene(self)
        self.scenemanager = scenemanager

    def update(self):
        pass

    def get_scene_name(self):
        return self.name
