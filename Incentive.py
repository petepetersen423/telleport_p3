from web3 import Web3
import pandas as pd
import qrcode

from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode  # noqa
import sys
import streamlit as st
from streamlit import cli as stcli


def main():

    ganache_url = "http://127.0.0.1:7545"
    web3 = Web3(Web3.HTTPProvider(ganache_url))

    # Get the addresses of the Ganace accounts and make them available
    # to the program

    accounts = web3.eth.accounts

    #

    # create dataframe from accounts with balances
    df = pd.DataFrame(columns=["Account", "Balance", "Private Key", "Index"])
    i = -1

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

    def transfer_eth(from_account, to_account, amount):
        web3.eth.sendTransaction(
            {
                "from": from_account,
                "to": to_account,
                "value": amount,
            }
        )

    # build the QR code for the account and amount
    def qr_code(from_account, to_account, amount):

        img = qrcode.make(to_account)
        # img.save(‘QR Code.png’)
        # img.show()
        return img

    # get a private key from the user
    st.title("Tellaport ETH Transfer Program")
    st.subheader("Transfer ETH to a new account")
    st.write("This program will allow you to transfer ETH to a new account")
    st.write("Select a sender account from the list below")
    sender = st.selectbox(
        "Account", df.index + "    bal=" + df.Balance.astype(str) + ""
    )

    # get the address of the recipient

    st.write("Select the address of the recipient")
    recipient = st.selectbox("Account", df.index + "(Recipient)")

    # get the amount of tokens to be sent

    st.write("Enter the amount of tokens to be sent")
    amount = st.number_input("Amount", value=0)

    st.sidebar.subheader("Transaction details")

    st.sidebar.write("The selected sender is: " + sender)
    st.sidebar.write("The selected recipient is: " + recipient)
    st.sidebar.write("The amount of tokens to be sent is: " + str(amount))

    st.sidebar.subheader("QR Code")

    st.sidebar.write("You can share this transaction with the recipient by QR code")

    image = qr_code(sender, recipient, amount)
    image.save("QRCode.png")
    st.sidebar.image("QRCode.png", width=300)


if __name__ == "__main__":
    if st._is_running_with_streamlit:
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
