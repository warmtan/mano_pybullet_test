from mano_pybullet.envs.hand_push_env import HandPushEnv
if __name__ == '__main__':
    from mano_pybullet.envs.wrappers.json_player import JSONPlayer

    env = HandPushEnv()
    env.show_window(True)
    env = JSONPlayer(env, './data/push_teddy.json')
    env.reset()
    while True:
        _observation, _reward, done, _info = env.step()
        if done:
            break