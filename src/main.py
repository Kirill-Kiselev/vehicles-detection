from src.common_controller import CommonController
from src.service_factory import ServiceFactory


if __name__ == '__main__':
    cli_controller: CommonController = CommonController(service_factory=ServiceFactory)
    cli_controller.execute()
