import json


class Config:
    shared_state = {}

    def __init__(self, config_file='./config.json'):
        if (len(self.shared_state) == 0):
            with open(config_file) as cfg_file:
                self.shared_state["config"] = json.load(cfg_file)
        self.__dict__ = self.shared_state
        print(self.__dict__)

    def get_config(self, key):
        return self.config[key]
