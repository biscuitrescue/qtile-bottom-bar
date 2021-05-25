# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

###3from typing import List  # noqa: F401

#####from libqtile import bar, layout, widget
#####from libqtile.config import Click, Drag, Group, Key, Screen
#####from libqtile.lazy import lazy
#####from libqtile.utils import guess_terminal
#####from libqtile.config import Group, Match
#####from libqtile.dgroups import simple_key_binder


#import os
#import re
#import socket
#import subprocess
#import qtilea
#from libqtile.config import Drag, Key, Screen, Group, Drag, Click, Rule
#from libqtile.command import lazy
#from libqtile import layout, bar, widget, hook
#from libqtile.widget import Spacer

import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from typing import List  # noqa: F401


#mod4 or mod = super key
mod = "mod4"
mod1 = "mod1"
mod2 = "control"
mod3  = "shift"
home = os.path.expanduser('~')
myTerm = "kitty"

@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

#############################################
############ SHORTCUTS ######################
#############################################


keys = [
#    Key([mod], "x", lazy.spawn("poweroff")),
    #Key([mod], "d", lazy.spawn("rofi -show drun")),
    Key([mod], "x", lazy.spawn("sh .config/polybar.new/colorblocks/scripts/powermenu.sh")),
    #Key([mod, "shift"], "s", lazy.spawn("./git/polybar-themes/simple/scripts/color-switch.sh")),
    Key([mod, "shift"], "d", lazy.spawn("rofi -show drun")),
    Key([mod], "d", lazy.spawn("dmenu_run -fn 'Novamono for Powerline-12' -nb '#000000' -nf '#ffffff' -sb '#e2d5dc' -sf '#000000' -p 'RUN:'")),


##################################################
################# MEDIA CONTROLS #################
##################################################

# INCREASE/DECREASE/MUTE VOLUME
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),

    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("light -A 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("light -U 5")),
    Key([mod], "XF86MonBrightnessDown", lazy.spawn("light -S 0")),
    Key([mod], "XF86MonBrightnessUp", lazy.spawn("light -S 10")),



    # Switch between windows in current stack pane
###################################################
################  SWITCH LAYOUT ###################
###################################################

# TOGGLE FLOATING LAYOUT
    Key([mod, "control"], "a", lazy.window.toggle_floating()),

    # CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "o", lazy.layout.left()),
    Key([mod], "p", lazy.layout.right()),
    Key([mod], "l",lazy.layout.grow(), lazy.layout.increase_nmaster()),
    Key([mod], "m", lazy.layout.shrink(), lazy.layout.decrease_nmaster()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "w", lazy.window.toggle_fullscreen()),
# FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "shift"], "f", lazy.layout.flip()),

# MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),
    Key([mod], "period", lazy.layout.next()),
    Key([mod], "s", lazy.layout.next()),
    Key([mod], "comma", lazy.layout.previous()),
    Key([mod, "shift"], "space", lazy.layout.rotate()),

#########################################
############### BSPWM ###################
#########################################
    Key([mod], "Down", lazy.layout.down()),
Key([mod], "Up", lazy.layout.up()),
Key([mod], "Left", lazy.layout.left()),
Key([mod], "Right", lazy.layout.right()),
Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
Key([mod, "shift"], "Left", lazy.layout.shuffle_left()),
Key([mod, "shift"], "Right", lazy.layout.shuffle_right()),
Key([mod, "mod1"], "Down", lazy.layout.flip_down()),
Key([mod, "mod1"], "Up", lazy.layout.flip_up()),
Key([mod, "mod1"], "Left", lazy.layout.flip_left()),
Key([mod, "mod1"], "Right", lazy.layout.flip_right()),
Key([mod, "control"], "Down", lazy.layout.grow_down()),
Key([mod, "control"], "Up", lazy.layout.grow_up()),
Key([mod, "shift"], "l", lazy.layout.grow_left()),
Key([mod, "shift"], "m", lazy.layout.grow_right()),
Key([mod, "shift"], "n", lazy.layout.normalize()),
Key([mod], "z", lazy.layout.toggle_split()),



 # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "a", lazy.prev_layout()),
    Key([mod], "q", lazy.window.kill()),
    Key([mod, "shift"], "q", lazy.shutdown()),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod], "r", lazy.spawncmd()),
    Key([mod, "shift"], "x", lazy.spawn("poweroff")),
##############################################
############## SCREENSHOTS ###################
##############################################

    Key([], "Print", lazy.spawn("scrot 'screenshot_%Y%m%d_%H%M%S.png' -e 'mkdir -p ~/Pictures/screenshots && mv $f ~/Pictures/screenshots && xclip -selection clipboard -t image/png -i ~/Pictures/screenshots/`ls -1 -t ~/Pictures/screenshots | head -1`'")),

    Key(["shift"], "Print", lazy.spawn("scrot -s 'screenshot_%Y%m%d_%H%M%S.png' -e 'mkdir -p ~/Pictures/screenshots && mv $f ~/Pictures/screenshots && xclip -selection clipboard -t image/png -i ~/Pictures/screenshots/`ls -1 -t ~/Pictures/screenshots | head -1`'")),
