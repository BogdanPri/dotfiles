#####################################################################################
#####################################################################################
####                                                                             ####
####       ____   _    _  _               _____                __  _             ####
####      / __ \ | |  (_)| |             / ____|              / _|(_)            ####
####     | |  | || |_  _ | |  ___       | |      ___   _ __  | |_  _   __ _      ####
####     | |  | || __|| || | / _ \      | |     / _ \ | '_ \ |  _|| | / _` |     ####
####     | |__| || |_ | || ||  __/      | |____| (_) || | | || |  | || (_| |     ####
####      \___\_\ \__||_||_| \___|       \_____|\___/ |_| |_||_|  |_| \__, |     ####
####                                                                   __/ |     ####
####                                                                  |___/      ####
####                                                                             ####
#####################################################################################
#####################################################################################

# Author:   Bogdan Pricope
# Date:     2022-08-01

################################### - Modules - #####################################

import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from typing import List  # noqa: F401from typing import List  # noqa: F401
from libqtile.dgroups import simple_key_binder

# from modules.keys import keys, mod
# from modules.groups import groups
# from modules.layouts import layouts, floating_layout
# from modules.mouse import mouse
# from modules.hooks import *
# from modules.screens import screens

################################### - Variables - ###################################

mod =               "mod4"              # Sets the <super> key as the mod key.
terminal =          "alacritty"         # My terminal app of choice.
browser =           "firefox"           # My browser of choice.
fileManager =       "thunar"            # My file manager of choice.
emailManager =      "thunderbird"       # My email manager of choice.

##################################### - Keys - ######################################

keys = [
    # Switch between windows.
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus to down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus to up"),
    # Move windows around.
    Key([mod, "shift"], "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        desc="Move window to the down"),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        desc="Move window to the up"),
    # Shrink and grow windows.
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.grow().when(layout=["monadtall"]),
        desc="Grow window to the left"),
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.shrink().when(layout=["monadtall"]),
        desc="Grow window to the right"),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        desc="Grow window up"),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "n",
        lazy.layout.reset(),
        desc="Resets all window sizes"),
    # Spawn programs.
    Key([mod], "q", lazy.window.kill(), desc="Kill foucsed window"),
    Key([mod], "t", lazy.spawn(terminal), desc="Spawns my terminal of choice"),
    Key([mod], "w", lazy.spawn(browser), desc="Spawns my browser of choice"),
    Key([mod], "f", lazy.spawn(fileManager), desc="Spawns my file manager of choice"),
    Key([mod], "m", lazy.spawn(emailManager), desc="Spawns my email manager of choice"),
    Key([mod], "slash", lazy.spawn("rofi -show combi"), desc="Spawn rofi"),
    Key([mod, "shift"], "q", lazy.spawn("archlinux-logout"), desc="Spawns logout menu"),
    # Layouts
    Key([mod], "space",
        lazy.window.toggle_floating(),
        desc="Toggles between docked and floating"),
    Key([mod], "Tab",
        lazy.next_layout(),
        desc="Toggle between layouts"),
    Key([], "Print", lazy.spawn('xfce4-screenshooter -f --save="Pictures"'),
        desc="Print screen of the full screen"),
    Key(["control"], "Print", lazy.spawn('xfce4-screenshooter -w --save="Pictures"'),
        desc="Print screen of the current window"),
    Key(["shift", "control"], "Print", lazy.spawn('xfce4-screenshooter -r -c'),
        desc="Print screen of the selected region"),
    # KeyChord([mod],"e", [
    #     Key([], "e",
    #     lazy.spawn("emacsclient -c -a 'emacs'"),
    #     desc='Emacsclient Dashboard'
    # ),
    # Key([], "a",
    #     lazy.spawn("emacsclient -c -a 'emacs' --eval '(emms)' --eval '(emms-play-directory-tree \"~/Music/\")'"),
    #     desc='Emacsclient EMMS (music)'
    # ),
    # Key([], "b",
    #     lazy.spawn("emacsclient -c -a 'emacs' --eval '(ibuffer)'"),
    #     desc='Emacsclient Ibuffer'
    # ),
    # Key([], "d",
    #     lazy.spawn("emacsclient -c -a 'emacs' --eval '(dired nil)'"),
    #     desc='Emacsclient Dired'
    # ),
    # Key([], "i",
    #     lazy.spawn("emacsclient -c -a 'emacs' --eval '(erc)'"),
    #     desc='Emacsclient ERC (IRC)'
    # ),
    # Key([], "n",
    #     lazy.spawn("emacsclient -c -a 'emacs' --eval '(elfeed)'"),
    #     desc='Emacsclient Elfeed (RSS)'
    # ),
    # Key([], "s",
    #     lazy.spawn("emacsclient -c -a 'emacs' --eval '(eshell)'"),
    #     desc='Emacsclient Eshell'
    # ),
    # Key([], "v",
    #     lazy.spawn("emacsclient -c -a 'emacs' --eval '(+vterm/here nil)'"),
    #     desc='Emacsclient Vterm'
    # ),
    # Key([], "w",
    #     lazy.spawn("emacsclient -c -a 'emacs' --eval '(doom/window-maximize-buffer(eww \"distro.tube\"))'"),
    #     desc='Emacsclient EWW Browser'
    #     ),
    # ]),
    Key([mod], "e",
        lazy.spawn("emacsclient -c -a 'emacs'"),
        desc='Emacsclient Dashboard'
    ),
    # Reload Qtile Config
    Key([mod, "shift"], "r",
        lazy.reload_config(),
        desc="Reloads the confg.py"
    ),
    # Media Keys
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 3%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 3%-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle")),
]

