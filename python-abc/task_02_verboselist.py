#!/usr/bin/python3


class VerboseList(list):
    def append(self, item):
        super().append(item)
        print("Add [{}] to the list".format(item))

    def extend(self, iterable):
        super().extend(iterable)
        length = len(iterable)
        print("Extended the list with [{}] items".format(iterable))

    def remove(self, item):
        try:
            print("Removed [{}] from the list".format(item))
            super().remove(item)
        except:
            ValueError(f"{item} not found in the list. Cannot remove")

    def pop(self, index=None):
        if index is None:
            item = super().pop()
        else:
            item = super().pop(index)
        print("Popped [{}] from the list".format(item))
        return item
