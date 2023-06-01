const Web3 = require('web3')
const axios = require('axios')
require('dotenv').config()

//get some needed constants
const RPC_URL = process.env.RPC_URL
const PRIVATE_KEY = process.env.PRIVATE_KEY
const FROM_WALLET = process.env.FROM_WALLET
const UNISWAP_WALLET = process.env.UNISWAP_WALLET

//set up the wallet using the private key as 'signing'
const web3 = new Web3(RPC_URL)
const wallet = web3.eth.accounts.wallet.add(PRIVATE_KEY)

const ps = require('prompt-sync')
const prompt = ps({ sigint: true })




//for running shell commands
function exec(cmd, handler = function (error, stdout, stderr) {
    console.log(stdout);
    if (error !== null) {
        console.log(stderr)
    }
}) {
    const childfork = require('child_process');
    return childfork.exec(cmd, handler);
}

function transform_data(text_file) {
    var fs = require('fs')
    var text = fs.readFileSync(String(text_file), 'utf-8')
    //safe data into an array
    var raw_data = text.split(' ')
    // console.log(raw_data)
    return raw_data

}

//simple sleep function
function sleep(seconds) {
    milliseconds = seconds * 1000
    const date = Date.now();
    let currentDate = null;
    do {
        currentDate = Date.now();
    } while (currentDate - date < milliseconds);
}
//generates the required task link
async function get_task_pancake(from_token_name, to_token_name, from_token_amount) {

    //since all tokens have a decimal of 18 we can do this globally
    const to_decimal = '000000000000000000'
    const send_amount = String(from_token_amount) + to_decimal


    //Set the from adress:
    if (from_token_name == 'BUSD') { //BUSD: decimal=18
        var from_token_adress = '0xe9e7cea3dedca5984780bafc599bd69add087d56'

    } else if (from_token_name == 'RBC') { //RBC: decimal=18
        var from_token_adress = '0x8e3bcc334657560253b83f08331d85267316e08a'

    } else if (from_token_name == 'XED') { //XED: decimal=18
        var from_token_adress = '0x5621b5a3f4a8008c4ccdd1b942b121c8b1944f1f'

    } else {
        console.log('I could not find the from adress you were looking for')
        console.log(err)
    }

    //set the to adress:
    if (to_token_name == 'BUSD') {//BUSD: decimal=18
        var to_token_adress = '0xe9e7cea3dedca5984780bafc599bd69add087d56'

    } else if (to_token_name == 'RBC') { //RBC: decimal=18
        var to_token_adress = '0x8e3bcc334657560253b83f08331d85267316e08a'

    } else if (to_token_name == 'XED') { //XED: decimal=18
        var to_token_adress = '0x5621b5a3f4a8008c4ccdd1b942b121c8b1944f1f'

    } else {
        console.log('I could not find the to adress you were looking for')
        console.log(err)
    }



    const task = `https://api.1inch.exchange/v4.0/56/swap?fromTokenAddress=${from_token_adress}&toTokenAddress=${to_token_adress}&amount=${send_amount}&fromAddress=${FROM_WALLET}&slippage=1&gasPrice=7000000000&disableEstimate=true&allowPartialFill=true&gasLimit=600000`


    return task

}
async function get_task_uniswap(from_token_name, to_token_name, from_token_amount) {


    //Set the from adress:
    if (from_token_name == 'BUSD') { //USDT: decimal=6
        var from_token_adress = '0xdac17f958d2ee523a2206206994597c13d831ec7'

    } else if (from_token_name == 'RBC') { //RBC: decimal=18
        var from_token_adress = '0xa4eed63db85311e22df4473f87ccfc3dadcfa3e3'

    } else if (from_token_name == 'XED') { //XED: decimal=18
        var from_token_adress = '0xee573a945b01b788b9287ce062a0cfc15be9fd86'

    } else {
        console.log('I could not find the from adress you were looking for')
        console.log(err)
    }

    //set the to adress:
    if (to_token_name == 'BUSD') {//USDT: decimal=6
        var to_token_adress = '0xdac17f958d2ee523a2206206994597c13d831ec7'

    } else if (to_token_name == 'RBC') { //RBC: decimal=18
        var to_token_adress = '0xa4eed63db85311e22df4473f87ccfc3dadcfa3e3'

    } else if (to_token_name == 'XED') { //XED: decimal=18
        var to_token_adress = '0xee573a945b01b788b9287ce062a0cfc15be9fd86'

    } else {
        console.log('I could not find the to adress you were looking for')
        console.log(err)
    }

    if (from_token_name == 'BUSD') {
        const to_decimal = '000000'
        var send_amount_uniswap = String(from_token_amount) + to_decimal
    } else {
        const to_decimal = '000000000000000000'
        var send_amount_uniswap = String(from_token_amount) + to_decimal
    }



    const task = `https://api.1inch.exchange/v4.0/1/swap?fromTokenAddress=${from_token_adress}&toTokenAddress=${to_token_adress}&amount=${send_amount_uniswap}&fromAddress=${UNISWAP_WALLET}&slippage=1&disableEstimate=true&allowPartialFill=true`


    return task

}

