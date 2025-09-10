# How to install mini

### Follow instructions below 

1.  Install system packages
    <br>`sudo apt update`
    <br>`sudo apt upgrade`
    <br>`sudo apt install -y \
    git python3 python3-pip python3-tk \
    build-essential net-tools iproute2 iputils-ping \
    ethtool openvswitch-switch xterm tmux`

2. Install mininet
    <br>`git clone https://github.com/mininet/mininet.git`
    <br>`cd mininet/util`

3. Use install script for software installation
    <br>`sudo ./install.sh -a`
    <br> the `-a` option install everything 