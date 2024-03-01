# Run Python script on Kubernetes

## Imperative commands

### Make sure to pull the `https://raw.*` version of your file
    kubectl run python-test --image=python -- sh -c 'curl -LO https://raw.githubusercontent.com/eddiegaeta/python/main/python_helloworld.py; python3 ./python_helloworld.py 2>&1 | tee output.log; sleep 1200'

### Grab output (example)
    k exec -it python-test -- cat output.log

    or 

    k logs python-test

---

## Generic command - Make sure to pull the `https://raw.*` version of your file
    kubectl run <pod_name> --image=python -- sh -c 'curl -LO <url_to_script.py>; python3 ./<script>.py > optional.txt; sleep <12345>'