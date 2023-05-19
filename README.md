# Welcome to ExPoser 2.0!
> This branch is unstable. Pushes may either work or not work whenever one is submitted. Do not run this in your mod project until its released unless you want to test it.

ExPoser 2.0 is a new expression tool that provides an easier posing experience for Ren'Py 7+ modders for any character they wish to pose for .

## Features
- Improved posing syntax.
- Improved pathing system.
- Improved asset groups.
- Imporved directories
- Natural Blinking Expression Integration Support
   > As of today, you have to install NBE's asset files (not the RPY code) onto your mod project and uncomment the `blink` group in each characters' layeredimage file in order for NBE to work.

## How to use ExPoser 2.0?
ExPoser 2.0 is pretty similar to that of MPT (Mood Pose Tool), however it is different in how the bases are called.

For example, if we were to express Sayori in a casual outfit with an awkward expression:

MPT (Mood Pose Tool)
```py
show sayori turned casual awkw
```
However for ExPoser 2.0, it is now 
```py
show sayori base casual eh
```

There are a lot of syntax to cover so if you are interested in getting started, why not look at the syntax available in this PDF (TBA) file and learn how to use ExPoser 2.0 to it's full use.

## What do you need to use ExPoser
1. A mod you are working on.
2. (Optional) Natural Blinking Expressions

## Install Guide
1. Open ExPoser's ZIP file, and copy all of it's assets over to your mod. Replace any files if requested.
2. (Optional) Copy the files in each characters' folders in `the NBE ZIP folder/game/mod_assets/MPT/<character>` over to ExPoser in `your mod folder/game/mod_assets/ExP/<character>/blinks`.
3. (If you did step 3) Uncommment the `blink` groups in each characters' layered image RPY file.
4. Done!

## Credits
- u/ZachmanAwesomenessII - Fixed Poses for Natsuki's `fta`/`turned_away_face` pose.
- Willinisian - Natural Blinking Expressions Code
- NekoLaiS - Pathing system inspiration.

Copyright © 2023 GanstaKingofSA. All rights reserved. The ExPoser project is unaffiliated with Team Salvato. 
