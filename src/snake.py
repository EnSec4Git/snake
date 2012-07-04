#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Yavor
#
# Created:
# Copyright:   (c) Yavor
# Licence:     GPLv3
#-------------------------------------------------------------------------------

import threading
import msvcrt
import time
import copy
import os

should_stop = False
c = '4'

def clearscreen(numlines=100):
    """Clear the console.

    numlines is an optional argument used only as a fall-back.
    """
    if os.name == "posix":
        # Unix/Linux/MacOS/BSD/etc
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
        # DOS/Windows
        os.system('CLS')
    else:
        # Fallback for other operating systems.
        print('\n' * numlines)

def get_empty_level():
    level_list = []
    cur_list = ['#'] * 64
    level_list.append(cur_list)
    for i in range(1, 23):
        cur_list = ['#']
        cur_list.extend([' ']*62)
        cur_list.append('#')
        level_list.append(cur_list)
    cur_list = ['#'] * 64
    level_list.append(cur_list)
    return level_list

def print_level(level):
    big_str = "";
    for i in level:
        str = ""
        for j in i:
            str += j
        big_str += (str + "\n")
    return big_str

def background_action():
    global c
    while True:
        if should_stop:
            return
        ch = msvcrt.getch()
        if(ch == b'A'):
            c = '4'
        elif(ch == b'D'):
            c = '6'
        elif(ch == b'S'):
            c = '2'
        elif(ch == b'W'):
            c = '8'
        elif(ch == b'Q'):
            return

def get_input():
    time.sleep(0.2)

def init_snake():
    return [(13,13), (17, 13)]

def init_state():
    return [get_empty_level(), init_snake()]

def print_snake(snake):
    print("Snake = ", snake)

def redraw(state):
    level = copy.deepcopy(state[0])
    snake = state[1]
    for i in range(0, len(snake) - 1):
        current_node = snake[i]
        next_node = snake[i+1]
        dx = next_node[0] - current_node[0]
        dy = next_node[1] - current_node[1]
        dist = abs(dx+dy) # dx == 0 or dy == 0 =>
        # Manhattan distance == Euclidean distance
        unit_diff = (dx//dist, dy//dist)
        for j in range(0, dist+1):
            cell = (current_node[0]+j*unit_diff[0], current_node[1]+j*unit_diff[1])
            level[cell[1]][cell[0]] = 'X'
    level_string = print_level(level)
    clearscreen()
    print(level_string)
    print_snake(snake)

def next_state(state):
    if not bg_thread.is_alive():
        return False
    level = state[0]
    snake = state[1]
    snake_head = snake[0]
    snake_neck = snake[1]
    snake_back = snake[-1]
    snake_ass = snake[-2]
    print("Snake head = ", snake_head)
    print("Snake neck = ", snake_neck)
    print("Snake back = ", snake_back)
    print("Snake ass = ", snake_ass)
    head_dx = snake_head[0] - snake_neck[0]
    head_dy = snake_head[1] - snake_neck[1]
    head_dist = abs(head_dx + head_dy)
    head_dir = (head_dx//head_dist, head_dy//head_dist)
    print("Head dir = ", head_dir)
    if c == '8':
        new_dir = (0,-1)
    elif c == '2':
        new_dir = (0,1)
    elif c == '4':
        new_dir = (-1,0)
    else:
        new_dir = (1,0)
    if(head_dir != new_dir and not (head_dir[0] == -new_dir[0] and head_dir[1] == -new_dir[1])):
        print("New direction set!!")
        new_head_pos = (snake_head[0] + new_dir[0], snake_head[1] + new_dir[1])
        state[1] = [new_head_pos] + snake
        snake = state[1]
        print("New snake: ", state[1])
        #time.sleep(1)
    else:
        new_head_pos = (snake_head[0] + head_dir[0], snake_head[1] + head_dir[1])
        snake[0] = new_head_pos
    print("New head position = ", new_head_pos)
    back_dx = snake_ass[0] - snake_back[0]
    back_dy = snake_ass[1] - snake_back[1]
    back_dist = abs(back_dx + back_dy)
    back_dir = (back_dx//back_dist, back_dy//back_dist)
    print("Back dir = ", back_dir)
    new_back_pos = (snake_back[0]+back_dir[0], snake_back[1]+back_dir[1])
    print("New back position = ", new_back_pos)
    if(new_back_pos == snake_ass): # remove last node
        snake.pop()
    else:
        snake[-1] = new_back_pos
    current_char = level[new_head_pos[1]][new_head_pos[0]]
    return (current_char != '#')

def main():
    global bg_thread, should_stop
    bg_thread = threading.Thread(target=background_action, args=())
    bg_thread.start()
    current_state = init_state()
    while True:
        redraw(current_state)
        get_input()
        if not next_state(current_state):
            should_stop = True
            break
        #time.sleep(1)

if __name__ == '__main__':
    main()
    #pass
