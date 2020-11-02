name='aurora'

""":py:mod:`aurora` 
"""

#with open('./VERSION') as vfile:
#    version = vfile.read().strip()

__version__ = '1.3.1'

import numpy as np, sys
if not np.any([('sphinx' in k and not 'sphinxcontrib' in k) for k in sys.modules]):
    from ._aurora import run,time_steps

from .core import *
from .atomic import *
from .adas_files import *

from .source_utils import *
from .default_nml import *
from .grids_utils import *
from .coords import *
from .radiation import *

from .particle_conserv import *
from .plot_tools import *
from .animate import *

from .janev_smith_rates import *
from .nbi_neutrals import *

