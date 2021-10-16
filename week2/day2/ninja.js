// exercise 1:
// const bDate1 = 1979, bDate2 = 2000;

// const age1 = 2021 - Number(bDate1), age2 = 2021 - Number(bDate2);
// const val = age2 / age1;
// const result = val === 0.5 ? 'bDate2' : val === 2 ? 'bDate1' : null;
// console.log(`age1 = ${age1}, age2 = ${age2} result = ${result}`);
//------------------------------------------------

// exercise 2:
// const checkZip = (zip) => {
//     if (zip.length !== 5) return false;
//     for (l of zip.split('')) {
//         if (isNaN(l) || l == ' ') return false;
//     }
//     return true;
// }

// with regex
// const checkZipRegex = (zip) => /^(\d{5})$/.test(zip);

// const zip = prompt('please enter your zip code');
// console.log(checkZipRegex(zip) ? 'success' : 'error');

// exercise 3
// const zip = prompt('enter any word');
// console.log(zip.replace(/[aeiouAEIOU]/g, ''));
// console.log(zip.replace(/[aeiouAEIOU]/g, '*'));