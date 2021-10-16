function number(num) {
    const v = document.getElementById("output").innerHTML;
    document.getElementById("output").innerHTML = v === '0' ? num : v + num;
}

function operator(operator) {
    document.getElementById("output").innerHTML += operator;
}

function equal() {
    const v = document.getElementById("output").innerHTML;
    const result = eval(v);
    document.getElementById("output").innerHTML = result;
}

function reset() {
    document.getElementById("output").innerHTML = 0;
}

function _clear() {
    const v = document.getElementById("output").innerHTML;
    document.getElementById("output").innerHTML = v.length === 1 ? '0' : v.slice(0, -1)
}