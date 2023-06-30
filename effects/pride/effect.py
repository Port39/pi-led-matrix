from random import random

levels = []
should_rise = []
colors = [
        (205, 102, 255),
        (255, 101, 153),
        (255, 0, 0),
        (255, 142, 0),
        (255, 255, 0),
        (0, 142, 0),
        (0, 192, 192),
        (64, 0, 152),
        (142, 0, 142),
    ]

def initialize():
    global levels
    levels = [random() for i in range(len(colors))]
    for _ in levels:
        should_rise.append(random() < 0.6)

def dim(color, brightness):
    (r,g,b) = color
    return (r*brightness, g*brightness, b*brightness)

def update_levels():
    for i, level in enumerate(levels):
        if should_rise[i]:
            levels[i] = level + 0.01
        else:
            levels[i] = level - 0.01
        if level > 0.8:
            should_rise[i] = False
        if level < 0.2:
            should_rise[i] = True


def run(matrix, config):
    initialize()
    barheight = config['pixel_height'] // len(colors)
    while matrix.ready():
        for (i,color) in enumerate(colors):
            offset = i * barheight
            matrix.rectangle((0,offset),(config['pixel_width'], offset + barheight), dim(color, levels[i]), -1)
        matrix.show(enhance_image=False)
        update_levels()