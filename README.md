# ubuntu-setup

```console
sudo apt install libopenblas-dev,libopenblas-base
sudo apt install liblapacke-dev
sudo ln -s /usr/include/lapacke.h /usr/include/x86_64-linux-gnu # corrected path for the library 
export Open_BLAS_INCLUDE_SEARCH_PATHS=/usr/include/x86_64-linux-gnu
export Open_BLAS_LIB_SEARCH_PATHS=/usr/lib/x86_64-linux-gnu

sudo apt install ca-certificates
pip3 install certifi
sudo update-ca-certificates --fresh
export SSL_CERT_DIR=/etc/ssl/certs

imsky@ubuntu:~$ python3
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>> requests.get("https://google.com")
<Response [200]>

ps aux --sort -rss

gsettings set org.gnome.nautilus.preferences default-folder-viewer 'list-view'

gsettings set org.gnome.mutter edge-tiling false
gsettings set org.gnome.desktop.background show-desktop-icons false
   
gsettings set org.gnome.desktop.background picture-uri ''
gsettings set org.gnome.desktop.background primary-color "#FFFFFF"
gsettings set org.gnome.desktop.background secondary-color "#FFFFFF"
gsettings set org.gnome.desktop.background color-shading-type "solid"
   
conda config --set auto_activate_base false
```

