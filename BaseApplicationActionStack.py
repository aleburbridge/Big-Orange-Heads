from action import Action


class BaseApplicationActionStack:
    def __init__(self, base, actions=None):
        if actions is None:
            actions = []
        self.base = base
        self._actions = actions

    def add(self, action: Action):
        self._actions.append(action)
        self._actions.sort(key=lambda a: a.priority)
        return self

    def apply(self, *args):
        result = []
        applied_base = self.base(*args)
        for action in self._actions:
            result = action.fn(applied_base, result)
        return result


