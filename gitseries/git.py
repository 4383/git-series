from os.path import basename

from gitseries import executor


def clone(repo, exit=False):
    executor.execute(['git', 'clone', repo])
    return basename(repo)


def add(path='.'):
    executor.execute(['git', 'add', path])


def commit(template):
    executor.execute(['git', 'commit', '--file', template])


#def review():
#    return
#    executor.execute(['git', 'review', '-s')
#    executor.execute(['git', 'review')
