class Agent:
    def __init__(self, name):
        self.name = name
        self.state = {}

    def observe(self, environment_state):
        return environment_state

    def act(self, observation):
        return None
