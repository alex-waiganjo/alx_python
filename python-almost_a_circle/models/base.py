#!/usr/bin/python3
"""
Base models
"""
import json
import os.path
import csv


class Base():
    """ class """
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save information into a file """
        list = []
        if list_objs is not None:
            list = [items.to_dictionary() for items in list_objs]
        with open("{}.json".format(cls.__name__), "w") as file:
            file.write(cls.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        """returns list of the JSON string """
        list = []
        if json_string is None or len(json_string) == 0:
            return list
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            holder = cls(1, 1)
        if cls.__name__ == "Square":
            holder = cls(1)
        holder.update(**dictionary)
        return holder

    @classmethod
    def load_from_file(cls):
        """file to instances"""
        if not os.path.exists(cls.__name__ + ".json"):
            return []
        with open(cls.__name__ + ".json", "r") as file:
            stuff = cls.from_json_string(file.read())
        return [cls.create(**index) for index in stuff]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Save information into a csv file """
        file_name = cls.__name__ + ".csv"
        with open(file_name, 'w', newline='') as file:
            if list_objs is None or list_objs == []:
                file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    headers = ["id", "width", "height", "x", "y"]
                else:
                    headers = ["id", "size", "x", "y"]
                new_csv = csv.DictWriter(file, fieldnames=headers)
                for object in list_objs:
                    new_csv.writerow(object.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ Load csv data """
        file_name = cls.__name__ + ".csv"
        try:
            with open(file_name, 'r', newline='') as file:
                if cls.__name__ == "Rectangle":
                    headers = ["id", "width", "height", "x", "y"]
                else:
                    headers = ["id", "size", "x", "y"]
                dict_list = csv.DictReader(file, fieldnames=headers)
                dict_list = [dict([key, int(value)] for key,
                                  value in f.items())
                             for f in dict_list]
                return [cls.create(**argument) for argument in dict_list]
        except IOError:
            return []