async function get_money_info(first_coin, second_coin, first_coin_amount, trigger_amount) {
    try {

        //get the needed url with specific parameters:
        var got_task_1 = await get_task_pancake(first_coin, second_coin, first_coin_amount)//use the single words in function
        const response = await axios.get(got_task_1)

        var got_task_2 = await get_task_uniswap(first_coin, second_coin, first_coin_amount)//use the single words in function
        const response_uniswap = await axios.get(got_task_2)


        you_will_get_with_decimal = response.data.toTokenAmount
        you_will_get = you_will_get_with_decimal / 1000000000000000000


        you_will_get_with_decimal_uniswap = response_uniswap.data.toTokenAmount

        if (first_coin == 'BUSD') {
            you_will_get_uniswap = you_will_get_with_decimal_uniswap / 1000000000000000000
        } else {
            you_will_get_uniswap = you_will_get_with_decimal_uniswap / 1000000
        }


        if (first_coin == 'BUSD') {
            token_price_uniswap = first_coin_amount / you_will_get_uniswap
        } else {
            token_price_uniswap = you_will_get_uniswap / first_coin_amount
        }
        if (first_coin == 'BUSD') {
            token_price = first_coin_amount / you_will_get
        } else {
            token_price = you_will_get / first_coin_amount
        }




        coin_amount_difference = you_will_get - you_will_get_uniswap


        //get the average of both prices and get the final price
        coin_price = (token_price + token_price_uniswap) / 2
        if (first_coin == 'BUSD') {
            difference_in_dollar = coin_amount_difference * coin_price
        } else {
            difference_in_dollar = coin_amount_difference
        }
        console.log(you_will_get)
        return you_will_get;

    } catch (err) {
        console.log("I didn't swap bro :(")
        console.log(err)
    }

}

function write_csv(time, diff, price) {
    var fs_csv = require("fs");
    fs_csv.appendFileSync("C:/Users/radli/code/documentation/plt/doc/sell_rbc.csv", `${time},${diff},${price}\r\n`);

}
function write_txt(time, first_coin_amount, first_coin, you_will_get, you_will_get_uniswap, second_coin, difference_in_dollar, trigger_amount) {
    var fs_txt = require('fs')
    fs_txt.appendFileSync("C:/Users/radli/code/documentation/txt/doc/sell_rbc.txt", `${time}\n`)
    fs_txt.appendFileSync("C:/Users/radli/code/documentation/txt/doc/sell_rbc.txt", 'For ' + first_coin_amount + ' ' + first_coin + ' you get:\n')
    fs_txt.appendFileSync("C:/Users/radli/code/documentation/txt/doc/sell_rbc.txt", (you_will_get).toFixed(2) + ' ' + second_coin + ' on Pancakeswap\n')
    fs_txt.appendFileSync("C:/Users/radli/code/documentation/txt/doc/sell_rbc.txt", (you_will_get_uniswap).toFixed(2) + ' ' + second_coin + ' on Uniswap\n')
    fs_txt.appendFileSync("C:/Users/radli/code/documentation/txt/doc/sell_rbc.txt", 'The difference is: ' + (difference_in_dollar).toFixed(2) + ' $' + ' (tolerance = ' + trigger_amount + ')\n\n')
}


