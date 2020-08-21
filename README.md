# git-series

*Fresh paint - Still in development*

Tool for uploading series of changesets to Gerrit from git

This project aim to provide tooling to generate series of patches by using
on configuation files based on [oslo.config](https://docs.openstack.org/oslo.config/latest/)

## Install

```sh
$ git clone git@github.com:4383/git-series
```

## Usages

Create a new serie of patches ([example of generated serie](ttps://review.opendev.org/#/q/topic:oslo-pre-commit)):

```sh
$ tox -e venv -- git-series create --config-file sample.conf
```

Update an existing serie:

```sh
$ tox -e venv -- git-series update --config-file sample.conf
```

## Config

Sample config:
```
[SERIE]
projects =
    https://opendev.org/openstack/castellan,
    https://opendev.org/openstack/oslo.cache,
    https://opendev.org/openstack/oslo.concurrency,
    https://opendev.org/openstack/oslo.config,
    https://opendev.org/openstack/oslo.context,
    https://opendev.org/openstack/oslo.db,
    https://opendev.org/openstack/oslo.messaging,
    https://opendev.org/openstack/oslo.middleware,
    https://opendev.org/openstack/oslo.privsep,
    https://opendev.org/openstack/oslo.rootwrap,
    https://opendev.org/openstack/oslo.service,
    https://opendev.org/openstack/oslo.utils,
    https://opendev.org/openstack/oslo.vmware
commands = cmd.sh
commit_msg = Bump hacking's version\n\ntest test, test\nblablabla
topic = bump-hacking-version
commit = true
review = false

[TOX]
run = true
blocking = true
```

The SERIE section:
- SERIE.projects: list of projects to patch
- SERIE.commands: list of commands to execute to patch projects
- SERIE.commit_msg: the commit message to assign to the related commit
- SERIE.topic: the gerrit topic to assign to your patches
- SERIE.commit: if true changes will be commited
- SERIE.review: if true review will be submitted to gerrit

The TOX section:
- TOX.run: tox testing environment will be runned
- TOX.blocking: stop the execution if tox tests fails

## How to help us

This project is still in development. Help would be really appreciated
