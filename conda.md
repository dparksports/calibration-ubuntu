```sh


ln -s /usr/local/cuda/lib64/libcusolver.so.11 ~/miniconda3/envs//lib/libcusolver.so.10

import tensorflow as tf A = tf.random.normal((5, 5)) b = tf.random.normal((5,1)) tf.linalg.solve(A,b)

python -c "import tensorflow.python as x; print(x.path[0])" 
ln -s /usr/local/cuda-11.1/targets/x86_64-linux/lib/libcusolver.so.11 $(python -c "import tensorflow.python as x; print(x.path[0])")/libcusolver.so.10
```
