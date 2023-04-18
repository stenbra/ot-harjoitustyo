from ui.scene import Scene


class Scenemanager:
    def __init__(self, scene_list, screen):
        self.scenes = {}
        for i in scene_list:
            self.scenes[i.get_scene_name()] = i
            i.scenemanager = self
        self.active_scene = None
        self.screen = screen

    def update(self):
        self.active_scene.update()

    def add_scene(self, scene: Scene):
        if scene.get_scene_name() in self.scenes:
            return
        self.scenes[scene.get_scene_name()] = scene
        scene.scenemanager = self

    def set_active_scene(self, scene_name):
        if scene_name in self.scenes:
            self.active_scene = self.scenes[scene_name]
