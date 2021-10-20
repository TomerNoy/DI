const input = document.getElementById('input');
console.log(input.value);

/// "keyup" has latency issues !?
// input.addEventListener('keyup', (e) => {
//     const letter = e.key;
//     input.value = input.value.slice(0, -1);
//     if (/[a-zA-Z]/.test(letter)) input.value += letter
// });

/// this works better
input.addEventListener('input', () => {
    const found = input.value.match(/[a-zA-Z]/g);
    found !== null ? input.value = found.join('') : input.value = input.value.slice(0, -1);
});