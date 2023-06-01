# Trading bot on top of various Blockchains

Note that this project started out as a private trading bot to achieve real profit. This project however expanded into a Bachelor thesis at the top technical university in Germany, at the [RWTH](https://www.rwth-aachen.de/) university in Aachen. The title of the Bachelor Thesis is "Designing a Trading and Analysis Algorithm on Top of the Ethereum and Binance Blockchain" and covers exactly what is described in the title. 

## General Idea:

A modified arbitrage trading technique was firstly tested without any code. Many coins, that were traded both on the Ethereum and BNB blockchain, were taken into consideration. Tremendous criteria were found which are necessary for the entire concept to work. Viable coins which fulfilled those criteria were then bought and sold at a profit. Throughout the design phase of this project, the concept was applied to be compatible with autonomous machine execution and finally was run on a local Laptop that served as a server (deployment on a real server is feasible as well).

Note that, this code example covers multi thread processing for two coins. However, other coins can be used as well with simultaneous tracking and trading properties.

## Code evolution:

- Notification Bot in case of major price difference 
  - SMTP for automatic mail generation and transport
  - Python for web scraping of data
- Trading tool
  - Moralis API for onchain data
  - 1inch API integration for interaction with smart contracts via JavaScript
  - multi thread processing in Python
- Analysis tool
  - python for file management and plotting 
  - better understanding of market moves and opportunities
  
  
 ## Numbers: 
 (roughly one year of data from mid 2021 - mid 2022)
 
 - trading volume produced: $468.692,55
 - total gain (pure profit): 1900% 

