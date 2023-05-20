
init python:
    from store import exp_core
    s_paths = exp_core.ExPPaths("mod_assets/ExP/sayori")

layeredimage sayori base: 
    at Flatten
    
    always s_paths + "/facebase.png" #Always need this face.

    group outfit:
        attribute uniform default null
        attribute casual null
    
    # (Formerly Blush) Cheek Expressions
    group cheek: 
        attribute norm default null # Normal
        attribute eh null # Awkward/Eh.
        attribute shy null # Blushing (shy used as synomyn)
        attribute shyeh null # Both Shy and Awkward
    
    # Left Half
    group left:
        attribute ldown default if_any(["uniform"]):
            s_paths + "/base/body/uniform_ldown.png"
        attribute ldown default if_any(["casual"]):
            s_paths + "/base/body/casual_ldown.png"
        attribute lpoint if_any(["uniform"]):
            s_paths + "/base/body/uniform_lpoint.png"
        attribute lpoint if_any(["casual"]):
            s_paths + "/base/body/casual_lpoint.png"
    
    # Right Half
    group right:
        attribute rdown default if_any(["uniform"]):
            s_paths + "/base/body/uniform_rdown.png"
        attribute rdown default if_any(["casual"]):
            s_paths + "/base/body/casual_rdown.png"
        attribute rhip if_any(["uniform"]):
            s_paths + "/base/body/uniform_rhip.png"
        attribute rhip if_any(["casual"]):
            s_paths + "/base/body/casual_rhip.png"
    
    # Nose
    group nose:
        attribute nose default if_any(["norm"]): # default nose
            s_paths + "/base/noses/nose1.png"
        attribute nose default if_any(["eh"]): # default nose when "awkward"
            s_paths + "/base/noses/nose2.png"
        attribute nose default if_any(["shy"]): # default nose when "blushing"
            s_paths + "/base/noses/nose3.png"
        attribute nose default if_any(["shyeh"]): # default nose when "blushing and awkward"
            s_paths + "/base/noses/nose4.png"
        
        attribute nose1:
            s_paths + "/base/noses/nose1.png"
        attribute nose2:
            s_paths + "/base/noses/nose2.png"
        attribute nose3:
            s_paths + "/base/noses/nose3.png"
        attribute nose4:
            s_paths + "/base/noses/nose4.png"
        attribute nose5:
            s_paths + "/base/noses/nose5.png"

    # Mouth
    group mouth:
        attribute mouth_a:
            s_paths + "/base/mouth/mouth_a.png"
        attribute mouth_b:
            s_paths + "/base/mouth/mouth_b.png"
        attribute mouth_c:
            s_paths + "/base/mouth/mouth_c.png"
        attribute mouth_d:
            s_paths + "/base/mouth/mouth_d.png"
        attribute mouth_e:
            s_paths + "/base/mouth/mouth_e.png"
        attribute mouth_f:
            s_paths + "/base/mouth/mouth_f.png"
        attribute mouth_g:
            s_paths + "/base/mouth/mouth_g.png"
        attribute mouth_h:
            s_paths + "/base/mouth/mouth_h.png"
        attribute mouth_i:
            s_paths + "/base/mouth/mouth_i.png"
        attribute mouth_j:
            s_paths + "/base/mouth/mouth_j.png"
        attribute mouth_k:
            s_paths + "/base/mouth/mouth_k.png"
        attribute mouth_l:
            s_paths + "/base/mouth/mouth_l.png"
        attribute mouth_:
            s_paths + "/base/mouth/mouth_m.png"
        attribute mouth_n:
            s_paths + "/base/mouth/mouth_n.png"
        attribute mouth_o:
            s_paths + "/base/mouth/mouth_o.png"
        attribute mouth_p:
            s_paths + "/base/mouth/mouth_p.png"
        attribute mouth_q:
            s_paths + "/base/mouth/mouth_q.png"
        attribute mouth_r:
            s_paths + "/base/mouth/mouth_r.png"
    
    # Eyes
    group eyes:
        attribute eyes_a:
            s_paths + "/base/eyes/eyes_a.png"
        attribute eyes_b:
            s_paths + "/base/eyes/eyes_b.png"
        attribute eyes_c:
            s_paths + "/base/eyes/eyes_c.png"
        attribute eyes_d:
            s_paths + "/base/eyes/eyes_d.png"
        attribute eyes_e:
            s_paths + "/base/eyes/eyes_e.png"
        attribute eyes_f:
            s_paths + "/base/eyes/eyes_f.png"
        attribute eyes_g:
            s_paths + "/base/eyes/eyes_g.png"
        attribute eyes_h:
            s_paths + "/base/eyes/eyes_h.png"
        attribute eyes_i:
            s_paths + "/base/eyes/eyes_i.png"
        attribute eyes_j:
            s_paths + "/base/eyes/eyes_j.png"
        attribute eyes_k:
            s_paths + "/base/eyes/eyes_k.png"
        attribute eyes_l:
            s_paths + "/base/eyes/eyes_l.png"
        attribute eyes_m:
            s_paths + "/base/eyes/eyes_m.png"
        attribute eyes_n:
            s_paths + "/base/eyes/eyes_n.png"
        attribute eyes_o:
            s_paths + "/base/eyes/eyes_o.png"
        attribute eyes_p:
            s_paths + "/base/eyes/eyes_p.png"
        attribute eyes_q:
            s_paths + "/base/eyes/eyes_q.png"
        attribute eyes_r:
            s_paths + "/base/eyes/eyes_r.png"
        attribute eyes_s:
            s_paths + "/base/eyes/eyes_s.png"
        attribute eyes_t:
            s_paths + "/base/eyes/eyes_t.png"
        attribute eyes_u:
            s_paths + "/base/eyes/eyes_u.png"
    
    group eyebrows:
        ### Default Eyebrows
        attribute brow default if_any(["fine", "happy", "lightly_amazed", "flustered", "shocked", "neut","happ","lsur","flus","shoc"]):
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1a.png"
        attribute brow default if_any(["crying", "panicked", "yandere", "tense", "sad","cry","pani","yand","nerv"]):
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1b.png"
        attribute brow default if_any(["laughing", "very_amazed", "unease", "alluring", "laug","vsur","worr","sedu"]):
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1c.png"
        attribute brow default if_any(["annoyed", "anno","pout"]):
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1d.png"
        attribute brow default if_any(["angry", "angr","vang"]):
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1e.png"
        attribute brow default if_any(["curious", "doubtful", "curi","doub"]):
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1f.png"
        
        ### The following brows are for moods that differ between open and closed eyes:
        attribute brow default if_any(["aloof", "dist"]) if_all(["open_eyes"]) if_not(["closed_eyes", "ce"]):
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b2a.png"
        attribute brow default if_any(["aloof", "dist"]) if_all(["closed_eyes"]) if_not(["open_eyes", "oe"]):
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b3c.png"
        
        attribute brow default if_any(["aloof", "dist"]) if_all(["oe"]) if_not(["closed_eyes", "ce"]):
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b2a.png"
        attribute brow default if_any(["aloof", "dist"]) if_all(["ce"]) if_not(["open_eyes", "oe"]):
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b3c.png"
        
    # Eyebrows
    group eyebrows:
        attribute brow_a:
            s_paths + "/base/eyebrows/eyebrows_a.png"
        attribute brow_b:
            s_paths + "/base/eyebrows/eyebrows_b.png"
        attribute brow_c:
            s_paths + "/base/eyebrows/eyebrows_c.png"
        attribute brow_d:
            s_paths + "/base/eyebrows/eyebrows_d.png"
        attribute brow_e:
            s_paths + "/base/eyebrows/eyebrows_e.png"
        attribute brow_f:
            s_paths + "/base/eyebrows/eyebrows_f.png"
        attribute brow_g:
            s_paths + "/base/eyebrows/eyebrows_g.png"
        attribute brow_h:
            s_paths + "/base/eyebrows/eyebrows_h.png"
        attribute brow_i:
            s_paths + "/base/eyebrows/eyebrows_i.png"
        attribute brow_j if_any(["eyes_o","eyes_p","eyes_q","eyes_r","eyes_s"]):
            s_paths + "/base/eyebrows/eyebrows_j.png"
        attribute brow_k if_any(["eyes_o","eyes_p","eyes_q","eyes_r","eyes_s"]):
            s_paths + "/base/eyebrows/eyebrows_k.png"
        attribute brow_l if_any(["eyes_o","eyes_p","eyes_q","eyes_r","eyes_s"]):
            s_paths + "/base/eyebrows/eyebrows_l.png"
    
    #This group is intentionally last on this list, so it will render over top 
    # of every other thing on the face.
    group special:
        attribute s_scream:
            s_paths + "/base/special/special_scream.png"

    ## For use if NBE assets is installed
    # group blink:
    #     attribute blink_a default if_not(["eyes_o", "eyes_p", "eyes_q", "eyes_r", "eyes_s", "eyes_t", "eyes_e", "eyes_f"]):
    #         ConditionSwitch("persistent.enable_nbe", "_say_blink_a", True, "sprite_blank")
    #     attribute no_blink:
    #         "sprite_blank"

