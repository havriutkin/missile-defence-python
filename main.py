##########################################################
#
#    _______ _________ _______    ______   _______  _______  _______  _        _______  _______
#   (  ___  )\__   __/(  ____ )  (  __  \ (  ____ \(  ____ \(  ____ \( (    /|(  ____ \(  ____ \
#   | (   ) |   ) (   | (    )|  | (  \  )| (    \/| (    \/| (    \/|  \  ( || (    \/| (    \/
#   | (___) |   | |   | (____)|  | |   ) || (__    | (__    | (__    |   \ | || |      | (__
#   |  ___  |   | |   |     __)  | |   | ||  __)   |  __)   |  __)   | (\ \) || |      |  __)
#   | (   ) |   | |   | (\ (     | |   ) || (      | (      | (      | | \   || |      | (
#   | )   ( |___) (___| ) \ \__  | (__/  )| (____/\| )      | (____/\| )  \  || (____/\| (____/\
#   |/     \|\_______/|/   \__/  (______/ (_______/|/       (_______/|/    )_)(_______/(_______/
#
#    Author: Vladyslav Havriutkin.
#    Date: June 28, 2023.
#    Short description: In this project I tried to simulate a work of simple
#                       2d air defence system using linear regression, and using
#                       pygame for visualisation. More detailed description can be found
#                       in README file.
#
##########################################################


from Settings import Settings
from Scene import Scene

if __name__ == '__main__':
    settings = Settings()
    scene = Scene(settings)
    scene.start()


"""
Polynomials for trajectory

------x-------  ----------------y-------------------
[0, 0, 0.1, 0], [-0.00000000625, 0.000075, -0.2, 300]
"""