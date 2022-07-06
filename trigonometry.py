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
