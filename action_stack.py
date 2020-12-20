import functools

from action import Action


class ActionStack:
    def __init__(self, base):
        self.base = base
        self._actions = []

    def append(self, action: Action):
        self._actions.append(action)
        self._actions.sort(key=lambda a: a.priority)

    def apply(self, tags, *args):
        result = self.base(*args)
        filtered_actions = filter(lambda x: any(tag in tags for tag in x.tags), self._actions)
        for action in filtered_actions:
            result = action.fn(result)
        return result


if __name__ == "__main__":
    stack = ActionStack(lambda x: x)
    stack.append(Action(lambda x: x + 1, 2, []))
    stack.append(Action(lambda x: x * 2, 1, []))

    print(stack.apply(1))

    stack = ActionStack(lambda: 3)
    stack.append(Action(lambda x: x + 1, 2, []))
    stack.append(Action(lambda x: x * 2, 1, []))

    print(stack.apply())
