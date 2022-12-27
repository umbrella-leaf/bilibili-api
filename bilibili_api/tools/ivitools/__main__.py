"""
IVITools

A Simple IVI file manager & toolbox. 

BY Nemo2011 <yimoxia@outlook.com>

Licensed under the GNU General Public License v3+. 
"""
__author__ = "Nemo2011 <yimoxia@outlook.com>"
__license__ = "GPLv3+"

from typing import List
import sys
import warnings
import platform
from .scan import scan_ivi_file
from .extract import extract_ivi
from .touch import touch_ivi
from .download import download_interactive_video
from colorama import Fore

def run_args(command: str, args: List[str]):
    match command:
        case "help":
            print("IVITools - A Simple IVI file manager & toolbox. \n\
BY Nemo2011<yimoxia@outlook.com>\n\
\n\
Commands: download, extract, help, play, scan, touch\n\
\n\
ivitools download [BVID] [OUT]\n\
ivitools extract [IVI]\n\
ivitools help\n\
ivitools play [IVI]\n\
ivitools scan [IVI]\n\
ivitools touch [IVI]")
        case "scan":
            scan_ivi_file(args[0])
        case "extract":
            extract_ivi(args[0], args[1])
        case "touch":
            touch_ivi(args[0])
        case "download":
            download_interactive_video(args[0], args[1])
        case "play":
            try:
                import wx
            except ImportError:
                warnings.warn("IVITools Built-in Player require WXPython but IVITools can't find it. \nYou can install it by `pip3 install wxpython`. ")
                return
            if "darwin" in platform.system().lower():
                print("Notice: You should use `pythonw` command to start ivitools player if you are using conda right now. \nYou can install `pythonw` by `conda install Python.app`. \nMore details at: https://www.wxpython.org/pages/downloads/. \n\n")
            from .player import IVIPlayer
            app = wx.App()
            player = IVIPlayer()
            player.open_ivi(args[0])
            player.Show()
            app.MainLoop()
        case _:
            raise ValueError("Command not found. Use `ivitools help` for helps. ")

def main():
    if len(sys.argv) == 1:
        print(Fore.YELLOW + '[WRN]: No arguments. ' + Fore.RESET)
        print(Fore.YELLOW + '[WRN]: Use `ivitools help` for helps. ' + Fore.RESET)
        return
    try:
        args = sys.argv
        run_args(args[1], args[2:])
    except Exception as e:
        print(Fore.RED + '[ERR]: ' + str(e) + Fore.RESET)

if __name__ == '__main__':
    main()
