# EthermineInfo

⚠️ This repository is archived as Ethermine.org has suspended Ethereum mining indefinitely. [Please refer to their announcement for more information.](https://ethermine.org/announcement)

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)
## A custom component for [HomeAssistant](https://github.com/home-assistant/core) 

Provides data from [Ethermine.org](https://ethermine.org/) on a specified miner.

If this has been of use, please consider funding my caffeine habit:

<a href="https://www.buymeacoffee.com/tomprior" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png"></a>

# Functionality

* Create sensor items for Ethermine items:
  * Current statistics
  
      ✔ Unpaid balance
  
      ✔ Reported hash rate
  
      ✔ Average hash rate
  
      ✔ Current hash rate
  
      ✔ Valid shares
  
      ✔ Invalid shares
  
      ✔ Stale shares
  
      ✔ Active workers
      
      ✔ Balance in local currency
     
  * Payouts
  
      ✔ Paid on
  
      ✔ Amount
  
      ✔ Transaction hash
      
      ✔ Value in local currency

## Things you should know about EthermineInfo
* The Ethermine API has been subject to change - there may be occaisions where a code change is required before the component will work again.
* There are limits on how many requests can be made to Ethermine's API and therefore the data retrieved by EthermineInfo will be updated periodically and may be out of date by the time you look at it.
* Please do not use EthermineInfo in isolation to make decisions about your cryptocurrency holdings.
* EthermineInfo only reads the statistics of the provided miner.

## Pre-requisite knowledge

Before downloading and configuring EthermineInfo, please ensure you are familiar with the following items:

* HomeAssistant's configuration file [LINK](https://www.home-assistant.io/docs/configuration/)
* YAML syntax [LINK](https://www.home-assistant.io/docs/configuration/yaml/)
* Installation of custom components via:
  * HACS [LINK](https://hacs.xyz/docs/setup/prerequisites)
  * Manual custom component installation
* Adding template sensors to your configuration [LINK](https://www.home-assistant.io/integrations/template/)

## Installation

Copy the files in the /custom_components/ethermineinfo/ folder to: [homeassistant]/config/custom_components/ethermineinfo/

HACS users, you know what to do!
In case you don't:

1. Open HACS from your HomeAssistant sidebar
2. Press the "Explore & Add Repositories"
3. Enter "EthermineInfo" into the search box
4. Press "EthermineInfo"
5. Press "Install this repository in HACS"
6. Don't forget to complete the configuration before restart HomeAssistant!

## Configuration

To use EthermineInfo, please add the following items to your HomeAssistant ```configuration.yaml```
````
sensor:
  - platform: ethermineinfo
    miner_address: (required) the address of your Ethermine miner
    currency_name: (required) the currency you would like your unpaid balance to be converted to 
    name_override: (optional) name to identify your wallet instead of your miner address.
````

Please note that the Ethermine API accepts the address in two formats:

- 42 characters beginning with 0x
- 40 characters with the 0x removed

Both can be configured, but the 42 character options *must* be encapsulated in quote marks. Failure to do so will just return "unknown" in HomeAssistant.

Examples:

```
sensor:
  - platform: ethermineinfo
    miner_address: "0x1234567890123456789012345678901234567890"
    currency_name: USD
```

```
sensor:
  - platform: ethermineinfo
    miner_address: "1234567890123456789012345678901234567890"
    currency_name: USD
```

```
sensor:
  - platform: ethermineinfo
    miner_address: "1234567890123456789012345678901234567890"
    currency_name: USD
    name_override: "wallet name"
```

Multiple addresses can be configured.

## Templates

You can create a template sensor for any of the attributes returned by EthermineInfo. For example:

Stale shares:
```{{ states.sensor.ethermineinfo_miner_address.attributes['stale_shares'] }}```

Current hashrate:
```{{ states.sensor.ethermineinfo_miner_address.attributes['current_hashrate'] }}```

Unpaid amount:
```{{ states.sensor.ethermineinfo_miner_address.attributes['unpaid'] }}```

## How does it look?

![image](https://user-images.githubusercontent.com/34111848/119135501-6aef4c80-ba36-11eb-9006-dc756af23978.png)

Some rather pretty graphs are possible with the [mini-graph-card](https://github.com/kalkih/mini-graph-card):

![image](https://user-images.githubusercontent.com/34111848/143507616-a8bac318-5696-4a8a-bffe-7f4d14c8f5e5.png)

## Discussion

[Talk about EthermineInfo here](https://community.home-assistant.io/t/my-first-custom-component-ethermineinfo/302734)

[Post issues with EthermineInfo here](https://github.com/ThomasPrior/EthermineInfo/issues)

Issues should be posted with logs and relevant, redacted excerpts from your configuration.yaml file to ensure that help can be given most effectively.

Pull requests and constructive criticism are always welcome.

## Credits

[@heyajohnny's](https://github.com/heyajohnny) [CryptoInfo](https://github.com/heyajohnny/cryptoinfo) from which this component was born.

[W3Schools](https://www.w3schools.com/python/default.asp) for being an invaluable learning resource.
