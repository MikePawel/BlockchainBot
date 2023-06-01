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

var final_coin_name = ""



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
    console.log(raw_data)
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
    //var send_amount = from_token_amount*1000000000000000000

    const to_decimal = '000000000000000000'
    const send_amount = String(from_token_amount) + to_decimal


    //Set the from adress:
    if (from_token_name == 'BUSD') { //BUSD: decimal=18
        var from_token_adress = '0xe9e7cea3dedca5984780bafc599bd69add087d56'

    } else if (from_token_name == 'RBC') { //RBC: decimal=18
        var from_token_adress = '0x8e3bcc334657560253b83f08331d85267316e08a'

    } else if (from_token_name == 'XED') { //XED: decimal=18
        var from_token_adress = '0x5621b5a3f4a8008c4ccdd1b942b121c8b1944f1f'

    } else if (from_token_name == "DERC") { //decimal=18
        var from_token_adress = '0x373e768f79c820aa441540d254dca6d045c6d25b'

    } else if (from_token_name == "FWT") { //decimal=18
        var from_token_adress = '0x893169619461d3ABA810A40b5403c62F27e703F9'

    } else if (from_token_name == "RISE") { //decimal=18
        var from_token_adress = '0xC17c30e98541188614dF99239cABD40280810cA3'

    } else if (from_token_name == "GMT") { //decimal=18
        var from_token_adress = '0x7Ddc52c4De30e94Be3A6A0A2b259b2850f421989'

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

    } else if (to_token_name == "DERC") { //decimal=18
        var to_token_adress = '0x373e768f79c820aa441540d254dca6d045c6d25b'

    } else if (to_token_name == "FWT") { //decimal=18
        var to_token_adress = '0x893169619461d3ABA810A40b5403c62F27e703F9'

    } else if (to_token_name == "RISE") { //decimal=18
        var to_token_adress = '0xC17c30e98541188614dF99239cABD40280810cA3'

    } else if (to_token_name == "GMT") { //decimal=18
        var to_token_adress = '0x7Ddc52c4De30e94Be3A6A0A2b259b2850f421989'

    } else {
        console.log('I could not find the to adress you were looking for (pswap)')
        console.log(err)
    }



    const task = `https://api.1inch.exchange/v4.0/56/swap?fromTokenAddress=${from_token_adress}&toTokenAddress=${to_token_adress}&amount=${send_amount}&fromAddress=${FROM_WALLET}&slippage=1&gasPrice=7000000000&disableEstimate=true&allowPartialFill=true&gasLimit=600000`
    // console.log("p task:  " + task)

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

    } else if (from_token_name == "DERC") {
        var from_token_adress = '0x9fa69536d1cda4a04cfb50688294de75b505a9ae'

    } else if (from_token_name == "FWT") {
        var from_token_adress = '0x4a7397b0b86bb0f9482a3f4f16de942f04e88702'

    } else if (from_token_name == "RISE") {
        var from_token_adress = '0xC17c30e98541188614dF99239cABD40280810cA3'

    } else if (from_token_name == "GMT") {
        var from_token_adress = '0x7Ddc52c4De30e94Be3A6A0A2b259b2850f421989'

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

    } else if (to_token_name == "DERC") {
        var to_token_adress = '0x9fa69536d1cda4a04cfb50688294de75b505a9ae'

    } else if (to_token_name == "FWT") {
        var to_token_adress = '0x4a7397b0b86bb0f9482a3f4f16de942f04e88702'

    } else if (to_token_name == "RISE") {
        var to_token_adress = '0xC17c30e98541188614dF99239cABD40280810cA3'

    } else if (to_token_name == "GMT") {
        var to_token_adress = '0x7Ddc52c4De30e94Be3A6A0A2b259b2850f421989'

    } else {
        console.log('I could not find the to adress you were looking for (uniswap)')
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
    // console.log("u task: " + task)

    return task

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
            console.log('The difference is: ' + (difference_in_dollar).toFixed(2) + ' $' + ' (tolerance = ' + trigger_amount + ')')

            if (difference_in_dollar > parseFloat(trigger_amount)) {

                console.log("i would have traded")
                var fs = require('fs')
                fs.writeFileSync("swap_info.txt",
                    'For ' + first_coin_amount + ' ' + first_coin + ' you get:\n' +
                    (you_will_get).toFixed(2) + ' ' + second_coin + ' on Pancakeswap \n' +
                    (you_will_get_uniswap).toFixed(2) + ' ' + second_coin + ' on Uniswap\n' +
                    'The difference is: ' + (difference_in_dollar).toFixed(2) + ' $' + ' (tolerance = ' + trigger_amount + ')'
                )
                exec('python buy_notifier.py')
            }
            sleep(10)
        }


    } catch (err) {
        console.log("I didn't swap bro :(")
        console.log(err)
        exec('python ../autoswap_js/notifier/error.py')
        main_err()
    }

}


async function main() {
    txt_data = transform_data('current_token.txt')
    if (txt_data[0] <= 2240) {
        toleranz = 106
    }
    else if (txt_data[0] <= 2340) {
        toleranz = 112
    }
    else if (txt_data[0] <= 2440) {
        toleranz = 118
    }
    else if (txt_data[0] <= 2540) {
        toleranz = 120
    }
    else {
        toleranz = 126
    }

    all_coins = ["XED", "RBC", "FWT", "DERC", "GMT"]
    console.log(all_coins)
    let coin_name = prompt('What coin amk? ')
    set_final_coin_name(coin_name)

    await get_info(String(txt_data[1]), coin_name, String(txt_data[0]), toleranz)
}

function set_final_coin_name(coin_name) {
    final_coin_name = coin_name;
}

async function main_err() {
    txt_data = transform_data('current_token.txt')
    if (txt_data[0] <= 2240) {
        toleranz = 106
    }
    else if (txt_data[0] <= 2340) {
        toleranz = 112
    }
    else if (txt_data[0] <= 2440) {
        toleranz = 118
    }
    else if (txt_data[0] <= 2540) {
        toleranz = 120
    }
    else {
        toleranz = 126
    }



    await get_info(String(txt_data[1]), final_coin_name, String(txt_data[0]), toleranz)
}

main()
