#! /bin/bash

PYV=`python -c "import sys;t='{v[0]}{v[1]}{v[2]}'.format(v=list(sys.version_info[:3]));  correct = 'true' if int(t) > 275 else 'false'; sys.stdout.write(correct)"`

if $PYV
# if [ $PYV = "2.7.6" ]
then
    echo "Starting program . . ."
    python main.py
else

    PYV=`python -c "import sys;t='{v[0]}.{v[1]}.{v[2]}'.format(v=list(sys.version_info[:3])); sys.stdout.write(t)"`
    echo "Wrong python version $PYV"
    echo "Please download the python version 2.7.6"
fi
