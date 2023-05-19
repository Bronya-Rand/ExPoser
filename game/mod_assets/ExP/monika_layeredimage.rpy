
init python:
    from store import exp_core
    m_paths = exp_core.ExPPaths("mod_assets/ExP/monika")

layeredimage monika base:
    at Flatten
    
    # Since this tends to be just one asset, just put it in the base dir.
    always m_paths + "/facebase.png"
    
    # Outfits. Might consider changing this as a 1 outfit file
    group outfit:
        attribute uniform null
        attribute casual null
    
    # (Formerly Blush) Cheek Expressions
    group cheek: 
        attribute norm default null # Normal
        attribute eh null # Awkward/Eh.
        attribute shy null # Blushing (shy used as synomyn)
        attribute shyeh null # Both Shy and Awkward
    
    # Left Half
    group left:
        anchor (0,0)
        subpixel True
        attribute ldown default if_any(["uniform"]):
            m_paths + "/base/body/uniform_ldown.png"
        attribute ldown default if_any(["casual"]):
            m_paths + "/base/body/casual_ldown.png"
        attribute lpoint if_any(["uniform"]):
            m_paths + "/base/body/uniform_lpoint.png"
        attribute lpoint if_any(["casual"]):
            m_paths + "/base/body/casual_lpoint.png"
    
    # Right Half
    group right:
        anchor (0,0)
        subpixel True
        attribute rdown default if_any(["uniform"]):
            m_paths + "/base/body/uniform_rdown.png"
        attribute rdown default if_any(["casual"]):
            m_paths + "/base/body/casual_rdown.png"
        attribute rhip if_any(["uniform"]):
            m_paths + "/base/body/uniform_rhip.png"
        attribute rhip if_any(["casual"]):
            m_paths + "/base/body/casual_rhip.png"
    
    # Nose
    group nose:
        attribute nose default if_any(["norm"]): # default nose
            m_paths + "/base/noses/nose1.png"
        attribute nose default if_any(["eh"]): # default nose when "awkward"
            m_paths + "/base/noses/nose2.png"
        attribute nose default if_any(["shy"]): # default nose when "blushing"
            m_paths + "/base/noses/nose3.png"
        attribute nose default if_any(["shyeh"]): # default nose when "blushing and awkward"
            m_paths + "/base/noses/nose4.png"
        
        attribute nose1:
            m_paths + "/base/noses/nose1.png"
        attribute nose2:
            m_paths + "/base/noses/nose2.png"
        attribute nose3:
            m_paths + "/base/noses/nose3.png"
        attribute nose4:
            m_paths + "/base/noses/nose4.png"
    
    # Mouth
    group mouth:
        attribute mouth_a:
            m_paths + "/base/mouth/mouth_a.png"
        attribute mouth_b:
            m_paths + "/base/mouth/mouth_b.png"
        attribute mouth_c:
            m_paths + "/base/mouth/mouth_c.png"
        attribute mouth_d:
            m_paths + "/base/mouth/mouth_d.png"
        attribute mouth_e:
            m_paths + "/base/mouth/mouth_e.png"
        attribute mouth_f:
            m_paths + "/base/mouth/mouth_f.png"
        attribute mouth_g:
            m_paths + "/base/mouth/mouth_g.png"
        attribute mouth_h:
            m_paths + "/base/mouth/mouth_h.png"
        attribute mouth_i:
            m_paths + "/base/mouth/mouth_i.png"
        attribute mouth_j:
            m_paths + "/base/mouth/mouth_j.png"
        attribute mouth_k:
            m_paths + "/base/mouth/mouth_k.png"
        attribute mouth_l:
            m_paths + "/base/mouth/mouth_l.png"
        attribute mouth_:
            m_paths + "/base/mouth/mouth_m.png"
        attribute mouth_n:
            m_paths + "/base/mouth/mouth_n.png"
        attribute mouth_o:
            m_paths + "/base/mouth/mouth_o.png"
        attribute mouth_p:
            m_paths + "/base/mouth/mouth_p.png"
        attribute mouth_q:
            m_paths + "/base/mouth/mouth_q.png"
        attribute mouth_r:
            m_paths + "/base/mouth/mouth_r.png"

    # Eyes
    group eyes:
        attribute eyes_a:
            m_paths + "/base/eyes/eyes_a.png"
        attribute eyes_b:
            m_paths + "/base/eyes/eyes_b.png"
        attribute eyes_c:
            m_paths + "/base/eyes/eyes_c.png"
        attribute eyes_d:
            m_paths + "/base/eyes/eyes_d.png"
        attribute eyes_e:
            m_paths + "/base/eyes/eyes_e.png"
        attribute eyes_f:
            m_paths + "/base/eyes/eyes_f.png"
        attribute eyes_g:
            m_paths + "/base/eyes/eyes_g.png"
        attribute eyes_h:
            m_paths + "/base/eyes/eyes_h.png"
        attribute eyes_i:
            m_paths + "/base/eyes/eyes_i.png"
        attribute eyes_j:
            m_paths + "/base/eyes/eyes_j.png"
        attribute eyes_k:
            m_paths + "/base/eyes/eyes_k.png"
        attribute eyes_l:
            m_paths + "/base/eyes/eyes_l.png"
        attribute eyes_m:
            m_paths + "/base/eyes/eyes_m.png"
        attribute eyes_n:
            m_paths + "/base/eyes/eyes_n.png"
        attribute eyes_o:
            m_paths + "/base/eyes/eyes_o.png"
        attribute eyes_p:
            m_paths + "/base/eyes/eyes_p.png"
        attribute eyes_q:
            m_paths + "/base/eyes/eyes_q.png"
        attribute eyes_r:
            m_paths + "/base/eyes/eyes_r.png"
        attribute eyes_s:
            m_paths + "/base/eyes/eyes_s.png"
        attribute eyes_t:
            m_paths + "/base/eyes/eyes_t.png"
        attribute eyes_u:
            m_paths + "/base/eyes/eyes_u.png"

    # Eyebrows
    group eyebrows:
        attribute brow_a:
            m_paths + "/base/eyebrows/eyebrows_a.png"
        attribute brow_b:
            m_paths + "/base/eyebrows/eyebrows_b.png"
        attribute brow_c:
            m_paths + "/base/eyebrows/eyebrows_c.png"
        attribute brow_d:
            m_paths + "/base/eyebrows/eyebrows_d.png"
        attribute brow_e:
            m_paths + "/base/eyebrows/eyebrows_e.png"
        attribute brow_f:
            m_paths + "/base/eyebrows/eyebrows_f.png"
        attribute brow_g:
            m_paths + "/base/eyebrows/eyebrows_g.png"
        attribute brow_h:
            m_paths + "/base/eyebrows/eyebrows_h.png"
        attribute brow_i:
            m_paths + "/base/eyebrows/eyebrows_i.png"
        attribute brow_j if_any(["eyes_o","eyes_p","eyes_q","eyes_r","eyes_s"]):
            m_paths + "/base/eyebrows/eyebrows_j.png"
        attribute brow_k if_any(["eyes_o","eyes_p","eyes_q","eyes_r","eyes_s"]):
            m_paths + "/base/eyebrows/eyebrows_k.png"
        attribute brow_l if_any(["eyes_o","eyes_p","eyes_q","eyes_r","eyes_s"]):
            m_paths + "/base/eyebrows/eyebrows_l.png"

    # This group is intentionally last on this list, so it will render over top 
    # of every other thing on the face.
    group special:
        attribute s_scream:
            m_paths + "/base/special/special_scream.png"
    
    ## Uncomment if wanting to use NBE assets.
    # group blink:
    #     attribute blink_a default if_not(["eyes_o", "eyes_p", "eyes_q", "eyes_r", "eyes_s", "eyes_t", "eyes_e", "eyes_f"]):
    #         ConditionSwitch("persistent.enable_nbe", "_mon_blink_a", True, "sprite_blank")
    #     attribute no_blink:
    #         "sprite_blank"

