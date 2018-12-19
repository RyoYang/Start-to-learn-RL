from maze_env import Maze
from RL_brain import QLearningTable

def updata():
    # 学习100回合
    for episode in range(100):
        #初始化state观测值
        observation = env.reset()

        while True:
            env.render()

            action = RL.choose_action(str(observation))

            observation_,reward, done = env.step(action)

            RL.learn(str(observation),action,reward,str(observation_))

            observation = observation_

            if done:
                break

        print('game over')
        env.destory()

        if __name__=="__main__":
            env = Maze()
            RL = QLearningTable(action=list(range(env.n_actions)))

            env.after(100,updata)
            env.mainloop()