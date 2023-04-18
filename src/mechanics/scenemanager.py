from ui.scene import Scene
class Scenemanager:
    def __init__(self,sceneList,screen):
        self.scenes ={}
        for i in sceneList:
            self.scenes[i.get_scene_name()] = i
            i.scenemanager = self
        self.activeScene = None
        self.screen = screen

    def update(self):
        self.activeScene.update()

    def add_scene(self,scene:Scene):
        if scene.get_scene_name() in self.scenes:
            return
        self.scenes[scene.get_scene_name()]= scene
        scene.scenemanager = self

    def set_active_scene(self,sceneName):
        if sceneName in self.scenes:
            self.activeScene = self.scenes[sceneName]
        