import gym
from gym.envs.registration import register

from .cliff_walking import *
from .frozen_lake import *

__all__ = ['RewardingFrozenLakeEnv', 'WindyCliffWalkingEnv']


# register(
#     id='RewardingFrozenLakeRewards18x20-v0',
#     entry_point='environments:RewardingFrozenLakeEnv',
#     kwargs={'map_name': '18x20', 'rewarding': True}
# )
#
#
# register(
#     id='RewardingFrozenLakeSlipperyRewards18x20-v0',
#     entry_point='environments:RewardingFrozenLakeEnv',
#     kwargs={'map_name': '18x20', 'rewarding': True, 'is_slippery': True}
# )


register(
    id='WindyCliffWalking-v0',
    entry_point='environments:WindyCliffWalkingEnv',
)

# register(
#     id='CliffWalking-v0',
#     entry_point='environments:WindyCliffWalkingEnv',
#     kwargs={'wind_prob': 0.0}
# )




# def get_large_rewarding_frozen_lake_environment():
#     return gym.make('RewardingFrozenLakeRewards18x20-v0')
#
# def get_large_rewarding_frozen_lake_slipper_environment():
#     return gym.make('RewardingFrozenLakeSlipperyRewards18x20-v0')




# def get_cliff_walking_environment():
#     return gym.make('CliffWalking-v0')


def get_windy_cliff_walking_environment():
    return gym.make('WindyCliffWalking-v0')
