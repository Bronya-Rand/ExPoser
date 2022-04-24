
layeredimage natsuki base:
    at Flatten
    
    group outfit:
        attribute uniform default null
        attribute casual null
    
    group mood:
        attribute fine default null
        attribute angry null 
        attribute annoyed null 
        attribute crying null
        attribute curious null 
        attribute aloof null 
        attribute doubtful null 
        attribute flustered null
        attribute happy null
        attribute laughing null
        attribute lightly_amazed null 
        attribute tense null
        attribute panicked null 
        attribute sad null
        attribute alluring null 
        attribute shocked null
        attribute very_angry null
        attribute very_amazed null 
        attribute unease null
        attribute yandere null

        # Backwards Compatiblility (Old Syntax)
        attribute neut default null #neutral
        attribute angr null #angry
        attribute anno null #annoyed
        attribute cry null  #crying
        attribute curi null #curious
        attribute dist null #distant
        attribute doub null #doubtful
        attribute flus null #flustered
        attribute happ null #happy
        attribute laug null #laughing
        attribute lsur null #surprised (lightly)
        attribute nerv null #nervous
        attribute pani null #panicked
        attribute pout null #pouting
        attribute sad null  #sad
        attribute sedu null #seductive
        attribute shoc null #shocked
        attribute vang null #VERY angry
        attribute vsur null #surprised (very)
        attribute worr null #worried
        attribute yand null #yandere

    group blush: 
        attribute no_blush default null
        attribute awkward null 
        attribute blushing null 
        attribute awkward_blushing null
        attribute full_face_blush null

        attribute nobl default null #no blush or tear drop.
        attribute awkw null #awkward.  defaults for n
        attribute blus null #blushing.  defaults for n
        attribute blaw null #blushing AND awkward.  defaults for n
        attribute bful null #full face blush.  Currently only works on the side face.
    
    group left: 
        attribute ldown default if_any(["uniform"]):
            "mod_assets/MPT/natsuki/natsuki_turned_uniform_left_down.png"
        attribute ldown default if_any(["casual"]):
            "mod_assets/MPT/natsuki/natsuki_turned_casual_left_down.png"
        attribute lhip if_any(["uniform"]):
            "mod_assets/MPT/natsuki/natsuki_turned_uniform_left_hip.png"
        attribute lhip if_any(["casual"]):
            "mod_assets/MPT/natsuki/natsuki_turned_casual_left_hip.png"
        attribute lpoint if_any(["uniform"]):
            "mod_assets/MPT/natsuki/natsuki_turned_uniform_left_point.png"
        attribute lpoint if_any(["casual"]):
            "mod_assets/MPT/natsuki/natsuki_turned_casual_left_point.png"
    
    group right:
        attribute rdown default if_any(["uniform"]):
            "mod_assets/MPT/natsuki/natsuki_turned_uniform_right_down.png"
        attribute rdown default if_any(["casual"]):
            "mod_assets/MPT/natsuki/natsuki_turned_casual_right_down.png"
        attribute rhip if_any(["uniform"]):
            "mod_assets/MPT/natsuki/natsuki_turned_uniform_right_hip.png"
        attribute rhip if_any(["casual"]):
            "mod_assets/MPT/natsuki/natsuki_turned_casual_right_hip.png"
    
    # This needs to render above her body for her "turned" pose.
    group head:
        ## Simple Syntax
        attribute face_forward default:
            "mod_assets/MPT/natsuki/natsuki_face_forward.png"
        attribute sad_face:
            "mod_assets/MPT/natsuki/natsuki_face_sad.png"
        attribute turned_away_face:
            "mod_assets/MPT/natsuki/natsuki_face_turnedaway.png"

        ## Old MPT Syntax
        attribute ff default:
            "mod_assets/MPT/natsuki/natsuki_face_forward.png"
        attribute fs:
            "mod_assets/MPT/natsuki/natsuki_face_sad.png"
        attribute fta:
            "mod_assets/MPT/natsuki/natsuki_face_turnedaway.png"
    
    
    
    # First set of definitions is for Natsuki's "Forward" face
    group nose if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
        ### Default nose
        attribute nose default if_any(["no_blush", "nobl"]):
            "mod_assets/MPT/natsuki/natsuki_ff_nose_n1.png"
        attribute nose if_any(["awkward", "awkw"]):
            "mod_assets/MPT/natsuki/natsuki_ff_nose_n2.png"
        attribute nose if_any(["blushing", "blus"]):
            "mod_assets/MPT/natsuki/natsuki_ff_nose_n3.png"
        attribute nose if_any(["awkward_blushing", "blaw"]):
            "mod_assets/MPT/natsuki/natsuki_ff_nose_n4.png"

        ### All noses
        ### Simple Syntax
        attribute nose1:
            "mod_assets/MPT/natsuki/natsuki_ff_nose_n1.png"
        attribute nose2:
            "mod_assets/MPT/natsuki/natsuki_ff_nose_n2.png"
        attribute nose3:
            "mod_assets/MPT/natsuki/natsuki_ff_nose_n3.png"
        attribute nose4:
            "mod_assets/MPT/natsuki/natsuki_ff_nose_n4.png"

        ### Old MPT Syntax
        attribute n1:
            "mod_assets/MPT/natsuki/natsuki_ff_nose_n1.png"
        attribute n2:
            "mod_assets/MPT/natsuki/natsuki_ff_nose_n2.png"
        attribute n3:
            "mod_assets/MPT/natsuki/natsuki_ff_nose_n3.png"
        attribute n4:
            "mod_assets/MPT/natsuki/natsuki_ff_nose_n4.png"
    
    group mouth if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
        ### Closed Mouths
        attribute closed_mouth default if_any(["happy", "alluring", "tense", "happ","sedu","nerv"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_ma.png"
        attribute closed_mouth default if_any(["fine", "annoyed", "unease", "lightly_amazed", "neut","anno","worr","lsur"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_md.png"
        attribute closed_mouth default if_any(["curious", "pout","curi"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_me.png"
        attribute closed_mouth default if_any(["flustered", "shocked", "flus","shoc"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mg.png"
        attribute closed_mouth default if_any(["angry", "very_amazed", "aloof", "doubtful", "sad","angr","vsur","dist","doub"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mj.png"
        attribute closed_mouth default if_any(["very_angry", "panicked", "crying", "vang","pani","cry"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mm.png"
        attribute closed_mouth default if_any(["yandere", "yand"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mn.png"
        attribute closed_mouth default if_any(["laughing", "laug"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mo.png"

        attribute cm default if_any(["happy", "alluring", "tense", "happ","sedu","nerv"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_ma.png"
        attribute cm default if_any(["fine", "annoyed", "unease", "lightly_amazed", "neut","anno","worr","lsur"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_md.png"
        attribute cm default if_any(["curious", "pout","curi"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_me.png"
        attribute cm default if_any(["flustered", "shocked", "flus","shoc"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mg.png"
        attribute cm default if_any(["angry", "very_amazed", "aloof", "doubtful", "sad","angr","vsur","dist","doub"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mj.png"
        attribute cm default if_any(["very_angry", "panicked", "crying", "vang","pani","cry"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mm.png"
        attribute cm default if_any(["yandere", "yand"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mn.png"
        attribute cm default if_any(["laughing", "laug"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mo.png"
        
        ### Open Mouths
        attribute open_mouth if_any(["alluring", "tense", "yandere", "sedu","nerv","yand"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mb.png"
        attribute open_mouth if_any(["happy", "laughing", "happ","laug"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mc.png"
        attribute open_mouth if_any(["annoying", "unease", "lightly_amazed", "aloof", "sad","anno","worr","lsur","dist","pout"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mg.png"
        attribute open_mouth if_any(["fine", "curious", "neut","curi"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mh.png"
        attribute open_mouth if_any(["doubtful", "angry", "very_amazed", "doub","angr","vsur"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mi.png"
        attribute open_mouth if_any(["flustered", "shocked", "flus","shoc"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_ml.png"
        attribute open_mouth if_any(["crying", "very_angry", "panicked", "cry","vang","pani"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mq.png"

        attribute om if_any(["alluring", "tense", "yandere", "sedu","nerv","yand"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mb.png"
        attribute om if_any(["happy", "laughing", "happ","laug"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mc.png"
        attribute om if_any(["annoying", "unease", "lightly_amazed", "aloof", "sad","anno","worr","lsur","dist","pout"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mg.png"
        attribute om if_any(["fine", "curious", "neut","curi"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mh.png"
        attribute om if_any(["doubtful", "angry", "very_amazed", "doub","angr","vsur"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mi.png"
        attribute om if_any(["flustered", "shocked", "flus","shoc"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_ml.png"
        attribute om if_any(["crying", "very_angry", "panicked", "cry","vang","pani"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mq.png"
        
        ### All mouths
        ### Simple Syntax
        attribute mouth_a:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_ma.png"
        attribute mouth_b:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mb.png"
        attribute mouth_c:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mc.png"
        attribute mouth_d:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_md.png"
        attribute mouth_e:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_me.png"
        attribute mouth_f:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mf.png"
        attribute mouth_g:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mg.png"
        attribute mouth_h:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mh.png"
        attribute mouth_i:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mi.png"
        attribute mouth_j:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mj.png"
        attribute mouth_k:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mk.png"
        attribute mouth_l:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_ml.png"
        attribute mouth_m:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mm.png"
        attribute mouth_n:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mn.png"
        attribute mouth_o:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mo.png"
        attribute mouth_p:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mp.png"
        attribute mouth_q:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mq.png"
        attribute mouth_r:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mr.png"

        ### Old MPT Syntax
        attribute ma:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_ma.png"
        attribute mb:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mb.png"
        attribute mc:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mc.png"
        attribute md:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_md.png"
        attribute me:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_me.png"
        attribute mf:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mf.png"
        attribute mg:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mg.png"
        attribute mh:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mh.png"
        attribute mi:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mi.png"
        attribute mj:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mj.png"
        attribute mk:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mk.png"
        attribute ml:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_ml.png"
        attribute mm:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mm.png"
        attribute mn:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mn.png"
        attribute mo:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mo.png"
        attribute mp:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mp.png"
        attribute mq:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mq.png"
        attribute mr:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mr.png"
    
    group eyes if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
        ### Opened eyes
        attribute open_eyes default if_any(["fine", "happy", "laughing", "curious", "neut","happ","laug","pout","curi"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1a.png"
        attribute open_eyes default if_any(["unease", "flustered", "aloof", "sad","worr","flus","dist"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1b.png"
        attribute open_eyes default if_any(["annoyed", "allured", "doubtful", "anno","sedu","doub"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1d.png"
        attribute open_eyes default if_any(["crying", "cry"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1g.png"
        attribute open_eyes default if_any(["angry", "lightly_amazed", "tense", "angr","lsur","nerv"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2a.png"
        attribute open_eyes default if_any(["very_angry", "very_amazed", "panicked", "shocked", "vang","vsur","pani","shoc"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2d.png"
        attribute open_eyes default if_any(["yandere", "yand"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e3a.png"

        attribute oe default if_any(["fine", "happy", "laughing", "curious", "neut","happ","laug","pout","curi"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1a.png"
        attribute oe default if_any(["unease", "flustered", "aloof", "sad","worr","flus","dist"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1b.png"
        attribute oe default if_any(["annoyed", "allured", "doubtful", "anno","sedu","doub"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1d.png"
        attribute oe default if_any(["crying", "cry"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1g.png"
        attribute oe default if_any(["angry", "lightly_amazed", "tense", "angr","lsur","nerv"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2a.png"
        attribute oe default if_any(["very_angry", "very_amazed", "panicked", "shocked", "vang","vsur","pani","shoc"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2d.png"
        attribute oe default if_any(["yandere", "yand"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e3a.png"
        
        ### Closed eyes
        attribute closed_eyes if_any(["unease", "annoyed", "angry", "very_angry", "very_amazed", "flustered", "aloof", "tense", "doubtful", "sad","worr","anno","angr","vang","vsur","flus","dist","sedu","nerv","doub"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4a.png"
        attribute closed_eyes if_any(["fine", "happy", "laughing", "lightly_amazed", "yandere", "curious", "neut","happ","laug","lsur","yand","pout","curi"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4b.png"
        attribute closed_eyes if_any(["shocked", "panicked", "shoc","pani"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4c.png"
        attribute closed_eyes if_any(["crying", "cry"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4e.png"

        attribute ce if_any(["unease", "annoyed", "angry", "very_angry", "very_amazed", "flustered", "aloof", "tense", "doubtful", "sad","worr","anno","angr","vang","vsur","flus","dist","sedu","nerv","doub"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4a.png"
        attribute ce if_any(["fine", "happy", "laughing", "lightly_amazed", "yandere", "curious", "neut","happ","laug","lsur","yand","pout","curi"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4b.png"
        attribute ce if_any(["shocked", "panicked", "shoc","pani"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4c.png"
        attribute ce if_any(["crying", "cry"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4e.png"
        
        ### All eyes
        ## Simple Syntax
        attribute eyes_a:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1a.png"
        attribute eyes_b:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1b.png"
        attribute eyes_c:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1c.png"
        attribute eyes_d:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1d.png"
        attribute eyes_e:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1e.png"
        attribute eyes_f:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1f.png"
        attribute eyes_g:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1g.png"
        attribute eyes_h:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1h.png"
        attribute eyes_i:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2a.png"
        attribute eyes_j:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2b.png"
        attribute eyes_k:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2c.png"
        attribute eyes_l:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2d.png"
        attribute eyes_m:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e3a.png"
        attribute eyes_n:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e3b.png"
        attribute eyes_o:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4a.png"
        attribute eyes_p:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4b.png"
        attribute eyes_q:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4c.png"
        attribute eyes_r:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4d.png"
        attribute eyes_s:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4e.png"
        attribute eyes_t:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e0a.png"
        attribute eyes_u:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e0b.png"

        ### New MPT Syntax
        attribute ea:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1a.png"
        attribute eb:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1b.png"
        attribute ec:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1c.png"
        attribute ed:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1d.png"
        attribute ee:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1e.png"
        attribute ef:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1f.png"
        attribute eg:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1g.png"
        attribute eh:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1h.png"
        attribute ei:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2a.png"
        attribute ej:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2b.png"
        attribute ek:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2c.png"
        attribute el:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2d.png"
        attribute em:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e3a.png"
        attribute en:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e3b.png"
        attribute eo:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4a.png"
        attribute ep:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4b.png"
        attribute eq:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4c.png"
        attribute er:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4d.png"
        attribute es:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4e.png"
        attribute et:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e0a.png"
        attribute eu:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e0b.png"

        ### Old MPT Syntax
        attribute e1a:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1a.png"
        attribute e1b:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1b.png"
        attribute e1c:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1c.png"
        attribute e1d:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1d.png"
        attribute e1e:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1e.png"
        attribute e1f:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1f.png"
        attribute e1g:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1g.png"
        attribute e1h:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1h.png"
        attribute e2a:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2a.png"
        attribute e2b:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2b.png"
        attribute e2c:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2c.png"
        attribute e2d:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2d.png"
        attribute e3a:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e3a.png"
        attribute e3b:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e3b.png"
        attribute e4a:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4a.png"
        attribute e4b:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4b.png"
        attribute e4c:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4c.png"
        attribute e4d:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4d.png"
        attribute e4e:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4e.png"
        attribute e0a:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e0a.png"
        attribute e0b:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e0b.png"
    
    group eyebrows if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]): #eyebrows.
        #Default Eyebrows:
        attribute brow default if_any(["fine", "aloof", "allured", "neut","dist","sedu"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1a.png"
        attribute brow default if_any(["panicked", "flustered", "tense", "sad","pani","flus","pout","nerv"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1b.png"
        attribute brow default if_any(["happy", "unsure", "shocked", "happ","worr","shoc"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1c.png"
        attribute brow default if_any(["curious", "doubtful", "curi","doub"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1f.png"
        attribute brow default if_any(["lightly_amazed", "lsur"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b2a.png"
        attribute brow default if_any(["crying", "very_amazed", "cry","vsur"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b2c.png"
        
    # Some of Natsuki's eyebrows can only be used with closed eye expressions
    # the following moods take advantage of this, and thus need logic to check 
    # whether the eyes are open or not.
    # In case you're wondering why there's no if_all or if_not logic on this group 
    # line, it's because the attributes below explicitly use the same logic - and 
    # if you have a group and an attribute both using the same logic tag, the attribute 
    # one will COMPLETELY overwrite and ignore the group logic.  It took me way too long 
    # to figure this out.
    group eyebrows:
        attribute brow default if_any(["very_angry", "vang"]) if_all(["face_forward", "open_eyes"]) if_not(["turned_away_face", "sad_face", "closed_eyes", "fta","fs","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1d.png"
        attribute brow default if_any(["very_angry","vang"]) if_all(["closed_eyes", "face_forward"]) if_not(["turned_away_face", "sad_face", "open_eyes", "fta","fs","oe"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3a.png"
        attribute brow default if_any(["laughing", "laug"]) if_all(["face_forward", "open_eyes"]) if_not(["turned_away_face", "sad_face", "closed_eyes", "fta","fs","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1b.png"
        attribute brow default if_any(["laughing", "laug"]) if_all(["closed_eyes", "face_forward"]) if_not(["turned_away_face", "sad_face", "open_eyes", "fta","fs","oe"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3a.png"
        attribute brow default if_any(["yandere", "yand"]) if_all(["face_forward", "open_eyes"]) if_not(["turned_away_face", "sad_face", "closed_eyes", "fta","fs","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b2a.png"
        attribute brow default if_any(["yandere", "yand"]) if_all(["closed_eyes", "face_forward"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3c.png"
        attribute brow default if_any(["annoyed", "angry", "anno","angr"]) if_all(["face_forward", "open_eyes"]) if_not(["turned_away_face", "sad_face", "closed_eyes", "fta","fs","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1d.png"
        attribute brow default if_any(["annoyed", "angry", "anno","angr"]) if_all(["closed_eyes", "face_forward"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3b.png"

        attribute brow default if_any(["very_angry", "vang"]) if_all(["ff","oe"]) if_not(["turned_away_face", "sad_face", "closed_eyes", "fta","fs","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1d.png"
        attribute brow default if_any(["very_angry","vang"]) if_all(["ce","ff"]) if_not(["turned_away_face", "sad_face", "open_eyes", "fta","fs","oe"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3a.png"
        attribute brow default if_any(["laughing", "laug"]) if_all(["ff","oe"]) if_not(["turned_away_face", "sad_face", "closed_eyes", "fta","fs","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1b.png"
        attribute brow default if_any(["laughing", "laug"]) if_all(["ce","ff"]) if_not(["turned_away_face", "sad_face", "open_eyes", "fta","fs","oe"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3a.png"
        attribute brow default if_any(["yandere", "yand"]) if_all(["ff","oe"]) if_not(["turned_away_face", "sad_face", "closed_eyes", "fta","fs","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b2a.png"
        attribute brow default if_any(["yandere", "yand"]) if_all(["ce","ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3c.png"
        attribute brow default if_any(["annoyed", "angry", "anno","angr"]) if_all(["ff","oe"]) if_not(["turned_away_face", "sad_face", "closed_eyes", "fta","fs","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1d.png"
        attribute brow default if_any(["annoyed", "angry", "anno","angr"]) if_all(["ce","ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3b.png"
    
    group eyebrows:
        ## TODO: finish here to down below
        ###All eyebrows - truncated tags:
        attribute b1a if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1a.png"
        attribute b1b if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1b.png"
        attribute b1c if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs",]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1c.png"
        attribute b1d if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1d.png"
        attribute b1e if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1e.png"
        attribute b1f if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1f.png"
        attribute b2a if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b2a.png"
        attribute b2b if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b2b.png"
        attribute b2c if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b2c.png"
        attribute b3a if_all(["forward_face", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]) if_any(["eyes_o", "eo", "eyes_p", "ep", "eyes_q", "eq", "eyes_r", "er", "eyes_s", "es", "closed_eyes", "e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3a.png"
        attribute b3b if_all(["forward_face", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]) if_any(["eyes_o", "eo", "eyes_p", "ep", "eyes_q", "eq", "eyes_r", "er", "eyes_s", "es", "closed_eyes", "e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3b.png"
        attribute b3c if_all(["forward_face"]) if_not(["turned_away_face", "sad_face", "fta","fs"]) if_any(["eyes_o", "eo", "eyes_p", "ep", "eyes_q", "eq", "eyes_r", "er", "eyes_s", "es", "closed_eyes", "e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3c.png"
        #If the user tries to specifically use a closed-eyebrow variant with open eyes, we intentionally replace the eyebrow graphic in use with an appropriate - but not identical - replacement from the regular eyebrows:
        attribute b3a if_all(["forward_face"]) if_not(["turned_away_face", "sad_face", "eyes_o", "eo", "eyes_p", "ep", "eyes_q", "eq", "eyes_r", "er", "eyes_s", "es", "closed_eyes", "fta","fs","e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1e.png"
        attribute b3b if_all(["forward_face"]) if_not(["turned_away_face", "sad_face", "eyes_o", "eo", "eyes_p", "ep", "eyes_q", "eq", "eyes_r", "er", "eyes_s", "es", "closed_eyes", "fta","fs","e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1d.png"
        attribute b3c if_all(["forward_face"]) if_not(["turned_away_face", "sad_face", "eyes_o", "eo", "eyes_p", "ep", "eyes_q", "eq", "eyes_r", "er", "eyes_s", "es", "closed_eyes", "fta","fs","e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1c.png"

        attribute b3a if_all(["ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]) if_any(["eyes_o", "eo", "eyes_p", "ep", "eyes_q", "eq", "eyes_r", "er", "eyes_s", "es", "closed_eyes", "e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3a.png"
        attribute b3b if_all(["ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]) if_any(["eyes_o", "eo", "eyes_p", "ep", "eyes_q", "eq", "eyes_r", "er", "eyes_s", "es", "closed_eyes", "e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3b.png"
        attribute b3c if_all(["ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]) if_any(["eyes_o", "eo", "eyes_p", "ep", "eyes_q", "eq", "eyes_r", "er", "eyes_s", "es", "closed_eyes", "e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3c.png"
        #If the user tries to specifically use a closed-eyebrow variant with open eyes, we intentionally replace the eyebrow graphic in use with an appropriate - but not identical - replacement from the regular eyebrows:
        attribute b3a if_all(["ff"]) if_not(["turned_away_face", "sad_face", "eyes_o", "eo", "eyes_p", "ep", "eyes_q", "eq", "eyes_r", "er", "eyes_s", "es", "closed_eyes", "fta","fs","e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1e.png"
        attribute b3b if_all(["ff"]) if_not(["turned_away_face", "sad_face", "eyes_o", "eo", "eyes_p", "ep", "eyes_q", "eq", "eyes_r", "er", "eyes_s", "es", "closed_eyes", "fta","fs","e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1d.png"
        attribute b3c if_all(["ff"]) if_not(["turned_away_face", "sad_face", "eyes_o", "eo", "eyes_p", "ep", "eyes_q", "eq", "eyes_r", "er", "eyes_s", "es", "closed_eyes", "fta","fs","e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1c.png"
    
    #This group is intentionally last on this list, so it will render over top of every other thing on the face.
    group special if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
        attribute special_scream:
            "mod_assets/MPT/natsuki/natsuki_face_special_scream.png"
        
        attribute s_scream:
            "mod_assets/MPT/natsuki/natsuki_face_special_scream.png"
    
####################The "sad, turned away" face, and the few expressions it has.
    
    group nose if_any(["sad_face", "fs"]) if_not(["face_forward", "turned_away_face", "ff","fta"]):
        #Default nose/blush.
        attribute nose default if_any(["no_blush", "nobl"]):
            "mod_assets/MPT/natsuki/natsuki_fs_nose_n1.png"
        attribute nose default if_any(["awkward", "awkw"]):
            "mod_assets/MPT/natsuki/natsuki_fs_nose_n2.png"
        attribute nose default if_any(["blushing", "blus"]):
            "mod_assets/MPT/natsuki/natsuki_fs_nose_n3.png"
        attribute nose default if_any(["awkward_blushing", "blaw"]):
            "mod_assets/MPT/natsuki/natsuki_fs_nose_n4.png"
        attribute nose default if_any(["full_face_blush", "bful"]):
            "mod_assets/MPT/natsuki/natsuki_fs_nose_n5.png"
        
        #All noses
        attribute nose1:
            "mod_assets/MPT/natsuki/natsuki_fs_nose_n1.png"
        attribute nose2:
            "mod_assets/MPT/natsuki/natsuki_fs_nose_n2.png"
        attribute nose3:
            "mod_assets/MPT/natsuki/natsuki_fs_nose_n3.png"
        attribute nose4:
            "mod_assets/MPT/natsuki/natsuki_fs_nose_n4.png"
        attribute nose5:
            "mod_assets/MPT/natsuki/natsuki_fs_nose_n5.png"

        attribute n1:
            "mod_assets/MPT/natsuki/natsuki_fs_nose_n1.png"
        attribute n2:
            "mod_assets/MPT/natsuki/natsuki_fs_nose_n2.png"
        attribute n3:
            "mod_assets/MPT/natsuki/natsuki_fs_nose_n3.png"
        attribute n4:
            "mod_assets/MPT/natsuki/natsuki_fs_nose_n4.png"
        attribute n5:
            "mod_assets/MPT/natsuki/natsuki_fs_nose_n5.png"
    
    group mouth if_any(["sad_face", "fs"]) if_not(["face_forward", "turned_away_face", "ff","fta"]):
        #Closed mouths
        attribute closed_mouth default if_any(["fine", "neut"]):
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m1.png"
        attribute closed_mouth default if_any(["crying", "sad","cry"]):
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m2.png"

        attribute cm default if_any(["fine", "neut"]):
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m1.png"
        attribute cm default if_any(["crying", "sad","cry"]):
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m2.png"
        
        #Open mouths. Note that there's only one at this time.
        attribute open_mouth if_any(["crying", "fine", "sad","cry","neut"]):
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m3.png"

        attribute om if_any(["crying", "fine", "sad","cry","neut"]):
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m3.png"
        
        #All mouths
        attribute mouth_a:
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m1.png"
        attribute mouth_b:
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m2.png"
        attribute mouth_c:
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m3.png"
        attribute mouth_d:
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m4.png"

        attribute ma:
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m1.png"
        attribute mb:
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m2.png"
        attribute mc:
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m3.png"
        attribute md:
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m4.png"

        attribute m1:
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m1.png"
        attribute m2:
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m2.png"
        attribute m3:
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m3.png"
        attribute m4:
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m4.png"
    
    group eyes if_any(["sad_face", "fs"]) if_not(["face_forward", "turned_away_face", "nose5", "full_face_blush", "ff","fta","n5","bful"]): #Cannot show if full-face blush is present.
        #Open eyes
        attribute open_eyes default if_any(["fine", "neut"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e1.png"
        attribute open_eyes default if_any(["sad"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e2.png"
        attribute open_eyes default if_any(["crying", "cry"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e3.png"

        attribute oe default if_any(["neut"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e1.png"
        attribute oe default if_any(["sad"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e2.png"
        attribute oe default if_any(["crying", "cry"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e3.png"
        
        #Closed eyes
        attribute closed_eyes if_any(["fine", "neut"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e4.png"
        attribute closed_eyes if_any(["sad"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e5.png"
        attribute closed_eyes if_any(["crying", "cry"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e6.png"

        attribute ce if_any(["fine", "neut"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e4.png"
        attribute ce if_any(["sad"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e5.png"
        attribute ce if_any(["crying", "cry"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e6.png"
        
        ### All eyes
        attribute eyes_a:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e1.png"
        attribute eyes_b:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e2.png"
        attribute eyes_c:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e3.png"
        attribute eyes_d:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e4.png"
        attribute eyes_e:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e5.png"
        attribute eyes_f:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e6.png"

        attribute ea:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e1.png"
        attribute eb:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e2.png"
        attribute ec:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e3.png"
        attribute ed:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e4.png"
        attribute ee:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e5.png"
        attribute ef:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e6.png"

        attribute e1:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e1.png"
        attribute e2:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e2.png"
        attribute e3:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e3.png"
        attribute e4:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e4.png"
        attribute e5:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e5.png"
        attribute e6:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e6.png"
    
    group eyebrows if_any(["sad_face", "fs"]) if_not(["face_forward", "turned_away_face", "nose5", "full_face_blush", "ff","fta","n5","bful"]): #Cannot show if full-face blush is present.
        #default brows
        attribute brow default if_any(["fine", "neut"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyebrows_b1.png"
        attribute brow default if_any(["sad"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyebrows_b3.png"
    
    group eyebrows:#Required separate group definition because of additional logic for showing these particular eyebrows.
        attribute brow default if_any(["crying", "cry"]) if_all(["sad_face", "open_eyes"]) if_not(["face_forward", "turned_away_face", "nose5", "full_face_blush", "closed_eyes", "ff","fta","n5","bful","ce"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyebrows_b3.png"
        attribute brow default if_any(["crying", "cry"]) if_all(["sad_face", "closed_eyes"]) if_not(["face_forward", "turned_away_face", "nose5", "full_face_blush", "open_eyes", "ff","fta","n5","bful","oe"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyebrows_b2.png"
        
        attribute brow default if_any(["crying", "cry"]) if_all(["fs","oe"]) if_not(["face_forward", "turned_away_face", "nose5", "full_face_blush", "closed_eyes", "ff","fta","n5","bful","ce"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyebrows_b3.png"
        attribute brow default if_any(["crying", "cry"]) if_all(["fs","ce"]) if_not(["face_forward", "turned_away_face", "nose5", "full_face_blush", "open_eyes", "ff","fta","n5","bful","oe"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyebrows_b2.png"
    
    group eyebrows if_any(["sad_face", "fs"]) if_not(["face_forward", "turned_away_face", "nose5", "full_face_blush", "ff","fta","n5","bful"]): #Cannot show if full-face blush is present.
        #All eyebrows - truncated tags:
        attribute b1:
            "mod_assets/MPT/natsuki/natsuki_fs_eyebrows_b1.png"
        attribute b2:
            "mod_assets/MPT/natsuki/natsuki_fs_eyebrows_b2.png"
        attribute b3:
            "mod_assets/MPT/natsuki/natsuki_fs_eyebrows_b3.png"

    ## For use if NBE assets is installed
    # group blink if_any(["forward_face", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
    #     attribute blink_a default if_not(["closed_eyes", "eyes_o", "eo", "eyes_p", "ep", "eyes_q", "eq", "eyes_r", "er", "eyes_s", "es", "eyes_e", "ee", "eyes_f", "ef", "ce","e4a","e4b","e4c", "e4d", "e4e", "e1e", "e1f"]):
    #         "_nat_blink_a"
    #     attribute no_blink:
    #         "sprite_blank"

    # group blink if_any(["sad_face", "fs"]) if_not(["turned_away_face", "forward_face", "fta","ff"]):
    #     attribute blink_a default if_not(["closed_eyes", "ce", "eyes_d", "eyes_e", "eyes_f", "ed", "ee", "ef", "nose5", "full_face_blush", "e4","e5","e6","n5","bful"]):
    #         "_nat_blink_s_a"

layeredimage natsuki cross:
    at Flatten

    # Body definitions.  There are two variations on both types, since one of the 
    # bodies provided in the MPT specifically works better with the "fs" head than 
    # the other.
    always:
        "mod_assets/MPT/natsuki/natsuki_crossed(ff)_uniform.png" if_all(["uniform"]) if_any(["face_forward", "ff"])
    always:
        "mod_assets/MPT/natsuki/natsuki_crossed(fs)_uniform.png" if_all(["uniform"]) if_any(["sad_face", "fs" ])
    always:
        "mod_assets/MPT/natsuki/natsuki_crossed(ff)_casual.png" if_all(["casual"]) if_any(["face_forward", "ff"])
    always:
        "mod_assets/MPT/natsuki/natsuki_crossed(fs)_casual.png" if_all(["casual"]) if_any(["sad_face", "fs"])
    always:
        "mod_assets/MPT/natsuki/natsuki_crossed(fta)_uniform.png" if_all(["uniform"]) if_any(["turned_away_face", "fta"])
    always:
        "mod_assets/MPT/natsuki/natsuki_crossed(fta)_casual.png" if_all(["casual"]) if_any(["turned_away_face", "fta"])
    
    group outfit:
        attribute uniform default null
        attribute casual null
    
    group mood:
        attribute fine default null
        attribute angry null 
        attribute annoyed null 
        attribute crying null
        attribute curious null 
        attribute aloof null 
        attribute doubtful null 
        attribute flustered null
        attribute happy null
        attribute laughing null
        attribute lightly_amazed null 
        attribute tense null
        attribute panicked null 
        attribute sad null
        attribute alluring null 
        attribute shocked null
        attribute very_angry null
        attribute very_amazed null 
        attribute unease null
        attribute yandere null

        attribute neut default null #neutral
        attribute angr null #angry
        attribute anno null #annoyed
        attribute cry null  #crying
        attribute curi null #curious
        attribute dist null #distant
        attribute doub null #doubtful
        attribute flus null #flustered
        attribute happ null #happy
        attribute laug null #laughing
        attribute lsur null #surprised (lightly)
        attribute nerv null #nervous
        attribute pani null #panicked
        attribute pout null #pouting
        attribute sad null  #sad
        attribute sedu null #seductive
        attribute shoc null #shocked
        attribute vang null #VERY angry
        attribute vsur null #surprised (very)
        attribute worr null #worried
        attribute yand null #yandere
    
    group blush:
        attribute no_blush default null
        attribute awkward null 
        attribute blushing null 
        attribute awkward_blushing null
        attribute full_face_blush null

        attribute nobl default null #no blush or tear drop.
        attribute awkw null #awkward.  defaults for n
        attribute blus null #blushing.  defaults for n
        attribute blaw null #blushing AND awkward.  defaults for n
        attribute bful null #full face blush.  Currently only works on the side face.
    
    group head: #This needs to render below her body for her "cross" pose.
        xoffset (18)
        yoffset (21)
        attribute face_forward default:
            "mod_assets/MPT/natsuki/natsuki_face_forward.png"
        attribute sad_face:
            "mod_assets/MPT/natsuki/natsuki_face_sad.png"
        attribute turned_away_face:
            "mod_assets/MPT/natsuki/natsuki_face_turnedaway.png"

        attribute ff default:
            "mod_assets/MPT/natsuki/natsuki_face_forward.png"
        attribute fs:
            "mod_assets/MPT/natsuki/natsuki_face_sad.png"
        attribute fta:
            "mod_assets/MPT/natsuki/natsuki_face_turnedaway.png"
    
    group nose if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
        xoffset (18)
        yoffset (21)
        
        ###Default nose
        attribute nose default if_any(["no_blush", "nobl"]):
            "mod_assets/MPT/natsuki/natsuki_ff_nose_n1.png"
        attribute nose if_any(["awkward", "awkw"]):
            "mod_assets/MPT/natsuki/natsuki_ff_nose_n2.png"
        attribute nose if_any(["blushing", "blus"]):
            "mod_assets/MPT/natsuki/natsuki_ff_nose_n3.png"
        attribute nose if_any(["awkward_blushing", "blaw"]):
            "mod_assets/MPT/natsuki/natsuki_ff_nose_n4.png"
        
        ### All noses
        attribute nose1:
            "mod_assets/MPT/natsuki/natsuki_ff_nose_n1.png"
        attribute nose2:
            "mod_assets/MPT/natsuki/natsuki_ff_nose_n2.png"
        attribute nose3:
            "mod_assets/MPT/natsuki/natsuki_ff_nose_n3.png"
        attribute nose4:
            "mod_assets/MPT/natsuki/natsuki_ff_nose_n4.png"
            
        attribute n1:
            "mod_assets/MPT/natsuki/natsuki_ff_nose_n1.png"
        attribute n2:
            "mod_assets/MPT/natsuki/natsuki_ff_nose_n2.png"
        attribute n3:
            "mod_assets/MPT/natsuki/natsuki_ff_nose_n3.png"
        attribute n4:
            "mod_assets/MPT/natsuki/natsuki_ff_nose_n4.png"
    
    group mouth if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
        xoffset (18)
        yoffset (21)
        
        ### Closed Mouths
        attribute closed_mouth default if_any(["happy", "alluring", "tense", "happ","sedu","nerv"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_ma.png"
        attribute closed_mouth default if_any(["fine", "annoyed", "unease", "lightly_amazed", "neut","anno","worr","lsur"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_md.png"
        attribute closed_mouth default if_any(["curious", "pout","curi"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_me.png"
        attribute closed_mouth default if_any(["flustered", "shocked", "flus","shoc"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mg.png"
        attribute closed_mouth default if_any(["angry", "very_amazed", "aloof", "doubtful", "sad","angr","vsur","dist","doub"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mj.png"
        attribute closed_mouth default if_any(["very_angry", "panicked", "crying", "vang","pani","cry"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mm.png"
        attribute closed_mouth default if_any(["yandere", "yand"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mn.png"
        attribute closed_mouth default if_any(["laughing", "laug"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mo.png"

        attribute cm default if_any(["happy", "alluring", "tense", "happ","sedu","nerv"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_ma.png"
        attribute cm default if_any(["fine", "annoyed", "unease", "lightly_amazed", "neut","anno","worr","lsur"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_md.png"
        attribute cm default if_any(["curious", "pout","curi"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_me.png"
        attribute cm default if_any(["flustered", "shocked", "flus","shoc"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mg.png"
        attribute cm default if_any(["angry", "very_amazed", "aloof", "doubtful", "sad","angr","vsur","dist","doub"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mj.png"
        attribute cm default if_any(["very_angry", "panicked", "crying", "vang","pani","cry"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mm.png"
        attribute cm default if_any(["yandere", "yand"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mn.png"
        attribute cm default if_any(["laughing", "laug"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mo.png"
        
        ### Open Mouths
        attribute open_mouth if_any(["alluring", "tense", "yandere", "sedu","nerv","yand"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mb.png"
        attribute open_mouth if_any(["happy", "laughing", "happ","laug"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mc.png"
        attribute open_mouth if_any(["annoyed", "unease", "lightly_amazed", "aloof", "sad","anno","worr","lsur","dist","pout"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mg.png"
        attribute open_mouth if_any(["fine", "curious", "neut","curi"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mh.png"
        attribute open_mouth if_any(["doubtful", "angry", "very_amazed", "doub","angr","vsur"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mi.png"
        attribute open_mouth if_any(["flustered", "shocked", "flus","shoc"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_ml.png"
        attribute open_mouth if_any(["crying", "very_angry", "panicked", "cry","vang","pani"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mq.png"

        attribute om if_any(["alluring", "tense", "yandere", "sedu","nerv","yand"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mb.png"
        attribute om if_any(["happy", "laughing", "happ","laug"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mc.png"
        attribute om if_any(["annoyed", "unease", "lightly_amazed", "aloof", "sad","anno","worr","lsur","dist","pout"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mg.png"
        attribute om if_any(["fine", "curious", "neut","curi"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mh.png"
        attribute om if_any(["doubtful", "angry", "very_amazed", "doub","angr","vsur"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mi.png"
        attribute om if_any(["flustered", "shocked", "flus","shoc"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_ml.png"
        attribute om if_any(["crying", "very_angry", "panicked", "cry","vang","pani"]):
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mq.png"
        
        ### All mouths
        ### Simple Syntax
        attribute mouth_a:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_ma.png"
        attribute mouth_b:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mb.png"
        attribute mouth_c:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mc.png"
        attribute mouth_d:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_md.png"
        attribute mouth_e:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_me.png"
        attribute mouth_f:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mf.png"
        attribute mouth_g:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mg.png"
        attribute mouth_h:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mh.png"
        attribute mouth_i:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mi.png"
        attribute mouth_j:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mj.png"
        attribute mouth_k:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mk.png"
        attribute mouth_l:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_ml.png"
        attribute mouth_m:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mm.png"
        attribute mouth_n:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mn.png"
        attribute mouth_o:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mo.png"
        attribute mouth_p:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mp.png"
        attribute mouth_q:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mq.png"
        attribute mouth_r:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mr.png"
            
        ### Old MPT Syntax
        attribute ma:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_ma.png"
        attribute mb:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mb.png"
        attribute mc:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mc.png"
        attribute md:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_md.png"
        attribute me:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_me.png"
        attribute mf:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mf.png"
        attribute mg:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mg.png"
        attribute mh:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mh.png"
        attribute mi:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mi.png"
        attribute mj:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mj.png"
        attribute mk:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mk.png"
        attribute ml:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_ml.png"
        attribute mm:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mm.png"
        attribute mn:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mn.png"
        attribute mo:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mo.png"
        attribute mp:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mp.png"
        attribute mq:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mq.png"
        attribute mr:
            "mod_assets/MPT/natsuki/natsuki_ff_mouth_mr.png"
    
    group eyes if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
        xoffset (18)
        yoffset (21)
        
        ### Open eyes
        attribute open_eyes default if_any(["fine", "happy", "laughing", "curious", "neut","happ","laug","pout","curi"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1a.png"
        attribute open_eyes default if_any(["unease","flustered","aloof", "sad","worr","flus","dist"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1b.png"
        attribute open_eyes default if_any(["annoyed", "alluring", "doubtful", "anno","sedu","doub"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1d.png"
        attribute open_eyes default if_any(["crying", "cry"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1g.png"
        attribute open_eyes default if_any(["angry", "lightly_amazed", "tense", "angr","lsur","nerv"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2a.png"
        attribute open_eyes default if_any(["very_angry", "very_amazed", "panicked", "shocked", "vang","vsur","pani","shoc"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2d.png"
        attribute open_eyes default if_any(["yandere", "yand"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e3a.png"

        attribute oe default if_any(["fine", "happy", "laughing", "curious", "neut","happ","laug","pout","curi"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1a.png"
        attribute oe default if_any(["unease","flustered","aloof", "sad","worr","flus","dist"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1b.png"
        attribute oe default if_any(["annoyed", "alluring", "doubtful", "anno","sedu","doub"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1d.png"
        attribute oe default if_any(["crying", "cry"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1g.png"
        attribute oe default if_any(["angry", "lightly_amazed", "tense", "angr","lsur","nerv"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2a.png"
        attribute oe default if_any(["very_angry", "very_amazed", "panicked", "shocked", "vang","vsur","pani","shoc"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2d.png"
        attribute oe default if_any(["yandere", "yand"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e3a.png"
        
        ### Closed eyes
        attribute closed_eyes if_any(["unease", "annoyed", "angry", "very_angry", "very_amazed", "flustered", "aloof", "alluring", "tense", "doubtful", "sad","worr","anno","angr","vang","vsur","flus","dist","sedu","nerv","doub"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4a.png"
        attribute closed_eyes if_any(["fine", "happy", "laughing", "lightly_amazed", "yandere", "curious", "neut","happ","laug","lsur","yand","pout","curi"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4b.png"
        attribute closed_eyes if_any(["shocked", "panicked""shoc","pani"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4c.png"
        attribute closed_eyes if_any(["crying", "cry"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4e.png"

        attribute ce if_any(["unease", "annoyed", "angry", "very_angry", "very_amazed", "flustered", "aloof", "alluring", "tense", "doubtful", "sad","worr","anno","angr","vang","vsur","flus","dist","sedu","nerv","doub"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4a.png"
        attribute ce if_any(["fine", "happy", "laughing", "lightly_amazed", "yandere", "curious", "neut","happ","laug","lsur","yand","pout","curi"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4b.png"
        attribute ce if_any(["shocked", "panicked""shoc","pani"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4c.png"
        attribute ce if_any(["crying", "cry"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4e.png"
        
        ### All eyes
        ### Simple Syntax
        attribute eyes_a:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1a.png"
        attribute eyes_b:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1b.png"
        attribute eyes_c:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1c.png"
        attribute eyes_d:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1d.png"
        attribute eyes_e:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1e.png"
        attribute eyes_f:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1f.png"
        attribute eyes_g:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1g.png"
        attribute eyes_h:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1h.png"
        attribute eyes_i:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2a.png"
        attribute eyes_j:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2b.png"
        attribute eyes_k:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2c.png"
        attribute eyes_l:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2d.png"
        attribute eyes_m:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e3a.png"
        attribute eyes_n:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e3b.png"
        attribute eyes_o:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4a.png"
        attribute eyes_p:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4b.png"
        attribute eyes_q:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4c.png"
        attribute eyes_r:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4d.png"
        attribute eyes_s:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4e.png"
        attribute eyes_t:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e0a.png"
        attribute eyes_u:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e0b.png"

        ### New MPT Syntax
        attribute ea:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1a.png"
        attribute eb:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1b.png"
        attribute ec:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1c.png"
        attribute ed:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1d.png"
        attribute ee:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1e.png"
        attribute ef:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1f.png"
        attribute eg:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1g.png"
        attribute eh:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1h.png"
        attribute ei:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2a.png"
        attribute ej:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2b.png"
        attribute ek:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2c.png"
        attribute el:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2d.png"
        attribute em:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e3a.png"
        attribute en:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e3b.png"
        attribute eo:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4a.png"
        attribute ep:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4b.png"
        attribute eq:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4c.png"
        attribute er:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4d.png"
        attribute es:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4e.png"
        attribute et:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e0a.png"
        attribute eu:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e0b.png"

        ### Old MPT Syntax
        attribute e1a:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1a.png"
        attribute e1b:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1b.png"
        attribute e1c:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1c.png"
        attribute e1d:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1d.png"
        attribute e1e:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1e.png"
        attribute e1f:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1f.png"
        attribute e1g:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1g.png"
        attribute e1h:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1h.png"
        attribute e2a:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2a.png"
        attribute e2b:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2b.png"
        attribute e2c:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2c.png"
        attribute e2d:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2d.png"
        attribute e3a:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e3a.png"
        attribute e3b:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e3b.png"
        attribute e4a:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4a.png"
        attribute e4b:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4b.png"
        attribute e4c:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4c.png"
        attribute e4d:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4d.png"
        attribute e4e:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4e.png"
        attribute e0a:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e0a.png"
        attribute e0b:
            "mod_assets/MPT/natsuki/natsuki_ff_eyes_e0b.png"
    
    group eyebrows if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]): #eyebrows.
        xoffset (18)
        yoffset (21)
        
        ### Default Eyebrows
        attribute brow default if_any(["fine", "aloof", "alluring", "neut","dist","sedu"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1a.png"
        attribute brow default if_any(["panicked", "flustered", "tense", "sad","pani","flus","pout","nerv"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1b.png"
        attribute brow default if_any(["happy", "unease", "shocked", "happ","worr","shoc"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1c.png"
        attribute brow default if_any(["curious", "doubtful", "curi","doub"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1f.png"
        attribute brow default if_any(["lightly_amazed", "lsur"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b2a.png"
        attribute brow default if_any(["crying", "very_amazed", "cry","vsur"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b2c.png"
    
    #Some of Natsuki's eyebrows can only be used with closed eye expressions: the following moods take advantage of this, and thus need logic to check whether the eyes are open or not.
    group eyebrows:#In case you're wondering why there's no if_all or if_not logic on this group line, it's because the attributes below explicitly use the same logic - and if you have a group and an attribute both using the same logic tag, the attribute one will COMPLETELY overwrite and ignore the group logic.  It took me way too long to figure this out.
        xoffset (18)
        yoffset (21)
        
        attribute brow default if_any(["very_angry", "vang"]) if_all(["face_forward", "open_eyes"]) if_not(["turned_away_face", "sad_face", "closed_face", "fta","fs","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1d.png"
        attribute brow default if_any(["very_angry", "vang"]) if_all(["closed_eyes", "face_forward"]) if_not(["turned_away_face", "sad_face", "open_eyes", "fta","fs","oe"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3a.png"
        attribute brow default if_any(["laughing", "laug"]) if_all(["face_forward", "open_eyes"]) if_not(["turned_away_face", "sad_face", "closed_face", "fta","fs","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1b.png"
        attribute brow default if_any(["laughing", "laug"]) if_all(["closed_eyes", "face_forward"]) if_not(["turned_away_face", "sad_face", "open_eyes", "fta","fs","oe"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3a.png"
        attribute brow default if_any(["yandere", "yand"]) if_all(["face_forward", "open_eyes"]) if_not(["turned_away_face", "sad_face", "closed_face", "fta","fs","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b2a.png"
        attribute brow default if_any(["yandere", "yand"]) if_all(["closed_eyes", "face_forward"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3c.png"
        attribute brow default if_any(["annoyed", "angry", "anno","angr"]) if_all(["face_forward", "open_eyes"]) if_not(["turned_away_face", "sad_face", "closed_face", "fta","fs","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1d.png"
        attribute brow default if_any(["annoyed", "angry", "anno","angr"]) if_all(["closed_eyes", "face_forward"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3b.png"

        attribute brow default if_any(["very_angry", "vang"]) if_all(["ff","oe"]) if_not(["turned_away_face", "sad_face", "closed_face", "fta","fs","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1d.png"
        attribute brow default if_any(["very_angry", "vang"]) if_all(["ce","ff"]) if_not(["turned_away_face", "sad_face", "open_eyes", "fta","fs","oe"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3a.png"
        attribute brow default if_any(["laughing", "laug"]) if_all(["ff","oe"]) if_not(["turned_away_face", "sad_face", "closed_face", "fta","fs","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1b.png"
        attribute brow default if_any(["laughing", "laug"]) if_all(["ce","ff"]) if_not(["turned_away_face", "sad_face", "open_eyes", "fta","fs","oe"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3a.png"
        attribute brow default if_any(["yandere", "yand"]) if_all(["ff","oe"]) if_not(["turned_away_face", "sad_face", "closed_face", "fta","fs","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b2a.png"
        attribute brow default if_any(["yandere", "yand"]) if_all(["ce","ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3c.png"
        attribute brow default if_any(["annoyed", "angry", "anno","angr"]) if_all(["ff","oe"]) if_not(["turned_away_face", "sad_face", "closed_face", "fta","fs","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1d.png"
        attribute brow default if_any(["annoyed", "angry", "anno","angr"]) if_all(["ce","ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3b.png"
    
    group eyebrows:
        xoffset (18)
        yoffset (21)
        
        ### All eyebrows
        ### Simple Syntax
        attribute brow_a if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1a.png"
        attribute brow_b if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1b.png"
        attribute brow_c if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs",]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1c.png"
        attribute brow_d if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1d.png"
        attribute brow_e if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1e.png"
        attribute brow_f if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1f.png"
        attribute brow_g if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b2a.png"
        attribute brow_h if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b2b.png"
        attribute brow_i if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b2c.png"
        attribute brow_j if_all(["forward_face"]) if_not(["turned_away_face", "sad_face", "fta","fs"]) if_any(["eyes_o", "eo", "eyes_p", "ep", "eyes_q", "eq", "eyes_r", "er", "eyes_s", "es", "closed_eyes", "e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3a.png"
        attribute brow_k if_all(["forward_face"]) if_not(["turned_away_face", "sad_face", "fta","fs"]) if_any(["eyes_o", "eo", "eyes_p", "ep", "eyes_q", "eq", "eyes_r", "er", "eyes_s", "es", "closed_eyes", "e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3b.png"
        attribute brow_l if_all(["forward_face"]) if_not(["turned_away_face", "sad_face", "fta","fs"]) if_any(["eyes_o", "eo", "eyes_p", "ep", "eyes_q", "eq", "eyes_r", "er", "eyes_s", "es", "closed_eyes", "e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3c.png"
        #If the user tries to specifically use a closed-eyebrow variant with open eyes, we intentionally replace the eyebrow graphic in use with an appropriate - but not identical - replacement from the regular eyebrows:
        attribute brow_j if_all(["forward_face"]) if_not(["turned_away_face", "sad_face", "fta","fs","e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1e.png"
        attribute brow_k if_all(["forward_face"]) if_not(["turned_away_face", "sad_face", "fta","fs","e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1d.png"
        attribute brow_l if_all(["forward_face"]) if_not(["turned_away_face", "sad_face", "fta","fs","e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1c.png"

        attribute brow_j if_all(["ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]) if_any(["eyes_o", "eo", "eyes_p", "ep", "eyes_q", "eq", "eyes_r", "er", "eyes_s", "es", "closed_eyes", "e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3a.png"
        attribute brow_k if_all(["ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]) if_any(["eyes_o", "eo", "eyes_p", "ep", "eyes_q", "eq", "eyes_r", "er", "eyes_s", "es", "closed_eyes", "e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3b.png"
        attribute brow_l if_all(["ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]) if_any(["eyes_o", "eo", "eyes_p", "ep", "eyes_q", "eq", "eyes_r", "er", "eyes_s", "es", "closed_eyes", "e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3c.png"
        #If the user tries to specifically use a closed-eyebrow variant with open eyes, we intentionally replace the eyebrow graphic in use with an appropriate - but not identical - replacement from the regular eyebrows:
        attribute brow_j if_all(["ff"]) if_not(["turned_away_face", "sad_face", "fta","fs","e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1e.png"
        attribute brow_k if_all(["ff"]) if_not(["turned_away_face", "sad_face", "fta","fs","e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1d.png"
        attribute brow_l if_all(["ff"]) if_not(["turned_away_face", "sad_face", "fta","fs","e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1c.png"

        ### New MPT Syntax
        attribute ba if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1a.png"
        attribute bb if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1b.png"
        attribute bc if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs",]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1c.png"
        attribute bd if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1d.png"
        attribute be if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1e.png"
        attribute bf if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1f.png"
        attribute bg if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b2a.png"
        attribute bh if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b2b.png"
        attribute bi if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b2c.png"
        attribute bj if_any(["face_forward", "ff", "eyes_o", "eo", "eyes_p", "ep", "eyes_q", "eq", "eyes_r", "er", "eyes_s", "es", "closed_eyes", "e4a","e4b","e4c","e4d","e4e","ce"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3a.png"
        attribute bk if_any(["face_forward", "ff", "eyes_o", "eo", "eyes_p", "ep", "eyes_q", "eq", "eyes_r", "er", "eyes_s", "es", "closed_eyes", "e4a","e4b","e4c","e4d","e4e","ce"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3b.png"
        attribute bl if_any(["face_forward", "ff", "eyes_o", "eo", "eyes_p", "ep", "eyes_q", "eq", "eyes_r", "er", "eyes_s", "es", "closed_eyes", "e4a","e4b","e4c","e4d","e4e","ce"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3c.png"
        #If the user tries to specifically use a closed-eyebrow variant with open eyes, we intentionally replace the eyebrow graphic in use with an appropriate - but not identical - replacement from the regular eyebrows:
        attribute bj if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs","e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1e.png"
        attribute bk if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs","e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1d.png"
        attribute bl if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs","e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1c.png"

        ### Old MPT Syntax
        attribute b1a if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1a.png"
        attribute b1b if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1b.png"
        attribute b1c if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs",]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1c.png"
        attribute b1d if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1d.png"
        attribute b1e if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1e.png"
        attribute b1f if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1f.png"
        attribute b2a if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b2a.png"
        attribute b2b if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b2b.png"
        attribute b2c if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b2c.png"
        attribute b3a if_any(["face_forward", "ff", "eyes_o", "eo", "eyes_p", "ep", "eyes_q", "eq", "eyes_r", "er", "eyes_s", "es", "closed_eyes", "e4a","e4b","e4c","e4d","e4e","ce"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3a.png"
        attribute b3b if_any(["face_forward", "ff", "eyes_o", "eo", "eyes_p", "ep", "eyes_q", "eq", "eyes_r", "er", "eyes_s", "es", "closed_eyes", "e4a","e4b","e4c","e4d","e4e","ce"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3b.png"
        attribute b3c if_any(["face_forward", "ff", "eyes_o", "eo", "eyes_p", "ep", "eyes_q", "eq", "eyes_r", "er", "eyes_s", "es", "closed_eyes", "e4a","e4b","e4c","e4d","e4e","ce"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3c.png"
        #If the user tries to specifically use a closed-eyebrow variant with open eyes, we intentionally replace the eyebrow graphic in use with an appropriate - but not identical - replacement from the regular eyebrows:
        attribute b3a if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs","e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1e.png"
        attribute b3b if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs","e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1d.png"
        attribute b3c if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs","e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1c.png"
    
    #This group is intentionally last on this list, so it will render over top of every other thing on the face.
    group special if_any(["face_forward", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
        xoffset (18)
        yoffset (21)
        attribute special_scream:
            "mod_assets/MPT/natsuki/natsuki_face_special_scream.png"

        attribute s_scream:
            "mod_assets/MPT/natsuki/natsuki_face_special_scream.png"
    
####################The "sad, turned away" face, and the few expressions it has.
    
    group nose if_any(["sad_face", "fs"]) if_not(["face_forward", "turned_away_face", "ff","fta"]):
        xoffset (18)
        yoffset (21)
        
        ### Default nose
        attribute nose default if_any(["no_blush", "nobl"]):
            "mod_assets/MPT/natsuki/natsuki_fs_nose_n1.png"
        attribute nose default if_any(["awkward", "awkw"]):
            "mod_assets/MPT/natsuki/natsuki_fs_nose_n2.png"
        attribute nose default if_any(["blushing", "blus"]):
            "mod_assets/MPT/natsuki/natsuki_fs_nose_n3.png"
        attribute nose default if_any(["awkward_blushing", "blaw"]):
            "mod_assets/MPT/natsuki/natsuki_fs_nose_n4.png"
        attribute nose default if_any(["full_face_blush", "bful"]):
            "mod_assets/MPT/natsuki/natsuki_fs_nose_n5.png"
        
        ### All noses
        ### Simple Syntax
        attribute nose1:
            "mod_assets/MPT/natsuki/natsuki_fs_nose_n1.png"
        attribute nose2:
            "mod_assets/MPT/natsuki/natsuki_fs_nose_n2.png"
        attribute nose3:
            "mod_assets/MPT/natsuki/natsuki_fs_nose_n3.png"
        attribute nose4:
            "mod_assets/MPT/natsuki/natsuki_fs_nose_n4.png"
        attribute nose5:
            "mod_assets/MPT/natsuki/natsuki_fs_nose_n5.png"

        ### Old MPT Syntax
        attribute n1:
            "mod_assets/MPT/natsuki/natsuki_fs_nose_n1.png"
        attribute n2:
            "mod_assets/MPT/natsuki/natsuki_fs_nose_n2.png"
        attribute n3:
            "mod_assets/MPT/natsuki/natsuki_fs_nose_n3.png"
        attribute n4:
            "mod_assets/MPT/natsuki/natsuki_fs_nose_n4.png"
        attribute n5:
            "mod_assets/MPT/natsuki/natsuki_fs_nose_n5.png"
    
    group mouth if_any(["sad_face", "fs"]) if_not(["face_forward", "turned_away_face", "ff","fta"]):
        xoffset (18)
        yoffset (21)
        
        ### Closed mouth
        attribute closed_mouth default if_any(["fine", "neut"]):
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m1.png"
        attribute closed_mouth default if_any(["crying", "sad","cry"]):
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m2.png"

        attribute cm default if_any(["fine", "neut"]):
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m1.png"
        attribute cm default if_any(["crying", "sad","cry"]):
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m2.png"
        
        #Open mouths.  Note that there's only one at this time.
        attribute open_mouth if_any(["crying", "fine", "sad","cry","neut"]):
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m3.png"

        attribute om if_any(["crying", "fine", "sad","cry","neut"]):
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m3.png"
        
        ### All mouths
        ### Simple Syntax
        attribute mouth_a:
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m1.png"
        attribute mouth_b:
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m2.png"
        attribute mouth_c:
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m3.png"
        attribute mouth_d:
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m4.png"

        ### New MPT Syntax
        attribute ma:
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m1.png"
        attribute mb:
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m2.png"
        attribute mc:
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m3.png"
        attribute md:
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m4.png"

        ### Old MPT Syntax
        attribute m1:
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m1.png"
        attribute m2:
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m2.png"
        attribute m3:
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m3.png"
        attribute m4:
            "mod_assets/MPT/natsuki/natsuki_fs_mouth_m4.png"
    
    group eyes if_any(["sad_face", "fs"]) if_not(["face_forward", "turned_away_face", "nose5", "full_face_blush", "ff","fta","n5","bful"]): #Cannot show if full-face blush is present.
        xoffset (18)
        yoffset (21)
        
        ### Open eyes
        attribute open_eyes default if_any(["fine", "neut"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e1.png"
        attribute open_eyes default if_any(["sad"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e2.png"
        attribute open_eyes default if_any(["crying", "cry"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e3.png"

        attribute oe default if_any(["fine", "neut"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e1.png"
        attribute oe default if_any(["sad"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e2.png"
        attribute oe default if_any(["crying", "cry"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e3.png"
        
        ### Closed eyes
        attribute closed_eyes if_any(["fine", "neut"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e4.png"
        attribute closed_eyes if_any(["sad"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e5.png"
        attribute closed_eyes if_any(["crying", "cry"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e6.png"

        attribute ce if_any(["fine", "neut"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e4.png"
        attribute ce if_any(["sad"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e5.png"
        attribute ce if_any(["crying", "cry"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e6.png"
        
        ### All eyes
        ### Simple Syntax
        attribute eyes_a:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e1.png"
        attribute eyes_b:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e2.png"
        attribute eyes_c:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e3.png"
        attribute eyes_d:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e4.png"
        attribute eyes_e:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e5.png"
        attribute eyes_f:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e6.png"

        ### New MPT Syntax
        attribute ea:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e1.png"
        attribute eb:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e2.png"
        attribute ec:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e3.png"
        attribute ed:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e4.png"
        attribute ee:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e5.png"
        attribute ef:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e6.png"

        ### Old MPT Syntax
        attribute e1:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e1.png"
        attribute e2:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e2.png"
        attribute e3:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e3.png"
        attribute e4:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e4.png"
        attribute e5:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e5.png"
        attribute e6:
            "mod_assets/MPT/natsuki/natsuki_fs_eyes_e6.png"
    
    group eyebrows if_any(["sad_face", "fs"]) if_not(["face_forward", "turned_away_face", "nose5", "full_face_blush", "ff","fta","n5","bful"]): #Cannot show if full-face blush is present.
        xoffset (18)
        yoffset (21)
        
        #default brows
        attribute brow default if_any(["fine", "neut"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyebrows_b1.png"
        attribute brow default if_any(["sad"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyebrows_b3.png"
    
    group eyebrows:#Required separate group definition because of additional logic for showing these particular eyebrows.
        xoffset (18)
        yoffset (21)
        
        attribute brow default if_any(["crying", "cry"]) if_all(["sad_face", "open_eyes"]) if_not(["face_forward", "turned_away_face", "nose5", "full_face_blush", "ff","fta","n5","bful","ce","closed_eyes"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyebrows_b3.png"
        attribute brow default if_any(["crying", "cry"]) if_all(["sad_face", "closed_eyes"]) if_not(["face_forward", "turned_away_face", "nose5", "full_face_blush", "ff","fta","n5","bful","open_eyes","oe"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyebrows_b2.png"

        attribute brow default if_any(["crying", "cry"]) if_all(["fs", "oe"]) if_not(["face_forward", "turned_away_face", "nose5", "full_face_blush", "ff","fta","n5","bful","ce","closed_eyes"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyebrows_b3.png"
        attribute brow default if_any(["crying", "cry"]) if_all(["fs", "ce"]) if_not(["face_forward", "turned_away_face", "nose5", "full_face_blush", "ff","fta","n5","bful","open_eyes","oe"]):
            "mod_assets/MPT/natsuki/natsuki_fs_eyebrows_b2.png"
    
    group eyebrows if_any(["sad_face", "fs"]) if_not(["face_forward", "turned_away_face", "nose5", "full_face_blush", "ff","fta","n5","bful"]): #Cannot show if full-face blush is present.
        xoffset (18)
        yoffset (21)
        
        #All eyebrows - truncated tags:
        attribute b1:
            "mod_assets/MPT/natsuki/natsuki_fs_eyebrows_b1.png"
        attribute b2:
            "mod_assets/MPT/natsuki/natsuki_fs_eyebrows_b2.png"
        attribute b3:
            "mod_assets/MPT/natsuki/natsuki_fs_eyebrows_b3.png"

    ## For use if NBE assets is installed
    # group blink if_any(["forward_face", "ff"]) if_not(["turned_away_face", "sad_face", "fta","fs"]):
    #     xoffset (18)
    #     yoffset (21)

    #     attribute blink_a default if_not(["closed_eyes", "eyes_o", "eo", "eyes_p", "ep", "eyes_q", "eq", "eyes_r", "er", "eyes_s", "es", "eyes_e", "ee", "eyes_f", "ef", "ce","e4a","e4b","e4c", "e4d", "e4e", "e1e", "e1f"]):
    #         "_nat_blink_a"
    #     attribute no_blink:
    #         "sprite_blank"

    # group blink if_any(["sad_face", "fs"]) if_not(["turned_away_face", "forward_face", "fta","ff"]):
    #     xoffset (18)
    #     yoffset (22)

    #     attribute blink_a default if_not(["closed_eyes", "eyes_d", "eyes_e", "eyes_f", "ed", "ee", "ef", "nose5", "full_face_blush", "ce","e4","e5","e6","n5","bful"]):
    #         "_nat_blink_s_a"

image sprite_blank:
    alpha 0.0
    "mod_assets/MPT/natsuki/_blink_am.png"

image _nat_blink_a:
    alpha 0.0
    renpy.random.randint(20, 100)*0.1
    choice:
        alpha 1.0
        "mod_assets/MPT/natsuki/_blink_am.png"
        0.015
        "mod_assets/MPT/natsuki/_blink_af.png"
        0.035
        "mod_assets/MPT/natsuki/_blink_am.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/natsuki/_blink_am.png"
        0.015
        "mod_assets/MPT/natsuki/_blink_af.png"
        0.065
        "mod_assets/MPT/natsuki/_blink_am.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/natsuki/_blink_am.png"
        0.015
        "mod_assets/MPT/natsuki/_blink_af.png"
        0.095
        "mod_assets/MPT/natsuki/_blink_am.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/natsuki/_blink_am.png"
        0.015
        "mod_assets/MPT/natsuki/_blink_af.png"
        0.035
        "mod_assets/MPT/natsuki/_blink_am.png"
        0.015
        alpha 0.0
        0.15
        alpha 1.0
        "mod_assets/MPT/natsuki/_blink_am.png"
        0.015
        "mod_assets/MPT/natsuki/_blink_af.png"
        0.035
        "mod_assets/MPT/natsuki/_blink_am.png"
        0.015
    repeat

image _nat_blink_s_a:
    alpha 0.0
    renpy.random.randint(30, 60)*0.1
    choice:
        alpha 1.0
        "mod_assets/MPT/natsuki/_blink_s_am.png"
        0.015
        "mod_assets/MPT/natsuki/_blink_s_af.png"
        0.035
        "mod_assets/MPT/natsuki/_blink_s_am.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/natsuki/_blink_s_am.png"
        0.015
        "mod_assets/MPT/natsuki/_blink_s_af.png"
        0.065
        "mod_assets/MPT/natsuki/_blink_s_am.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/natsuki/_blink_s_am.png"
        0.015
        "mod_assets/MPT/natsuki/_blink_s_af.png"
        0.095
        "mod_assets/MPT/natsuki/_blink_s_am.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/natsuki/_blink_s_am.png"
        0.015
        "mod_assets/MPT/natsuki/_blink_s_af.png"
        0.035
        "mod_assets/MPT/natsuki/_blink_s_am.png"
        0.015
        alpha 0.0
        0.15
        alpha 1.0
        "mod_assets/MPT/natsuki/_blink_s_am.png"
        0.015
        "mod_assets/MPT/natsuki/_blink_s_af.png"
        0.035
        "mod_assets/MPT/natsuki/_blink_s_am.png"
        0.015
    repeat