#################################### - Mouse - ######################################

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_app_rules = []  # type: List
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False

#################################### - Groups - #####################################

groups = [
    Group("\u03b1",     layout="monadtall"),
    Group("\u03b2",     layout="monadtall"),
    Group("\u03b3",     layout="monadtall"),
    Group("\u03b4",     layout="monadtall"),
    Group("\u03b5",     layout="monadtall"),
    Group("\u03b6",     layout="monadtall"),
    Group("\u03b7",     layout="monadtall"),
    Group("\u03b8",     layout="monadtall"),
    Group("\u03b9",     layout="floating"),
]

dgroups_key_binder = simple_key_binder("mod4")

################################### - Layouts - #####################################

layout_settings = {
    "margin":8,
    "border_focus":"#5294e2",
    "border_normal":"#2c5380",
    "border_width":2,
}

layouts = [
    layout.MonadTall(**layout_settings),
    layout.Max(**layout_settings)
]

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    # *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(wm_class='confirm'),
    Match(wm_class='error'),
    Match(wm_class='dialog'),
    Match(wm_class='file_progress'),
    Match(wm_class='notification'),
    Match(wm_class='splash'),
    Match(wm_class='toolbar'),
    Match(wm_class='download'),
    Match(wm_class='ssh-askpass'),
    Match(wm_class='nextcloud'),
    Match(wm_class='system-config-printer'),
    Match(title='branchdialog'),  # gitk
    Match(title='Bitwarden'),
    Match(title='pinentry'),  # GPG key password entry
    Match(title='MEGAsync'),
    Match(title='Volume Control'),
    Match(title='Confirmation'),      # tastyworks exit box
    Match(title='Qalculate!'),        # qalculate-gtk
    Match(wm_class='kdenlive'),       # kdenlive
    Match(wm_class='pinentry-gtk-2'), # GPG key password entry
    Match(title='Bluetooth Devices'),
    ],
    border_focus = "#5294e2",
    border_normal = "#2c5380",
    border_width = 2,
)

#################################### - Wigets - #####################################

colors = [["#282c34", "#282c34"],   #  0
          ["#1c1f24", "#1c1f24"],   #  1
          ["#dfdfdf", "#dfdfdf"],   #  2
          ["#ff6c6b", "#ff6c6b"],   #  3
          ["#98be65", "#98be65"],   #  4
          ["#da8548", "#da8548"],   #  5
          ["#51afef", "#51afef"],   #  6
          ["#c678dd", "#c678dd"],   #  7
          ["#46d9ff", "#46d9ff"],   #  8
          ["#a9a1e1", "#a9a1e1"],   #  9
          ["#404552", "#404552"]]   # 10

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

