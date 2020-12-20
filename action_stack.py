import functools

from action import Action


class ActionStack:
    def __init__(self, base):
        self.base = base
        self._actions = []

    def add(self, action: Action):
        self._actions.append(action)
        self._actions.sort(key=lambda a: a.priority)

    def apply(self, *args):
        result = self.base(*args)
        for action in self._actions:
            result = action.fn(result)
        return result



if __name__ == "__main__":
    stack = ActionStack(lambda x: x)
    stack.add(Action(lambda x: x + 1, 2, []))
    stack.add(Action(lambda x: x*2, 1, []))

    print(stack.apply(1))

    stack = ActionStack(lambda: 3)
    stack.add(Action(lambda x: x + 1, 2, []))
    stack.add(Action(lambda x: x*2, 1, []))

    print(stack.apply())