//swap the token
async function get_info(first_coin, second_coin, first_coin_amount, trigger_amount) {
    try {




        while (true) {
            //
            sleep(0.1)

            //get the needed url with specific parameters:
            var got_task_1 = await get_task_pancake(first_coin, second_coin, first_coin_amount)//use the single words in function
            const response = await axios.get(got_task_1)

            var got_task_2 = await get_task_uniswap(first_coin, second_coin, first_coin_amount)//use the single words in function
            const response_uniswap = await axios.get(got_task_2)


            you_will_get_with_decimal = response.data.toTokenAmount
            you_will_get = you_will_get_with_decimal / 1000000000000000000


            you_will_get_with_decimal_uniswap = response_uniswap.data.toTokenAmount

            if (first_coin == 'BUSD') {
                you_will_get_uniswap = you_will_get_with_decimal_uniswap / 1000000000000000000
            } else {
                you_will_get_uniswap = you_will_get_with_decimal_uniswap / 1000000
            }


            if (first_coin == 'BUSD') {
                token_price_uniswap = first_coin_amount / you_will_get_uniswap
            } else {
                token_price_uniswap = you_will_get_uniswap / first_coin_amount
            }
            if (first_coin == 'BUSD') {
                token_price = first_coin_amount / you_will_get
            } else {
                token_price = you_will_get / first_coin_amount
            }




            coin_amount_difference = you_will_get - you_will_get_uniswap


            //get the average of both prices and get the final price
            coin_price = (token_price + token_price_uniswap) / 2
            if (first_coin == 'BUSD') {
                difference_in_dollar = coin_amount_difference * coin_price
            } else {
                difference_in_dollar = coin_amount_difference
            }

            console.log(' ')
            console.log(' ')
            var currentdate = new Date();
            var datetime = currentdate.getHours() + ":"
                + currentdate.getMinutes() + ":"
                + currentdate.getSeconds();
            console.log(datetime)
            console.log('For ' + first_coin_amount + ' ' + first_coin + ' you get:')
            console.log((you_will_get).toFixed(2) + ' ' + second_coin + ' on Pancakeswap')
            console.log((you_will_get_uniswap).toFixed(2) + ' ' + second_coin + ' on Uniswap')
            console.log('The difference is: ' + (difference_in_dollar).toFixed(2) + ' $' + ' (tolernace = ' + trigger_amount + ')')
            write_txt(datetime, first_coin_amount, first_coin, you_will_get, you_will_get_uniswap, second_coin, difference_in_dollar, trigger_amount)
            write_csv(datetime, (difference_in_dollar).toFixed(2), coin_price)
            var swap_data = 'For ' + first_coin_amount + ' ' + first_coin + ' you get:\n' + (you_will_get).toFixed(2) + ' ' + second_coin + ' on Pancakeswap\n' + (you_will_get_uniswap).toFixed(2) + ' ' + second_coin + ' on Uniswap\n' + 'The difference is: ' + (difference_in_dollar).toFixed(2) + ' $' + ' (tolerance = ' + trigger_amount + ')'
            if (difference_in_dollar > parseFloat(trigger_amount)) {

                if (response.data) {
                    data = response.data
                    data.tx.gas = 700000 //hard set max gas fees
                    // console.log(data)
                    tx = await web3.eth.sendTransaction(data.tx)
                    if (tx.status) {
                        console.log("Just swapped :)")
                        var fs = require('fs')
                        fs.writeFileSync("txt/suicide.txt", 'SWAPPED')

                        var fs_2 = require('fs')
                        fs_2.writeFileSync("C:/Users/radli/code/autoswap_js/notifier/txt/swap_info", swap_data)
                        exec("C:/Users/radli/code/autoswap_js/notifier/swapped")
                        break;
                    } else {
                        console.log("Slippage kicked in :/")
                    }
                }
            }
            //read text data
            var fs = require('fs')
            var text = fs.readFileSync("txt/suicide.txt", 'utf-8')
            //safe data into an array
            var txt_data = text.split(' ')
            if (txt_data[0] == 'YES') {
                console.log('I will die intentionally :)')
                break
            }
            if (txt_data[0] == 'SWAPPED') {
                console.log('I will die intentionally :)')
                break
            }
            sleep(10)
        }


    } catch (err) {
        console.log("I didn't swap bro :(")
        console.log(err)
    }

}


async function main() {
    var fs = require('fs')
    fs.writeFileSync("C:/Users/radli/code/documentation/txt/doc/sell_rbc.txt", '')
    var fs_csv = require('fs')
    fs_csv.writeFileSync("C:/Users/radli/code/documentation/plt/doc/sell_rbc.csv", 'time,diff,price\r\n')
    txt_data = transform_data('C:/Users/radli/code/autoswap_js/wallet/wallet_info.txt')
    txt_data[1] = 'RBC'
    console.log(txt_data[0])
    console.log(txt_data[1])

    var x = await get_money_info(String(txt_data[1]), 'BUSD', String(txt_data[0]), 10000000)

    if (x <= 2240) {
        toleranz = 54
    }
    else if (txt_data[0] <= 2340) {
        toleranz = 50
    }
    else if (txt_data[0] <= 2440) {
        toleranz = 56
    }
    else if (txt_data[0] <= 2540) {
        toleranz = 62
    }
    else {
        toleranz = 68
    }

    await get_info(String(txt_data[1]), 'BUSD', String(txt_data[0]), toleranz)
}

main()
