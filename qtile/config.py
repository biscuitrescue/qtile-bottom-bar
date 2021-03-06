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
    Key([], "F4", lazy.spawn("rofi -show drun")),
    Key([mod], "d", lazy.spawn("dmenu_run -fn 'novamono for powerline-12' -nb '#1b1c26' -nf '#ffffff' -sb '#aed1dc' -sf '#000000' -p 'RUN:'")),
    Key([], "XF86Search", lazy.spawn("dmenu_run -fn 'novamono for powerline-12' -nb '#1b1c26' -nf '#ffffff' -sb '#aed1dc' -sf '#000000' -p 'RUN:'")),


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
    Key([mod], "c", lazy.restart()),
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

    Key([mod], "space", lazy.spawn("st")),
    Key([mod, "shift"], "s", lazy.spawn("spotify")),
    Key([], "XF86Tools", lazy.spawn("spotify")),
    Key([mod, "shift"], "space", lazy.spawn("pcmanfm")),
    Key([mod, "shift"], "a", lazy.spawn("i3lock -c 000000")),
    Key([], "F6", lazy.spawn("betterlockscreen -l pixel")),
    Key([mod], "Return", lazy.spawn(myTerm)),
    Key([mod], "KP_Enter", lazy.spawn(myTerm)),
    Key([mod], "v", lazy.spawn("pavucontrol")),
    Key([mod], "e", lazy.spawn("emacs")),

    KeyChord([mod], "i",[
        Key([], "f", lazy.spawn("firefox")),
        Key([], "v", lazy.spawn("vivaldi-stable")),
        Key([], "b", lazy.spawn("brave")),
        Key([], "l", lazy.spawn("librewolf")),
    ]),
    ]

groups= [
    Group("1",
          label="???",
          spawn='brave',
          matches=[Match(wm_class=["firefox"]),
                   Match(wm_class=["Vivaldi-stable"]),
                   Match(wm_class=["Icecat"]),
                   Match(wm_class=["Brave-browser"]),
                   ],
          ),

    Group("2",
          label="???",
          matches=[Match(wm_class=["Zathura"]),
                   Match(wm_class=["Evince"]),
                   ],
          ),

    Group("3",
          label="???",
          matches=[Match(wm_class=["st-256color"]),
                   # Match(wm_class=["kitty"]),
                   ],
          ),

    Group("4",
          label="???",
          matches=[Match(wm_class=["discord"]),
                   ],
          ),

    Group("5",
          label="???",
          layout="max",
          matches=[Match(wm_class=["Mplayer"]),
                   ],
          ),

    Group("6",
          label="???",
          matches=[Match(wm_class=["pcmanfm"]),
                   ],
          ),

    Group("7",
          label="???",
          layout="bsp",
          matches=[Match(wm_class=["pavucontrol"]),
                   ],
          ),

    Group("8",
          label="???",
          matches=[Match(wm_class=["emacs"]),
                   ],
          ),

    Group("9",
          label="???",
          layout="max",
          matches=[Match(wm_class=["zoom"]),
                   Match(wm_class=["Microsoft Teams - Preview"]),
                   ],
          ),

    Group("0",
          label="???"),
]

for i in range(len(groups)):
   keys.append(Key([mod], str((i)), lazy.group[str(i)].toscreen()))
   keys.append(Key([mod, "shift"], str((i)), lazy.window.togroup(str(i), switch_group=False)))
   keys.append(Key([mod1, "shift"], str((i)), lazy.window.togroup(str(i), switch_group=True)))

# LAYOUTS
layouts = [
    layout.MonadTall(margin=8, border_width=0, border_focus="#bc7cf7", border_normal="#4c566a"),
    layout.MonadWide(margin=8, border_width=0, border_focus="#bc7cf7", border_normal="#4c566a"),
    layout.Bsp      (margin=5, border_width=0, border_focus="#bc7cf7", border_normal="#4c566a", fair=False),
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
    font='novamono for Powerline',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper='/home/karttikeya/Pictures/Wallpapers/bluey.png',
        wallpaper_mode='fill',
        bottom=bar.Bar(
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
            widget.TextBox(
                text=" ???",
                foreground=colors[5],
                background=colors[3],
                padding=0,
                fontsize=33
            ),
            widget.Memory(
                background=colors[3],
                foreground=colors[5],
                font="novamono for powerline bold",
                fontsize=14,
                format='{MemUsed: .0f} MB',
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
                text="???",
                foreground=colors[5],
                background=colors[3],
                padding=0,
                fontsize=33
            ),
            widget.CPU(
                background=colors[3],
                foreground=colors[5],
                format=' {load_percent}% |',
                font='novamono for powerline bold',
                fontsize=14
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
            widget.Battery(
                foreground=colors[5],
                background=colors[7],
                fontsize=17,
                low_percentage=0.2,
                low_foreground=colors[5],
                font="fontawesome",
                update_interval=1,
                format='{char}',
                charge_char='???',
                discharge_char='???',
            ),
            widget.Battery(
                background=colors[7],
                foreground=colors[5],
                charge_char='???',
                discharge_char='???',
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
            37,
            background=colors[0],
            # margin=[0,8,8,8],
            # opacity=0.8,
        ),
    ),
]
#############################################
#############################################
############# AUTOSTART #####################
#############################################
@hook.subscribe.startup_once
def autostart():
    processes = [
        ['nm-applet'],
        ['picom'],
    ]

    for p in processes:
        subprocess.Popen(p)


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
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
    border_width=0,
    float_rules=[
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