layeredimage monika lean:
    at Flatten

    group outfit:
        attribute uniform default null
        attribute casual null
    
    group cheek:
        attribute norm default null # Normal
        attribute eh null # Awkward/Eh.
        attribute shy null # Blushing (shy used as synomyn)
        attribute shyeh null # Both Shy and Awkward
        attribute vshy null # full face blush.
    
    group body:
        attribute body default if_any(["uniform"]):
            m_paths + "/lean/body/uniform_body.png"
        attribute body default if_any(["casual"]):
            m_paths + "/lean/body/casual_body.png"
    
    group head:
        attribute head default if_any(["uniform"]):
            m_paths + "/lean/head/uniform_face.png"
        attribute head default if_any(["casual"]):
            m_paths + "/lean/head/casual_face.png"

    group nose:
        attribute nose default if_any(["norm"]): #default nose
            m_paths + "/lean/nose/nose1.png"
        attribute nose default if_any(["eh"]): #default nose when "awkward"
            m_paths + "/lean/nose/nose2.png"
        attribute nose default if_any(["shy"]): #default nose when "blushing"
            m_paths + "/lean/nose/nose3.png"
        attribute nose default if_any(["shyeh"]): #default nose when both "blushing" and "awkward"
            m_paths + "/lean/nose/nose4.png"
        attribute nose default if_any(["vshy"]): #full face blush, obscures eyes/eyebrows.
            m_paths + "/lean/nose/nose5.png"

        attribute nose1:
            m_paths + "/lean/nose/nose1.png"
        attribute nose2:
            m_paths + "/lean/nose/nose2.png"
        attribute nose3:
            m_paths + "/lean/nose/nose3.png"
        attribute nose4:
            m_paths + "/lean/nose/nose4.png"
        attribute nose5:
            m_paths + "/lean/nose/nose5.png"
    
    group mouth:
        attribute mouth_a:
            m_paths + "/lean/mouth/mouth_a.png"
        attribute mouth_b:
            m_paths + "/lean/mouth/mouth_b.png"
        attribute mouth_c:
            m_paths + "/lean/mouth/mouth_c.png"
        attribute mouth_d:
            m_paths + "/lean/mouth/mouth_d.png"
    
    group eyes if_not(["nose5", "vshy"]): #Cannot show if full-face blush is present.
        attribute eyes_a:
            m_paths + "/lean/eyes/eyes_a.png"
        attribute eyes_b:
            m_paths + "/lean/eyes/eyes_b.png"
        attribute eyes_c:
            m_paths + "/lean/eyes/eyes_c.png"
        attribute eyes_d:
            m_paths + "/lean/eyes/eyes_d.png"
        attribute eyes_e:
            m_paths + "/lean/eyes/eyes_e.png"
        attribute eyes_f:
            m_paths + "/lean/eyes/eyes_f.png"
    
    group eyebrows if_not(["nose5", "vshy"]): #Cannot show if full-face blush is present.
        attribute brow_a:
            m_paths + "/lean/eyebrows/eyebrows_a.png"
        attribute brow_b:
            m_paths + "/lean/eyebrows/eyebrows_b.png"
        attribute brow_c:
            m_paths + "/lean/eyebrows/eyebrows_c.png"

    ## For use if NBE assets is installed
    # group blink:
    #     attribute blink_a default if_not(["eyes_d", "eyes_e", "nose5", "vshy"]):
    #         ConditionSwitch("persistent.enable_nbe", "_mon_blink_l_a", True, "sprite_blank")
    #     attribute no_blink:
    #         "sprite_blank"
