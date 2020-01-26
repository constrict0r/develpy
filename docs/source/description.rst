Description
------------------------------------------------------------------------------

Ansible role to apply python developer configuration.

This is capable of:

- Upgrade the system.

- Add `apt <https://wiki.debian.org/Apt>`_ repository sources.

- Updated the apt cache.

- Uninstall apt packages.

- Install apt packages.

- Install `npm <http://npmjs.org/>`_ packages.

- Install `pip <https://pypi.org/project/pip/>`_ packages.

- Apply system-wide configuration using git.

- Stop services and disable them.

- Enable services and restart them.

- Create users.

- Add users to groups.

- Apply user-wide configuration using git.

- Run custom user tasks.

By default this role applies the following configuration:

- Installs the base software:

 .. include:: parts/packages/base.inc

- Installs the base developer software:

 .. include:: parts/packages/dev_base.inc

- Installs the python developer software:

 .. include:: parts/packages/dev_python.inc

- Configures the base software:

 .. include:: parts/configured/base.inc

- Configures the base developer software:

 .. include:: parts/configured/dev_base.inc

- Configures the python developer software:

 .. include:: parts/configured/dev_python.inc

- Creates the following home directory layout:

 .. code-block:: bash

  home/
  ├── .emacs.d
  │   ├── base.el
  │   ├── init.el
  │   ├── python.el
  │   └── themes
  │       └── wintermute-theme.el
  └── .vimrc

- Modifies the following files:

 .. code-block:: bash

  home/
  ├── .bashrc
  └── .profile
