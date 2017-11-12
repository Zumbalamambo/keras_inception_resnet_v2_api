# keras_inception_resnet_v2_api
Implement an image classification web api using keras_inception_resnet_v2 model and keras-rest-server.

[![Updates](https://pyup.io/repos/github/charlesgreen/keras_inception_resnet_v2_api/shield.svg)](https://pyup.io/repos/github/charlesgreen/keras_inception_resnet_v2_api/)
[![Python 3](https://pyup.io/repos/github/charlesgreen/keras_inception_resnet_v2_api/python-3-shield.svg)](https://pyup.io/repos/github/charlesgreen/keras_inception_resnet_v2_api/)

This repository is based on the [ansrivas/Keras-rest-server](https://github.com/ansrivas/keras-rest-server) for loading and serving keras models as an API using flask.

## Getting started:
---
1. Install Anaconda:
```
https://docs.continuum.io/anaconda/install
```

2. Clone this repository
```
git clone https://github.com/charlesgreen/keras_inception_resnet_v2_api.git
cd keras_inception_resnet_v2_api
```

3. Create a new python 3.x environment and activate it:
```
conda create --name keras-server -y python=3
source activate keras-server
```

4. Install all the dependencies:
```
conda env update -n keras-server  --file requirements.txt
```

5. To remove the environment run:
```
conda remove -n keras-server --all -y
```

### Usage
------------------

### Run to generate pickle files:
```
python createpickles.py
```

### Run the server (defaults to http://localhost:7171)
```
python server.py
```

### Send a post request to this server to test your model
```
python client.py
```
