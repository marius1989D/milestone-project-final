var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
    var currentScrollPos = window.pageYOffset;
    if (prevScrollpos > currentScrollPos) {
        document.getElementById("footer").style.bottom = "0", transitionTimingFunction = "linear";
        document.getElementById("footer").style.transition = "all 0.7s";
    } else {
        document.getElementById("footer").style.bottom = "-50px", transitionTimingFunction = "linear";
        document.getElementById("footer").style.transition = "all 0.7s";
    }
    prevScrollpos = currentScrollPos;
}