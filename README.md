# background 
```sh


gsettings set org.gnome.nautilus.preferences default-folder-viewer 'list-view'
gsettings set org.gnome.mutter edge-tiling false
gsettings set org.gnome.desktop.background show-desktop-icons false
gsettings set org.gnome.desktop.background picture-uri ''
gsettings set org.gnome.desktop.background primary-color "#0"
gsettings set org.gnome.desktop.background secondary-color "#0"
gsettings set org.gnome.desktop.background color-shading-type "solid"

```

## use HTTPS
```bash


sudo cp /etc/apt/sources.list /etc/apt/sources.list.backup
sudo sed --in-place --regexp-extended 's http://(us\.archive\.ubuntu\.com|security\.ubuntu\.com) https://mirrors.wikimedia.org g' /etc/apt/sources.list

```


## history
```bash

export HISTTIMEFORMAT="%d/%m/%y %T "
```

## certs
```bashrc
sudo apt install ca-certificates
pip3 install certifi
sudo update-ca-certificates --fresh
export SSL_CERT_DIR=/etc/ssl/certs
```

