#!/usr/bin/env python3
from mininet.net import Mininet
from mininet.node import OVSController
from mininet.topo import Topo
from mininet.log import setLogLevel

class TwoHostTopo(Topo):
    def build(self):
        s1 = self.addSwitch('s1')
        h1 = self.addHost('h1', ip='10.0.0.1/24')
        h2 = self.addHost('h2', ip='10.0.0.2/24')
        self.addLink(h1, s1)
        self.addLink(h2, s1)

def run():
    topo = TwoHostTopo()
    net  = Mininet(topo=topo, controller=OVSController)
    net.start()
    h1, h2 = net.get('h1', 'h2')
    print(h1.cmd('ping -c1 10.0.0.2'))
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
