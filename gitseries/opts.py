import sys

from oslo_config import cfg

# Define an option group
grp_serie = cfg.OptGroup(
    'serie',
    help='Allow you to configure your serie')

grp_tox = cfg.OptGroup(
    'tox',
    help='Allow you to configure how tox integrate with your serie')

opts_serie = [
    cfg.ListOpt(
        'projects',
        help='List of projects to patch in the serie.'
    ),
    cfg.StrOpt(
        'commands',
        default='cmd.sh',
        help='Script to execute to patch projects in the serie. '
             'This script should start with a shebang to specify the '
             'interpreter to call. It will be converted as an exectuable '
             "script if isn't already the case and it will be called "
             'in a relative manner. The shebang allow you to use all the '
             'available commands on your system.'
    ),
    cfg.StrOpt(
        'commit_msg',
        help='Commit message to use during commit. '
             'Templated values can be used, by default git-series '
             'provide to you {{ project_name }}.'
    ),
    cfg.StrOpt(
        'topic',
        default="",
        help='Gerrit topic to associate with your patches. If not provided '
             'the serie name will be used in place.'
    ),
    cfg.BoolOpt(
        'commit',
        default=True,
        help='If true changes applied against projects will be commited '
             'in git.'
    ),
    cfg.BoolOpt(
        'review',
        default=False,
        help='If True your patches will be submitted to the associated '
             'gerrit host'
    )
]

opts_tox = [
    cfg.BoolOpt(
        'run',
        default=False,
        help='If True tox will be called'
    ),
    cfg.BoolOpt(
        'blocking',
        default=False,
        help='If True and if tox exited in error patches will '
             'not be submitted '
    ),
]

cfg.CONF.register_group(grp_serie)
cfg.CONF.register_group(grp_tox)
cfg.CONF.register_opts(opts_serie, group=grp_serie)
cfg.CONF.register_opts(opts_tox, group=grp_tox)
