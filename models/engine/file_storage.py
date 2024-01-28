#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from os.path import isfile
from json import dump, load
import sys


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            dt = {k: v for k, v in self.__objects.items() if cls == type(v)}
            return dt
        else:
            return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects.update({key: obj})

    def save(self):
        """Saves storage dictionary to file"""
        j_dict = {}
        for key, val in FileStorage.__objects.items():
            j_dict.update({key: val.to_dict()})
        with open(FileStorage.__file_path, mode='w', encoding='UTF-8') as f:
            dump(j_dict, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models import place, city, state, review
        from models import base_model, user, amenity
        cls = {'BaseModel': base_model, 'User': user, 'Amenity': amenity,
               'Place': place, 'City': city, 'State': state, 'Review': review}
        if isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, encoding='UTF-8') as file:
                from_json = load(file)
                for val in from_json.values():
                    cls_name = val["__class__"]
                    cls_obj = getattr(cls[cls_name], cls_name)
                    self.new(cls_obj(**val))

    def delete(self, obj=None):
        """ Deletes obj from __objects if it's inside """
        if obj:
            key = f"{type(obj).__name__}.{obj.id}"
            if self.__objects[key]:
                del self.__objects[key]
                self.save()

    def close(self):
        """ Calls reload() method for deserializing JSON file to objects """
        self.reload()
