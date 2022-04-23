
layeredimage sayori base: 
    at Flatten
    
    always "mod_assets/MPT/sayori/sayori_turned_facebase.png" #Always need this face.

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
    
    # These are intentionally separate from mood; the idea being that these aren't
    # consciously controlled by the character - rather, they're a result of their 
    # emotions making them blush/sweat/etc.
    group blush: 
        attribute no_blush default null
        attribute awkward null 
        attribute blushing null 
        attribute awkward_blushing null

        # Backwards Compatibility
        attribute nobl null #No blush.
        attribute awkw null #awkward.  defaults for n
        attribute blus null #blushing.  defaults for n
        attribute blaw null #blushing and awkward.  defaults for n
    
    ### Left Half
    group left:
        attribute ldown default if_any(["uniform"]):
            "mod_assets/MPT/sayori/sayori_turned_uniform_left_down.png"
        attribute ldown default if_any(["casual"]):
            "mod_assets/MPT/sayori/sayori_turned_casual_left_down.png"
        attribute lup if_any(["uniform"]):
            "mod_assets/MPT/sayori/sayori_turned_uniform_left_up.png"
        attribute lup if_any(["casual"]):
            "mod_assets/MPT/sayori/sayori_turned_casual_left_up.png"
    
    ### Right Half
    group right:
        attribute rdown default if_any(["uniform"]):
            "mod_assets/MPT/sayori/sayori_turned_uniform_right_down.png"
        attribute rdown default if_any(["casual"]):
            "mod_assets/MPT/sayori/sayori_turned_casual_right_down.png"
        attribute rup if_any(["uniform"]):
            "mod_assets/MPT/sayori/sayori_turned_uniform_right_up.png"
        attribute rup if_any(["casual"]):
            "mod_assets/MPT/sayori/sayori_turned_casual_right_up.png"
    
    group nose:
        ### Default nose
        attribute nose default if_any(["no_blush", "nobl"]): #default nose
            "mod_assets/MPT/sayori/sayori_turned_nose_n1.png"
        attribute nose default if_any(["awkward", "awkw"]): #default nose when "awkward"
            "mod_assets/MPT/sayori/sayori_turned_nose_n2.png"
        attribute nose default if_any(["blushing", "blus"]): #default nose when "blushing"
            "mod_assets/MPT/sayori/sayori_turned_nose_n3.png"
        attribute nose default if_any(["awkward_blushing", "blaw"]): #default nose when "blushing and awkward"
            "mod_assets/MPT/sayori/sayori_turned_nose_n4.png"
        
        ### All noses
        ### Simple Syntax
        attribute nose1:
            "mod_assets/MPT/sayori/sayori_turned_nose_n1.png"
        attribute nose2:
            "mod_assets/MPT/sayori/sayori_turned_nose_n2.png"
        attribute nose3:
            "mod_assets/MPT/sayori/sayori_turned_nose_n3.png"
        attribute nose4:
            "mod_assets/MPT/sayori/sayori_turned_nose_n4.png"
        attribute nose5:
            "mod_assets/MPT/sayori/sayori_turned_nose_nl.png"

        ### Old MPT Syntax
        attribute n1:
            "mod_assets/MPT/sayori/sayori_turned_nose_n1.png"
        attribute n2:
            "mod_assets/MPT/sayori/sayori_turned_nose_n2.png"
        attribute n3:
            "mod_assets/MPT/sayori/sayori_turned_nose_n3.png"
        attribute n4:
            "mod_assets/MPT/sayori/sayori_turned_nose_n4.png"
        attribute nl:
            "mod_assets/MPT/sayori/sayori_turned_nose_nl.png"
    
    group mouth:
        ### Closed Mouth
        attribute closed_mouth default if_any(["happy", "alluring", "tense", "happ","sedu","nerv"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_ma.png"
        attribute closed_mouth default if_any(["fine", "annoyed", "unease", "curious", "neut","anno","worr","curi"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_md.png"
        attribute closed_mouth default if_any(["aloof", "flustered", "dist","flus"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_me.png"
        attribute closed_mouth default if_any(["lightly_amazed", "shocked", "lsur","shoc"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mf.png"
        attribute closed_mouth default if_any(["angry", "doubtful", "sad","angr","pout","doub"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mj.png"
        attribute closed_mouth default if_any(["crying", "panicked", "very_amazed", "cry","pani","vsur"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mk.png"
        attribute closed_mouth default if_any(["very_angry", "vang"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mm.png"
        attribute closed_mouth default if_any(["laughing", "laug"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mn.png"
        attribute closed_mouth default if_any(["yandere", "yand"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mo.png"

        attribute cm default if_any(["happy", "alluring", "tense", "happ","sedu","nerv"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_ma.png"
        attribute cm default if_any(["fine", "annoyed", "unease", "curious", "neut","anno","worr","curi"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_md.png"
        attribute cm default if_any(["aloof", "flustered", "dist","flus"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_me.png"
        attribute cm default if_any(["lightly_amazed", "shocked", "lsur","shoc"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mf.png"
        attribute cm default if_any(["angry", "doubtful", "sad","angr","pout","doub"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mj.png"
        attribute cm default if_any(["crying", "panicked", "very_amazed", "cry","pani","vsur"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mk.png"
        attribute cm default if_any(["very_angry", "vang"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mm.png"
        attribute cm default if_any(["laughing", "laug"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mn.png"
        attribute cm default if_any(["yandere", "yand"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mo.png"
        
        ### Open Mouth
        attribute open_mouth if_any(["happy", "laughing", "happ","laug"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mb.png"
        attribute open_mouth if_any(["yandere", "tense", "yand","nerv"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mc.png"
        attribute open_mouth if_any(["alluring", "pout","sedu"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mf.png"
        attribute open_mouth if_any(["lightly_amazed", "aloof", "sad","lsur","dist"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mg.png"
        attribute open_mouth if_any(["fine", "annoyed", "shocked", "unease", "neut","anno","shoc","worr"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mh.png"
        attribute open_mouth if_any(["curious", "doubtful", "curi","doub"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mi.png"
        attribute open_mouth if_any(["flustered", "flus"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mk.png"
        attribute open_mouth if_any(["crying", "very_amazed", "cry","vsur"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_ml.png"
        attribute open_mouth if_any(["angry", "panicked", "very_angry", "angr","pani","vang"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mq.png"

        attribute om if_any(["happy", "laughing", "happ","laug"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mb.png"
        attribute om if_any(["yandere", "tense", "yand","nerv"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mc.png"
        attribute om if_any(["alluring", "pout","sedu"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mf.png"
        attribute om if_any(["lightly_amazed", "aloof", "sad","lsur","dist"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mg.png"
        attribute om if_any(["fine", "annoyed", "shocked", "unease", "neut","anno","shoc","worr"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mh.png"
        attribute om if_any(["curious", "doubtful", "curi","doub"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mi.png"
        attribute om if_any(["flustered", "flus"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mk.png"
        attribute om if_any(["crying", "very_amazed", "cry","vsur"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_ml.png"
        attribute om if_any(["angry", "panicked", "very_angry", "angr","pani","vang"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mq.png"
        
        ### All mouths
        ### Simple Syntax
        attribute mouth_a:
            "mod_assets/MPT/sayori/sayori_turned_mouth_ma.png"
        attribute mouth_b:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mb.png"
        attribute mouth_c:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mc.png"
        attribute mouth_d:
            "mod_assets/MPT/sayori/sayori_turned_mouth_md.png"
        attribute mouth_e:
            "mod_assets/MPT/sayori/sayori_turned_mouth_me.png"
        attribute mouth_f:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mf.png"
        attribute mouth_g:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mg.png"
        attribute mouth_h:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mh.png"
        attribute mouth_i:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mi.png"
        attribute mouth_j:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mj.png"
        attribute mouth_k:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mk.png"
        attribute mouth_l:
            "mod_assets/MPT/sayori/sayori_turned_mouth_ml.png"
        attribute mouth_m:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mm.png"
        attribute mouth_n:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mn.png"
        attribute mouth_o:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mo.png"
        attribute mouth_p:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mp.png"
        attribute mouth_q:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mq.png"
        attribute mouth_r:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mr.png"

        ### Old MPT Syntax
        attribute ma:
            "mod_assets/MPT/sayori/sayori_turned_mouth_ma.png"
        attribute mb:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mb.png"
        attribute mc:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mc.png"
        attribute md:
            "mod_assets/MPT/sayori/sayori_turned_mouth_md.png"
        attribute me:
            "mod_assets/MPT/sayori/sayori_turned_mouth_me.png"
        attribute mf:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mf.png"
        attribute mg:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mg.png"
        attribute mh:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mh.png"
        attribute mi:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mi.png"
        attribute mj:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mj.png"
        attribute mk:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mk.png"
        attribute ml:
            "mod_assets/MPT/sayori/sayori_turned_mouth_ml.png"
        attribute mm:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mm.png"
        attribute mn:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mn.png"
        attribute mo:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mo.png"
        attribute mp:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mp.png"
        attribute mq:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mq.png"
        attribute mr:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mr.png"
    
    group eyes:
        ### Opened Eyes
        attribute open_eyes default if_any(["fine", "angry", "happy", "laughing", "neut","angr","happ","laug","sad"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1a.png"
        attribute open_eyes default if_any(["aloof", "unease", "dist","worr","pout"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1b.png"
        attribute open_eyes default if_any(["annoyed", "alluring", "doubtful", "anno","sedu","doub"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1d.png"
        attribute open_eyes default if_any(["crying", "cry"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1g.png"
        attribute open_eyes default if_any(["lightly_amazed", "flustered", "very_amazed", "curious", "lsur","flus","vsur","curi"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e2a.png"
        attribute open_eyes default if_any(["tense", "nerv"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e2b.png"
        attribute open_eyes default if_any(["panicked", "very_angry", "shocked", "pani","vang","shoc"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e2d.png"
        attribute open_eyes default if_any(["yandere", "yand"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e3a.png"

        attribute oe default if_any(["fine", "angry", "happy", "laughing", "neut","angr","happ","laug","sad"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1a.png"
        attribute oe default if_any(["aloof", "unease", "dist","worr","pout"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1b.png"
        attribute oe default if_any(["annoyed", "alluring", "doubtful", "anno","sedu","doub"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1d.png"
        attribute oe default if_any(["crying", "cry"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1g.png"
        attribute oe default if_any(["lightly_amazed", "flustered", "very_amazed", "curious", "lsur","flus","vsur","curi"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e2a.png"
        attribute oe default if_any(["tense", "nerv"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e2b.png"
        attribute oe default if_any(["panicked", "very_angry", "shocked", "pani","vang","shoc"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e2d.png"
        attribute oe default if_any(["yandere", "yand"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e3a.png"
        
        ### Closed Eyes
        attribute closed_eyes if_any(["annoyed", "angry", "aloof", "shocked", "unease", "tense", "curious", "doubtful", "sad","anno","angr","dist","shoc","worr","nerv","curi","doub"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e4a.png"
        attribute closed_eyes if_any(["fine", "happy", "lightly_amazed", "laughing", "very_amazed", "yandere", "alluring", "neut","happ","lsur","laug","vsur","yand","pout","sedu"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e4b.png"
        attribute closed_eyes if_any(["very_angry", "flustered", "panicked", "vang","flus","pani"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e4c.png"
        attribute closed_eyes if_any(["crying", "cry"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e4d.png"

        attribute ce if_any(["annoyed", "angry", "aloof", "shocked", "unease", "tense", "curious", "doubtful", "sad","anno","angr","dist","shoc","worr","nerv","curi","doub"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e4a.png"
        attribute ce if_any(["fine", "happy", "lightly_amazed", "laughing", "very_amazed", "yandere", "alluring", "neut","happ","lsur","laug","vsur","yand","pout","sedu"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e4b.png"
        attribute ce if_any(["very_angry", "flustered", "panicked", "vang","flus","pani"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e4c.png"
        attribute ce if_any(["crying", "cry"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e4d.png"
        
        ### All eyes
        ### Simple Syntax
        attribute eyes_a:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1a.png"
        attribute eyes_b:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1b.png"
        attribute eyes_c:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1c.png"
        attribute eyes_d:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1d.png"
        attribute eyes_e:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1e.png"
        attribute eyes_f:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1f.png"
        attribute eyes_g:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1g.png"
        attribute eyes_h:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1h.png"
        attribute eyes_i:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e2a.png"
        attribute eyes_j:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e2b.png"
        attribute eyes_k:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e2c.png"
        attribute eyes_l:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e2d.png"
        attribute eyes_m:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e3a.png"
        attribute eyes_n:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e3b.png"
        attribute eyes_o:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e4a.png"
        attribute eyes_p:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e4b.png"
        attribute eyes_q:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e4c.png"
        attribute eyes_r:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e4d.png"
        attribute eyes_s:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e4e.png"
        attribute eyes_t:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e0a.png"
        attribute eyes_u:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e0b.png"

        ### New MPT Syntax (e[A-Z])
        attribute ea:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1a.png"
        attribute eb:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1b.png"
        attribute ec:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1c.png"
        attribute ed:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1d.png"
        attribute ee:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1e.png"
        attribute ef:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1f.png"
        attribute eg:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1g.png"
        attribute eh:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1h.png"
        attribute ei:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e2a.png"
        attribute ej:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e2b.png"
        attribute ek:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e2c.png"
        attribute el:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e2d.png"
        attribute em:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e3a.png"
        attribute en:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e3b.png"
        attribute eo:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e4a.png"
        attribute ep:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e4b.png"
        attribute eq:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e4c.png"
        attribute er:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e4d.png"
        attribute es:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e4e.png"
        attribute et:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e0a.png"
        attribute eu:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e0b.png"

        ### Old MPT Syntax
        attribute e1a:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1a.png"
        attribute e1b:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1b.png"
        attribute e1c:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1c.png"
        attribute e1d:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1d.png"
        attribute e1e:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1e.png"
        attribute e1f:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1f.png"
        attribute e1g:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1g.png"
        attribute e1h:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1h.png"
        attribute e2a:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e2a.png"
        attribute e2b:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e2b.png"
        attribute e2c:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e2c.png"
        attribute e2d:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e2d.png"
        attribute e3a:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e3a.png"
        attribute e3b:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e3b.png"
        attribute e4a:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e4a.png"
        attribute e4b:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e4b.png"
        attribute e4c:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e4c.png"
        attribute e4d:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e4d.png"
        attribute e4e:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e4e.png"
        attribute e0a:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e0a.png"
        attribute e0b:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e0b.png"
    
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
        
        ### All eyebrows
        ### Simple Syntax
        attribute brow_a:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1a.png"
        attribute brow_b:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1b.png"
        attribute brow_c:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1c.png"
        attribute brow_d:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1d.png"
        attribute brow_e:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1e.png"
        attribute brow_f:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1f.png"
        attribute brow_g:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b2a.png"
        attribute brow_h:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b2b.png"
        attribute brow_i:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b2c.png"
        attribute brow_j if_any(["e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b3a.png"
        attribute brow_k if_any(["e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b3b.png"
        attribute brow_l if_any(["e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b3c.png"
        
        ### New MPT Syntax (b[A-Z])
        attribute ba:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1a.png"
        attribute bb:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1b.png"
        attribute bc:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1c.png"
        attribute bd:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1d.png"
        attribute be:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1e.png"
        attribute bf:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1f.png"
        attribute bg:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b2a.png"
        attribute bh:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b2b.png"
        attribute bi:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b2c.png"
        attribute bj if_any(["eyes_o", "eyes_p", "eyes_q", "eyes_r", "eyes_s", "eyes_t", "eyes_u", "eo", "ep", "eq", "er", "es", "et", "eu", "e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b3a.png"
        attribute bk if_any(["eyes_o", "eyes_p", "eyes_q", "eyes_r", "eyes_s", "eyes_t", "eyes_u", "eo", "ep", "eq", "er", "es", "et", "eu", "e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b3b.png"
        attribute bl if_any(["eyes_o", "eyes_p", "eyes_q", "eyes_r", "eyes_s", "eyes_t", "eyes_u", "eo", "ep", "eq", "er", "es", "et", "eu", "e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b3c.png"

        ### Old MPT Syntax (bX[A-Z])
        attribute b1a:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1a.png"
        attribute b1b:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1b.png"
        attribute b1c:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1c.png"
        attribute b1d:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1d.png"
        attribute b1e:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1e.png"
        attribute b1f:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1f.png"
        attribute b2a:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b2a.png"
        attribute b2b:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b2b.png"
        attribute b2c:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b2c.png"
        attribute b3a if_any(["eyes_o", "eyes_p", "eyes_q", "eyes_r", "eyes_s", "eyes_t", "eyes_u", "eo", "ep", "eq", "er", "es", "et", "eu", "e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b3a.png"
        attribute b3b if_any(["eyes_o", "eyes_p", "eyes_q", "eyes_r", "eyes_s", "eyes_t", "eyes_u", "eo", "ep", "eq", "er", "es", "et", "eu", "e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b3b.png"
        attribute b3c if_any(["eyes_o", "eyes_p", "eyes_q", "eyes_r", "eyes_s", "eyes_t", "eyes_u", "eo", "ep", "eq", "er", "es", "et", "eu", "e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b3c.png"
    
    #This group is intentionally last on this list, so it will render over top 
    # of every other thing on the face.
    group special:
        attribute special_scream:
            "mod_assets/MPT/sayori/sayori_turned_special_scream.png"

        attribute s_scream:
            "mod_assets/MPT/sayori/sayori_turned_special_scream.png"

    ## For use if NBE assets is installed
    # group blink:
    #     attribute blink_a default if_not(["closed_eyes", "eyes_o","eyes_p","eyes_q", "eyes_r", "eyes_s", "eyes_t", "eyes_u", "eo","ep","eq", "er", "es", "et", "eyes_e", "ee" "eyes_f", "ef", "ce","e4a","e4b","e4c", "e4d", "e4f", "e4e", "e1e", "e1f"]):
    #         "_say_blink_a"
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
    #         "_say_blink_t_a"
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
