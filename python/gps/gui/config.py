""" Default configuration and hyperparameter values for GUI objects. """
import itertools

from gps.proto.gps_pb2 import TRIAL_ARM, AUXILIARY_ARM
from gps.gui.ps3_config import PS3_BUTTON, INVERTED_PS3_BUTTON


# Mappings from actions to their corresponding keyboard bindings.
keyboard_bindings = {
    # Target Setup.
    'ptn': 'left',  # previous target number
    'ntn': 'right', # next target number
    'pat': 'down',  # previous actuator type
    'nat': 'up',    # next actuator type

    'sip': 'i',     # set initial position
    'stp': 't',     # set target position
    'sii': 'p',     # set initial image
    'sti': 'a',     # set target image

    'mti': 'm',     # move to initial
    'mtt': 'g',     # move to target
    'rc': 'r',      # relax controller
    'mm': 'q',      # mannequin mode

    # GPS Training.
    'stop' : 's',   # stop
    'reset': 'r',   # reset
    'go'   : 'g',   # go
    'fail' : 'f',   # fail

    # Image Visualizer
    'oii'  : 'o',   # overlay initial image
    'oti'  : 'x',   # overlay target image
}
inverted_keyboard_bindings = {value: key
                              for key, value in keyboard_bindings.iteritems()}

# Mappings from actions to their corresponding PS3 controller bindings.
ps3_bindings = {
    # Target Setup
    'ptn': (PS3_BUTTON['rear_right_1'], PS3_BUTTON['cross_left']),
    'ntn': (PS3_BUTTON['rear_right_1'], PS3_BUTTON['cross_right']),
    'pat': (PS3_BUTTON['rear_right_1'], PS3_BUTTON['cross_down']),
    'nat': (PS3_BUTTON['rear_right_1'], PS3_BUTTON['cross_up']),

    'sip': (PS3_BUTTON['rear_right_1'], PS3_BUTTON['action_square']),
    'stp': (PS3_BUTTON['rear_right_1'], PS3_BUTTON['action_circle']),
    'sii': (PS3_BUTTON['rear_right_1'], PS3_BUTTON['action_cross']),
    'sti': (PS3_BUTTON['rear_right_1'], PS3_BUTTON['action_triangle']),

    'mti': (PS3_BUTTON['rear_right_2'], PS3_BUTTON['cross_left']),
    'mtt': (PS3_BUTTON['rear_right_2'], PS3_BUTTON['cross_right']),
    'rc' : (PS3_BUTTON['rear_right_2'], PS3_BUTTON['cross_down']),
    'mm' : (PS3_BUTTON['rear_right_2'], PS3_BUTTON['cross_up']),

    # GPS Training
    'stop' : (PS3_BUTTON['rear_right_2'], PS3_BUTTON['action_square']),
    'reset': (PS3_BUTTON['rear_right_2'], PS3_BUTTON['action_triangle']),
    'go'   : (PS3_BUTTON['rear_right_2'], PS3_BUTTON['action_circle']),
    'fail' : (PS3_BUTTON['rear_right_2'], PS3_BUTTON['action_cross']),

    # Image Visualizer
    'oii'  : (PS3_BUTTON['cross_up']    ,),
    'oti'  : (PS3_BUTTON['cross_down']  ,),
}
inverted_ps3_bindings = {value: key for key, value in ps3_bindings.iteritems()}

permuted_inverted_ps3_bindings = {}
for key, value in list(inverted_ps3_bindings.iteritems()):
    for permuted_key in itertools.permutations(key, len(key)):
        permuted_inverted_ps3_bindings[permuted_key] = value

config = {
    'ps3_topic': 'joy',
    'ps3_process_rate': 20,  # Only process 1/20 of PS3 messages.
    'ps3_button': PS3_BUTTON,
    'inverted_ps3_button': INVERTED_PS3_BUTTON,

    'keyboard_bindings': keyboard_bindings,
    'inverted_keyboard_bindings': inverted_keyboard_bindings,
    'ps3_bindings': ps3_bindings,
    'inverted_ps3_bindings': inverted_ps3_bindings,
    'permuted_inverted_ps3_bindings': permuted_inverted_ps3_bindings,

    'display_images': True,
    'image_topic': '/camera/rgb/image_color',
    'image_size': (240, 240),
    'image_overlay_actuator': 'trial_arm',
    'image_overlay_alpha': 0.3,

    'figsize': (12, 12),

    # Target Setup
    'num_targets': 10,
    'actuator_types': [TRIAL_ARM, AUXILIARY_ARM],
    'actuator_names': ['trial_arm', 'auxiliary_arm'],
    'target_output_fontsize': 10,

    # GPS Training
    'initial_mode': 'run',
    'algthm_output_max_display_size': 15,
    'algthm_output_fontsize': 10,
}
