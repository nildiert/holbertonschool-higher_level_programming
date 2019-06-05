#!/usr/bin/python3
class MyInt(int):

    def __eq__(self, other):
        if int(self) is other:
            return False

    def __ne__(self, other):
        if int(self) is other:
            return True
