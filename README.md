# calibration-ubuntu

```console
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

gnome-extensions disable ubuntu-dock@ubuntu.com

gsettings set org.gnome.nautilus.preferences default-folder-viewer 'list-view'

gsettings set org.gnome.mutter edge-tiling false
gsettings set org.gnome.desktop.background show-desktop-icons false
   
gsettings set org.gnome.desktop.background picture-uri ''
gsettings set org.gnome.desktop.background primary-color "#FFFFFF"
gsettings set org.gnome.desktop.background secondary-color "#FFFFFF"
gsettings set org.gnome.desktop.background color-shading-type "solid"
   
conda config --set auto_activate_base false
```