layeredimage sayori tap: 
    at Flatten

    always "mod_assets/MPT/sayori/sayori_tapping_facebase.png"

    group outfit:
        attribute uniform default null
        attribute casual null
    
    group mood:
        attribute tense default null
        attribute angry null 
        attribute aloof null 
        attribute fine null 

        attribute nerv default null #nervous
        attribute angr null #angry
        attribute dist null #distant
        attribute neut null #neutral
        attribute pout null #pouting

    group blush: #Have to separate these out, they can't share moods.
        attribute no_blush default null
        attribute awkward null 
        attribute blushing null 
        attribute awkward_blushing null 
        attribute full_face_blush null 

        attribute nobl default null #no blush applied.
        attribute awkw null #awkward.  defaults for n
        attribute blus null #blushing.  defaults for n
        attribute blaw null #blushing AND awkward.  defaults for n
        attribute bful null #full face blush.
    
    group body:
        attribute uniform default if_any(["uniform"]):
            "mod_assets/MPT/sayori/sayori_tapping_uniform_bodybase.png"
        attribute casual default if_any(["casual"]):
            "mod_assets/MPT/sayori/sayori_tapping_casual_bodybase.png"

    group nose:
        ### Default nose
        attribute nose default if_any(["no_blush", "nobl"]): #default nose
            "mod_assets/MPT/sayori/sayori_tapping_nose_n1.png"
        attribute nose default if_any(["awkward", "awkw"]): #default nose when "awkward"
            "mod_assets/MPT/sayori/sayori_tapping_nose_n2.png"
        attribute nose default if_any(["blushing", "blus"]): #default nose when "blushing"
            "mod_assets/MPT/sayori/sayori_tapping_nose_n3.png"
        attribute nose default if_any(["awkward_blushing", "blaw"]): #default nose when "blushing" and "awkward"
            "mod_assets/MPT/sayori/sayori_tapping_nose_n4.png"
        attribute nose default if_any(["full_face_blush", "bful"]): #default nose when "blushing" and "awkward"
            "mod_assets/MPT/sayori/sayori_tapping_nose_n5.png"
        
        ### All noses
        ### Simple Syntax
        attribute nose1:
            "mod_assets/MPT/sayori/sayori_tapping_nose_n1.png"
        attribute nose2:
            "mod_assets/MPT/sayori/sayori_tapping_nose_n2.png"
        attribute nose3:
            "mod_assets/MPT/sayori/sayori_tapping_nose_n3.png"
        attribute nose4:
            "mod_assets/MPT/sayori/sayori_tapping_nose_n4.png"
        attribute nose5:
            "mod_assets/MPT/sayori/sayori_tapping_nose_n5.png"

        ### Old MPT Syntax
        attribute n1:
            "mod_assets/MPT/sayori/sayori_tapping_nose_n1.png"
        attribute n2:
            "mod_assets/MPT/sayori/sayori_tapping_nose_n2.png"
        attribute n3:
            "mod_assets/MPT/sayori/sayori_tapping_nose_n3.png"
        attribute n4:
            "mod_assets/MPT/sayori/sayori_tapping_nose_n4.png"
        attribute n5:
            "mod_assets/MPT/sayori/sayori_tapping_nose_n5.png"
    
    group mouth:
        ### Closed Mouths
        attribute closed_mouth default if_any(["pout"]):
            "mod_assets/MPT/sayori/sayori_tapping_mouth_m2.png"
        attribute closed_mouth default if_any(["fine", "tense", "angry", "aloof", "neut","nerv","angr","dist"]):
            "mod_assets/MPT/sayori/sayori_tapping_mouth_m3.png"

        attribute cm default if_any(["pout"]):
            "mod_assets/MPT/sayori/sayori_tapping_mouth_m2.png"
        attribute cm default if_any(["fine", "tense", "angry", "aloof", "neut","nerv","angr","dist"]):
            "mod_assets/MPT/sayori/sayori_tapping_mouth_m3.png"
        
        ### Open Mouths
        attribute open_mouth if_any(["tense", "nerv"]):
            "mod_assets/MPT/sayori/sayori_tapping_mouth_m1.png"
        attribute open_mouth if_any(["fine", "angry", "aloof", "neut","pout","angr","dist"]):
            "mod_assets/MPT/sayori/sayori_tapping_mouth_m4.png"

        attribute om if_any(["tense", "nerv"]):
            "mod_assets/MPT/sayori/sayori_tapping_mouth_m1.png"
        attribute om if_any(["fine", "angry", "aloof", "neut","pout","angr","dist"]):
            "mod_assets/MPT/sayori/sayori_tapping_mouth_m4.png"
        
        ### All mouths
        ### Simple Syntax
        attribute mouth_a:
            "mod_assets/MPT/sayori/sayori_tapping_mouth_m1.png"
        attribute mouth_b:
            "mod_assets/MPT/sayori/sayori_tapping_mouth_m2.png"
        attribute mouth_c:
            "mod_assets/MPT/sayori/sayori_tapping_mouth_m3.png"
        attribute mouth_d:
            "mod_assets/MPT/sayori/sayori_tapping_mouth_m4.png"

        ### New MPT Syntax    
        attribute ma:
            "mod_assets/MPT/sayori/sayori_tapping_mouth_m1.png"
        attribute mb:
            "mod_assets/MPT/sayori/sayori_tapping_mouth_m2.png"
        attribute mc:
            "mod_assets/MPT/sayori/sayori_tapping_mouth_m3.png"
        attribute md:
            "mod_assets/MPT/sayori/sayori_tapping_mouth_m4.png"

        ### Old MPT Syntax
        attribute m1:
            "mod_assets/MPT/sayori/sayori_tapping_mouth_m1.png"
        attribute m2:
            "mod_assets/MPT/sayori/sayori_tapping_mouth_m2.png"
        attribute m3:
            "mod_assets/MPT/sayori/sayori_tapping_mouth_m3.png"
        attribute m4:
            "mod_assets/MPT/sayori/sayori_tapping_mouth_m4.png"
    
    group eyes if_not(["nose5", "full_face_blush", "n5","bful"]):
        ### Open eyes
        attribute open_eyes default if_any(["fine", "tense", "neut","nerv"]):
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e1.png"
        attribute open_eyes default if_any(["aloof", "pout","dist"]):
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e2.png"
        attribute open_eyes default if_any(["angry", "angr"]):
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e5.png"

        attribute oe default if_any(["fine", "tense", "neut","nerv"]):
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e1.png"
        attribute oe default if_any(["aloof", "pout","dist"]):
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e2.png"
        attribute oe default if_any(["angry", "angr"]):
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e5.png"
        
        ### Closed eyes
        attribute closed_eyes if_any(["fine", "tense", "angry", "aloof", "neut","nerv","pout","angr","dist"]):
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e6.png"

        attribute ce if_any(["fine", "tense", "angry", "aloof", "neut","nerv","pout","angr","dist"]):
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e6.png"
        
        ### All eyes
        ### Simple Syntax
        attribute eyes_a:
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e1.png"
        attribute eyes_b:
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e2.png"
        attribute eyes_c:
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e3.png"
        attribute eyes_d:
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e4.png"
        attribute eyes_e:
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e5.png"
        attribute eyes_f:
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e6.png"

        ### New MPT Syntax
        attribute ea:
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e1.png"
        attribute eb:
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e2.png"
        attribute ec:
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e3.png"
        attribute ed:
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e4.png"
        attribute ee:
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e5.png"
        attribute ef:
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e6.png"

        ### Old MPT Syntax
        attribute e1:
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e1.png"
        attribute e2:
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e2.png"
        attribute e3:
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e3.png"
        attribute e4:
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e4.png"
        attribute e5:
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e5.png"
        attribute e6:
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e6.png"
    
    group eyebrows if_not(["nose5", "full_face_blush", "n5","bful"]):
        ### Default Eyebrows
        attribute brow default if_any(["fine", "neut"]):
            "mod_assets/MPT/sayori/sayori_tapping_eyebrows_b3.png"
        attribute brow default if_any(["tense", "aloof", "nerv","dist"]):
            "mod_assets/MPT/sayori/sayori_tapping_eyebrows_b1.png"
        attribute brow default if_any(["angry", "pout","angr"]):
            "mod_assets/MPT/sayori/sayori_tapping_eyebrows_b2.png"
        
        ### All eyebrows
        ### Simple Syntax
        attribute brow_a:
            "mod_assets/MPT/sayori/sayori_tapping_eyebrows_b1.png"
        attribute brow_b:
            "mod_assets/MPT/sayori/sayori_tapping_eyebrows_b2.png"
        attribute brow_c:
            "mod_assets/MPT/sayori/sayori_tapping_eyebrows_b3.png"

        ### New MPT Syntax
        attribute ba:
            "mod_assets/MPT/sayori/sayori_tapping_eyebrows_b1.png"
        attribute bb:
            "mod_assets/MPT/sayori/sayori_tapping_eyebrows_b2.png"
        attribute bc:
            "mod_assets/MPT/sayori/sayori_tapping_eyebrows_b3.png"

        ### Old MPT Syntax
        attribute b1:
            "mod_assets/MPT/sayori/sayori_tapping_eyebrows_b1.png"
        attribute b2:
            "mod_assets/MPT/sayori/sayori_tapping_eyebrows_b2.png"
        attribute b3:
            "mod_assets/MPT/sayori/sayori_tapping_eyebrows_b3.png"
    
    ## For use if NBE assets is installed
    # group blink:
    #     attribute blink_a default if_not(["closed_eyes", "ef", "eyes_f", "nose5", "full_face_blush", "ce","e6","n5","bful"]):
    #         ConditionSwitch("persistent.enable_nbe", "_say_blink_t_a", True, "sprite_blank")
    #     attribute no_blink:
    #         "sprite_blank"

