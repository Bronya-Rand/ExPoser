# Taken from NBE code and moved to a separate RPY file.

# Monika Blinks
image _mon_blink_a:
    alpha 0.0
    renpy.random.randint(20, 100)*0.1
    choice:
        alpha 1.0
        m_paths + "/blinks/_blink_am.png"
        0.015
        m_paths + "/blinks/eyes_a.png"
        0.035
        m_paths + "/blinks/_blink_am.png"
        0.015
    choice:
        alpha 1.0
        m_paths + "/blinks/_blink_am.png"
        0.015
        m_paths + "/blinks/eyes_a.png"
        0.065
        m_paths + "/blinks/_blink_am.png"
        0.015
    choice:
        alpha 1.0
        m_paths + "/blinks/_blink_am.png"
        0.015
        m_paths + "/blinks/eyes_a.png"
        0.095
        m_paths + "/blinks/_blink_am.png"
        0.015
    choice:
        alpha 1.0
        m_paths + "/blinks/_blink_am.png"
        0.015
        m_paths + "/blinks/eyes_a.png"
        0.035
        m_paths + "/blinks/_blink_am.png"
        0.015
        alpha 0.0
        0.15
        alpha 1.0
        m_paths + "/blinks/_blink_am.png"
        0.015
        m_paths + "/blinks/eyes_a.png"
        0.035
        m_paths + "/blinks/_blink_am.png"
        0.015
    repeat

image _mon_blink_l_a:
    alpha 0.0
    renpy.random.randint(30, 60)*0.1
    choice:
        alpha 1.0
        m_paths + "/blinks/_blink_l_am.png"
        0.015
        m_paths + "/blinks/_blink_l_af.png"
        0.035
        m_paths + "/blinks/_blink_l_am.png"
        0.015
    choice:
        alpha 1.0
        m_paths + "/blinks/_blink_l_am.png"
        0.015
        m_paths + "/blinks/_blink_l_af.png"
        0.065
        m_paths + "/blinks/_blink_l_am.png"
        0.015
    choice:
        alpha 1.0
        m_paths + "/blinks/_blink_l_am.png"
        0.015
        m_paths + "/blinks/_blink_l_af.png"
        0.095
        m_paths + "/blinks/_blink_l_am.png"
        0.015
    choice:
        alpha 1.0
        m_paths + "/blinks/_blink_l_am.png"
        0.015
        m_paths + "/blinks/_blink_l_af.png"
        0.035
        m_paths + "/blinks/_blink_l_am.png"
        0.015
        alpha 0.0
        0.15
        alpha 1.0
        m_paths + "/blinks/_blink_l_am.png"
        0.015
        m_paths + "/blinks/_blink_l_af.png"
        0.035
        m_paths + "/blinks/_blink_l_am.png"
        0.015
    repeat
