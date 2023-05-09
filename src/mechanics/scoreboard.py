import os.path as path
import json

class Scoreboard:
         
    def __init__(self, path="src/gamedata/"):
        self.path = path
        self.scoreboard ={}
        self.load_scoreboard()

    def update_scoreboard(self,name,score):
        scoreboard_entries =[]
        new_entry = {}
        new_entry["name"]=name
        new_entry["score"]=score
        scoreboard_entries.append(new_entry)
        for i in self.scoreboard:
            print(self.scoreboard[i])
            scoreboard_entries.append(self.scoreboard[i])
        sorted_scoreboard=sorted(scoreboard_entries,key=lambda x: x["score"],reverse=True)
        self.scoreboard = {}
        for i in range(len(sorted_scoreboard)):
             self.scoreboard[i+1] = sorted_scoreboard[i]
        self.save_scoreboard(self.scoreboard)
             
              

    def load_scoreboard(self):
        print("loading")
        if path.isfile(self.path+"scoreboard.json"):
            with open(self.path+"scoreboard.json","r") as open_file:
                self.scoreboard = json.load(open_file)
                print(self.scoreboard)

    def save_scoreboard(self,score_data):
        with open(self.path+"scoreboard.json","w") as open_file:
                json.dump(score_data,open_file)

the_scoreboard = Scoreboard()
