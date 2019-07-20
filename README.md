# srvwrapper
Create Windows service from executable

## Install
### Step 1:
Download and install the `srvwrapper` package for python.
```
pip install srvwrapper-1.0-py3-none-any.whl
```
### Step 2:
Use the `srvwrapper` command and pass the service name and program path to create a service. Other optional commands are listed with the `--help` command.
```
usage: srvwrapper [-h] [--arguments ARGUMENTS] [--display DISPLAY]
                  [--description DESCRIPTION] [--start START] [--obj OBJ]
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
  --obj OBJ             the account used to run the service
                        (default=LocalSystem)
```

## Uninstall
Use Windows `sc` command.
```
sc delete ServiceName
```
