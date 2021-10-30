let a = []

for (x = 0; x < 7; x++) {

    a.push([]);
    for (y = 0; y < 7; y++) {
        // a[x].push(`${x}|${y}`)
        if ((x > 0 && [1, 5].includes(y)) ||
            ([0, 3].includes(x) && [2, 3, 4].includes(y))) {
            a[x].push('*');
        }

        else {
            a[x].push(' ');
        }
    }
}

a = a.map(e => e.join(''));
a = a.join('\n');
console.log(a)