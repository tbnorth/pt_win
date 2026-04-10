"""Windows dependent plugins."""

import asyncio

import win32con
import win32gui

from textual.widgets import Button

class NoTitle(Button):

    def __init__(self, *args, **kwargs):
        kwargs["compact"] = True
        super().__init__(*args, **kwargs)

    async def action_press(self) -> None:

        colors = ["red", "white"]
        for i in range(15):
            self.styles.color = colors[i % 2]
            self.app.refresh()
            await asyncio.sleep(0.2)
        self.styles.color = "white"
        hwnd = win32gui.GetForegroundWindow()   
        current_style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
        new_style = current_style ^ win32con.WS_CAPTION
        win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, new_style)
        win32gui.SetWindowPos(
            hwnd,
            0,
            0,
            0,
            0,
            0,
            win32con.SWP_NOMOVE
            | win32con.SWP_NOSIZE
            | win32con.SWP_NOZORDER
            | win32con.SWP_FRAMECHANGED,
        )

    on_click = action_press
