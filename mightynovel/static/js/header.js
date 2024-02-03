window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    const header = document.getElementById('header');
    if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
        header.classList.remove('header');
        header.classList.add('header-scroll');
    } else {
        header.classList.add('header');
        header.classList.remove('header-scroll');
    }
}