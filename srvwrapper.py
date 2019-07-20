import subprocess
import os
import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description='Wrap any applications to run as Windows Service', add_help=True)
    parser.add_argument('name', help='service name')
    parser.add_argument('program', help='application path')
    parser.add_argument('--arguments', dest='arguments', action='store', default='', help='arguments for program')
    parser.add_argument('--display', dest='display', help='the display name of the service')
    parser.add_argument('--description', dest='description', help='service description')
    parser.add_argument('--start', dest='start', help='how the service starts '
                                                      '<boot|system|auto|demand|disabled|delayed-auto>')
    parser.add_argument('--obj', dest='obj', help='the account used to run the service (default=LocalSystem)')

    args = parser.parse_args()
    if os.path.exists(args.program):
        file_path = os.path.abspath(args.program)
    else:
        try:
            path_lists = subprocess.check_output(f'where {args.program}').decode().split()
            if not path_lists:
                raise ValueError(f'can not locate program path \'{args.program}\'')
            file_path = path_lists[0]
        except subprocess.CalledProcessError:
            raise ValueError(f'can not locate program path \'{args.program}\'')

    print(f'Service Name: {args.name}')
    print(f'Using \'{file_path}\'')
    bin_path = ' '.join([f"\\\"{str(Path(os.path.dirname(__file__)) / Path('ServiceWrapper.exe'))}\\\"",
                         f"\\\"{os.getcwd()}\\\"",
                         f"\\\"{file_path}\\\"",
                         eval(args.arguments)])
    command = f"sc create {args.name} "
    if args.display:
        command += f"DisplayName= \"{args.display}\" "
    command += f"binPath= \"{bin_path}\" "
    if args.start:
        command += f"start= {args.start} "
    if args.obj:
        command += f"obj= \"{args.obj}\" "

    print(command)
    subprocess.check_call(command)

    if args.description:
        command = f"sc description {args.name} \"{args.description}\""
    print(command)
    subprocess.check_call(command)


if __name__ == '__main__':
    main()
