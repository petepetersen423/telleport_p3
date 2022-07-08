
# Final Project

## Teleport Web3 to Ganache

## Crowdfunding Pitch

### Pete Petersen and Dakota Braxton

July 6,2022

![alt text](graduation.jpeg "Yeah Graduation")

## Overview

This project is the third and final project for the Pepperdine Fintech Bootcamp.  For reference and more background refer to the previous 2 projects.

[Project 1 Project Directory](https://github.com/petepetersen423/p1-tellaporte)  
[Project 2 Project Directory](https://github.com/petepetersen423/tellaport_v2)  

The obective of this project is to demonstrate proficiency in several of the technologies covered during course.  In particular, project three focuses on coding style and code reusability in python. Secondary, goals for this project include demonstrating extreme agility in front end development to build POC's to convey the founder vision.

The idea behind this project is that after the first two projects were pitched to potential investors for the startup, Tellporte recieved $2,000,000 in a convertible note.  As a result, the platform was able to be developed. Further, after a successful platform launch and highly targeted social media marketing campaign was implemented, Telleport now has 50,000 active users.

After conducting platform utilization studies, we find the nurses are underutilizing the assistive technologies of the platform.  In order to drive adoption of platform features, we are issuing an incentive NFT called Tellecoin.  This coin will represent 10% of the free float of the company and will be issued to the users of the system based on their enagement level.  These coins may spent on upgraded platform services, saved for capital apreciation or traded on platform for more fungible crypto if desired.

Additionally, to fund the advanced development Telleport requires, we will be issuing $20,000,0000 in interest bearing 5% preferred NFTs available to the public.  The NFT will track ownership dates and increment the interest rate by .25% for every year of contiguous ownership.The proceeds will be also be used to pay off the orginal convertible debt.

## Technologies

This project utilizes the following python libraries in order to use web3 to connect to a local Ganache blockchain, query the wallets, present them in the front end and post a transfer transaction.  Once the applications post and confirms the transaction a QRcode is displayed to the user for convience in referencing the transaction the future.  This appliocation is prototyped in streamlit and represents the NFT transfer mechanism required for spending or trading the Tellcoin common token.

```python
from web3 import Web3
import pandas as pd
import qrcode

from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode  # noqa
import sys
import streamlit as st
from streamlit import cli as stcli
from pathlib import Path

```

## Files

This project includes three demo movies.

1. (NFT_App.mp4)  - UI demo if the transaction app in streamlit
2. (Portfoliio_Dashboard.mp4) - UI demo of the dashboard app in streamlit.
3. (Incentive_app_code_review.mp4) -A quick code review of the transaction app.
4. (Incentive.py) - The web3 transaction application
5. (app.py) -  Sample porfolio dashboard application taken from the streamlit sample library that demonstrates the reusability and rapid prototyping that can be done.  
6. (Sample.csv) -  portfolio data in the fidelity download form.
