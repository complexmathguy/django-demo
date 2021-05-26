from django.db import models
 #======================================================================
# 
# Encapsulates data for model TournamentType
#
# @author Dev Team
#
#======================================================================

#======================================================================
# Class TournamentType Declaration (enumerated type)
#======================================================================
from enum import Enum 
class TournamentType(Enum):   # A subclass of Enum
	Pro = 'Pro'
	Amateur = 'Amateur'
