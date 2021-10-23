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

