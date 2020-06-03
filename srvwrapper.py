import subprocess
import os
import sys
import argparse


def main():
    parser = argparse.ArgumentParser(description='Wrap any applications to run as Windows Service', add_help=True)
    parser.add_argument('name', help='service name')
    parser.add_argument('program', help='application path')
    parser.add_argument('--arguments', dest='arguments', action='store', default='', help='arguments for program')
    parser.add_argument('--display', dest='display', help='the display name of the service')
    parser.add_argument('--description', dest='description', help='service description')
    parser.add_argument('--start', dest='start', help='how the service starts '
                                                      '<boot|system|auto|demand|disabled|delayed-auto>')
    parser.add_argument('--depend', dest='depend', help='dependencies(separated by / (forward slash))')
    parser.add_argument('--obj', dest='obj', help='the account used to run the service (default=LocalSystem)')
    parser.add_argument('--password', dest='password', help='password of the account')
    parser.add_argument('--failure-reset', dest='failure_reset', help="specifies the length of the period (in seconds) "
                                                                      "with no failures after which the failure count "
                                                                      "should be reset to 0 (zero).", type=int)
    parser.add_argument('--failure-command', dest='failure_command', help="specifies the command-line command to be run"
                                                                          " when the specified service fails.")
    parser.add_argument('--failure-actions', dest="failure_actions", help="specifies one or more failure actions and "
                                                                          "their delay times (in milliseconds), "
                                                                          "separated by a forward slash (/). "
                                                                          "Valid actions are run, restart, and reboot.")

    args = parser.parse_args()
    if os.path.exists(args.program) and os.path.isfile(args.program):
        file_path = os.path.abspath(args.program)
    else:
        try:
            path_lists = subprocess.check_output('where %s' % args.program).decode().split('\r\n')
            if not path_lists:
                raise ValueError('can not locate program path \'%s\'' % args.program)
            file_path = path_lists[0]
        except subprocess.CalledProcessError:
            raise ValueError('can not locate program path \'%s\'' % args.program)

    print('Service Name: %s' % args.name)
    print('Using \'%s\'' % file_path)
    bin_path = ' '.join(["\\\"%s\\\"" % os.path.join(os.path.dirname(sys.argv[0]), 'ServiceWrapper.exe'),
                         "\\\"%s\\\"" % os.getcwd(),
                         "\\\"%s\\\"" % file_path,
                         args.arguments])
    command = "sc create %s " % args.name
    if args.display:
        command += "DisplayName= \"%s\" " % args.display
    command += "binPath= \"%s\" " % bin_path
    if args.start:
        command += "start= %s " % args.start
    if args.obj:
        command += "obj= \"%s\" " % args.obj
    if args.password:
        command += "password= \"%s\" " % args.password
    if args.depend:
        command += "depend= %s" % args.depend

    print(command)
    subprocess.check_call(command)

    if args.description:
        command = "sc description %s \"%s\"" % (args.name, args.description)
        print(command)
        subprocess.check_call(command)

    if any([args.failure_reset, args.failure_command, args.failure_actions]):
        command = "sc failure %s " % args.name
        if args.failure_reset:
            command += "reset= %d " % args.failure_reset
        if args.failure_command:
            command += "command= %s " % args.failure_command
        if args.failure_actions:
            command += "actions= %s " % args.failure_actions
        print(command)
        subprocess.check_call(command)


if __name__ == '__main__':
    main()