def init_widgets_list():
    return [
        widget.Sep(
            linewidth = 0,
            padding = 6,
            foreground = colors[2],
            background = colors[0]
        ),
        # widget.Image(
        #     filename = "~/.config/qtile/icons/python-white.png",
        #     scale = "False",
        #     mouse_callbacks = {
        #         "Button1": lambda: qtile.cmd_spawn("rofi -show combi")
        #     }
        # ),
        widget.TextBox(
            text = "\ue235",
            font = "MesloLGS NF",
            padding = 6,
            fontsize = 26,
            background = colors[0],
            foreground = colors[2],
            mouse_callbacks = {
                "Button1": lambda: qtile.cmd_spawn("rofi -show combi")
            }
        ),
        widget.Sep(
            linewidth = 0,
            padding = 6,
            foreground = colors[2],
            background = colors[0]
        ),
        widget.GroupBox(
               font = "Ubuntu Bold",
               fontsize = 12,
               margin_y = 3,
               margin_x = 0,
               padding_y = 5,
               padding_x = 3,
               borderwidth = 3,
               active = colors[2],
               inactive = colors[7],
               rounded = False,
               highlight_color = colors[1],
               highlight_method = "line",
               this_current_screen_border = colors[6],
               this_screen_border = colors [4],
               other_current_screen_border = colors[6],
               other_screen_border = colors[4],
               foreground = colors[2],
               background = colors[0]
        ),
        widget.TextBox(
               text = '|',
               font = "Ubuntu Mono",
               background = colors[0],
               foreground = '474747',
               padding = 2,
               fontsize = 14
       ),
        widget.CurrentLayoutIcon(
               custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
               foreground = colors[2],
               background = colors[0],
               padding = 0,
               scale = 0.7
       ),
        widget.CurrentLayout(
               foreground = colors[2],
               background = colors[0],
               padding = 5
       ),
        widget.TextBox(
               text = '|',
               font = "Ubuntu Mono",
               background = colors[0],
               foreground = '474747',
               padding = 2,
               fontsize = 14
       ),
        widget.WindowName(
               foreground = colors[6],
               background = colors[0],
               padding = 0
        ),
        widget.Sep(
                linewidth = 0,
                padding = 6,
                foreground = colors[0],
                background = colors[0]
        ),
        widget.CheckUpdates(
            update_interval = 1800,
            distro = "Arch_yay",
            display_format = "\uf01e  {updates} Updates ",
            foreground = colors[2],
            background = colors[0],
            mouse_callbacks ={
                'Button1':
                lambda: qtile.cmd_spawn(terminal + ' -e yay -Syu')
            },
        ),
        widget.TextBox(
            text = "\uf0d9",
            font = "MesloLGS NF",
            fontsize = 18,
            padding = 0,
            background = colors[0],
            foreground = colors[10]
        ),
        # widget.Net(
        #     interface = "wlp0s20f3",
        #     format = " jdown} ↓↑ {up} ",
        #     foreground = colors[2],
        #     background = colors[10],
        #     padding = 2
        # ),
        widget.ThermalSensor(
            foreground = colors[2],
            background = colors[10],
            font = "mesloLGS NF",
            fontsize = 14,
            padding = 2,
            fmt = " \ue350 {} "
            
        ),
        widget.Volume(
            fmt = " \uf028 {} ",
            font = "Hack Nerd Font",
            fontsize = 14,
            foreground = colors[2],
            background = colors[10],
            mouse_callbacks = {
                "Button1": lambda: qtile.cmd_spawn("pavucontrol")
            }
        ),
        widget.Battery(
            discharge_char = '\uf57f',
            charge_char = '\uf583',
            empty_char = '\uf58d',
            full_char = '\uf578',
            background = colors[10],
            foreground = colors[2],
            padding =2,
            font = "MesloLGS NF",
            format = " {char} {percent:2.0%} "
        ),
        widget.TextBox(
            text = "\uf0d9",
            font = "MesloLGS NF",
            fontsize = 18,
            padding = 0,
            background = colors[10],
            foreground = colors[0]
        ),
        widget.TextBox(
            text="\uf64f",
            font = "MesloLGS NF",
            fontsize=18,
            padding = 6,
            foreground = colors[4],
            background = colors[0]
        ),
        widget.Clock(
            format = "%a %d-%m-%Y | %I:%M %p ",
            foreground = colors[4],
            background = colors[0],
            font = "MesloLGS NF",
            fontsize = 14
        ),
        widget.TextBox(
            text = "\uf0d9",
            font = "MesloLGS NF",
            fontsize = 18,
            padding = 0,
            background = colors[0],
            foreground = colors[10]
        ),
        widget.Systray(
            background = colors[10],
            padding = 5,
            icon_size = 16
        ),
        widget.Sep(
            background = colors[10],
            foreground = colors[10],
            padding = 2,
            linewidth = 0
        ),
        widget.TextBox(
            text = "\uf011",
            font = "MesloLGS NF",
            fontsize = 18,
            padding = 8,
            background = colors[10],
            foreground = colors[5],
            mouse_callbacks = {
                "Button1": lambda: qtile.cmd_spawn("archlinux-logout")
            }
        ),
    ]

################################### - Hooks - #######################################

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

################################### - Screens - #####################################

screens = [
    Screen(top=bar.Bar(widgets=init_widgets_list(), opacity=1.0, size=25))
]

wmname = "LG3D"
