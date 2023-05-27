A 15 hour project I've been meaning to do for over two years but something always pops up.

### "But why" I hear you ask.
I yearn for simplicity in my hectic, complicated existence. Home assistant is like using a sledgehammer to crack a walnut for what I need. Discord is part of my daily life for a million and one reasons, so why not? However, if any of you poor souls fancy adding something else into the mix, please, get a coffee and have some asprin on the side and go for it.

### "But how" I hear you ask.
Schopenhauer would be proud. Discord bot does the hokey-pokey with a container running the app on the local network. This, in turn, shakes hands with a microcontroller that's  doing whatever it's doing on the same network.

### Why Docker, though?
Well I run this on a slightly-better-than-a-raspberry-pi office PC, crammed into the dusty, forgotten corner of my apartment, juggling a random collection of self-hosted stuff like a circus act.

### And why Python?
Oh, how I wished to evade the python's slithering coils, but alas! An excude to not having to arm-wrestle with mutexes and locks. But above all, there's the ability to toss in more crap at runtime without having to reboot the service or any other annoying crap.

### How do you do it?
Well, Sherlock, feast your eyes on the commands.yaml under `local/`. Copy the entry, make a few tweaks here and there, save and voila – you're a config-writing Picasso! Masterpiece! No need to hit the restart button. Oh and don't forget to registera Discord bot with read and write message intent, copy `local/example_env` into `local/.env` and put your Discord token there. Hook it up to a private channel, or public if you're a thrill-seeker, looking to be a massive trolling target.

### What now?
In case you're still lost in this jigsaw the same way I am:

![woah](/assets/woah.gif "woah")

There you have it, I've emptied my wisdom basket. Peace out!
