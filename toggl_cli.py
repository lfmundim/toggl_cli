import argparse
import command_handler

parser = argparse.ArgumentParser(prog='toggl-cli', description='Work with Toggl')

parser.add_argument('command', type=str, help='config, timesheet')

parser.add_argument('--key', '-k', type=str, help='Your Toggl API Key', required=False)
parser.add_argument('--start', '-s', type=str, help='Start date, YYYY-MM-DD', required=False)
parser.add_argument('--end', '-e', type=str, help='End date, YYYY-MM-DD', required=False)
parser.add_argument('--file', '-f', action='store_true', help='uses config file when specified', required=False)
parser.add_argument('--json', '-j', action='store_true', help='outputs json when specified', required=False)
parser.add_argument('--csv', '-c', action='store_true', help='outputs csv when specified', required=False)

args = parser.parse_args()

if args.command == 'config':
    command_handler.configure(args)

elif args.command == 'timesheet':
    command_handler.timesheet(args)

else:
    print('bla')