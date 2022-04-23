
layeredimage yuri base:
    at Flatten
    
    always "mod_assets/MPT/yuri/yuri_turned_facebase.png"
    
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
        attribute nobl default null # Default, no blush.
        attribute awkw null # awkward.  defaults for n
        attribute blus null # blushing.  defaults for n
        attribute blaw null # blushing and awkward.  defaults for n
        #attribute bful null #full face blush.  Currently unused for her turned pose.
    
    ### Right Half
    group right:
        anchor (0,0)
        subpixel True
        attribute rdown default if_any(["uniform"]):
            "mod_assets/MPT/yuri/yuri_turned_uniform_right_down.png"
        attribute rdown default if_any(["casual"]):
            "mod_assets/MPT/yuri/yuri_turned_casual_right_down.png"
        attribute rup if_any(["uniform"]):
            "mod_assets/MPT/yuri/yuri_turned_uniform_right_up.png"
        attribute rup if_any(["casual"]):
            "mod_assets/MPT/yuri/yuri_turned_casual_right_up.png"
        attribute rcut if_any(["uniform"]):
            "mod_assets/MPT/yuri/yuri_turned_uniform_right_cut.png"
    
    ### Left Half
    group left:
        anchor (0,0)
        subpixel True
        attribute ldown default if_any(["uniform"]):
            "mod_assets/MPT/yuri/yuri_turned_uniform_left_down.png"
        attribute ldown default if_any(["casual"]):
            "mod_assets/MPT/yuri/yuri_turned_casual_left_down.png"
        attribute lup if_any(["rup","rcut"]) if_all(["uniform"]):
            "mod_assets/MPT/yuri/yuri_turned_uniform_left_up.png"
        attribute lup if_any(["rup","rcut"]) if_all(["casual"]):
            "mod_assets/MPT/yuri/yuri_turned_casual_left_up.png"
        attribute lup if_not(["rup","rcut"]) if_all(["uniform"]):
            "mod_assets/MPT/yuri/yuri_turned_uniform_left_up.png"
        attribute lup if_not(["rup","rcut"]) if_all(["casual"]):
            "mod_assets/MPT/yuri/yuri_turned_casual_left_up.png"
    
    group nose:
        ### Default nose
        attribute nose default if_any(["no_blush", "nobl"]): #default nose
            "mod_assets/MPT/yuri/yuri_turned_nose_n1.png"
        attribute nose default if_any(["awkward", "awkw"]): #default nose when "awkward"
            "mod_assets/MPT/yuri/yuri_turned_nose_n2.png"
        attribute nose default if_any(["blushing", "blus"]): #default nose when "blushing"
            "mod_assets/MPT/yuri/yuri_turned_nose_n3.png"
        attribute nose default if_any(["awkward_blushing", "blaw"]): #default nose when "blushing" and "awkward"
            "mod_assets/MPT/yuri/yuri_turned_nose_n4.png"
        
        ### All noses
        ### Simple Syntax
        attribute nose1:
            "mod_assets/MPT/yuri/yuri_turned_nose_n1.png"
        attribute nose2:
            "mod_assets/MPT/yuri/yuri_turned_nose_n2.png"
        attribute nose3:
            "mod_assets/MPT/yuri/yuri_turned_nose_n3.png"
        attribute nose4:
            "mod_assets/MPT/yuri/yuri_turned_nose_n4.png"
        
        ### Old MPT Syntax
        attribute n1:
            "mod_assets/MPT/yuri/yuri_turned_nose_n1.png"
        attribute n2:
            "mod_assets/MPT/yuri/yuri_turned_nose_n2.png"
        attribute n3:
            "mod_assets/MPT/yuri/yuri_turned_nose_n3.png"
        attribute n4:
            "mod_assets/MPT/yuri/yuri_turned_nose_n4.png"
    
    group mouth:
        ### Closed Mouth
        attribute closed_mouth default if_any(["happy", "laughing", "happ","laug"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_ma.png"
        attribute closed_mouth default if_any(["fine", "lightly_amazed", "unease", "neut","lsur","worr"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_md.png"
        attribute closed_mouth default if_any(["alluring", "sedu"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_me.png"
        attribute closed_mouth default if_any(["curious", "pout","curi"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mf.png"
        attribute closed_mouth default if_any(["shocked", "shoc"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mg.png"
        attribute closed_mouth default if_any(["aloof", "annoyed", "very_amazed", "angry", "crying", "doubtful", "dist","anno","vsur","sad","angr","cry","doub"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mj.png"
        attribute closed_mouth default if_any(["tense", "flustered", "nerv","flus"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mk.png"
        attribute closed_mouth default if_any(["very_angry", "panicked", "vang","pani"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mm.png"
        attribute closed_mouth default if_any(["yandere", "yand"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mo.png"

        attribute cm default if_any(["happy", "laughing", "happ","laug"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_ma.png"
        attribute cm default if_any(["fine", "lightly_amazed", "unease", "neut","lsur","worr"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_md.png"
        attribute cm default if_any(["alluring", "sedu"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_me.png"
        attribute cm default if_any(["curious", "pout","curi"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mf.png"
        attribute cm default if_any(["shocked", "shoc"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mg.png"
        attribute cm default if_any(["aloof", "annoyed", "very_amazed", "angry", "crying", "doubtful", "dist","anno","vsur","sad","angr","cry","doub"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mj.png"
        attribute cm default if_any(["tense", "flustered", "nerv","flus"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mk.png"
        attribute cm default if_any(["very_angry", "panicked", "vang","pani"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mm.png"
        attribute cm default if_any(["yandere", "yand"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mo.png"
        
        ### Open Mouth
        attribute open_mouth if_any(["happy", "happ"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mb.png"
        attribute open_mouth if_any(["laughing", "tense", "yandere", "laug","nerv","yand"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mc.png"
        attribute open_mouth if_any(["unease", "worr","pout"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_me.png"
        attribute open_mouth if_any(["alluring", "sedu"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mf.png"
        attribute open_mouth if_any(["aloof", "lightly_amazed", "angry", "crying", "dist","lsur","angr","cry"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mg.png"
        attribute open_mouth if_any(["fine", "annoyed", "very_amazed", "curious", "neut","anno","vsur","curi"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mh.png"
        attribute open_mouth if_any(["flustered", "doubtful", "flus","doub"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mi.png"
        attribute open_mouth if_any(["sad"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mk.png"
        attribute open_mouth if_any(["very_angry", "shocked", "panicked", "vang","shoc","pani"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_ml.png"

        attribute om if_any(["happy", "happ"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mb.png"
        attribute om if_any(["laughing", "tense", "yandere", "laug","nerv","yand"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mc.png"
        attribute om if_any(["unease", "worr","pout"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_me.png"
        attribute om if_any(["alluring", "sedu"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mf.png"
        attribute om if_any(["aloof", "lightly_amazed", "angry", "crying", "dist","lsur","angr","cry"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mg.png"
        attribute om if_any(["fine", "annoyed", "very_amazed", "curious", "neut","anno","vsur","curi"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mh.png"
        attribute om if_any(["flustered", "doubtful", "flus","doub"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mi.png"
        attribute om if_any(["sad"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mk.png"
        attribute om if_any(["very_angry", "shocked", "panicked", "vang","shoc","pani"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_ml.png"
        
        ### All mouths
        ### Simple Syntax
        attribute mouth_a:
            "mod_assets/MPT/yuri/yuri_turned_mouth_ma.png"
        attribute mouth_b:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mb.png"
        attribute mouth_c:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mc.png"
        attribute mouth_d:
            "mod_assets/MPT/yuri/yuri_turned_mouth_md.png"
        attribute mouth_e:
            "mod_assets/MPT/yuri/yuri_turned_mouth_me.png"
        attribute mouth_f:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mf.png"
        attribute mouth_g:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mg.png"
        attribute mouth_h:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mh.png"
        attribute mouth_i:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mi.png"
        attribute mouth_j:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mj.png"
        attribute mouth_k:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mk.png"
        attribute mouth_l:
            "mod_assets/MPT/yuri/yuri_turned_mouth_ml.png"
        attribute mouth_m:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mm.png"
        attribute mouth_n:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mn.png"
        attribute mouth_o:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mo.png"
        attribute mouth_p:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mp.png"
        attribute mouth_q:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mq.png"
        attribute mouth_r:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mr.png"

        ### Old MPT Syntax
        attribute ma:
            "mod_assets/MPT/yuri/yuri_turned_mouth_ma.png"
        attribute mb:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mb.png"
        attribute mc:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mc.png"
        attribute md:
            "mod_assets/MPT/yuri/yuri_turned_mouth_md.png"
        attribute me:
            "mod_assets/MPT/yuri/yuri_turned_mouth_me.png"
        attribute mf:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mf.png"
        attribute mg:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mg.png"
        attribute mh:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mh.png"
        attribute mi:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mi.png"
        attribute mj:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mj.png"
        attribute mk:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mk.png"
        attribute ml:
            "mod_assets/MPT/yuri/yuri_turned_mouth_ml.png"
        attribute mm:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mm.png"
        attribute mn:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mn.png"
        attribute mo:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mo.png"
        attribute mp:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mp.png"
        attribute mq:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mq.png"
        attribute mr:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mr.png"
    
    group eyes:
        ### Opened Eyes
        attribute open_eyes default if_any(["fine", "alluring", "neut","sedu"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1a.png"
        attribute open_eyes default if_any(["aloof", "unease", "dist","worr"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1b.png"
        attribute open_eyes default if_any(["happy", "angry", "curious", "happ","angr","pout","curi"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1d.png"
        attribute open_eyes default if_any(["crying", "cry"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1h.png"
        attribute open_eyes default if_any(["lightly_amazed", "very_angry", "lsur","vang"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e2a.png"
        attribute open_eyes default if_any(["annoyed", "flustered", "laughing", "anno","flus","laug","sad"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e2b.png"
        attribute open_eyes default if_any(["tense", "doubtful", "nerv","doub"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e2c.png"
        attribute open_eyes default if_any(["shocked", "panicked", "very_amazed", "shoc","pani","vsur"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e2d.png"
        attribute open_eyes default if_any(["yandere", "yand"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e3a.png"

        attribute oe default if_any(["fine", "alluring", "neut","sedu"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1a.png"
        attribute oe default if_any(["aloof", "unease", "dist","worr"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1b.png"
        attribute oe default if_any(["happy", "angry", "curious", "happ","angr","pout","curi"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1d.png"
        attribute oe default if_any(["crying", "cry"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1h.png"
        attribute oe default if_any(["lightly_amazed", "very_angry", "lsur","vang"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e2a.png"
        attribute oe default if_any(["annoyed", "flustered", "laughing", "anno","flus","laug","sad"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e2b.png"
        attribute oe default if_any(["tense", "doubtful", "nerv","doub"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e2c.png"
        attribute oe default if_any(["shocked", "panicked", "very_amazed", "shoc","pani","vsur"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e2d.png"
        attribute oe default if_any(["yandere", "yand"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e3a.png"
        
        ### Closed Eyes
        attribute closed_eyes if_any(["aloof", "annoyed", "very_angry", "flustered", "lightly_amazed", "shocked", "very_amazed", "unease", "angry", "tense", "curious", "doubtful", "dist","anno","vang","flus","lsur","shoc","vsur","worr","sad","angr","nerv","curi","doub"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e4a.png"
        attribute closed_eyes if_any(["fine", "happy", "yandere", "panicked", "laughing", "alluring", "neut","happ","yand","pani","laug","sedu","pout"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e4b.png"
        attribute closed_eyes if_any(["crying", "cry"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e4e.png"

        attribute ce if_any(["aloof", "annoyed", "very_angry", "flustered", "lightly_amazed", "shocked", "very_amazed", "unease", "angry", "tense", "curious", "doubtful", "dist","anno","vang","flus","lsur","shoc","vsur","worr","sad","angr","nerv","curi","doub"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e4a.png"
        attribute ce if_any(["fine", "happy", "yandere", "panicked", "laughing", "alluring", "neut","happ","yand","pani","laug","sedu","pout"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e4b.png"
        attribute ce if_any(["crying", "cry"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e4e.png"
        
        ### All eyes
        ### Simple Syntax
        attribute eyes_a:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1a.png"
        attribute eyes_b:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1b.png"
        attribute eyes_c:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1c.png"
        attribute eyes_d:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1d.png"
        attribute eyes_e:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1e.png"
        attribute eyes_f:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1f.png"
        attribute eyes_g:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1g.png"
        attribute eyes_h:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1h.png"
        attribute eyes_i:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e2a.png"
        attribute eyes_j:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e2b.png"
        attribute eyes_k:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e2c.png"
        attribute eyes_l:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e2d.png"
        attribute eyes_m:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e3a.png"
        attribute eyes_n:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e3b.png"
        attribute eyes_o:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e4a.png"
        attribute eyes_p:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e4b.png"
        attribute eyes_q:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e4c.png"
        attribute eyes_r:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e4d.png"
        attribute eyes_s:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e4e.png"
        attribute eyes_t:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e0a.png"
        attribute eyes_u:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e0b.png"
        attribute eyes_v:
            "mod_assets/MPT/yuri/yuri_turned_eyes_ela.png"
        attribute eyes_w:
            "mod_assets/MPT/yuri/yuri_turned_eyes_elb.png"

        ### New MPT Syntax
        attribute ea:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1a.png"
        attribute eb:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1b.png"
        attribute ec:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1c.png"
        attribute ed:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1d.png"
        attribute ee:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1e.png"
        attribute ef:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1f.png"
        attribute eg:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1g.png"
        attribute eh:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1h.png"
        attribute ei:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e2a.png"
        attribute ej:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e2b.png"
        attribute ek:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e2c.png"
        attribute el:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e2d.png"
        attribute em:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e3a.png"
        attribute en:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e3b.png"
        attribute eo:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e4a.png"
        attribute ep:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e4b.png"
        attribute eq:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e4c.png"
        attribute er:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e4d.png"
        attribute es:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e4e.png"
        attribute et:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e0a.png"
        attribute eu:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e0b.png"
        attribute ev:
            "mod_assets/MPT/yuri/yuri_turned_eyes_ela.png"
        attribute ew:
            "mod_assets/MPT/yuri/yuri_turned_eyes_elb.png"

        ### Old MPT Syntax
        attribute e1a:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1a.png"
        attribute e1b:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1b.png"
        attribute e1c:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1c.png"
        attribute e1d:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1d.png"
        attribute e1e:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1e.png"
        attribute e1f:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1f.png"
        attribute e1g:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1g.png"
        attribute e1h:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1h.png"
        attribute e2a:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e2a.png"
        attribute e2b:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e2b.png"
        attribute e2c:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e2c.png"
        attribute e2d:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e2d.png"
        attribute e3a:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e3a.png"
        attribute e3b:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e3b.png"
        attribute e4a:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e4a.png"
        attribute e4b:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e4b.png"
        attribute e4c:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e4c.png"
        attribute e4d:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e4d.png"
        attribute e4e:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e4e.png"
        attribute e0a:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e0a.png"
        attribute e0b:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e0b.png"
        attribute ela:
            "mod_assets/MPT/yuri/yuri_turned_eyes_ela.png"
        attribute elb:
            "mod_assets/MPT/yuri/yuri_turned_eyes_elb.png"
    
    group eyebrows:
        ### Default Eyebrows
        attribute brow default if_any(["fine", "neut"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1a.png"
        attribute brow default if_any(["flustered", "lightly_amazed", "laughing", "flus","lsur","laug"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1b.png"
        attribute brow default if_any(["aloof", "alluring", "dist","sedu"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1c.png"
        attribute brow default if_any(["annoyed", "anno"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1d.png"
        attribute brow default if_any(["very_angry", "angry", "vang","angr"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1e.png"
        attribute brow default if_any(["curious", "doubtful", "curi","doub"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1f.png"
        attribute brow default if_any(["happy", "happ"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b2a.png"
        attribute brow default if_any(["unease", "tense", "crying", "worr","sad","nerv","cry"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b2b.png"
        attribute brow default if_any(["yandere", "shocked", "very_amazed", "panicked", "yand","shoc","vsur","pani"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b2c.png"
        attribute brow default if_any(["pout"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b3b.png"
        
        
        ### All eyebrows
        ### Simple Syntax
        attribute brow_a:
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1a.png"
        attribute brow_b:
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1b.png"
        attribute brow_c if_not(["eyes_u", "eu", "eyes_l", "el", "eyes_m", "em", "eyes_n", "en", "shocked", "panicked", "very_amazed", "yandere", "e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1c.png"
        attribute brow_d if_not(["eyes_u", "eu", "eyes_l", "el", "eyes_m", "em", "eyes_n", "en", "shocked", "panicked", "very_amazed", "yandere", "e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1d.png"
        attribute brow_e if_not(["eyes_u", "eu", "eyes_l", "el", "eyes_m", "em", "eyes_n", "en", "shocked", "panicked", "very_amazed", "yandere", "e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1e.png"
        attribute brow_f:
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1f.png"
        attribute brow_g:
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b2a.png"
        attribute brow_h if_not(["eyes_u", "eu", "eyes_l", "el", "eyes_m", "em", "eyes_n", "en", "shocked", "panicked", "very_amazed", "yandere", "e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b2b.png"
        attribute brow_i:
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b2c.png"
        attribute brow_j if_not(["eyes_u", "eu", "eyes_l", "el", "eyes_m", "em", "eyes_n", "en", "shocked", "panicked", "very_amazed", "yandere", "e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b3a.png"
        attribute brow_k if_not(["eyes_u", "eu", "eyes_l", "el", "eyes_m", "em", "eyes_n", "en", "shocked", "panicked", "very_amazed", "yandere", "e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b3b.png"
        attribute brow_l:
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b3c.png"

        attribute brow_c if_any(["shoc","pani","vsur","yand"]) if_all(["closed_eyes"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1c.png"
        attribute brow_d if_any(["shoc","pani","vsur","yand"]) if_all(["closed_eyes"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1d.png"
        attribute brow_e if_any(["shoc","pani","vsur","yand"]) if_all(["closed_eyes"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1e.png"
        attribute brow_h if_any(["shoc","pani","vsur","yand"]) if_all(["closed_eyes"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b2b.png"
        attribute brow_j if_any(["shoc","pani","vsur","yand"]) if_all(["closed_eyes"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b3a.png"
        attribute brow_k if_any(["shoc","pani","vsur","yand"]) if_all(["closed_eyes"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b3b.png"

        attribute brow_c if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1c.png"
        attribute brow_d if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1d.png"
        attribute brow_e if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1e.png"
        attribute brow_h if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b2b.png"
        attribute brow_j if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b3a.png"
        attribute brow_k if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b3b.png"

        ### New MPT Syntax
        attribute ba:
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1a.png"
        attribute bb:
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1b.png"
        attribute bc if_not(["eyes_u", "eu", "eyes_l", "el", "eyes_m", "em", "eyes_n", "en", "shocked", "panicked", "very_amazed", "yandere", "e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1c.png"
        attribute bd if_not(["eyes_u", "eu", "eyes_l", "el", "eyes_m", "em", "eyes_n", "en", "shocked", "panicked", "very_amazed", "yandere", "e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1d.png"
        attribute be if_not(["eyes_u", "eu", "eyes_l", "el", "eyes_m", "em", "eyes_n", "en", "shocked", "panicked", "very_amazed", "yandere", "e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1e.png"
        attribute bf:
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1f.png"
        attribute bg:
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b2a.png"
        attribute bh if_not(["eyes_u", "eu", "eyes_l", "el", "eyes_m", "em", "eyes_n", "en", "shocked", "panicked", "very_amazed", "yandere", "e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b2b.png"
        attribute bi:
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b2c.png"
        attribute bj if_not(["eyes_u", "eu", "eyes_l", "el", "eyes_m", "em", "eyes_n", "en", "shocked", "panicked", "very_amazed", "yandere", "e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b3a.png"
        attribute bk if_not(["eyes_u", "eu", "eyes_l", "el", "eyes_m", "em", "eyes_n", "en", "shocked", "panicked", "very_amazed", "yandere", "e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b3b.png"
        attribute bl:
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b3c.png"

        attribute bc if_any(["shocked", "panicked", "very_amazed", "yandere", "shoc","pani","vsur","yand"]) if_all(["closed_eyes"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1c.png"
        attribute bd if_any(["shocked", "panicked", "very_amazed", "yandere", "shoc","pani","vsur","yand"]) if_all(["closed_eyes"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1d.png"
        attribute be if_any(["shocked", "panicked", "very_amazed", "yandere", "shoc","pani","vsur","yand"]) if_all(["closed_eyes"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1e.png"
        attribute bh if_any(["shocked", "panicked", "very_amazed", "yandere", "shoc","pani","vsur","yand"]) if_all(["closed_eyes"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b2b.png"
        attribute bj if_any(["shocked", "panicked", "very_amazed", "yandere", "shoc","pani","vsur","yand"]) if_all(["closed_eyes"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b3a.png"
        attribute bk if_any(["shocked", "panicked", "very_amazed", "yandere", "shoc","pani","vsur","yand"]) if_all(["closed_eyes"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b3b.png"

        attribute bc if_any(["shocked", "panicked", "very_amazed", "yandere", "shoc","pani","vsur","yand"]) if_all(["ce"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1c.png"
        attribute bd if_any(["shocked", "panicked", "very_amazed", "yandere", "shoc","pani","vsur","yand"]) if_all(["ce"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1d.png"
        attribute be if_any(["shocked", "panicked", "very_amazed", "yandere", "shoc","pani","vsur","yand"]) if_all(["ce"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1e.png"
        attribute bh if_any(["shocked", "panicked", "very_amazed", "yandere", "shoc","pani","vsur","yand"]) if_all(["ce"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b2b.png"
        attribute bj if_any(["shocked", "panicked", "very_amazed", "yandere", "shoc","pani","vsur","yand"]) if_all(["ce"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b3a.png"
        attribute bk if_any(["shocked", "panicked", "very_amazed", "yandere", "shoc","pani","vsur","yand"]) if_all(["ce"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b3b.png"
        
        ### Old MPT Syntax
        attribute b1a:
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1a.png"
        attribute b1b:
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1b.png"
        attribute b1c if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1c.png"
        attribute b1d if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1d.png"
        attribute b1e if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1e.png"
        attribute b1f:
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1f.png"
        attribute b2a:
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b2a.png"
        attribute b2b if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b2b.png"
        attribute b2c:
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b2c.png"
        attribute b3a if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b3a.png"
        attribute b3b if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b3b.png"
        attribute b3c:
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b3c.png"
        
        #This second set allows those above eyebrows to render on problematic moods...so long as their eyes are closed.
        attribute b1c if_any(["shoc","pani","vsur","yand"]) if_all(["closed_eyes"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1c.png"
        attribute b1d if_any(["shoc","pani","vsur","yand"]) if_all(["closed_eyes"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1d.png"
        attribute b1e if_any(["shoc","pani","vsur","yand"]) if_all(["closed_eyes"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1e.png"
        attribute b2b if_any(["shoc","pani","vsur","yand"]) if_all(["closed_eyes"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b2b.png"
        attribute b3a if_any(["shoc","pani","vsur","yand"]) if_all(["closed_eyes"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b3a.png"
        attribute b3b if_any(["shoc","pani","vsur","yand"]) if_all(["closed_eyes"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b3b.png"

        attribute b1c if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1c.png"
        attribute b1d if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1d.png"
        attribute b1e if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1e.png"
        attribute b2b if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b2b.png"
        attribute b3a if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b3a.png"
        attribute b3b if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b3b.png"
    
    group special:
        attribute special_scream:
            "mod_assets/MPT/yuri/yuri_turned_special_scream.png"

        attribute s_scream:
            "mod_assets/MPT/yuri/yuri_turned_special_scream.png"

    ## For use if NBE assets is installed
    # group blink:
    #     attribute blink_a default if_not(["closed_eyes", "ce","eyes_o","eyes_p","eyes_q","eyes_r","eyes_s","eyes_t", "eyes_e", "eyes_f","e4a","e4b","e4c","e4d","e4f","e4e","e1e","e1f"]):
    #         "_yur_blink_a"
    #     attribute no_blink:
    #         "sprite_blank"

layeredimage yuri shy:
    at Flatten
    
    always "mod_assets/MPT/yuri/yuri_shy_facebase.png"
    
    group outfit:
        attribute uniform default null
        attribute casual null
    
    group mood:
        attribute angry null 
        attribute happy null 

        attribute angr null #angry
        attribute happ null #happy
        attribute sad null  #sad

    group blush:
        attribute no_blush default null
        attribute awkward null 
        attribute blushing null 
        attribute awkward_blushing null 
        attribute full_face_blush null 

        attribute nobl default null #No blush.
        attribute awkw null #awkward.  defaults for n
        attribute blus null #blushing.  defaults for n
        attribute blaw null #blushing AND awkward.  defaults for n
        attribute bful null #full face blush.  Currently only works on the side face.
    
    group body:
        attribute body default if_any(["uniform"]):
            "mod_assets/MPT/yuri/yuri_shy_uniform_bodybase.png"
        attribute body default if_any(["casual"]):
            "mod_assets/MPT/yuri/yuri_shy_casual_bodybase.png"
    
    group nose:
        ### Default nose
        attribute nose default if_any(["no_blush","nobl"]):#default nose
            "mod_assets/MPT/yuri/yuri_shy_nose_n1.png"
        attribute nose default if_any(["awkward", "awkw"]):#default nose when "awkward"
            "mod_assets/MPT/yuri/yuri_shy_nose_n2.png"
        attribute nose default if_any(["blushing", "blus"]):#default nose when "blushing"
            "mod_assets/MPT/yuri/yuri_shy_nose_n3.png"
        attribute nose default if_any(["awkward_blushing", "blaw"]):#default nose when "blushing" and "awkward"
            "mod_assets/MPT/yuri/yuri_shy_nose_n4.png"
        attribute nose default if_any(["full_face_blush", "bful"]):#Full face blush
            "mod_assets/MPT/yuri/yuri_shy_nose_n5.png"
        
        ### All noses
        ### Simple Syntax
        attribute nose_1:
            "mod_assets/MPT/yuri/yuri_shy_nose_n1.png"
        attribute nose_2:
            "mod_assets/MPT/yuri/yuri_shy_nose_n2.png"
        attribute nose_3:
            "mod_assets/MPT/yuri/yuri_shy_nose_n3.png"
        attribute nose_4:
            "mod_assets/MPT/yuri/yuri_shy_nose_n4.png"
        attribute nose_5:
            "mod_assets/MPT/yuri/yuri_shy_nose_n5.png"

        attribute n1:
            "mod_assets/MPT/yuri/yuri_shy_nose_n1.png"
        attribute n2:
            "mod_assets/MPT/yuri/yuri_shy_nose_n2.png"
        attribute n3:
            "mod_assets/MPT/yuri/yuri_shy_nose_n3.png"
        attribute n4:
            "mod_assets/MPT/yuri/yuri_shy_nose_n4.png"
        attribute n5:
            "mod_assets/MPT/yuri/yuri_shy_nose_n5.png"
    
    group mouth:
        ### Closed Mouths
        attribute closed_mouth default if_any(["fine", "neut"]):
            "mod_assets/MPT/yuri/yuri_shy_mouth_m1.png"
        attribute closed_mouth default if_any(["angry", "angr","sad"]):
            "mod_assets/MPT/yuri/yuri_shy_mouth_m2.png"
        attribute closed_mouth default if_any(["happy", "happ"]):
            "mod_assets/MPT/yuri/yuri_shy_mouth_m3.png"

        attribute cm default if_any(["fine", "neut"]):
            "mod_assets/MPT/yuri/yuri_shy_mouth_m1.png"
        attribute cm default if_any(["angry", "angr","sad"]):
            "mod_assets/MPT/yuri/yuri_shy_mouth_m2.png"
        attribute cm default if_any(["happy", "happ"]):
            "mod_assets/MPT/yuri/yuri_shy_mouth_m3.png"
        
        ### Open Mouth
        attribute open_mouth:
            "mod_assets/MPT/yuri/yuri_shy_mouth_m4.png"

        attribute om:
            "mod_assets/MPT/yuri/yuri_shy_mouth_m4.png"
        
        ### All mouths
        ### Simple Syntax
        attribute mouth_a:
            "mod_assets/MPT/yuri/yuri_shy_mouth_m1.png"
        attribute mouth_b:
            "mod_assets/MPT/yuri/yuri_shy_mouth_m2.png"
        attribute mouth_c:
            "mod_assets/MPT/yuri/yuri_shy_mouth_m3.png"
        attribute mouth_d:
            "mod_assets/MPT/yuri/yuri_shy_mouth_m4.png"

        ### New MPT Syntax
        attribute ma:
            "mod_assets/MPT/yuri/yuri_shy_mouth_m1.png"
        attribute mb:
            "mod_assets/MPT/yuri/yuri_shy_mouth_m2.png"
        attribute mc:
            "mod_assets/MPT/yuri/yuri_shy_mouth_m3.png"
        attribute md:
            "mod_assets/MPT/yuri/yuri_shy_mouth_m4.png"

        ### Old MPT Syntax
        attribute m1:
            "mod_assets/MPT/yuri/yuri_shy_mouth_m1.png"
        attribute m2:
            "mod_assets/MPT/yuri/yuri_shy_mouth_m2.png"
        attribute m3:
            "mod_assets/MPT/yuri/yuri_shy_mouth_m3.png"
        attribute m4:
            "mod_assets/MPT/yuri/yuri_shy_mouth_m4.png"
    
    group eyes if_not(["nose5", "full_face_blush", "n5","bful"]): #Cannot show if full-face blush is present.
        ### Open eyes
        attribute open_eyes default if_any(["happy", "happ"]):
            "mod_assets/MPT/yuri/yuri_shy_eyes_e1.png"
        attribute open_eyes default if_any(["fine", "neut"]):
            "mod_assets/MPT/yuri/yuri_shy_eyes_e2.png"
        attribute open_eyes default if_any(["angry", "angr"]):
            "mod_assets/MPT/yuri/yuri_shy_eyes_e3.png"
        attribute open_eyes default if_any(["sad"]):
            "mod_assets/MPT/yuri/yuri_shy_eyes_e4.png"

        attribute oe default if_any(["happy", "happ"]):
            "mod_assets/MPT/yuri/yuri_shy_eyes_e1.png"
        attribute oe default if_any(["fine", "neut"]):
            "mod_assets/MPT/yuri/yuri_shy_eyes_e2.png"
        attribute oe default if_any(["angry", "angr"]):
            "mod_assets/MPT/yuri/yuri_shy_eyes_e3.png"
        attribute oe default if_any(["sad"]):
            "mod_assets/MPT/yuri/yuri_shy_eyes_e4.png"
        
        ### Closed eyes
        attribute closed_eyes if_any(["angry", "fine", "happy", "angr","neut","happ"]):
            "mod_assets/MPT/yuri/yuri_shy_eyes_e5.png"
        attribute closed_eyes if_any(["sad"]):
            "mod_assets/MPT/yuri/yuri_shy_eyes_e6.png"

        attribute ce if_any(["angry", "fine", "happy", "angr","neut","happ"]):
            "mod_assets/MPT/yuri/yuri_shy_eyes_e5.png"
        attribute ce if_any(["sad"]):
            "mod_assets/MPT/yuri/yuri_shy_eyes_e6.png"
        
        
        ### All eyes
        ### Simple Syntax
        attribute eyes_a:
            "mod_assets/MPT/yuri/yuri_shy_eyes_e1.png"
        attribute eyes_b:
            "mod_assets/MPT/yuri/yuri_shy_eyes_e2.png"
        attribute eyes_c:
            "mod_assets/MPT/yuri/yuri_shy_eyes_e3.png"
        attribute eyes_d:
            "mod_assets/MPT/yuri/yuri_shy_eyes_e4.png"
        attribute eyes_e:
            "mod_assets/MPT/yuri/yuri_shy_eyes_e5.png"
        attribute eyes_f:
            "mod_assets/MPT/yuri/yuri_shy_eyes_e6.png"

        ### New MPT Syntax
        attribute ea:
            "mod_assets/MPT/yuri/yuri_shy_eyes_e1.png"
        attribute eb:
            "mod_assets/MPT/yuri/yuri_shy_eyes_e2.png"
        attribute ec:
            "mod_assets/MPT/yuri/yuri_shy_eyes_e3.png"
        attribute ed:
            "mod_assets/MPT/yuri/yuri_shy_eyes_e4.png"
        attribute ee:
            "mod_assets/MPT/yuri/yuri_shy_eyes_e5.png"
        attribute ef:
            "mod_assets/MPT/yuri/yuri_shy_eyes_e6.png"

        ### Old MPT Syntax
        attribute e1:
            "mod_assets/MPT/yuri/yuri_shy_eyes_e1.png"
        attribute e2:
            "mod_assets/MPT/yuri/yuri_shy_eyes_e2.png"
        attribute e3:
            "mod_assets/MPT/yuri/yuri_shy_eyes_e3.png"
        attribute e4:
            "mod_assets/MPT/yuri/yuri_shy_eyes_e4.png"
        attribute e5:
            "mod_assets/MPT/yuri/yuri_shy_eyes_e5.png"
        attribute e6:
            "mod_assets/MPT/yuri/yuri_shy_eyes_e6.png"
    
    group eyebrows if_not(["nose5", "full_face_blush", "n5","bful"]): #Cannot show if full-face blush is present.
        ### Default eyebrows
        attribute brow default if_any(["happy", "happ"]):
            "mod_assets/MPT/yuri/yuri_shy_eyebrows_b1.png"
        attribute brow default if_any(["fine", "neut","sad"]):
            "mod_assets/MPT/yuri/yuri_shy_eyebrows_b2.png"
        attribute brow default if_any(["angry", "angr"]):
            "mod_assets/MPT/yuri/yuri_shy_eyebrows_b3.png"
        
        ### All eyebrows
        ### Simple Syntax
        attribute brow_a:
            "mod_assets/MPT/yuri/yuri_shy_eyebrows_b1.png"
        attribute brow_b:
            "mod_assets/MPT/yuri/yuri_shy_eyebrows_b2.png"
        attribute brow_c:
            "mod_assets/MPT/yuri/yuri_shy_eyebrows_b3.png"

        ### New MPT Syntax
        attribute ba:
            "mod_assets/MPT/yuri/yuri_shy_eyebrows_b1.png"
        attribute bb:
            "mod_assets/MPT/yuri/yuri_shy_eyebrows_b2.png"
        attribute bc:
            "mod_assets/MPT/yuri/yuri_shy_eyebrows_b3.png"

        ### Old MPT Syntax
        attribute b1:
            "mod_assets/MPT/yuri/yuri_shy_eyebrows_b1.png"
        attribute b2:
            "mod_assets/MPT/yuri/yuri_shy_eyebrows_b2.png"
        attribute b3:
            "mod_assets/MPT/yuri/yuri_shy_eyebrows_b3.png"

    ## For use if NBE assets is installed
    # group blink:
    #     attribute blink_a default if_not(["closed_eyes", "eyes_e", "eyes_f", "nose5", "full_face_blush", "ce","e5","e6","n5", "bful"]):
    #         "_yur_blink_s_a"
    #     attribute no_blink:
    #         "sprite_blank"

image _yur_blink_a:
    alpha 0.0
    renpy.random.randint(20, 100)*0.1
    choice:
        alpha 1.0
        "mod_assets/MPT/yuri/_blink_am.png"
        0.015
        "mod_assets/MPT/yuri/yuri_turned_eyes_e4a.png"
        0.035
        "mod_assets/MPT/yuri/_blink_am.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/yuri/_blink_am.png"
        0.015
        "mod_assets/MPT/yuri/yuri_turned_eyes_e4a.png"
        0.065
        "mod_assets/MPT/yuri/_blink_am.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/yuri/_blink_am.png"
        0.015
        "mod_assets/MPT/yuri/yuri_turned_eyes_e4a.png"
        0.095
        "mod_assets/MPT/yuri/_blink_am.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/yuri/_blink_am.png"
        0.015
        "mod_assets/MPT/yuri/yuri_turned_eyes_e4a.png"
        0.035
        "mod_assets/MPT/yuri/_blink_am.png"
        0.015
        alpha 0.0
        0.15
        alpha 1.0
        "mod_assets/MPT/yuri/_blink_am.png"
        0.015
        "mod_assets/MPT/yuri/yuri_turned_eyes_e4a.png"
        0.035
        "mod_assets/MPT/yuri/_blink_am.png"
        0.015
    repeat

image _yur_blink_s_a:
    alpha 0.0
    renpy.random.randint(30, 60)*0.1
    choice:
        alpha 1.0
        "mod_assets/MPT/yuri/_blink_s_am.png"
        0.015
        "mod_assets/MPT/yuri/_blink_s_af.png"
        0.035
        "mod_assets/MPT/yuri/_blink_s_am.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/yuri/_blink_s_am.png"
        0.015
        "mod_assets/MPT/yuri/_blink_s_af.png"
        0.065
        "mod_assets/MPT/yuri/_blink_s_am.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/yuri/_blink_s_am.png"
        0.015
        "mod_assets/MPT/yuri/_blink_s_af.png"
        0.095
        "mod_assets/MPT/yuri/_blink_s_am.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/yuri/_blink_s_am.png"
        0.015
        "mod_assets/MPT/yuri/_blink_s_af.png"
        0.035
        "mod_assets/MPT/yuri/_blink_s_am.png"
        0.015
        alpha 0.0
        0.15
        alpha 1.0
        "mod_assets/MPT/yuri/_blink_s_am.png"
        0.015
        "mod_assets/MPT/yuri/_blink_s_af.png"
        0.035
        "mod_assets/MPT/yuri/_blink_s_am.png"
        0.015
    repeat
