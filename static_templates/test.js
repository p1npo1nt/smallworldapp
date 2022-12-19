const divs = document.querySelectorAll('div');

const reset = () => {
    divs.forEach(div => div.classList.remove('active'))
}

divs.forEach(div => div.addEventListener('mouseover', () => {
    reset();
    div.classList.toggle('active');
}));

divs.forEach(div => div.addEventListener('mouseout', () => {
    reset();
}))