import pytest

from logger.logger import logger


@pytest.mark.usefixtures('load_data')
class TestExample2:

    def test_edit_profile(self, load_data):
        logger.info(load_data[0])
        logger.info(load_data[2])
        print(load_data)
