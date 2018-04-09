from pykkar import *
create_world("""
 #######
 # >  5#
 #     #
 #     #
 #     #
 #     #
 #     #
 #######
""")
def left():
    right()
    right()
    right()
def võta_torbik():
    left()
    while True:
        if not is_wall():
            step()
        if is_wall:
            break
    right()
    while True:
        if not is_cone():
            step()
        if is_wall() or is_cone():
            break
def pane_torbik():
    right()
    right()
    while True:
        if is_wall():
            step()
        if is_wall:
            break
    left()
    while True:
        if is_wall():
            step()
        if is_wall:
            break
    left()
    while True:
        if not is_wall or not is_cone():
            step()
        if is_wall:
            break
    right()
    right()
    step()
    right()
    right()
    put()
left()
while True:
    if not is_wall:
        step()
    if is_wall:
        break
right()
while True:
    if not is_cone():
        step()
    if is_cone():
        break
take()
while True:
    pane_torbik
    võta_torbik
    if is_wall():
        break
        