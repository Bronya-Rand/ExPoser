# Welcome to ExPoser!

ExPoser is a WIP expression tool based off u/chronoshag's Mood Pose Tool (MPT) that attempts to fix MPT related bugs and provide a easier posing experience for Ren'Py 7 modders whether they are new to modding or not.

## What has changed from MPT?
All code in ExPoser is based off MPT and should work the same as intended for all projects except for one condition.

Many users have communicated some issues in regards to how MPT separates a special pose and a base pose. Mood Pose Tool normally defines the special poses fine such as `tap`, `lean`, `cross` for Sayori, Monika and Natsuki, but for base poses, it changes it to be a unusual mix of `turned` for Sayori, Natsuki and Yuri and `forward` for Monika alone. 

ExPoser addresses this by renaming these `turned`/`forward` to `base` which stands for their normal poses (don't confuse this for their outfits). Due to this, if you are transferring from MPT to ExPoser, you will need to change the MPT syntax over to ExPoser's new syntax.

Example:

In Mood Pose Tool you will call a awkward Sayori as such.
```py
show sayori turned casual awkw
```
In ExPoser however, you will call Sayori like this instead
```py
show sayori base casual awkw
```

Additionally there is now new syntaxes available that actually makes posing easier to understand with actual english words to describe the poses themselves over the traditional MPT syntax for newcomers to get into modding.

Example:

In Mood Pose Tool you will call a awkward Sayori as such.
```py
show sayori turned casual awkw
```
In ExPoser however, you will call Sayori like this instead
```py
show sayori base casual awkward
```
You can still use the MPT syntax however. This is just a easier way to call it for newcomers than referring to a long guide list and trying to understand each var for debugging purposes.

There are a lot of new syntax changes to cover so if you are interested in getting started, why not look at the new syntax available in this [PDF](New%20Tool%20Syntax%20Guide.pdf) file and learn how to use ExPoser for your daily needs.

Copyright 2022 GanstaKingofSA. All rights reserved. The ExPoser project is unaffiliated with the Mood Pose Tool team and Team Salvato. 