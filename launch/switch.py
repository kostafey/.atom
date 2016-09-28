# python -m pip install --upgrade pip
# pip install pywin32
import win32gui
import sys
import re
import subprocess

class WindowMgr:
    """Encapsulates some calls to the winapi for window management"""
    def __init__ (self):
        """Constructor"""
        self._handle = None

    def find_window(self, class_name, window_name = None):
        """find a window by its class_name"""
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        '''Pass to win32gui.EnumWindows() to check all the opened windows'''
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) != None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        """put the window in the foreground"""
        win32gui.BringWindowToTop(self._handle)
        win32gui.SetForegroundWindow(self._handle)
        # win32gui.ShowWindow(self._handle, win32con.SW_MAXIMIZE)

    def set_background(self):
        """put the window in the background"""
        # win32gui.ShowWindow(self._handle, win32con.SW_MINIMIZE)

if (len(sys.argv) > 1 and sys.argv[1] != None):
    subprocess.call(['atom', sys.argv[1]], shell=True)

w = WindowMgr()
w.find_window_wildcard(".*Atom.*")
w.set_foreground()
