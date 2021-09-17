let fadeElement = [...document.querySelectorAll('.fade-up')];
let fadeIn = [...document.querySelectorAll('.fade-in')];
let fadeIn2 = [...document.querySelectorAll('.fade-in2')];
let fadeIn3 = [...document.querySelectorAll('.fadeImg')];
let fadeIn4 = [...document.querySelectorAll('.fadeImg2')];

let options = {
    rootMargin: '-10%',
    threshold: 0.0
}

/* --------------text's transition---------------- */

let observer = new IntersectionObserver(showItem, options);

function showItem(entries){
    entries.forEach(entry => {
        if(entry.isIntersecting){
            entry.target.classList.add('active');
        }
    })
}

fadeElement.forEach(item => {
    observer.observe(item);
})

/* --------------flask's transition--------------- */

let observer2 = new IntersectionObserver(showItem2, options);

function showItem2(entries){
    entries.forEach(entry => {
        if(entry.isIntersecting){
            entry.target.classList.add('in');
        }
    })
}

fadeIn.forEach(item => {
    observer2.observe(item);
})


/* --------------html's transition---------------- */

let observer3 = new IntersectionObserver(showItem3, options);

function showItem3(entries){
    entries.forEach(entry => {
        if(entry.isIntersecting){
            entry.target.classList.add('in2');
        }
    })
}

fadeIn2.forEach(item => {
    observer3.observe(item);
})

/* --------------question's movements----------------------- */

function onClick(id){
    let element = document.getElementById(id);
    let childes = element.childNodes;
    childes[1].classList.toggle("turn");

    let sibling = element.nextElementSibling;

    if( sibling.style.height == ""){
        sibling.style.height = "fit-content";
        sibling.style.padding = "10px 20px";
        /* sibling.style.transition = "height 3s"; */
    }else{
        sibling.style.height = "";
        sibling.style.padding = "";
    }

}

/* --------------html's transition---------------- */

let observer4 = new IntersectionObserver(showItem4, options);

function showItem4(entries){
    entries.forEach(entry => {
        if(entry.isIntersecting){
            entry.target.classList.add('imggg');
        }
    })
}

fadeIn3.forEach(item => {
    observer4.observe(item);
})

/* --------------html's transition---------------- */

let observer5 = new IntersectionObserver(showItem5, options);

function showItem5(entries){
    entries.forEach(entry => {
        if(entry.isIntersecting){
            entry.target.classList.add('imgggg');
        }
    })
}

fadeIn4.forEach(item => {
    observer5.observe(item);
})
