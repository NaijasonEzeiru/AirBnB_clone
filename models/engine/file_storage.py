#!/usr/bin/python3
''' module for FileStorage class '''
import json
import datetime
import os


class FileStorage:
    ''' class for persistent storage '''
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        ''' initializes a storage engine '''
        pass

    def all(self):
        ''' gets all objects '''
        return FilesStorage.__objects

    def new(self, obj):
        ''' registers a new object '''
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        ''' saves all objects to a file '''
        with open(FileStorage.__file_path, 'w') as file:
            r_objs = FileStorage.__objects
            objs = {}
            for k in r_objs:
                v = r_objs[k]
                objs[k] = v.to_dict()
            json.dump(objs, file)

    def reload(self):
        """reload method deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                json_dict = json.load(f)
                for obj_dict in json_dict.values():
                    cls = obj_dict['__class__']
                    self.new(eval('{}({})'.format(cls, '**obj_dict')))
        except FileNotFoundError:
            return
<<<<<<< HEAD
=======
            
>>>>>>> 3bfd6872242ceade76d13dcaea96e1bc03b825cf
