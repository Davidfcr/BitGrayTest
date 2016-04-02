import logging
from datetime import date


class LogFilter(logging.Filter):
	"""Filter use to just log the Select, Update and Delete statements in a query"""
	def __init__(self, select=None, update=None, delete=None):
		self.select = select
		self.update = update
		self.delete = delete

	def filter(self, record):
		allow = False
		if 'migrations' not in record.getMessage():
			if self.select in record.getMessage():
				allow = True
			elif self.select in record.getMessage():
				allow = True
			elif self.select in record.getMessage():
				allow = True
		return allow


class LogDbHandler(logging.Handler):
	"""Class to handle the log, a custom log"""
	def __init__(self):
		logging.Handler.__init__(self)

	def emit(self, record):
		try:
			from Log.models import log
			log_entry = log(fecha=date.today(), descripcion=record.getMessage())
			log_entry.save()
		except:
			pass
		return