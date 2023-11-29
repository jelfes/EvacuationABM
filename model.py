import mesa
import numpy as np

from agent import PanicAgent2
from helpers import get_panic_level, get_num_agents


class PanicModel(mesa.Model):
    """An ABM to model the development of mass panic during an evacuation scenario."""

    def __init__(
        self,
        N,
        height,
        width,
        max_group_size,
        min_group_size,
        resilience,
        min_radius,
        min_velocity=0.1,
    ):
        """
        Args:
            N (int): number of agents
            height (float): height of the model space
            width (float): width of the model space
            max_group_size (int): maximum size of friend groups
            min_group_size (int): minimum size of friend groups
            resilience (int): number of epochs before an agent switches into panic
            min_radius (flaot): minimal radius of agents
            min_velocity (flaot): minimal velocity of agents

        """

        self.num_agents = N
        self.space = mesa.space.ContinuousSpace(width, height, torus=True)
        self.schedule = mesa.time.RandomActivation(self)

        # Create agents
        for i in range(self.num_agents):
            a = PanicAgent2(
                i,
                self,
                resilience=resilience,
                min_radius=min_radius,
                min_velocity=min_velocity,
            )
            self.schedule.add(a)

            # place agent on model space
            x = self.random.uniform(0, width)
            y = self.random.uniform(0, height)
            self.space.place_agent(a, (x, y))

        # devide agents into friend groups
        self.friend_groups = []
        agents = self.schedule.agents.copy()

        while len(agents) > 0:
            group_size = min(
                [self.random.randint(min_group_size, max_group_size), len(agents)]
            )

            group = self.random.sample(agents, group_size)
            self.friend_groups.append(group)

            agents = list(set(agents).difference(set(group)))

        for i, group in enumerate(self.friend_groups):
            for agent in group:
                agent.friends = group
                agent.group_number = i

        # set up data collection
        self.datacollector = mesa.DataCollector(
            model_reporters={
                "panic": get_panic_level,
                "num_agents": get_num_agents,
            },
            agent_reporters={
                "panic": "panic",
                "exporsure": "exposure",
                "position": "pos",
            },
        )

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()
