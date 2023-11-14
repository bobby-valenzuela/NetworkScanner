# NetworkScanner
Simple network scanner (arp-based)


## Init

* If you don’t have Python installed, [install it from here](https://www.python.org/downloads/).

* Clone this repository.

* Navigate into the project directory:

   ```bash
   cd NetworkScanner
   ```

<br />

## Create a new virtual environment

<br />

### Using python-venv
  
```bash
python3 -m venv env && . env/bin/activate && python3 -m pip3 install -r requirements.txt
```

<br />

### Using Docker



<br />

Build docker image
```bash
docker build -t network_scanner:v1.0 .
```

<br />

Running ephemeral container
```bash
docker run --name network_scanner_container -it --rm -v ./:/usr/src/app network_scanner:v1.0
``` 

<br />

Running persistent container
```bash
docker run --name network_scanner_container -d --rm -v ./:/usr/src/app network_scanner:v1.0 tail -f /dev/null
```

<br />

Entering into an interactive terminal session of your long-running container
```bash
docker exec -it network_scanner_container /bin/bash
```
