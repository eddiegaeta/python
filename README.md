# Collection of code meant to python test

## kubectl run pod with these script(s): 

### make sure to pull the `https://raw.*` version of your code
    kubectl run python-test --image=python -- sh -c 'curl -LO https://raw.githubusercontent.com/eddiegaeta/python/main/python_helloworld.py; python3 ./python_helloworld.py > output.txt; sleep 1200'

### grab output
    k exec -it python-test -- cat output.txt