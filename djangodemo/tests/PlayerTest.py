import datetime

from django.test import TestCase
from django.utils import timezone
from djangodemo.models.Player import Player
from djangodemo.delegates.PlayerDelegate import PlayerDelegate

 #======================================================================
# 
# Encapsulates data for model Player
#
# @author Dev Team
#
#======================================================================

#======================================================================
# Class PlayerTest Declaration
#======================================================================
class PlayerTest (TestCase) :
	def test_crud(self) :
		player = Player()
		player.name = "default name field value"
		player.dateOfBirth = datetime.datetime.now()
		player.height = 25.0
		player.isProfessional = False
		
		delegate = PlayerDelegate()
		responseObj = delegate.create(player)
		
		self.assertEqual(responseObj, delegate.get( responseObj.id ))
	
		allObj = delegate.getAll()
		self.assertEqual(allObj.count(), 1 )		
		delegate.delete(responseObj.id)
		
		allObj = delegate.getAll()
		self.assertEqual(allObj.count(), 0 )		


