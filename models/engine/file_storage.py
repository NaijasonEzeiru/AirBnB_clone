#!/usr/bin/python3
""" Module to serialize and deserialize python objects to/from json """


import json


class FileStorage():
    """ classs to serialize and deserialize python objects """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return the dictionary of all objects """
        self.reload()
        return FileStorage.__objects

    def new(self, object):
        """ sets in __objects the obj with key <obj class name>.id """
        self.reload()
        string = object.__class__.__name__ + "." + object.id
        FileStorage.__objects[string] = object.to_dict()

    def save(self):
        """ save __objects dict to json file """
        with open(FileStorage.__file_path, mode="w", encoding='utf-8') as file:
            json.dump(FileStorage.__objects, file)
        FileStorage.__objects = {}

    def reload(self):
        """ loads a json object from a file """
        try:
            with open(FileStorage.__file_path, mode="r",
                      encoding="utf-8") as file:
                FileStorage.__objects = json.load(file)
        except IOError:
            pass
