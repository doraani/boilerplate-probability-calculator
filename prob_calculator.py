import copy
import random
# Consider using the modules imported above.

class Hat:
    # A Hat will have at least one ball
    def __init__(self, **balls):
        self.contents = []
        for ball in balls:
            color = ball
            num = balls[ball]
            for i in range(num):
                self.contents.append(color)
    
    def draw(self, num):
        balls = []
        if num <= len(self.contents):
            for i in range(0, num):
                rand_index = random.randint(0, len(self.contents)-1)
                balls.append(self.contents[rand_index])
                self.contents.pop(rand_index)
            return balls
        else:
            return self.contents

def included(balls_list, balls_object):
    # balls_list is a list of balls color strings format: [color, color,...]
    # balls_list colors can not contain a color that is not in ball_object
    # balls_object is an object format: {color: amount,...}
    # returns true if the number of balls in the list is equal or higer than the number of balls in the object fo each color
    for color in balls_object:
        if balls_list.count(color) < balls_object[color]:
            return False
    return True
            

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0
    for i in range(0, num_experiments):
        hat_copy = copy.deepcopy(hat)
        result = hat_copy.draw(num_balls_drawn)
        if included(result, expected_balls):
            successes += 1
    p = successes / num_experiments
    return p
