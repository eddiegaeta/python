# Collection of code meant to python test

## kubectl run pod with script(s): 

### Make sure to pull the `https://raw.*` version of your code (example)
    kubectl run python-test --image=python -- sh -c 'curl -LO https://raw.githubusercontent.com/eddiegaeta/python/main/python_helloworld.py; python3 ./python_helloworld.py > output.txt; sleep 1200'

### Grab output (example)
    k exec -it python-test -- cat output.txt

## Generic command - Make sure to pull the `https://raw.*`
    kubectl run <pod_name> --image=python -- sh -c 'curl -LO <url_to_script.py>; python3 ./<script>.py > optional.txt; sleep <12345>'