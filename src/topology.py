#!/usr/bin/python

from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSController
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI

'''
Single switch connected to n hosts.
'''
class SingleSwitchTopo(Topo):
    def build(self, n = 2):
        # Add switches to a topology
		s = []
		for i in range(9):
			switch = self.addSwitch('s' + str(i + 1))
			s.append(switch)
        # Add the hosts to a topology
		h = []
		for j in range(6):
			host = self.addHost('h' + str(j + 1))
			h.append(host)
		# Add bidirectional links to a topology (host, switch, bw = ?, delay = '?ms', loss = ?(%))
		self.addLink(h[0], s[0], bw = 12, delay = '6ms', loss = 2)
		self.addLink(s[0], s[7], bw = 20, delay = '7ms', loss = 15)
		self.addLink(s[7], s[3], bw = 23, delay = '6ms', loss = 10)
		self.addLink(s[3], h[4], bw = 14, delay = '5ms', loss = 2)
		self.addLink(s[7], s[5], bw = 30, delay = '1ms', loss = 12)
		self.addLink(s[5], h[1], bw = 18, delay = '2ms', loss = 3)
		self.addLink(s[7], s[1], bw = 25, delay = '6ms', loss = 14)
		self.addLink(s[1], s[8], bw = 30, delay = '3ms', loss = 18)
		self.addLink(s[8], s[4], bw = 30, delay = '3ms', loss = 20)
		self.addLink(s[4], h[5], bw = 15, delay = '4ms', loss = 3)
		self.addLink(s[8], s[6], bw = 33, delay = '8ms', loss = 10)
		self.addLink(s[6], h[2], bw = 18, delay = '6ms', loss = 6)
		self.addLink(s[8], s[2], bw = 35, delay = '2ms', loss = 17)
		self.addLink(s[2], h[3], bw = 13, delay = '3ms', loss = 5)
    
'''
Create and test a simple network
'''
def simpleTest():
    # Create a topology with 2 hosts and 1 switch
    topo = SingleSwitchTopo(n = 2)
    # Create and manage a network with a OvS controller and use TCLink
    net = Mininet(
        topo = topo, 
        controller = OVSController,
        link = TCLink)
    # Start a network
    net.start()
    # Test connectivity by trying to have all nodes ping each other
    print("Testing network connectivity")
    net.pingAll()
    #Åã¥Ü«ü©w¸`ÂIªºconnection
    dumpNodeConnections(net.hosts)
    dumpNodeConnections(net.switches)
    #µ¥«ÝÁä¤J©R¥O
    CLI(net)
    # Stop a network
    net.stop()

'''
Main (entry point)
'''
if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    # Create and test a simple network
    simpleTest()
