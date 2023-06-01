const axios = require("axios")
require('dotenv').config()
const XAPI = process.env.X_API_KEY
const FROM_WALLET = process.env.FROM_WALLET

async function fun() {
    var response = await axios
        .get(
            `https://deep-index.moralis.io/api/v2/${FROM_WALLET}/erc20?chain=bsc`,
            {
                headers: {
                    accept: "application/json",
                    "X-API-Key": XAPI,
                },
            }
        )
    stringeroo = ""
    for (let i = 0; i < response.data.length; i++) {
        if (response.data[i].symbol == "BUSD") {
            var res = response.data[i].balance
            res = res * 10 ** -18
            res = Math.trunc(res)
            stringeroo = String(res) + " BUSD"
            if (res < 1000) {
                for (let j = 0; j < response.data.length; j++) {
                    if (response.data[j].symbol == "XED") {
                        res = response.data[j].balance
                        res = res * 10 ** -18
                        res = Math.trunc(res)
                        stringeroo = String(res) + " XED"
                        if (res < 100) {
                            for (let k = 0; k < response.data.length; k++) {
                                if (response.data[k].symbol == "RBC") {
                                    res = response.data[k].balance
                                    res = res * 10 ** -18
                                    res = Math.trunc(res)
                                    stringeroo = String(res) + " RBC"
                                    break
                                }
                            }
                        }
                    } else if (response.data[j].symbol == "BRBC") {
                        res = response.data[j].balance
                        res = res * 10 ** -18
                        res = Math.trunc(res)
                        stringeroo = String(res) + " RBC"
                        if (res < 100) {
                            for (let k = 0; k < response.data.length; k++) {
                                if (response.data[k].symbol == "XED") {
                                    res = response.data[k].balance
                                    res = res * 10 ** -18
                                    res = Math.trunc(res)
                                    stringeroo = String(res) + " XED"
                                    break
                                }
                            }
                        }
                        break
                    }
                }
            }

        } else if (response.data[i].symbol == "BRBC") {
            var res = response.data[i].balance
            res = res * 10 ** -18
            res = Math.trunc(res)
            if (res > 100) {
                stringeroo = String(res) + " RBC"
                break
            }
        } else if (response.data[i].symbol == "XED") {
            var res = response.data[i].balance
            res = res * 10 ** -18
            res = Math.trunc(res)
            if (res > 100) {
                stringeroo = String(res) + " XED"
                break
            }
        }
    }
    var fs = require('fs')
    fs.writeFileSync("C:/Users/radli/code/autoswap_js/wallet/wallet_info.txt", String(stringeroo))
}
fun()
