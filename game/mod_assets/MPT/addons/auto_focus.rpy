
init -1:
    default persistent.enable_auto_focus = True # Enables/Disables Autofocus
    default persistent.enable_auto_mouth = False # Enables/Disables Automouth
    default persistent.enable_breathing = True # Enables/Disables Breathing
    default char_list = ["sayori", "natsuki", "yuri", "monika"]

init python:
    import random

    def auto_focus(char, breath_speed, event, interact=True, **kwargs):
        if char is None: # If this is the narrator we exit this function
            return

        c = renpy.display.core.displayable_by_tag("master", char.lower()) # Borrowed from MPT to get the current sprite info
        at_list = []

        if event == "begin": # If character is speaking show focus
            if persistent.enable_breathing:
                at_list.append(fbreathe(c.xpos, c.zoom, breath_speed))
            else:
                at_list.append(focus(c.xpos))
            if persistent.enable_auto_mouth: 
                char += " om"
        elif event == "end": # If character has stopped speaking, show tcommon (normal)
            if persistent.enable_breathing:
                at_list.append(tbreathe(c.xpos, c.zoom, breath_speed))
            else:
                at_list.append(tcommon(c.xpos))
            if persistent.enable_auto_mouth:
                char += " cm"
        renpy.show(char.lower(), at_list=at_list)

    if persistent.enable_auto_focus:
        from functools import partial
        s_af_callback = partial(auto_focus,"sayori", round(random.uniform(1.4, 1.5), 2))
        n_af_callback = partial(auto_focus,"natsuki", round(random.uniform(1.4, 1.5), 2))
        m_af_callback = partial(auto_focus,"monika", round(random.uniform(1.4, 1.5), 2))
        y_af_callback = partial(auto_focus,"yuri", round(random.uniform(1.4, 1.5), 2))

        s.display_args["callback"] = s_af_callback 
        n.display_args["callback"] = n_af_callback 
        y.display_args["callback"] = y_af_callback 
        m.display_args["callback"] = m_af_callback 

transform fbreathe(x=640, z=0.8, bs):
    xcenter x yoffset 0 zoom z alpha 1.00 yanchor 1.0 ypos 1.03
    parallel:
        animation
        easein bs zoom .85 #1.5 zoom .85
        pause 0.1
        easeout 1.5 zoom .849
        repeat

transform tbreathe(x=640, z=0.8, bs):
    xcenter x yoffset 0 zoom z alpha 1.00 yanchor 1.0 ypos 1.03
    parallel:
        animation
        easein bs zoom .801 #1.5 zoom .81
        pause 0.1
        easeout 1.5 zoom .8
        repeat
