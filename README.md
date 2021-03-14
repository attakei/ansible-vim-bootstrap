vim-bootstrap
================

Configure vimrc for vim-bootstrap.

Requirements
------------

None.

Support languages
-----------------

This role support all languages of vim-bootstrap.

Role Variables
--------------

* `vim_command`: Target vim command (`vim` or `nvim`)
* `vim_langs`: List of languages supported from vim-bootstrap
* `vim_frameworks`: List of frameworks supported from vim-bootstrap
* `vim_theme`: Vim color theme supported from vim-boostrap
* `vim_additional_plugins`: List of plugins that you want to use

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
    - attakei.vim_bootstrap
```

For Python engineer (Case of specify language)

```
- hosts: localhost
  connection: local
  roles:
    - role: attakei.vim_bootstrap
      vim_langs:
        - python
```


License
-------

MIT License


Thanks
------

* [Vim Bootstrap](https://vim-bootstrap.com/)
