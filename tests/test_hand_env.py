from mano_pybullet.envs.hand_env import HandEnv
import pybullet as pb
if __name__ == '__main__':
    import time

    env = HandEnv(HandEnv.HAND_BOTH)
    env.show_window()
    env.seed(0)
    env.reset()

    while pb.isConnected():
        time.sleep(0.1)