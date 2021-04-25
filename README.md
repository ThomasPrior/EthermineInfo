# EthermineInfo
## A custom component for [HomeAssistant](https://github.com/home-assistant/core) 

<a href="https://www.buymeacoffee.com/tomprior" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png"></a>

# Goals

* Learn some more Python 🐍
* Make my first tangible code contribution to the HomeAssistant community
* Create sensor items for Ethermine items:
  * Current statistics
  
      ❌Unpaid balance
  
      ❌Unconfirmed balance
  
      ✔ Reported hash rate
  
      ❌Average hash rate
  
      ✔ Current hash rate
  
      ✔ Valid shares
  
      ✔ Invalid shares
  
      ✔ Stale shares
  
      ✔ Active workers
     
  * Payouts
  
      ❌Paid on
  
      ❌Amount
  
      ❌Transaction hash

## Things you should know

* I'm new at this, things might not work right away.
* There are limits on how many requests can be made to Ethermine's API and therefore the data retrieved by EthermineInfo will be updated periodically and may be out of date by the time you look at it.
* Please do not use EthermineInfo in isolation to make decisions about your cryptocurrency holdings.
* EthermineInfo only reads the statistics of the provided miner.

## Credits

@heyajohnny's [CryptoInfo](https://github.com/heyajohnny/cryptoinfo) from which this component was born.
W3Schools for being an invaluable learning resource.
