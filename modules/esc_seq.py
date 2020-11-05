#!/usr/bin/python3

# === HEADER ===
# serial: 21/10/2020|01
# description: Simple module that allows you to use the escape sequences easily
# project: None
# members: 
# - MICHON Mathieu (michon@et.intechinfo.fr)
# ==============

class esc_seq:

    # set/reset
    reset_all       = '\x1b[0m'
    reset_underl    = '\x1b[24m'
    reset_hid       = '\x1b[28m'
    underlined      = '\x1b[4m'
    hidden          = '\x1b[8m'

    # font colours
    default         = '\x1b[39m'
    red             = '\x1b[31m'
    green           = '\x1b[32m'
    yellow          = '\x1b[33m'
    blue            = '\x1b[34m'
    cyan            = '\x1b[36m'
    light_gray      = '\x1b[37m'
    light_red       = '\x1b[91m'
    light_green     = '\x1b[92m'
    light_yellow    = '\x1b[93m'
    light_blue      = '\x1b[94m'
    light_magenta   = '\x1b[95m'
    light_cyan      = '\x1b[96m'
    white           = '\x1b[97m'
    
    # background colours
    b_red           = '\x1b[41m'
    b_green         = '\x1b[42m'
    b_yellow        = '\x1b[43m'
    b_blue          = '\x1b[44m'
    b_magenta       = '\x1b[45m'
    b_cyan          = '\x1b[46m'
    b_light_gray    = '\x1b[47m'
    b_light_red     = '\x1b[101m'
    b_light_green   = '\x1b[102m'
    b_light_yellow  = '\x1b[103m'
    b_light_blue    = '\x1b[104m'
    b_light_magenta = '\x1b[105m'
    b_light_cyan    = '\x1b[106m'
    b_white         = '\x1b[107m'
