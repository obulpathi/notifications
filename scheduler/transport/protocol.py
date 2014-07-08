import sys
import six

from twisted.python import log
from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks
from twisted.internet.endpoints import serverFromString

from autobahn.wamp import router, types
from autobahn.twisted.util import sleep
from autobahn.twisted import wamp, websocket

from fabric.api import local


class SchedulerComponent(wamp.ApplicationSession):

    @inlineCallbacks
    def onJoin(self, details):

        def schedule(**kwargs):
		# create variable string
		variables = ""
		for arg in kwargs:
			if arg == "sense" or arg == "action":
				continue
			else:
				variables = variables + ' -e "NOTIFICATIONS_' + arg + ' = ' + kwargs[arg] + '"'	
		# create a container
		local("docker run -t %s python /src/orchestrator.py %s %s" % (variables, kwargs["sense"], kwargs["action"]))
		# add to the list of the containers
		# self.containers.append(container)
		# if its periodic .... execute it periodically 

        register = yield self.register(schedule, u'com.notifications.schedule')
