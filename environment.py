class Environment:
    def __init__(self):
        self.time = 0
        self.state = {}

    def apply_action(self, agent, action):
        pass

    def step(self):
        self.time += 1
