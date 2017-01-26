from random import choice, random
from math import sqrt
from math import sin, cos, tan, degrees, radians, pi

allVals = {'sin':{0:0, 15:(sqrt(6)-sqrt(2))/4, 30:1/2, 45:sqrt(2)/2, 60:sqrt(3)/2, 75:(sqrt(6)+sqrt(2))/4, 90:1},
           'tan':{0:0, 15:2-sqrt(3), 30:sqrt(3)/3, 45:1, 60:sqrt(3), 75:2+sqrt(3)}}

def val(func, param, mode='degrees'):
    if mode == 'radians':
        param = int(param*(180/pi))
    if func == 'cos':
        func = 'sin'
        param = 90 - param
    if func == 'cot':
        func = 'tan'
        param = 90 - param
    sign = 1
    if param >= 360:
        param -= param - param%360
    if param > 90:
        coef = (param - param%90) // 90
        if func == 'sin' and param >= 180:
            sign = -1
        if func == 'tan' and param <= 270:
            sign = -1
        if coef%2 == 1:
            if func == 'sin':
                return sign * val('cos', param-coef*90)
            else:
                return sign * val('cot', param-coef*90)
        else:
            return sign * val(func, param-coef*90)
    if param < 0:
        if func in ('sin','tan'):
            return -val(func, -param)
        else:
            return val(func, -param)
    return allVals[func][param]

MODE = 1 # 1-easy, 2-hard
FUNCTIONS = ('sin', 'cos', 'tan')

if MODE == 1:
    specials = (0,30,45,60,90)
    possibility = {0:20, 1:15, 2:15, 3:10, 4:10, 5:5}
    addon = [i for i,j in possibility.items() for k in range(j)]
if MODE == 2:
    speicals = (0,15,30,45,60,75,90)
    possibility = {0:1, 1:1, 2:1, 3:1, 4:1, 5:1}
    addon = [i for i,j in possibility.items() for k in range(j)]

while True:
    question = (choice(specials) + choice(addon) * 90)
    if random() < 0.4:
        question = -question
    while True:
        function = choice(FUNCTIONS)
        if function == 'tan' and question % 90 == 0:
            continue
        break
    answer = input('{}({}°) = '.format(function,question))
    if function not in answer:
        try:
            answerVal = eval(answer)
        except Exception:
            print('Invalid input!\n')
            continue
        correct = val(function, question)
        if answerVal == correct:
            print('Correct!\n')
        else:
            print('Incorrect!')
            print('Answer is: {}\n'.format(correct))
