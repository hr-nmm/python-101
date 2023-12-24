#!/usr/bin/env python3.10
## it will run python3.10 (of venv)
import numpy as np
import sys
import http as net
print(sys.version) ##3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] => to check python version of venv
print(np.array([1,2,4]))
print((net.HTTPStatus.OK) == 200)


