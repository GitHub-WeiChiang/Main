$(document).ready(function() {
    let anime = document.querySelector(".progress-bar.active");

    anime.addEventListener("animationend", function() {
        $(".alert.alert-success").fadeIn(500);
    });
});
