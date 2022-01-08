#Simulator options.
options = {}
options['FIG_SIZE'] = [8,8]
options['OBSTACLES'] = False

class Run:
    def __init__(self):
        self.dt = 0.2
        #Reference or set point the controller will achieve.
        self.reference1 = [10, 10, 0] # [x, y, angle]
        self.reference2 = None

    def run(self, current_state):
        x_t = current_state[0]  # X location [m]
        y_t = current_state[1]  # Y location [m]
        psi_t = current_state[2] # Angle [rad]
        v_t = current_state[3]  # Speed [m/s]
        pedal = 0
        steering = 0

        return [pedal, steering]