#####################3#########################
############## APPLICATIONS ###################
###############################################

    Key([mod, "shift"], "h", lazy.spawn("kitty -e htop")),
    Key([mod], "space", lazy.spawn("alacritty -e fish")),
    Key([mod, "shift"], "s", lazy.spawn("kitty -e devour LD_PRELOAD=/usr/local/lib/spotify-adblock.so spotify")),
    Key([mod, "shift"], "Return", lazy.spawn("kitty -e lf")),
    Key([mod, "shift"], "space", lazy.spawn("pcmanfm")),
    Key([mod], "i", lazy.spawn("betterlockscreen -l")),
    Key([mod, "shift"], "i", lazy.spawn("i3lock -c 000000")),
    Key([mod], "Return", lazy.spawn(myTerm)),
    Key([mod1, mod2], "v", lazy.spawn("vivaldi")),
    Key([mod], "v", lazy.spawn("pavucontrol")),
    Key([mod], "e", lazy.spawn("emacs")),
    Key([mod1, "control"], "n", lazy.spawn("pcmanfm")),
    Key([mod, "shift"], "p", lazy.spawn("qutebrowser")),
    Key([mod, "shift"], "o", lazy.spawn("kitty -e paru")),
    ]
groups = []
groups = []

# FOR QWERTY KEYBOARDS
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]


#group_labels = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",]

group_labels = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",]

group_layouts = ["monadtall", "monadwide", "monadtall", "max", "monadtall", "max", "bsp", "monadtall"
       , "max", "monadtall",]


for i in range(len(group_names)):
        groups.append(
        Group(
        name=group_names[i],
        layout=group_layouts[i].lower(),
        label=group_labels[i],
    ))

for i in groups:
        keys.extend([

# CHANGE WORKSPACES
    Key([mod], i.name, lazy.group[i.name].toscreen()),
    Key(["mod1"], "Tab", lazy.screen.next_group()),
    Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),


    Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
        ])
#LAYOUTS
#LAYOUTS
layouts = [
    # layout.Stack(num_stacks=2),
    # layout.Columns(margin=7, border_width=4, border_focus="#ffffff", border_normal="#4c566a", ),
    # layout.Matrix(),
    # layout.RatioTile(margin=7)
    # layout.Tile(margin=7, border_width=3, border_focus="#ffffff", border_normal="#4c566a", new_client_position='top', ratio=0.55),
    # layout.VerticalTile(),
    # layout.Zoomy(
    #    margin=7,
    #    columnwidth=300,
    #),
    layout.MonadTall(margin=8, border_width=4, border_focus="#bc7cf7", border_normal="#4c566a" ),
    layout.MonadWide(margin=8, border_width=4, border_focus="#bc7cf7", border_normal="#4c566a" ),
    layout.Bsp(margin=8, border_width=4, border_focus="#bc7cf7", border_normal="4c566a", fair=False),
    #layout.Tile(margin=8, border_width=4, border_focus="#ffffff", border_normal="#4c566a", ratio=0.5, shift_windows=True),
    #layout.TreeTab(
    #        active_bg = 'ffffff',
    #        active_fg = '000000',
    #        bg_color = '293136',
    #        font = 'novamono for powerline',
    #        fontsize = 15,
    #        panel_width = 200,
    #        inactive_bg = 'a1acff',
    #        inactive_fg = '000000',
    #        sections = ['Qtile'],
    #        section_fontsize = 18,
    #       section_fg = 'ffffff',
    #        section_left = 70
    #),
    layout.Max(),
]


colors =  [
        ["#1b1c26", "#14151C", "#1b1c26"], # color 0
        ["#485062", "#485062", "#485062"], # color 1
        ["#65bdd8", "#65bdd8", "#65bdd8"], # color 2
        ["#bc7cf7", "#a269cf", "#bc7cf7"], # color 3
        ["#aed1dc", "#98B7C0", "#aed1dc"], # color 4
        ["#ffffff", "#ffffff", "#ffffff"], # color 5
        ["#bb94cc", "#AB87BB", "#bb94cc"], # color 6
        ["#9859B3", "#8455A8", "#9859B3"], # color 7
        ["#744B94", "#694486", "#744B94"], # color 8
        ["#0ee9af", "#0ee9af", "#0ee9af"]] # color 9



