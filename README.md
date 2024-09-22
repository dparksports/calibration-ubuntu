# conda install cuda 11.8 & 12.1
```sh
conda install -c "nvidia/label/cuda-11.8.0" cuda-toolkit
conda install -c "nvidia/label/cuda-12.1" cuda-toolkit
```

# offline yt
```sh
./yt-dlp_macos -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]' -o video.mp4
```

## remove snapd 
```bash
snap list
#Let’s also stop snapd (snap daemon) services:

sudo systemctl disable snapd.service
sudo systemctl disable snapd.socket
sudo systemctl disable snapd.seeded.service
#Then remove each snap. It’s best to do so one-by-one, rather than all in one apt remove line. So something like:

sudo snap remove snapd-desktop-integration
sudo snap remove gtk-common-themes
sudo snap remove gnome-3-38-2004
sudo snap remove core18
sudo snap remove snap-store
sudo snap remove firefox

#Now, let’s delete any leftover snap cached data:
sudo apt autoremove --purge snapd
sudo rm -rf /var/cache/snapd/
rm -rf ~/snap
```


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



## use HTTPS using archive
```bash
sudo cp /etc/apt/sources.list /etc/apt/sources.list.backup
sudo sed --in-place --regexp-extended 's http://(us\.archive\.ubuntu\.com|security\.ubuntu\.com) https://mirrors.wikimedia.org g' /etc/apt/sources.list
```

## use HTTPS using ubuntu-ports
```bash
sudo cp /etc/apt/sources.list /etc/apt/sources.list.backup
sudo sed --in-place --regexp-extended 's http://(ports\.ubuntu\.com|security\.ubuntu\.com) https://mirrors.ocf.berkeley.edu/ubuntu-ports/ g' /etc/apt/sources.list
```

## use HTTPS using WSL-Ubuntu 
```bash
sudo cp /etc/apt/sources.list /etc/apt/sources.list.backup
sudo sed --in-place --regexp-extended 's http://(archive\.ubuntu\.com|security\.ubuntu\.com) https://mirrors.wikimedia.org g' /etc/apt/sources.list
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
sudo ufw allow out 22
sudo ufw allow out 1194
```

