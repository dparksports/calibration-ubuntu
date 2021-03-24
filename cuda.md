  ```sh


## disable CUDA
CUDA_VISIBLE_DEVICES=""

## successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
for a in /sys/bus/pci/devices/*; do echo 0 | sudo tee -a $a/numa_node; done


see https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2.md

git clone https://github.com/tensorflow/models.git

## Python Package Installation
cd models/research
### Compile protos.

protoc object_detection/protos/*.proto --python_out=.
### Install TensorFlow Object Detection API.
cp object_detection/packages/tf2/setup.py .
python3 -m pip install --user --use-feature=2020-resolver .


  
  137  python3 -m venv ~/.virtualenvs/tf_dev
  138  source ~/.virtualenvs/tf_dev/bin/activate  
  
  140  sudo apt install python3-dev python3-pip
  142  pip install -U pip numpy wheel
  143  pip install -U pip six 'numpy<1.19.0' wheel setuptools mock 'future>=0.17.1'
  144  pip install -U keras_applications --no-deps
  145  pip install -U keras_preprocessing --no-deps


conda create -n tf-gpu tensorflow-gpu cudatoolkit=9.0
ln -s ~/models/research/object_detection object_detection
pip install tf_slim
pip install git+https://github.com/waleedka/cocoapi.git#egg=pycocotools&subdirectory=PythonAPI
pip install -U scikit-image
pip install -U cython
protoc object_detection/protos/*.proto --python_out=.


ln -s /usr/local/cuda/lib64/libcusolver.so.11 ~/miniconda3/envs/<env-name>/lib/libcusolver.so.10

import tensorflow as tf
A = tf.random.normal((5, 5))
b = tf.random.normal((5,1))
tf.linalg.solve(A,b)


python -c "import tensorflow.python as x; print(x.__path__[0])"
ln -s /usr/local/cuda-11.1/targets/x86_64-linux/lib/libcusolver.so.11 $(python -c "import tensorflow.python as x; print(x.__path__[0])")/libcusolver.so.10

```
