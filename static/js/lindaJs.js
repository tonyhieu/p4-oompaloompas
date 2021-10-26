var quotes = [
    'Optimism is the one quality more associated with success and happiness than any other. - Brian Tracy',
    'Happiness is not something ready-made. It comes from your own actions.- Dalai Lama',
    'All our dreams can come true if we have the courage to pursue them. - Walt Disney',
    'Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill',
    'I can’t change the direction of the wind, but I can adjust my sails to always reach my destination. – Jimmy Dean',
    'Move out of your comfort zone. You can only grow if you are willing to feel awkward and uncomfortable when you try something new. - Brian Tracy' ,
    'We must be willing to let go of the life we planned so as to have the life that is waiting for us. – Joseph Campbell',
    'People who are crazy enough to think they can change the world, are the ones who do. - Rob Siltanen',
    'Happiness is not by chance, but by choice. – Jim Rohn',
    'We may encounter many defeats but we must not be defeated. – Maya Angelou'
]

function newQuote() {
    var randomNumber = Math.floor(Math.random() * (quotes.length));
    document.getElementById('quoteDisplay').innerHTML = quotes[randomNumber];
}


function find_twos_and_eights(){
    let num = document.getElementById('find-two-or-eight').value;
    let result = 0;
    for (let i = 0; i < num; i++){
        //check if i is an even number: if i divided by 2 gives me 0, i is an even number; if not, odd number.
        if(i % 2 !== 0) {
            //if not an even number, skip the following code
            continue
        }
        //check if i contains 2 or 8
        if(String(i).includes('2') || String(i).includes('8')){
            result=result+1;
        }
    }
    document.getElementById('result-for-find-two-or-right').innerHTML = "The result is :" + result;
    return result;
}

const msg_list = document.getElementById("send-messages");
const msg_input = document.getElementById("message-input");
const no_msg = document.getElementById("no-msg");

function sendMessage() {
    //console.log(msg_input.value);
    linode = document.createElement("li");
    textNode = document.createTextNode(msg_input.value);

    linode.appendChild(textNode);
    //console.log(linode);
    msg_list.appendChild(linode);

    // clear the input
    msg_input.value = "";

    msg_list.removeChild(no_msg);
}


function changeInput(btn){
    var current = document.getElementById(btn).textContent;
    if (current === '0'){
        current = '1'
    }else{
        current = '0'
    }
    document.getElementById(btn).textContent = current
    //display result
    const a = parseInt(document.getElementById('a').textContent);
    const b = parseInt(document.getElementById('b').textContent);
    const and = a & b;
    //inline if condition, syntax rule
    //and === 0 => true/false, ? => if, : => else
    document.getElementById('and').textContent = and === 0 ? "False" : "True";
    document.getElementById('nand').textContent = and === 0 ? "True" : "False";
    const or = a | b;
    document.getElementById('or').textContent = or === 0 ? "False" : "True";
    document.getElementById('nor').textContent = or === 0 ? "True" : "False";
    const xor = a ^ b;
    document.getElementById('xor').textContent = xor === 0 ? "False" : "True";
    document.getElementById('xnor').textContent = xor === 0 ? "True" : "False";
}