image _say_blink_a:
    alpha 0.0
    renpy.random.randint(20, 100)*0.1
    choice:
        alpha 1.0
        "mod_assets/MPT/sayori/_blink_am.png"
        0.015
        "mod_assets/MPT/sayori/_blink_af.png"
        0.035
        "mod_assets/MPT/sayori/_blink_am.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/sayori/_blink_am.png"
        0.015
        "mod_assets/MPT/sayori/_blink_af.png"
        0.065
        "mod_assets/MPT/sayori/_blink_am.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/sayori/_blink_am.png"
        0.015
        "mod_assets/MPT/sayori/_blink_af.png"
        0.095
        "mod_assets/MPT/sayori/_blink_am.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/sayori/_blink_am.png"
        0.015
        "mod_assets/MPT/sayori/_blink_af.png"
        0.035
        "mod_assets/MPT/sayori/_blink_am.png"
        0.015
        alpha 0.0
        0.15
        alpha 1.0
        "mod_assets/MPT/sayori/_blink_am.png"
        0.015
        "mod_assets/MPT/sayori/_blink_af.png"
        0.035
        "mod_assets/MPT/sayori/_blink_am.png"
        0.015
    repeat

image _say_blink_t_a:
    alpha 0.0
    renpy.random.randint(30, 60)*0.1
    choice:
        alpha 1.0
        "mod_assets/MPT/sayori/_blink_t_am.png"
        0.015
        "mod_assets/MPT/sayori/_blink_t_af.png"
        0.035
        "mod_assets/MPT/sayori/_blink_t_am.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/sayori/_blink_t_am.png"
        0.015
        "mod_assets/MPT/sayori/_blink_t_af.png"
        0.065
        "mod_assets/MPT/sayori/_blink_t_am.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/sayori/_blink_t_am.png"
        0.015
        "mod_assets/MPT/sayori/_blink_t_af.png"
        0.095
        "mod_assets/MPT/sayori/_blink_t_am.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/sayori/_blink_t_am.png"
        0.015
        "mod_assets/MPT/sayori/_blink_t_af.png"
        0.035
        "mod_assets/MPT/sayori/_blink_t_am.png"
        0.015
        alpha 0.0
        0.15
        alpha 1.0
        "mod_assets/MPT/sayori/_blink_t_am.png"
        0.015
        "mod_assets/MPT/sayori/_blink_t_af.png"
        0.035
        "mod_assets/MPT/sayori/_blink_t_am.png"
        0.015
    repeat
