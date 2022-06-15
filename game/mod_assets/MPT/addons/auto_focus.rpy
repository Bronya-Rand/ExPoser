
init -1:
    default persistent.enable_auto_focus = True # Enables/Disables Autofocus
    default persistent.enable_auto_mouth = False # Enables/Disables Automouth

init 1 python:

    class AutoFocus:

        def __init__(self, tag):
            self.tag = tag.lower()

        def __call__(self, event, **kwargs):
            if not renpy.showing(self.tag):
                return
            
            c = renpy.display.core.displayable_by_tag("master", self.tag)
            char = self.tag
            at_list = []

            if event == "begin": # If character is speaking show focus
                at_list.append(focus(c.xpos))
                if persistent.enable_auto_mouth: 
                    char += " om"
            elif event == "end": # If character has stopped speaking, show tcommon (normal)
                at_list.append(tcommon(c.xpos))
                if persistent.enable_auto_mouth:
                    char += " cm"
            renpy.show(char, at_list=at_list)
            
    if persistent.enable_auto_focus:
        s.display_args["callback"] = AutoFocus("sayori") 
        n.display_args["callback"] = AutoFocus("natsuki") 
        y.display_args["callback"] = AutoFocus("yuri") 
        m.display_args["callback"] = AutoFocus("monika")  
