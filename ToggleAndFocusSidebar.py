import sublime, sublime_plugin

from_group = 0

def is_sidebar_open(self):
    window = self.window
    view = window.active_view()
    if view:
        sel1 = view.sel()[0]
        window.run_command('focus_side_bar')
        window.run_command('move', {"by": "characters", "forward": True})
        sel2 = view.sel()[0]
        if sel1 != sel2:
            window.run_command('move', {"by": "characters", "forward": False})
            return False
        else:
            group, index = window.get_view_index(view)
            window.focus_view(view)
            window.focus_group(group)
            return True
    return False

class ToggleAndFocusSidebar(sublime_plugin.WindowCommand):
    def run(self):
        global from_group
        self.window.run_command("toggle_side_bar")
        if is_sidebar_open(self):
          from_group = self.window.active_group()
          self.window.run_command('focus_side_bar')
        else:
          self.window.run_command('focus_group', { "group": from_group } )
