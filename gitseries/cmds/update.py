import logging

from cliff.command import Command


class Update(Command):
    "Update an existing serie."

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        self.log.info('update')
        self.log.debug('debugging')
        self.app.stdout.write('update!\n')


class Error(Command):
    "Always raises an error"

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        self.log.info('causing error')
        raise RuntimeError('this is the expected exception')
