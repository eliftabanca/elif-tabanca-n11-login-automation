import pytest
from utils.config import HTTP_URL

@pytest.mark.usefixtures("setup")
class TestSecurity:

    def test_SEC_TC06_https_redirection(self):
      
        self.driver.get(HTTP_URL) #!Opening a URL in 'http' format.
        
        my_current_url = self.driver.current_url  
        
        #!We check if the actual opened URL starts with HTTPS.
        assert my_current_url.startswith("https"), f"Security issue! Page did not redirect to HTTPS: {my_current_url}"
        
      
