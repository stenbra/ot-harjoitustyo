import os.path as path
import json

class Scoreboard:
    """This class, is a singleton that handles the scoreboard date
        It saves,loads and updates the scoreboard.

    Attributes:
        path: path to where the scoreboard file should be or should be created
        scoreboard: dictionary that contains all scoreboard entries by order
    """
         
    def __init__(self, path="src/gamedata/"):
        self.path = path
        self.scoreboard ={}
        self.load_scoreboard()
        self.update_scoreboard()

    def update_scoreboard(self,name = None,score= None):
        """This function updates the scoreboard and saves it if not both name and score is given
            then it will just order the scoreboard and save it
        Args:
            name: name of the new entry to add
            score: score of the new entry to add
        """
        scoreboard_entries =[]
        if name is not None and score is not None:
            new_entry = {}
            new_entry["name"]=name
            new_entry["score"]=score
            scoreboard_entries.append(new_entry)
        for i in self.scoreboard:
            scoreboard_entries.append(self.scoreboard[i])
        sorted_scoreboard=sorted(scoreboard_entries,key=lambda x: x["score"],reverse=True)
        self.scoreboard = {}
        for i in range(len(sorted_scoreboard)):
             self.scoreboard[i+1] = sorted_scoreboard[i]
        self.save_scoreboard(self.scoreboard)
             
    def load_scoreboard(self):
        """loads the scoreboard data form a file if it exists
        """
        if path.isfile(self.path+"scoreboard.json"):
            with open(self.path+"scoreboard.json","r") as open_file:
                self.scoreboard = json.load(open_file)

    def save_scoreboard(self,score_data):
        """saves the scoreboard data to a file

        Args:
            score_data: the scoreboard data to be saved
        """
        with open(self.path+"scoreboard.json","w") as open_file:
                json.dump(score_data,open_file)

the_scoreboard = Scoreboard()
