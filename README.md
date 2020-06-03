# srvwrapper
Create Windows service from executable

## Install
### Step 1:
Download and install the `srvwrapper` package for python.
```
pip install srvwrapper
```
### Step 2:
Use the `srvwrapper` command and pass the service name and program path to create a service. Other optional commands are listed with the `--help` command.
```
usage: srvwrapper [-h] [--arguments ARGUMENTS] [--display DISPLAY]
                  [--description DESCRIPTION] [--start START]
                  [--depend DEPEND] [--obj OBJ] [--password PASSWORD]
                  name program

Wrap any applications to run as Windows Service

positional arguments:
  name                  service name
  program               application path

optional arguments:
  -h, --help            show this help message and exit
  --arguments ARGUMENTS
                        arguments for program
  --display DISPLAY     the display name of the service
  --description DESCRIPTION
                        service description
  --start START         how the service starts
                        <boot|system|auto|demand|disabled|delayed-auto>
  --depend DEPEND       dependencies(separated by / (forward slash))
  --obj OBJ             the account used to run the service
                        (default=LocalSystem)
  --password PASSWORD   password of the account
  --failure-reset FAILURE_RESET
                        specifies the length of the period (in seconds) with
                        no failures after which the failure count should be
                        reset to 0 (zero).
  --failure-command FAILURE_COMMAND
                        specifies the command-line command to be run when the
                        specified service fails.
  --failure-actions FAILURE_ACTIONS
                        specifies one or more failure actions and their delay
                        times (in milliseconds), separated by a forward slash
                        (/). Valid actions are run, restart, and reboot.
```
When using `--arguments`, make sure you added a double quote around it. Here are some examples:
1. Create a service named `service1` with command line `python test.py log.txt`.
```cmd
srvwrapper service1 python --arguments "test.py log.txt"
```
2. Use absolute program path to create a service.
```cmd
srvwrapper service2 C:\Python36\python.exe --arguments "\\\"D:\test 1\test.py\\\"" --display "Service 2" --description "A description" --start auto
```
3. Use specific account.
```cmd
srvwrapper service3 ping --arguments "-t github.com" --obj "NT AUTHORITY\NetworkService" --depend service2/service1
```

### Step 3:
To start/stop the service, use the `net` command
```cmd
net start service_name
net stop service_name
```


## Uninstall
Use Windows `sc` command.
```
sc delete ServiceName
```
