import logging

CONF_ID = "id"
CONF_CURRENCY_NAME = "currency_name"
CONF_MINER_ADDRESS = "miner_address"
CONF_UPDATE_FREQUENCY = "update_frequency"

SENSOR_PREFIX = "EthermineInfo "

ATTR_ACTIVE_WORKERS = "active_workers"
ATTR_CURRENT_HASHRATE = "current_hashrate"
ATTR_ERROR = "error"
ATTR_INVALID_SHARES = "invalid_shares"
ATTR_LAST_UPDATE = "last_update"
ATTR_REPORTED_HASHRATE = "reported_hashrate"
ATTR_STALE_SHARES = "stale_shares"
ATTR_UNPAID = "unpaid"
ATTR_VALID_SHARES = "valid_shares"

API_ENDPOINT = "https://api.ethermine.org/miner/"

_LOGGER = logging.getLogger(__name__)
