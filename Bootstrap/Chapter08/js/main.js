$(document).ready(function() {
    let anime = document.querySelector(".progress-bar.active");

    anime.addEventListener("animationend", function() {
        $(".alert.alert-success").fadeIn(500);
    });

    /////

    let charCount = $("#tweet-modal .char-count");
    let maxCharCount = parseInt(charCount.data("max"), 10);

    $("#tweet-modal textarea").on("keyup", function(e) {
        let tweetLength = $(e.currentTarget).val().length;
        charCount.html(maxCharCount - tweetLength);
    });

    /////

    $("[data-toggle='tooltip']").tooltip();

    /////

    let popoverContentTemplate = '' +
        '<div style="width: 15em">' +
        '    <img src="imgs/breed.jpg" class="img-rounded">' +
        '    <div class="info">' +
        '        <strong>狗品種</strong>' +
        '        <a href="#" class="btn btn-default">' +
        '            <span class="glyphicon glyphicon-plus" aria-hidden="true"></span>' +
        '            關注' +
        '        </a>' +
        '    </div>' +
        '</div>' +
    '';

    $("[data-toggle='popover']").popover({
        placement: "bottom",
        html: true,
        content: function() {
            return popoverContentTemplate;
        }
    });

    /////

    $("[data-toggle='popover']").on("show.bs.popover", function() {
        let icon = $(this).find("span.glyphicon");
        icon.removeClass("glyphicon-plus").addClass("glyphicon-ok");

        let content = $(this).find("span#content");
        content.text("關注中")
    });

    /////

    $("#profile").on("affix.bs.affix", function() {
        $(this).width($(this).width() - 0.5);
        $("#main").addClass("col-md-offset-3");
    }).on("affix-top.bs.affix", function() {
        $(this).css("width", "");
        $("#main").removeClass("col-md-offset-3");
    });
});
