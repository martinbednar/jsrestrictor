import pytest

import driver


driver.init()
pytest.main()
driver.driver.quit()