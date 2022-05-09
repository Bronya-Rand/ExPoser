
init -1:
    define persistent.enable_auto_focus = False # Enables/Disables Autofocus
    define persistent.enable_auto_mouth = False # Enables/Disables Automouth

init python:
    
    def auto_focus(event, interact=True, **kwargs):
        char = renpy.get_say_image_tag() # We grab who is the speaker
        if char is None: # If this is the narrator we exit this function
            return

        c = renpy.display.core.displayable_by_tag("master", char) # Borrowed from MPT to get the current sprite info
        if event == "begin": # If character is speaking show focus
            if persistent.enable_auto_mouth: renpy.show(char + " om", at_list=[focus(c.xpos)])
            else: renpy.show(char, at_list=[focus(c.xpos)])
        elif event == "end": # If character has stopped speaking, show tcommon (normal)
            if persistent.enable_auto_mouth: renpy.show(char + " cm", at_list=[tcommon(c.xpos)])
            else: renpy.show(char, at_list=[tcommon(c.xpos)])

    if persistent.enable_auto_focus:
        # This is more better than doing every callback per character.
        # If you want to do it per character, comment this out and type this instead
        # X.display_args["callback"] = auto_focus 
        #
        # Replace "X" with your characters' var
        config.all_character_callbacks.append(auto_focus)
    else:
        config.all_character_callbacks = []
