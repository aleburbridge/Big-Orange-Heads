from action.Action import Action


class ActionStack:
    def __init__(self):
        self._actions = []

    def append(self, action: Action):
        self._actions.append(action)
        self._actions.sort(key=lambda a: a.priority)

    def apply(self, x, tags=None):
        if len(self._actions) == 0:
            return x
        if tags is None:
            tags = []
        result = x
        filtered_actions = filter(lambda a: len(a) == 0 or any(tag in tags for tag in a.tags), self._actions)
        for action in filtered_actions:
            result = action.fn(result)
        return result


if __name__ == "__main__":
    stack = ActionStack()
    stack.append(Action(lambda x: x + 1, 2, []))
    stack.append(Action(lambda x: x * 2, 1, []))

    print(stack.apply(1))

    stack = ActionStack()
    stack.append(Action(lambda x: x + 1, 2, []))
    stack.append(Action(lambda x: x * 2, 1, []))

    print(stack.apply(2))
