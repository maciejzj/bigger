# Bigger
Very simple python script that changes terminal size in macOS. Works with one or two screens set horizontally.

## Installation
Just add the script to your `$PATH`, the best location is `\usr\local\bin`.

## Available options
* c – centers terminal window
* s – (default) small size (macOS default 80x24)
* m – medium size (128x39)
* b – large size (161x50)

## Suggested shell aliases
```shell
alias sc='bigger.py c'
alias ss='bigger.py s'
alias sm='bigger.py m'
alias sb='bigger.py b'
```
