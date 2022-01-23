"""beans are great"""

from typing import Union
from functools import wraps

BeansType = Union[str, int]

def beansfunc():
	"""beans is great"""
	pass

class Beans:
	"""class to represent some beans"""
	def __init__(self, beans: int) -> None:
		self.beans = beans #: the number of beans

	@staticmethod
	def getbeans(n: int) -> BeansType:
		"""
		method to get the beans

		:param int n: number of beans to get
		:return: the beans that were gotten
		:rtype: :const:`BeansType`
		"""
		pass

beans: int
"""number of beans to make"""

#: dictionary for differnet types of beans
BEANS = {
	"BEANS": 6,
	"CHEESE": 7,
	"TOAST": 8
}

def beansDecorator(num_beans: int = 5):
	"""
	
	"""

class TooManyBeansException(Exception):
	"""exception raised when too many beans"""
	pass