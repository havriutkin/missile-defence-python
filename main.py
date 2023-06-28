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