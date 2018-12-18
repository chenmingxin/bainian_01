import os
import yaml


class ReadYaml():
    def __init__(self,filename):
        self.filename = os.getcwd()+os.sep+"data"+os.sep+filename

    def read_yaml(self):
        with open(self.filename,"r",encoding="utf-8") as f:
            return yaml.load(f)


