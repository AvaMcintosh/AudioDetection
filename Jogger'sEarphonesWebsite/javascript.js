const buttons = document.querySelectorAll(".toggle-btn");

buttons.forEach(button => {
    button.addEventListener("click", () => {

        // turns all other buttons off
        buttons.forEach(btn => {
            btn.classList.remove("active");
        });

        // turns selected button on
        button.classList.add("active");

    });

});