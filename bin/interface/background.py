import os

from PIL import Image, ImageTk


i_case = 0
case = 0

i_ball_r = 0
i_ball_w = 0
i_ball_b = 0
i_ball_n = 0

ball_r = 0
ball_w = 0
ball_b = 0
ball_n = 0

i_active = 0
i_inactive = 0

i_is_p1_turn = 0
is_p1_turn = 0

i_is_p2_turn = 0
is_p2_turn = 0

i_not_p1_turn = 0
not_p1_turn = 0

i_not_p2_turn = 0
not_p2_turn = 0
active_r, active_d, active_l, active_u, inactive_r, inactive_d, inactive_l, inactive_u = (0, 0, 0, 0, 0, 0, 0, 0)


def load_images():
    """
    Load up every image in memory once a tk instance has been instantiated.
    """
    global i_case, case, i_ball_r, i_ball_w, i_ball_b, i_ball_n, ball_r, ball_w, ball_b, ball_n, i_active, i_inactive, i_is_p1_turn, is_p1_turn, i_is_p2_turn, is_p2_turn, i_not_p1_turn, not_p1_turn, i_not_p2_turn, not_p2_turn, active_r, active_d, active_l, active_u, inactive_r, inactive_d, inactive_l, inactive_u

    i_case = Image.open(os.path.join(os.path.dirname(__file__), "../../resources/interface/case.png"))
    case = ImageTk.PhotoImage(i_case, size="32x32")

    i_ball_r = Image.open(os.path.join(os.path.dirname(__file__), "../../resources/interface/ball_red.png"))
    i_ball_w = Image.open(os.path.join(os.path.dirname(__file__), "../../resources/interface/ball_white.png"))
    i_ball_b = Image.open(os.path.join(os.path.dirname(__file__), "../../resources/interface/ball_black.png"))
    i_ball_n = Image.open(os.path.join(os.path.dirname(__file__), "../../resources/interface/ball_none.png"))

    ball_r = ImageTk.PhotoImage(i_ball_r, size="32x32")
    ball_w = ImageTk.PhotoImage(i_ball_w, size="32x32")
    ball_b = ImageTk.PhotoImage(i_ball_b, size="32x32")
    ball_n = ImageTk.PhotoImage(i_ball_n, size="32x32")

    i_active = Image.open(os.path.join(os.path.dirname(__file__), "../../resources/interface/selector_active.png"))
    i_inactive = Image.open(os.path.join(os.path.dirname(__file__), "../../resources/interface/selector_inactive.png"))

    i_is_p1_turn = Image.open(os.path.join(os.path.dirname(__file__), "../../resources/interface/p_1_turn_on.png"))
    is_p1_turn = ImageTk.PhotoImage(i_is_p1_turn, size="256x128")

    i_is_p2_turn = Image.open(os.path.join(os.path.dirname(__file__), "../../resources/interface/p_2_turn_on.png"))
    is_p2_turn = ImageTk.PhotoImage(i_is_p2_turn, size="256x128")

    i_not_p1_turn = Image.open(os.path.join(os.path.dirname(__file__), "../../resources/interface/p_1_turn_off.png"))
    not_p1_turn = ImageTk.PhotoImage(i_not_p1_turn, size="256x128")

    i_not_p2_turn = Image.open(os.path.join(os.path.dirname(__file__), "../../resources/interface/p_2_turn_off.png"))
    not_p2_turn = ImageTk.PhotoImage(i_not_p2_turn, size="256x128")

    active_u = ImageTk.PhotoImage(i_active.rotate(0, expand=True))
    active_d = ImageTk.PhotoImage(i_active.rotate(180, expand=True))
    active_l = ImageTk.PhotoImage(i_active.rotate(90, expand=True))
    active_r = ImageTk.PhotoImage(i_active.rotate(-90, expand=True))

    inactive_u = ImageTk.PhotoImage(i_inactive.rotate(0, expand=True))
    inactive_d = ImageTk.PhotoImage(i_inactive.rotate(180, expand=True))
    inactive_l = ImageTk.PhotoImage(i_inactive.rotate(90, expand=True))
    inactive_r = ImageTk.PhotoImage(i_inactive.rotate(-90, expand=True))


def get_selector_image(state, d):
    """
    Returns the corresponding selector bg for each direction and state possible
    
    :param state: the selector state
    :param d: the selector direction
    :return: the corresponding rotated image
    """
    if state:
        if d == 'u':
            return active_u
        if d == 'l':
            return active_l
        if d == 'r':
            return active_r
        if d == 'd':
            return active_d
    else:
        if d == 'u':
            return inactive_u
        if d == 'l':
            return inactive_l
        if d == 'r':
            return inactive_r
        if d == 'd':
            return inactive_d
