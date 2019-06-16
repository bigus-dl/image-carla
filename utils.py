import numpy as np

def action_to_label(action) :
    # bizarre cases
    if action[3] != 0 or action[4]!= 0 :
        print ("bizarre expert action! handbrake {}, reverse {}".format(action[3], action[4]))
    # normal cases
    left = action[0]<0
    right = action[0]>0
    throttle = action[1]>0
    brake = action[2]>0
    label = 6
    if throttle :
        label = 0
        if left :
            label = 1
        if right :
            label = 2
    elif brake :
        label = 3
        if left :
            label = 4
        if right :
            label = 5
    else :
        label = 6
        if left :
            label = 7
        if right :
            label = 8
    return label

'''
0 : throttle
1 : throttle+left 
2 : throttle+right
3 : brake
4 : brake+left
5 : brake+right
6 : no-op
7 : left
8 : right

action : [steer, throttle, brake]
'''
# there's a better way to do this... meh
def label_to_action(label):
    action = [0.0, 0.0, 0.0]
    if label == 0:
        action = [0.0, 1.0, 0.0]
    elif label == 1:
        action = [-1.0, 1.0, 0.0]
    elif label == 2:
        action = [1.0, 1.0, 0.0]
    elif label == 3:
        action = [0.0, 0.0, 1.0]
    elif label == 4:
        action = [-1.0, 0.0, 1.0]
    elif label == 5:
        action = [1.0, 0.0, 1.0]
    elif label == 6:
        action = [0.0, 0.0, 0.0]
    elif label == 7:
        action = [-1.0, 0.0, 0.0]
    elif label == 8:
        action = [1.0, 0.0, 0.0]