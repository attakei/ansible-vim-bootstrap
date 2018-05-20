neovim-bootstrap
================

Install NeoVim and configure by vim-bootstrap.

Requirements
------------

If you run this role for macOS, require [homebrew](https://brew.sh/).


Role Variables
--------------

* `neovim_config_dir`: Target directory of installation config files
* `neovim_langs`: List of languages for vim-bootstrap

Dependencies
------------

None.


Example Playbook
----------------

Simply usage: (Install NeoVim and minimum config in vim-bootstrap)

```
- hosts: localhost
  connection: local
  roles:
    - attakei.neovim-bootstrap
```

For Python engineer (Case of specify language)

```
- hosts: localhost
  connection: local
  roles:
    - role: attakei.neovim-bootstrap
      neovim_langs:
        - python
```


License
-------

MIT License


Thanks
------

* [Vim Bootstrap](https://vim-bootstrap.com/)
  * Original of configs
