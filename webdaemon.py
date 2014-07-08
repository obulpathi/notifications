from scheduler.transport.protocol import SchedulerComponent
from autobahn.twisted import wamp, websocket
from autobahn.wamp import router
from twisted.internet.endpoints import serverFromString
from twisted.internet import reactor

if __name__ == "__main__":
    ## 1) create a WAMP router factory
    router_factory = router.RouterFactory()

    ## 2) create a WAMP router session factory
    session_factory = wamp.RouterSessionFactory(router_factory)

    ## 3) Optionally, add embedded WAMP application sessions to the router
    component_session = SchedulerComponent()
    session_factory.add(component_session)

    ## 4) create a WAMP-over-WebSocket transport server factory
    transport_factory = websocket.WampWebSocketServerFactory(session_factory, \
                                                             debug=True, \
                                                             debug_wamp=False)

    ## 5) start the server from a Twisted endpoint
    server = serverFromString(reactor, "tcp:8080")
    server.listen(transport_factory)

    ## 6) now enter the Twisted reactor loop
    reactor.run()