# no background 
```sh
gsettings set org.gnome.nautilus.preferences default-folder-viewer 'list-view'
gsettings set org.gnome.mutter edge-tiling false
gsettings set org.gnome.desktop.background show-desktop-icons false
gsettings set org.gnome.desktop.background picture-uri ''
gsettings set org.gnome.desktop.background primary-color "#0"
gsettings set org.gnome.desktop.background secondary-color "#0"
gsettings set org.gnome.desktop.background color-shading-type "solid"
```

## history with timestamp
```bash

export HISTTIMEFORMAT="%d/%m/%y %T "
```

## update certs
```bashrc
sudo apt install ca-certificates
pip3 install certifi
sudo update-ca-certificates --fresh
export SSL_CERT_DIR=/etc/ssl/certs
```

