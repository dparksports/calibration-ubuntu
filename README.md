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

## use HTTPS using ubuntu-ports
```bash
sudo cp /etc/apt/sources.list /etc/apt/sources.list.backup
sudo sed --in-place --regexp-extended 's http://(ports\.ubuntu\.com|security\.ubuntu\.com) https://mirrors.ocf.berkeley.edu/ubuntu-ports/ g' /etc/apt/sources.list
```

## use HTTPS using archive
```bash
sudo cp /etc/apt/sources.list /etc/apt/sources.list.backup
sudo sed --in-place --regexp-extended 's http://(us\.archive\.ubuntu\.com|security\.ubuntu\.com) https://mirrors.wikimedia.org g' /etc/apt/sources.list

```


## history
```bash

export HISTTIMEFORMAT="%d/%m/%y %T "
```

## firewall
```bash
sudo ufw enable
sudo ufw default deny outgoing
sudo ufw allow out 80
sudo ufw allow out 443
sudo ufw allow out 53
sudo ufw allow out 67
sudo ufw allow out 123
sudo ufw allow out 1194
```

