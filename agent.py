import time

import gym

env = gym.make("procgen:procgen-coinrun-v0")
obs = env.reset()

while True:
    obs, rew, done, info = env.step(env.action_space.sample())
    env.render()
    time.sleep(0.01)
    if done:
        break
