'''
This the the code that builds the transaction page for the user to send ether to 
another account.  The user will need to enter the account they want to send, 
the account they want to send to, and the amount of ether they want to send. It connects to the
Ganache blockchain and sends the ether to the recipient account.
'''

from web3 import Web3
import pandas as pd
import qrcode

from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode  # noqa
import sys
import streamlit as st
from streamlit import cli as stcli
from pathlib import Path


def main():
'''
This is the main function that runs the program.
'''
    ganache_url = "http://127.0.0.1:7545"
    web3 = Web3(Web3.HTTPProvider(ganache_url))

    # Get the addresses of the Ganace accounts and make them available
    # to the program

    accounts = web3.eth.accounts

    # create dataframe from accounts with balances
    df = pd.DataFrame(columns=["Account", "Balance", "Private Key", "Index"])
    i = -1  # index to match the Ganache`s accounts index`

    # for each account, get the balance and add it to the dataframe

    for account in accounts:
        i += 1
        balance = web3.eth.getBalance(account)
        df = df.append(
            {
                "Account": account,
                "Balance": balance,
                "Index": i,
            },
            ignore_index=True,
        )

    df.set_index("Account", inplace=True)

    def transfer_eth(sender, recipient, amount):
        """
        Transfer eth from sender to recipient
        """

        web3.eth.sendTransaction(
            {
                "from": sender,
                "to": recipient,
                "value": amount,
            }
        )

    # build the QR code for the account and amount
    def qr_code(from_account, to_account, amount):
        """
        Generate a QR code for the given account and amount
        """

        img = qrcode.make(to_account)
        # img.save(‘QR Code.png’)
        # img.show()
        return img

    # start the streamlit app
    st.title("Tellaport Preferred Equity NFT Transfer")
    st.subheader("Transfer your NFT's between accounts")
    with st.expander("What is an NFT"):
        st.write(Path("nft.md").read_text())

    st.write("This program will allow you to transfer ETH to a new account")

    st.write("Select a sender account from the list below")
    sender = st.selectbox("Sender Account", df.index)

    # get the address of the recipient

    st.write("Select the address of the recipient")
    recipient = st.selectbox("Recipient Account", df.index)

    # get the amount of tokens to be sent

    st.write("Enter the amount of tokens to be sent")
    amount = st.number_input("Amount", value=0)

    if st.button("Transfer"):
        transfer_eth(sender, recipient, amount)
        st.write("Transfer complete")
        st.write("You can share this transaction with the recipient by QR code")
        image = qr_code(sender, recipient, amount)
        image.save("QRCode.png")
        st.image("QRCode.png", width=300)

    st.sidebar.subheader("Transaction details")

    st.sidebar.write("The selected sender is: " + sender)
    st.sidebar.write("The selected recipient is: " + recipient)
    st.sidebar.write("The amount of tokens to be sent is: " + str(amount))


if __name__ == "__main__":
    if st._is_running_with_streamlit:
        # This is a Streamlit app, so we can use the Streamlit CLI to
        # run the main function.
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
