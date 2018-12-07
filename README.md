vim-bootstrap
================

Configure vimrc for vim-bootstrap.

Requirements
------------

If you run this role for macOS, require [homebrew](https://brew.sh/).

Support languages
-----------------

This role support all languages of vim-bootstrap.

Role Variables
--------------

* `vim_command`: Target vim command (`vim` or `neovim`)
* `vim_langs`: List of languages for vim-bootstrap

Dependencies
------------

None.


Example Playbook
----------------

Simply usage: (Minimum config in vim-bootstrap)

```
- hosts: localhost
  connection: local
  roles:
    - attakei.vim-bootstrap
```

For Python engineer (Case of specify language)

```
- hosts: localhost
  connection: local
  roles:
    - role: attakei.vim-bootstrap
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
