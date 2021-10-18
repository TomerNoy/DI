const getBold_items = () => document.getElementsByTagName('strong');

const highlight = (list) => {
    for (i of list) {
        i.style.color = 'blue';
    }
}

const return_normal = (list)=>{
    for (i of list) {
        i.style.color = 'black';
    }
}

const p = document.body.getElementsByTagName('p')[0];

p.onmousemove = () => highlight(getBold_items());
p.onmouseout = () => return_normal(getBold_items());

