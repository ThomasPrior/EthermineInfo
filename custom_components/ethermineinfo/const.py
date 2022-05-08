import logging

CONF_ID = "id"
CONF_CURRENCY_NAME = "currency_name"
CONF_MINER_ADDRESS = "miner_address"
CONF_UPDATE_FREQUENCY = "update_frequency"
CONF_NAME_OVERRIDE = "name_override"

SENSOR_PREFIX = "EthermineInfo "

ATTR_CURRENT_HASHRATE_MH_SEC = "current_hashrate_mh_sec"
ATTR_ACTIVE_WORKERS = "active_workers"
ATTR_CURRENT_HASHRATE = "current_hashrate"
ATTR_INVALID_SHARES = "invalid_shares"
ATTR_LAST_UPDATE = "last_update"
ATTR_REPORTED_HASHRATE = "reported_hashrate"
ATTR_REPORTED_HASHRATE_MH_SEC = "reported_hashrate_mh_sec"
ATTR_STALE_SHARES = "stale_shares"
ATTR_UNPAID = "unpaid"
ATTR_UNPAID_ETH = "unpaid_eth"
ATTR_VALID_SHARES = "valid_shares"
ATTR_START_BLOCK = "start_block"
ATTR_END_BLOCK = "end_block"
ATTR_AMOUNT = "amount"
ATTR_TXHASH = "txhash"
ATTR_PAID_ON = "paid_on"
ATTR_AVERAGE_HASHRATE_24h = "average_hashrate_24h"
ATTR_AVERAGE_HASHRATE_24h_MH_SEC = "average_hashrate_24h_mh_sec"
ATTR_SINGLE_COIN_LOCAL_CURRENCY = "single_coin_in_local_currency"
ATTR_TOTAL_UNPAID_LOCAL_CURRENCY = "unpaid_in_local_currency"
ATTR_COINS_PER_MINUTE = "coins_per_minute"

ETHERMINE_API_ENDPOINT = "https://api.ethermine.org/miner/"
COINGECKO_API_ENDPOINT = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies="

_LOGGER = logging.getLogger(__name__)
