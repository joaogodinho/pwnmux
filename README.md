# pwnmux

A `gdbinit` configuration that uses pwndbg and tmux to create multiple panes for different contexts, making debugging a more enjoying experience.

For a more detailed explaination on how to use and modify the layout, check my blogpost about it [here](https://blog.jcfg.re/posts/pwndbg-tmux/).

## Requirements

- [pwndbg](https://github.com/pwndbg/pwndbg)
- [tmux](https://github.com/tmux/tmux)
- [gdb](https://sourceware.org/gdb/)

## Installation

```bash
git clone https://github.com/joaogodinho/pwnmux
cd pwnmux
./setup.sh
```

## Usage

Start GDB from inside a tmux window, and all the panes should be created automatically.
The following image shows how the layout looks like:

![Screenshot of the pwnmux layout.](/images/layout.png)