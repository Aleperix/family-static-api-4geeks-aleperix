
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{
            "id": self._generateId(),
            "first_name": "John",
            "last_name": last_name,
            "age": 33,
            "lucky_numbers": [7, 13, 22]
            },
            {
            "id": self._generateId(),
            "first_name": "Jane",
            "last_name": last_name,
            "age": 35,
            "lucky_numbers": [10, 14, 3]
            },
            {
            "id": self._generateId(),
            "first_name": "Jimmy",
            "last_name": last_name,
            "age": 5,
            "lucky_numbers": [1]
            }]
            

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99)

    def add_member(self, member):
        # example list of members
        if not "id" in member:
            member["id"] = self._generateId()
        if (not "first_name" in member) or (not "last_name" in member) or (not "age" in member) or (not "lucky_numbers" in member):
            return False
        self._members.append({
            "id": member["id"],
            "first_name": member["first_name"],
            "last_name": self.last_name,
            "age": member["age"],
            "lucky_numbers": member["lucky_numbers"]
            })
        return True

    def delete_member(self, id):
        if len(self._members) == 1:
            return "last"
        id_exist = False
        for item in self._members:
            if item["id"] == id:
                self._members.remove(item)
                id_exist = True
        if id_exist == True:
            return True
        else:
            return False

    def update_member(self, id, member):
        id_exist = False
        for item in self._members:
            if item["id"] == id:
                if "first_name" in member:
                    item["first_name"] = member["first_name"]
                if "last_name" in member:
                    item["last_name"] = member["last_name"]
                if "age" in member:
                    item["age"] = member["age"]
                if "lucky_numbers" in member:
                    item["lucky_numbers"] = member["lucky_numbers"]
                id_exist = True
        if id_exist == True:
            return True
        else:
            return False

    def get_member(self, id):
        my_item = None
        id_exist = False
        for item in self._members:
            if item["id"] == id:
                id_exist = True
                my_item = item
        if id_exist == False:
            return False
        else:
            return my_item
            

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
