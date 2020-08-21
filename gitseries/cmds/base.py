import atexit
from cliff.command import Command


class BaseCommand(Command):
    "Base command."

    def get_parser(self, prog_name):
        parser = super(BaseCommand, self).get_parser(prog_name)
        parser.add_argument('--config-file', nargs='?', default='.')
        parser.add_argument('--config-dir', nargs='?', default='.')
        parser.add_argument(
            '-e',
            action='store_true',
            help='Exit immediately if a command exits with a non-zero status')
        return parser


@atexit.register
def abort():
    print('\nExecution aborted!')
