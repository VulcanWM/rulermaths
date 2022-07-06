import math


def get_angle_from_opp_hyp(o, h):
    num = o / h
    radian = math.asin(num)
    degrees = math.degrees(radian)
    return degrees


def get_angle_from_opp_adj(o, a):
    num = o / a
    radian = math.atan(num)
    degrees = math.degrees(radian)
    return degrees


def get_angle_from_adj_hyp(a, h):
    num = a / h
    radian = math.acos(num)
    degrees = math.degrees(radian)
    return degrees


def get_adj_from_angle_hyp(angle, h):
    a = h * math.cos(math.radians(angle))
    return a


def get_opp_from_angle_hyp(angle, h):
    o = h * math.sin(math.radians(angle))
    return o


def get_adj_from_angle_opp(angle, o):
    a = o / math.tan(math.radians(angle))
    return a


def get_opp_from_angle_adj(angle, a):
    o = a * math.tan(math.radians(angle))
    return o


def get_hyp_from_angle_adj(angle, a):
    h = a / math.cos(math.radians(angle))
    return h


def get_hyp_from_angle_opp(angle, o):
    h = o / math.sin(math.radians(angle))
    return h
