import threading

def init():
    global RANGE, SHOULD_EXIT, IMG_WIDTH, INVALID_VALUE, RANGE_FILE, \
    YAW_ERR, CAM_FPS, K_P_YAW, YAW_PWM_PIN, PWM_FREQ, ESP32_FILE, \
    MOTOR_NEUTRAL, YAW_CONTROL, ENCODER_COUNT

    """ ACTUAL SETTINGS """
    # Image width
    IMG_WIDTH = 640
    # FPS of the camera video stream
    CAM_FPS = 10
    # File address of the range sensor serial port
    RANGE_FILE = "/dev/ttyUSB0"
    # File address of the ESP32 controller
    ESP32_FILE = "/dev/ttyUSB0"
    # Gain for yaw control
    K_P_YAW = 0.4
    # PWM pin for the yaw motor
    YAW_PWM_PIN = 32
    # PWM frequency (DO NOT TOUCH!!)
    PWM_FREQ = 400
    # Duty cycle value representing neutral motor control
    MOTOR_NEUTRAL = 153

    """ GLOBAL VARIABLES """
    # Current range reading
    RANGE = float
    # Flag for telling the serial thread to exit
    SHOULD_EXIT = threading.Event()
    # Current yaw error in pixels
    YAW_ERR = int
    # Integer value for not performing control / bogus distance measurements
    INVALID_VALUE = 69420 # Also used by the server!
    # Current control input for the yaw
    YAW_CONTROL = MOTOR_NEUTRAL
    # The current encoder count
    ENCODER_COUNT = int
