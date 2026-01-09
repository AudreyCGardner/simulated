from simulation.agent import Agent
from simulation.environment import Environment
from simulation.simulation import Simulation

agents = [Agent("Agent A"), Agent("Agent B")]
env = Environment()

sim = Simulation(agents, env)
sim.run()
