#!/usr/bin/env python3

import requests
import voluptuous as vol
from datetime import datetime, date, timedelta
import urllib.error

from .const import (
    _LOGGER,
    CONF_CURRENCY_NAME,
    CONF_ID,
    CONF_MINER_ADDRESS,
    CONF_UPDATE_FREQUENCY,
    SENSOR_PREFIX,
    API_ENDPOINT,
    ATTR_ACTIVE_WORKERS,
    ATTR_CURRENT_HASHRATE,
    ATTR_ERROR,
    ATTR_INVALID_SHARES,
    ATTR_LAST_UPDATE,
    ATTR_REPORTED_HASHRATE,
    ATTR_STALE_SHARES,
    ATTR_UNPAID,
    ATTR_VALID_SHARES,
)

from homeassistant.components.sensor import PLATFORM_SCHEMA
import homeassistant.helpers.config_validation as cv
from homeassistant.const import CONF_RESOURCES
from homeassistant.util import Throttle
from homeassistant.helpers.entity import Entity

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_CURRENCY_NAME, default="usd"): cv.string,
        vol.Required(CONF_MINER_ADDRESS): cv.string,
        vol.Required(CONF_UPDATE_FREQUENCY, default=1): cv.string,
        vol.Optional(CONF_ID, default = ""): cv.string,
    }
)


def setup_platform(hass, config, add_entities, discovery_info=None):
    _LOGGER.debug("Setup EthermineInfo sensor")

    id_name = config.get(CONF_ID)
    miner_address = config.get(CONF_MINER_ADDRESS).strip()
    currency_name = config.get(CONF_CURRENCY_NAME).strip()
    update_frequency = timedelta(minutes=(int(config.get(CONF_UPDATE_FREQUENCY))))

    entities = []

    try:
        entities.append(
            EthermineInfoSensor(
                miner_address, currency_name, update_frequency, id_name
            )
        )
    except urllib.error.HTTPError as error:
        _LOGGER.error(error.reason)
        return False

    add_entities(entities)

class EthermineInfoSensor(Entity):
    def __init__(
        self, miner_address, currency_name, update_frequency, id_name
    ):
        self.data = None
        self.miner_address = miner_address
        self.currency_name = currency_name
        self.update = Throttle(update_frequency)(self._update)
        self._name = SENSOR_PREFIX + (id_name + " " if len(id_name) > 0  else "") + miner_address
        self._icon = "mdi:ethereum"
        self._state = None
        self._active_workers = None
        self._current_hashrate = None
        self._invalid_shares = None
        self._last_update = None
        self._reported_hashrate = None
        self._stale_shares = None
        self._unpaid = None
        self._valid_shares = None
        self._unit_of_measurement = "\u200b"
        self._error = None

    @property
    def name(self):
        return self._name

    @property
    def icon(self):
        return self._icon

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit_of_measurement

    @property
    def device_state_attributes(self):
        return {ATTR_ACTIVE_WORKERS: self._active_workers, ATTR_CURRENT_HASHRATE: self._current_hashrate, ATTR_ERROR: self._error, ATTR_INVALID_SHARES: self._invalid_shares, ATTR_LAST_UPDATE: self._last_update, ATTR_REPORTED_HASHRATE: self._reported_hashrate, ATTR_STALE_SHARES: self._stale_shares, ATTR_UNPAID: self._unpaid, ATTR_VALID_SHARES: self._valid_shares }

    def _update(self):
        url = (
            API_ENDPOINT
            + self.miner_address
            + "/dashboard"
        )
        # sending get request
        r = requests.get(url=url)
        # extracting response json
        self.data = r.json()
        etherminedata = self.data

        try:
            if etherminedata:
                self._error = False
                # Set the values of the sensor
                self._last_update = datetime.today().strftime("%d-%m-%Y %H:%M")
                self._state = r.json()['data']['currentStatistics']['activeWorkers']
                # set the attributes of the sensor
                self._active_workers = r.json()['data']['currentStatistics']['activeWorkers']
                self._current_hashrate = r.json()['data']['currentStatistics']['currentHashrate']
                self._invalid_shares= r.json()['data']['currentStatistics']['invalidShares']
                self._reported_hashrate= r.json()['data']['currentStatistics']['reportedHashrate']
                self._stale_shares= r.json()['data']['currentStatistics']['staleShares']
                self._unpaid= r.json()['data']['currentStatistics']['unpaid']
                self._valid_shares= r.json()['data']['currentStatistics']['validShares']
            else:
                raise ValueError()
        except ValueError:
            self._state = None
            self._last_update = datetime.today().strftime("%d-%m-%Y %H:%M")
            self._error = True
