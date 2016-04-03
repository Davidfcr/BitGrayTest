import logging
from datetime import date
from datetime import datetime
from django.db import connection


class LogFilter(logging.Filter):
	"""Filter use to just log the Select, Update and Delete statements in a query"""
	def filter(self, record):
		allow = False
		if 'migrations' not in record.getMessage():
			if 'INSERT' not in record.getMessage():
				if 'SELECT' in record.getMessage():
					allow = True
				elif 'UPDATE' in record.getMessage():
					allow = True
				elif 'DELETE' in record.getMessage():
					allow = True
		return allow


class LogDbHandler(logging.Handler):
	"""Class to handle the log, a custom log"""
	def __init__(self, model=""):
		super(LogDbHandler, self).__init__()
		self.model_name = 'Log.models.log'

	def emit(self, record):
		try:
			model = self.get_model(self.model_name)
		except:
			from Log.models import log as model
		
		try:
			now = datetime.now()
			msg = record.getMessage().split()
			if 'SELECT' in record.getMessage():
				mensaje = "{0} en {1} duracion {2}".format(msg[1], msg[2].split('.')[0], msg[0])
			elif 'UPDATE' in record.getMessage():
				mensaje = "{0} en {1} duracion {2}".format(msg[1], msg[2].split('.')[0], msg[0])
			elif 'DELETE' in record.getMessage():
				mensaje = "{0} en {1} duracion {2}".format(msg[1], msg[3], msg[0])
			log_entry = model(fecha=now,descripcion=mensaje)
			log_entry.save()
		except Exception, e:
			raise

		return