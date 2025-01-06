import os
import atexit

import gdb
from pwndbg.commands.context import contextoutput

panes = {
  # Split horizontal to make the main window at the bottom
  'disasm': os.popen('tmux split-window -vb -P -F "#{pane_id}:#{pane_tty}" -l 75% -d "cat -"').read().strip().split(":"),
  # Split horizontal to make the disasm + regs on the top, stack + stacktrace on bottom
  'stack': os.popen('tmux split-window -v -P -F "#{pane_id}:#{pane_tty}" -l 40% -t {top} -d "cat -"').read().strip().split(":"),
  # Split vertical next to the stack for the backtrace
  'backtrace': os.popen('tmux split-window -h -P -F "#{pane_id}:#{pane_tty}" -t -1 -l 30% -d "cat -"').read().strip().split(":"),
  # Split vertical next to the disassemble for the registers
  'regs': os.popen('tmux split-window -h -P -F "#{pane_id}:#{pane_tty}" -t {top} -l 30% -d "cat -"').read().strip().split(":"),
  'ipython': os.popen('tmux split-window -h -P -F "#{pane_id}:#{pane_tty}" -t {bottom} -l 30% -d "ipython"').read().strip().split(":"),
}

# Tell pwndbg which panes are to be used for what
for section, p in panes.items():
  contextoutput(section, p[1], True, 'top', False)

# Also add the sections legend and expressions to already existing panes
contextoutput("legend", panes['stack'][1], True)
contextoutput("expressions", panes['regs'][1], True, 'top', False)

# To see more options to customize run `theme` and `config` in gdb
# Increase the amount of lines shown in disasm and stack
gdb.execute("set context-disasm-lines 25")
gdb.execute("set context-stack-lines 18")
# Give backtrace a little more color
gdb.execute("set backtrace-prefix-color red,bold")
gdb.execute("set backtrace-address-color gray")
gdb.execute("set backtrace-symbol-color red")
gdb.execute("set backtrace-frame-label-color green")
# Remove the panes when gdb is exited
atexit.register(lambda: [os.popen(F"tmux kill-pane -t {p[0]}").read() for p in panes.values()])