import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/pawan/ROSmasterM3/install/yahboom_M3Pro_description'
