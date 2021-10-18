
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