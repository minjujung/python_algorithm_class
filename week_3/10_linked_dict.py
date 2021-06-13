class LinkdeTuple:
    def __init__(self):
        self.items = list()

# [("ksdfksdf8", "test")] -> [("ksdfksdfk", "test33")]
def add(self, key, value):
    self.items.append((key, value))

def get(self, key):
    for k, v in self.items:
        if key == k:
            return v

class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkdeTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index].add(key, value)
        return

    def get(self, key):
        index = hash(key) % len(self.items)
        self.items[index].get(key)
        return
        