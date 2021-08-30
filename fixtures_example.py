import pytest
from _pytest.fixtures import SubRequest
from wallet import Wallet
#==================== fixtures (from conftest.py as main file with fixtures)
@pytest.fixture
def wallet(request: SubRequest):
   param = getattr(request, ‘param’, None)
   if param:
     prepared_wallet = Wallet(initial_amount=param[0])
   else:
     prepared_wallet = Wallet()
   yield prepared_wallet
   prepared_wallet.close()
#==================== tests
def test_default_initial_amount(wallet):
   assert wallet.balance == 0
@pytest.mark.parametrize(‘wallet’, [(100,)], indirect=True)
def test_setting_initial_amount(wallet):
   assert wallet.balance == 100
@pytest.mark.parametrize(‘wallet’, [(10,)], indirect=True)
def test_wallet_add_cash(wallet):
   wallet.add_cash(amount=90)
   assert wallet.balance == 100
@pytest.mark.parametrize(‘wallet’, [(20,)], indirect=True)
def test_wallet_spend_cash(wallet):
   wallet.spend_cash(amount=10)
   assert wallet.balance == 10
   
 #=========================== if we need different parameters for each test_default_initial_amount
 @pytest.mark.parametrize(“setting_name, setting_value”, [(‘qdb_mem_usage’, ‘low’),
(‘report_crashes’, ‘yes’),
(‘stop_download_on_hang’, ‘no’),
(‘stop_download_on_disconnect’, ‘no’),
(‘reduce_connections_on_congestion’, ‘no’),
(‘global.max_web_users’, ‘1024’),
(‘global.max_downloads’, ‘5’),
(‘use_kernel_congestion_detection’, ‘no’),
(‘log_type’, ‘normal’),
(‘no_signature_check’, ‘no’),
(‘disable_xmlrpc’, ‘no’),
(‘disable_ntp’, ‘yes’),
(‘ssl_mode’, ‘tls_1_2’),])

def test_settings_defaults(self, setting_name, setting_value):
   assert product_shell.run_command(setting_name) == \
    self.”The current value for \’{0}\’ is     \’{1}\’.”.format(setting_name, setting_value), \
    ‘The {} default should be {}’.format(preference_name, preference_value)
    
#================ install pytest-xdict and run it (with 'pytest -s -v -n=2') for multithreading tests

#======================= run 'pytest test/file/path — junitxml=path' for XML tests report generating