class DataLoader:
    """class that loads and parses specific types of txt files
    """
    @staticmethod
    def load_data_from_file(file):
        """opens a file calls a function to parse its contents

        Returns: the parsed data of the file
        """
        with open(file,"r") as open_file:
            file_data = open_file.read()
            data = DataLoader.parse_data(file_data)
            return data

    @staticmethod
    def parse_data(data):
        """Parses certian fromated strings
        
        Returns: a dictionary based on the string
        """
        data_dict = {}
        body = data.split("##")[1].replace("\n", "")
        actions = body.split("_")
        for i in actions:
            action_data_dict = {}
            data_parts = i.split("|")
            for j in range(1, len(data_parts)):
                parts = data_parts[j].split(":")
                if len(parts) == 2:
                    action_data_dict[parts[0]] = parts[1]
                else:
                    action_data_dict[parts[0]] = None
            data_dict[data_parts[0]] = action_data_dict
        return data_dict
