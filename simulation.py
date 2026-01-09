class Simulation:
    def __init__(self, agents, environment, max_steps=10):
        self.agents = agents
        self.environment = environment
        self.max_steps = max_steps

    def run(self):
        for _ in range(self.max_steps):
            for agent in self.agents:
                obs = agent.observe(self.environment.state)
                action = agent.act(obs)
                self.environment.apply_action(agent, action)
            self.environment.step()
