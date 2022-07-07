import math


def get_angle_from_opp_hyp(o, h, dec=2):
    num = o / h
    radian = math.asin(num)
    degrees = math.degrees(radian)
    return round(degrees, dec)


def get_angle_from_opp_adj(o, a, dec=2):
    num = o / a
    radian = math.atan(num)
    degrees = math.degrees(radian)
    return round(degrees, dec)


def get_angle_from_adj_hyp(a, h, dec=2):
    num = a / h
    radian = math.acos(num)
    degrees = math.degrees(radian)
    return round(degrees, dec)


def get_adj_from_angle_hyp(angle, h, dec=2):
    a = h * math.cos(math.radians(angle))
    return round(a, dec)


def get_hyp_from_angle_adj(angle, a, dec=2):
    h = a / math.cos(math.radians(angle))
    return round(h, dec)


def get_opp_from_angle_hyp(angle, h, dec=2):
    o = h * math.sin(math.radians(angle))
    return round(o, dec)


def get_hyp_from_angle_opp(angle, o, dec=2):
    h = o / math.sin(math.radians(angle))
    return round(h, dec)


def get_adj_from_angle_opp(angle, o, dec=2):
    a = o / math.tan(math.radians(angle))
    return round(a, dec)


def get_opp_from_angle_adj(angle, a, dec=2):
    o = a * math.tan(math.radians(angle))
    return round(o, dec)
