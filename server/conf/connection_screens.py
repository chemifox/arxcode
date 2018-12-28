# -*- coding: utf-8 -*-
"""
Connection screen

Texts in this module will be shown to the user at login-time.

Evennia will look at global string variables (variables defined
at the "outermost" scope of this module and use it as the
connection screen. If there are more than one, Evennia will
randomize which one it displays.

The commands available to the user when the connection screen is shown
are defined in commands.default_cmdsets.UnloggedinCmdSet and the
screen is read and displayed by the unlogged-in "look" command.

"""

from django.conf import settings
from evennia import utils

CONNECTION_SCREEN = \
"""{w=============================================================={n

                    {gWelcome to Ithir{n
                    
 Ithir is a high fantasy MUSH in an original setting. Please
 visit our website at http://ithirmush.org for more info.
                                    

 If you have an existing account, connect to it by typing:
      {gconnect <username> <password>{n
      
 To join the game by creating a character or choosing one
 from our roster of characters, first login as a guest by
 typing '{gguest{n' and then use either the {g@roster{n command,
 or the '{g@charcreate <email>{n' command.
 
 Enter {whelp{n for more info. {wlook{n will re-show this screen.
 
{w=============================================================={n"""
