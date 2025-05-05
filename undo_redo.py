class UndoRedo:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def add_action(self, action, data):
        self.undo_stack.append((action, data))
        self.redo_stack.clear()

    def undo(self):
        if not self.undo_stack:
            return "Nothing to undo."
        action, data = self.undo_stack.pop()
        self.redo_stack.append((action, data))
        return f"Undid {action}: {data}"

    def redo(self):
        if not self.redo_stack:
            return "Nothing to redo."
        action, data = self.redo_stack.pop()
        self.undo_stack.append((action, data))
        return f"Redid {action}: {data}"
