from mano_pybullet.envs.hand_object_env import  HandObjectEnv
import pybullet as pb

if __name__ == '__main__':
    import time

    env = HandObjectEnv()
    env.show_window()
    env.reset(model_path='duck_vhacd.urdf', up_axis='y')

    while pb.isConnected():
        time.sleep(0.1)