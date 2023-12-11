from environment import env
from service_factory import ServiceFactory


class CommonController:
    def __init__(self, service_factory: ServiceFactory):
        self._service_factory = service_factory

    def execute(self):
        service = self._service_factory.create(env=env)
        service.process()
