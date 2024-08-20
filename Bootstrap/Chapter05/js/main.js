$(document).ready(function() {
    $("#contact form").on("submit", function(e) {
        e.preventDefault();

        let $form = $(e.currentTarget);
        let $email = $form.find("#contact-email");
        let $button = $form.find("button[type=submit]");

        if ($email.val().indexOf("@") == -1) {
            $email.closest(".form-group").addClass("has-error");
        } else {
            $form.find(".form-group").addClass("has-success").removeClass("has-error");
            $button.attr("disabled", "disabled");
            $button.after("<span>訊息已送出。我們將盡快與您聯繫。</span>");
        }
    });

    $("#sign-btn").on("click", function(e) {
        $(e.currentTarget).closest("ul").hide();
        $("form#signin").fadeIn("fast");
    });
});
