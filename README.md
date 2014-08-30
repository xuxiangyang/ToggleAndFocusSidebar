ToggleAndFocusSidebar
=====================

这个插件是对Focus File on Sidebar这个插件的一个改造，它使对于当前文件的一个reveal，而大部分的情景我们都是隐藏sidebar的，只有当我们不知道一个文件的名字才会去对sidebar进行查找。所以现在功能是这样的：
在隐藏sidebar的状态，调用命令,可以显示sidebar, 并且focus sidebar。
在显示sidebar的状态，调用命令,可以隐藏sidebar, 并且focus 到你的编辑窗口。最酷的是什么？是它会记住你显示sidebar前在编辑的group是什么，然后重新focus它。

你需要把它下载下来, 放到sublime 的plugins目录下。有一个更简单的办法，你可以点击Tools -> New Plugin，创建一个名为ToggleAndFocusSidebar.py 的Plugin, 然后把项目中的ToggleAndFocusSidebar.py内容粘贴过去。保存就ok了。

绑定快捷键，我修改的事super+k ,super+b键，别的键也是同理的。点击perference -> Key Bindings - User, 在数组中加入
  {
    "command": "toggle_and_focus_sidebar",
    "keys": ["super+k", "super+b"]
  },

另外之所以希望可以focus在sidebar的最根本原因是希望可以通过键盘navigate sidebar。默认的sublime键盘操作是上下左右键。我们可以通过绑定快捷键方式改成vim的方式（因为上下左右键一般都在右下角，手还要动，不如vim的h,j,k,l键方便）。点击perference -> Key Bindings - User, 在数组中加入

{ "keys": ["h"], "command": "move", "args": {"by": "characters", "forward": false}, "context":
      [ {"key": "control", "operand": "sidebar_tree"} ]
  },
  { "keys": ["j"], "command": "move", "args": {"by": "lines", "forward": true}, "context":
      [ {"key": "control", "operand": "sidebar_tree"} ]
  },
  { "keys": ["k"], "command": "move", "args": {"by": "lines", "forward": false}, "context":
      [ {"key": "control", "operand": "sidebar_tree"} ]
  },
  { "keys": ["l"], "command": "move", "args": {"by": "characters", "forward": true}, "context":
      [ {"key": "control", "operand": "sidebar_tree"} ]
  },
  
好了，搞定了
