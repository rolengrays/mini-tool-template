#
# mini-tool-template (Python3)
#
# This code is licensed under CC0.
# https://creativecommons.org/publicdomain/zero/1.0/deed
#
import sys
import argparse
import datetime
import logging

## Meta
PROG = sys.argv[0]
VERSION = '1.0.0'
AUTHOR = '### YOUR NAME HERE ###'
DESCRIPTION = '''
KEEP IT SIMPLE
'''

## Global
SUPPORTED_LOG_LEVEL = [
    logging.getLevelName(logging.DEBUG),
    logging.getLevelName(logging.INFO),
    logging.getLevelName(logging.WARNING),
    logging.getLevelName(logging.ERROR),
    logging.getLevelName(logging.CRITICAL)
]
DEFAULT_LOG_LEVEL = logging.getLevelName(logging.INFO)

## Argument
parser = argparse.ArgumentParser(
    prog=PROG,
    description=DESCRIPTION,
    epilog=f'Author: {AUTHOR}'
    )
parser.add_argument('--log', help='set log level', choices=SUPPORTED_LOG_LEVEL, default=DEFAULT_LOG_LEVEL)
parser.add_argument('--version', help='print version', action='version', version=f'{PROG} {VERSION}')
args = parser.parse_args()

## Logger
jst = datetime.timezone(datetime.timedelta(hours=+9), name='JST')
formatter = logging.Formatter(
    fmt=r'%(asctime)s [%(levelname)s] %(message)s'
    )
formatter.converter = lambda t: datetime.datetime.fromtimestamp(t, tz=jst).timetuple()
### info log handler
sh_std = logging.StreamHandler(stream=sys.stdout)
sh_std.setFormatter(formatter)
sh_std.setLevel(logging.DEBUG)
sh_std.addFilter(lambda r: logging.DEBUG <= r.levelno <= logging.INFO)
### error log handler
sh_err = logging.StreamHandler(stream=sys.stderr)
sh_err.setFormatter(formatter)
sh_err.setLevel(logging.WARNING)
sh_err.addFilter(lambda r: logging.WARNING <= r.levelno <= logging.CRITICAL)
### logger
logger = logging.getLogger(__name__)
logger.addHandler(sh_std)
logger.addHandler(sh_err)
logger.setLevel(args.log)

## Functions
def hello():
    logger.info('Hello from Hell.')

def bye():
    logger.info('Goodbye World.')

## Main
def main():
    hello()
    bye()

## Invoke
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logger.exception(e)
        sys.exit(1)