widget_defaults = dict(
    font='andale mono',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper='/home/trogdor/Pictures/Wallpapers/pinkic.jpg',
        wallpaper_mode='fill',
        top=bar.Bar(
        [
            widget.Sep(
                background=colors[8],
                padding=15,
                linewidth=0,
            ),
            widget.Clock(
                font="novamono for powerline",
                fontsize=14,
                foreground=colors[5],
                background=colors[8],
                format='%d %b | %A'
            ),
            widget.TextBox(
                text="\ue0b4",
                fonts="droid sans mono for powerline",
                foreground=colors[8],
                background=colors[7],
                padding=0,
                fontsize=33
            ),
            widget.Sep(
                background=colors[7],
                padding=12,
                linewidth=0,
            ),
            widget.CurrentLayout(
                background=colors[7],
                foreground=colors[5],
                font="novamono for powerline",
                fontsize=13,
            ),
            widget.CurrentLayoutIcon(
                custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                foreground=colors[1],
                background=colors[7],
                padding=0,
                scale=0.5
            ),
            widget.TextBox(
                text="\ue0b4",
                fonts="droid sans mono for powerline",
                foreground=colors[7],
                background=colors[3],
                padding=0,
                fontsize=33
            ),
            widget.CPU(
                background=colors[3],
                foreground=colors[5],
                format=' CPU: {load_percent}%',
                font='novamono for powerline bold',
                fontsize=14
            ),
            widget.TextBox(
                text="\ue0b4",
                fonts="droid sans mono for powerline",
                foreground=colors[3],
                padding=0,
                fontsize=33
            ),

            widget.Spacer(),

            widget.GroupBox(
                font="FontAwesome",
                fontsize=10,
                active=colors[6],
                inactive=colors[1],
                rounded=True,
                highlight_color=colors[0],
                highlight_method="line",
                this_current_screen_border=colors[0],
                block_highlight_text_color=colors[2],
                blockwidth=2,
                margin_y=5,
            ),
            
            widget.Spacer(),

            widget.TextBox(
                text="\uE0B6",
                fonts="droid sans mono for powerline",
                foreground=colors[3],
                padding=0,
                fontsize=33
            ),
            widget.TextBox(
                text=" 🖬",
                foreground=colors[5],
                background=colors[3],
                padding=0,
                fontsize=18
            ),
            widget.Memory(
                background=colors[3],
                foreground=colors[5],
                font="novamono for powerline bold",
                fontsize=14,
                format='{MemUsed: .0f} MB |',
            ),
            widget.Sep(
                background=colors[3],
                padding=6,
                linewidth=0,
            ),
            widget.Systray(
                background=colors[3],
                icons_size=20,
                padding=4,
            ),
            widget.Sep(
                background=colors[3],
                padding=10,
                linewidth=0,
            ),
            widget.TextBox(
                text="\uE0B6",
                fonts="droid sans mono for powerline",
                foreground=colors[4],
                background=colors[3],
                padding=0,
                fontsize=33
            ),
            widget.Volume(
                background=colors[4],
                foreground=colors[0],
                font="novamono for powerline bold",
                fontsize=15.25,
                mouse_callbacks={'Button3': lambda: qtile.cmd_spawn("pavucontrol")},
            ),
            widget.Sep(
                background=colors[4],
                padding=10,
                linewidth=0,
            ),
            widget.TextBox(
                text="\uE0B6",
                fonts="droid sans mono for powerline",
                foreground=colors[7],
                background=colors[4],
                padding=0,
                fontsize=33
            ),
            widget.Sep(
                background=colors[7],
                padding=6,
                linewidth=0,
            ),
            widget.TextBox(
                text=' ',
                fontsize='16',
                background=colors[7],
                foreground=colors[5],
            ),
            widget.Battery(
                background=colors[7],
                foreground=colors[5],
                charge_char='↑',
                discharge_char='↓',
                font="novamono for powerline bold",
                fontsize=14,
                update_interval=1,
                format='{percent:2.0%}'
            ),
            widget.Sep(
                background=colors[7],
                padding=6,
                linewidth=0,
            ),
            widget.TextBox(
                text="\uE0B6",
                fonts="droid sans mono for powerline",
                foreground=colors[8],
                background=colors[7],
                padding=0,
                fontsize=33
            ),
            widget.Sep(
                background=colors[8],
                padding=6,
                linewidth=0,
            ),
            widget.Clock(
                background=colors[8],
                foreground=colors[5],
                font="novamono for powerline",
                fontsize=15,
                format='%I:%M %p',
            ),
            widget.Sep(
                background=colors[8],
                padding=10,
                linewidth=0,
            ),
        ],
            39,
            background=colors[0],
            margin=[8,8,0,8],
            opacity=0.9,
        ),
    ),
]
#############################################
############# AUTOSTART #####################
#############################################
@hook.subscribe.startup_once
def autostart():
    processes = [
        ['connman-gtk'],
        ['blueman-applet'],
        ['picom']
    ]

    for p in processes:
        subprocess.Popen(p)


# Drag floating layouts.
mouse = [
    Drag([mod], "Button3", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button1", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(

    border_focus="#ffffff",
    border_width=6,
    float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(title='Confirmation'),      # tastyworks exit box
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
    {'wmclass': 'About Tor - Tor Browser'},
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
