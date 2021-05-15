# EthermineInfo
[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)
## A custom component for [HomeAssistant](https://github.com/home-assistant/core) 

Provides data from [Ethermine.org](https://ethermine.org/) on a specified miner.

If this has been of use, please consider funding my caffeine habit:

<a href="https://www.buymeacoffee.com/tomprior" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png"></a>

# Goals

* Learn some more Python 🐍
* Make my first tangible code contribution to the HomeAssistant community
* Create sensor items for Ethermine items:
  * Current statistics
  
      ✔ Unpaid balance
  
      ❌Unconfirmed balance
  
      ✔ Reported hash rate
  
      ❌Average hash rate
  
      ✔ Current hash rate
  
      ✔ Valid shares
  
      ✔ Invalid shares
  
      ✔ Stale shares
  
      ✔ Active workers
     
  * Payouts
  
      ✔ Paid on
  
      ✔ Amount
  
      ✔ Transaction hash

## Things you should know

* I'm new at this, things might not work right away, or at all. Please be kind!
* There are limits on how many requests can be made to Ethermine's API and therefore the data retrieved by EthermineInfo will be updated periodically and may be out of date by the time you look at it.
* Please do not use EthermineInfo in isolation to make decisions about your cryptocurrency holdings.
* EthermineInfo only reads the statistics of the provided miner.

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
````

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

![image](https://user-images.githubusercontent.com/34111848/115997170-18a74100-a5da-11eb-8975-d14a46a1cca4.png)

## Discussion

[Talk about EthermineInfo here](https://community.home-assistant.io/t/my-first-custom-component-ethermineinfo/302734)

Pull requests and constructive criticism are always welcome.

## Credits

[@heyajohnny's](https://github.com/heyajohnny) [CryptoInfo](https://github.com/heyajohnny/cryptoinfo) from which this component was born.

[W3Schools](https://www.w3schools.com/python/default.asp) for being an invaluable learning resource.
