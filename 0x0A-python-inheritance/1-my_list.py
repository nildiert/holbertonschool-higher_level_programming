class MyList(list):

    def __getitem__(self, key):
        return list.__getitem__(self, key-1)

    def print_sorted(self):
        print(sorted(self))
