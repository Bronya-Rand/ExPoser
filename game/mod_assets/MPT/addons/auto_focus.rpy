
init -1:
    default persistent.enable_auto_focus = True # Enables/Disables Autofocus
    default persistent.enable_auto_mouth = False # Enables/Disables Automouth

init python:
    import random

    class AutoFocus:

        def __init__(self, char):
            self.char = char.lower()

        def __call__(self):
            c = renpy.display.core.displayable_by_tag("master", self.char) # Borrowed from MPT to get the current sprite info
            at_list = []

            if event == "begin": # If character is speaking show focus
                at_list.append(focus(c.xpos))
                if persistent.enable_auto_mouth: 
                    char += " om"
            elif event == "end": # If character has stopped speaking, show tcommon (normal)
                at_list.append(tcommon(c.xpos))
                if persistent.enable_auto_mouth:
                    char += " cm"
            renpy.show(char.lower(), at_list=at_list)

    if persistent.enable_auto_focus:
        s.display_args["callback"] = AutoFocus("sayori")
        n.display_args["callback"] = AutoFocus("natsuki")
        y.display_args["callback"] = AutoFocus("yuri")
        m.display_args["callback"] = AutoFocus("monika")
