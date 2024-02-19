# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 21:47:19 2023

@author: Ashraf
"""

import psutil
import speedtest #pip install speedtest-cli
from tabulate import tabulate

class Network(object):
    def __init__(self):
        self.scanner = psutil.net_if_addrs()
        self.speed = speedtest.Speedtest()
        self.interfaces = self.interface()[0]
        
    def interface(self):
        interfaces = []
        for interface_name, _ in self.scanner.items():
            interfaces.append(str(interface_name))
        return interfaces
    
    def run_test(self):
        down = str(f"{round(self.speed.download() / 1_000_000, 2)} Mbps")
        up = str(f"{round(self.speed.upload() / 1_000_000, 2)} Mbps")
        interface = self.interfaces
        data = {"Interface:" : [interface],
                "Download:"  : [down],
                "Upload:"    : [up]}
        table = tabulate(data, headers=data, tablefmt="pretty")
        return table
    
    def __str__(self):
        return str(self.run_test())
    
    
if __name__ == "__main__":
    print(Network())