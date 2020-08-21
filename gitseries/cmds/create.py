import uuid
import os
import logging
import shlex
import stat
import sys
import tempfile

from gitseries import opts
from gitseries import executor
from gitseries import git
from gitseries.cmds import base as base_cmd


class Create(base_cmd.BaseCommand):
    "Create a new serie."

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        self.cfg = opts.cfg
        self.cfg.CONF(sys.argv[2:])
        exec_dir = os.path.join(tempfile.gettempdir(), str(uuid.uuid4()))
        self.app.stdout.write(f"Execution path: {exec_dir}\n")
        if not os.path.isfile(self.cfg.CONF.serie.commands):
            self.app.stdout.write(
                f"Commands file not found {self.cfg.CONF.serie.commands}")
        current_dir = os.getcwd()
        os.chmod(self.cfg.CONF.serie.commands, stat.S_IRWXU)
        os.mkdir(exec_dir)
        commit_msg = os.path.join(exec_dir, 'commit_msg')
        with open(commit_msg, 'w+') as fp:
            lines = str(self.cfg.CONF.serie.commit_msg).replace('\n', 'n').split("\n")
            print(lines)
            for line in lines:
                fp.write(line)
        os.chdir(exec_dir)
        for project in self.cfg.CONF.serie.projects:
            repo = git.clone(project)
            self.app.stdout.write(f"Running on {repo}\n")
            os.chdir(repo)
            executor.execute(
                [os.path.join(current_dir, self.cfg.CONF.serie.commands)])
            if self.cfg.CONF.serie.commit:
                git.add('.')
                git.commit(commit_msg)
            #if self.cfg.CONF.serie.review:
            #    git.review()
            os.chdir(exec_dir)


class Error(base_cmd.BaseCommand):
    "Always raises an error"

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        self.log.info('causing error')
        raise RuntimeError('this is the expected exception')
