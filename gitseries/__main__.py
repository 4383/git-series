import sys

from cliff.app import App
from cliff.commandmanager import CommandManager


class GitSeriesApp(App):

    def __init__(self):
        super(GitSeriesApp, self).__init__(
            description='Manage series of changesets',
            version='0.1',
            command_manager=CommandManager('gitseries.cmds'),
            deferred_help=True,
        )

    def initialize_app(self, argv):
        self.LOG.debug('Initialize git-serie')

    def prepare_to_run_command(self, cmd):
        self.LOG.debug('prepare to run command %s', cmd.__class__.__name__)

    def clean_up(self, cmd, result, err):
        self.LOG.debug('clean_up %s', cmd.__class__.__name__)
        if err:
            self.LOG.debug('got an error: %s', err)


def main(argv=sys.argv[1:]):
    myapp = GitSeriesApp()
    return myapp.run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
