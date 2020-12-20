class Action:
    def __init__(self, fn, priority, tags):
        self.fn = fn
        self.priority = priority
        self.tags = tags

class UseAction(Action):
    def __init__(self, fn, priority, tags, num_uses):
        Action.__init__(self, fn, priority, tags)
        self.num_uses = num_uses