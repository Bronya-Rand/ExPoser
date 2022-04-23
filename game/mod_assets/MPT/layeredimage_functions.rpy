init python:
    def clear_tag(character, target='master'):
        if not isinstance(character, str): 
            raise Exception("'character' argurment must be a string.")
        if not character in renpy.get_showing_tags(layer=target, sort=True):
            return
        pose = str(renpy.get_attributes(character, layer=target)[0])
        if not pose:
            return
        renpy.show(character + " " + pose + " refreshattribute", layer=target)
        renpy.show(character, layer=target)

    # Better cleaning
    def mref(target="master"):
        clear_tag("monika", target)
    
    def sref(target="master"):
        clear_tag("sayori", target)
    
    def nref(target="master"):
        clear_tag("natsuki", target)
    
    def yref(target="master"):
        clear_tag("yuri", target)
