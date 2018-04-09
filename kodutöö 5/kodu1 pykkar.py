from pykkar import *
create_world("""
##########
#        #
#   v    #
#        #
#        #
##########
""")
def liigu_seinani():
    while not is_wall():
        step()
    right()
    right()
    right()
liigu_seinani()
liigu_seinani()