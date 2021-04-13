# calibration-ubuntu

## fix LD_LIBRARY_PATH
```bash

export PATH=/usr/local/cuda-11.2/bin:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-11.2/lib64
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/extras/CUPTI/lib64
# export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
export CUDA_HOME=/usr/local/cuda

export PATH=/home/uv/bazel-3.1.0/output/:$PATH
export PATH=/home/uv/protobuf-3.15.6:$PATH

# export PYTHONPATH=/home/uv/models:/home/uv/models/research:/home/uv/models/research/slim:$PYTHONPATH

export SSL_CERT_DIR=/etc/ssl/certs

export Open_BLAS_INCLUDE_SEARCH_PATHS=/usr/include/x86_64-linux-gnu
export Open_BLAS_LIB_SEARCH_PATHS=/usr/lib/x86_64-linux-gnu

export HISTTIMEFORMAT="%d/%m/%y %T "
```

## fix cert issues
```bashrc
sudo apt install ca-certificates
pip3 install certifi
sudo update-ca-certificates --fresh
export SSL_CERT_DIR=/etc/ssl/certs

pseudoinverse@uv:~$ python3
>>> import requests
>>> requests.get("https://google.com")
<Response [200]>

sudo ldconfig /usr/local/cuda/lib64

ps aux --sort -rss

xinput set-button-map 14 1 0


sudo apt-get install libimobiledevice-utils libimobiledevice-dev libgpod-dev


conda config --set auto_activate_base false
```

# disable auto docking 
```sh
gnome-extensions disable ubuntu-dock@ubuntu.com

gsettings set org.gnome.nautilus.preferences default-folder-viewer 'list-view'

gsettings set org.gnome.mutter edge-tiling false
gsettings set org.gnome.desktop.background show-desktop-icons false
   
gsettings set org.gnome.desktop.background picture-uri ''
gsettings set org.gnome.desktop.background primary-color "#FFFFFF"
gsettings set org.gnome.desktop.background secondary-color "#FFFFFF"
gsettings set org.gnome.desktop.background color-shading-type "solid"
```
