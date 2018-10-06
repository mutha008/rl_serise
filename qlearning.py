import numpy as np
import pandas as pd
import time

"""
    Q-learning a simply case 
"""
N_STATES = 8 # S
ACTIONS = ["left", "right"]  # A
EPSILON = 0.9  # Policy random ratio
ALPHA = 0.1  # learning rate
LAMBDA = 0.9 # discount
MAX_EPOCH = 15 # max 
FRESH_TIME = 0.3 # fresh print time eval 

def build_qtable(n_status, actions):
    """
        q表初始化
    """
    qtable = pd.DataFrame(np.zeros((n_status, len(actions))), columns=actions)
    return qtable

def update_qtable(cur_status, qtable, end_tag):
    """
        q表更新
    """
    action = choose_action(cur_status, qtable, ACTIONS)
    next_status, reward = env_feedback(cur_status, action, N_STATES)
    q_predict = qtable.loc[cur_status, action]
    if next_status == N_STATES - 1:
        end_tag = True
        q_target = reward
    else:
        q_target = reward + LAMBDA * qtable.iloc[next_status].max()
    qtable.loc[cur_status, action] += ALPHA * (q_target - q_predict)
    return next_status, end_tag

def choose_action(state, qtable, actions):
    """
        动作策略
    """
    status_actions = qtable.iloc[state]
    if(np.random.uniform(0, 1) > EPSILON) or (status_actions.all() == 0):
        action_name = np.random.choice(actions)
    else:
        action_name = status_actions.idxmax()
    return action_name

def env_feedback(state, action, state_len):
    """
        环境反馈
    """
    reward = 0
    if (state == state_len - 2) and action == 'right':
        reward = 1
        state += 1
    elif state == 0 and action == "left":
        reward = -1
    elif action == "right":
        state += 1
    elif action == "left":
        state -= 1
    return state, reward

def env_fresh(status, epoch, step):
    """
        环境更新
    """
    env_list = ["-"] * (N_STATES-1) + ["●"]
    if status == N_STATES - 1:
        env_list[status] = "☺"
    else:
        env_list[status] = "☹"
    game_reslt = "%s\tEpoch: %s, total step: %s" %(''.join(env_list), epoch, step)
    print("\r{}".format(game_reslt), end="")
    time.sleep(FRESH_TIME)


def main():
    qtable = build_qtable(N_STATES, ACTIONS)
    for epoch in range(MAX_EPOCH):
        end_tag = False
        cur_status = 0
        cur_epoch_step = 0
        env_fresh(cur_status, epoch, cur_epoch_step)
        while not end_tag:
            cur_status, end_tag = update_qtable(cur_status, qtable, end_tag)
            cur_epoch_step += 1
            env_fresh(cur_status, epoch, cur_epoch_step)
        print()
        print(qtable)
            


if __name__ == "__main__":
    main()
