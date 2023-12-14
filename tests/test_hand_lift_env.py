

from mano_pybullet.envs.hand_lift_env import HandLiftEnv
import pybullet as pb
if __name__ == '__main__':
    from mano_pybullet.envs.wrappers.json_player import JSONPlayer

    env = HandLiftEnv()
    env.show_window(True)
    env = JSONPlayer(env, './data/lift_duck.json')
    env.reset()
    while True:
        _observation, _reward, done, _info = env.step()
        if done:
            break