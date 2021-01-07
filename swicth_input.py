# encoding=utf8
from vcp import *
import sys

def get_monitor(name):
    try:
        monitors = enumerate_monitors()
    except OSError as err:
        exit(1)
    phy_monitors = []
    for i in monitors:
        try:
            monitor = PhyMonitor(i)
        except OSError as err:
            logging.error(err)
            # 忽略这个显示器并继续
            continue
        if monitor.model == name:
            return monitor
        else:
            continue

input_names = ["Digital Video (TMDS) 3 HDMI 1", "Analog video (R/G/B) 1"]
def switch_input(monitor, input_index=None):
    curent_input_index = input_names.index(monitor.input_src)
    if input_index == None:
        next_input_index = (curent_input_index + 1) % len(input_names)
    else:
        next_input_index = input_index
    next_input_name = input_names[next_input_index]
    
    monitor.input_src = next_input_name
    print("switch input src to :" + next_input_name)
    return next_input_name
    
if __name__ == "__main__":
    monitor = get_monitor("T24A-10")
    switch_input(monitor)

