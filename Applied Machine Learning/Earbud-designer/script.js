const earbud = document.getElementById("earbud");
const colorPicker = document.getElementById("colorPicker");
const patternSelect = document.getElementById("pattern");
const sizeSlider = document.getElementById("sizeSlider");

colorPicker.addEventListener("input", () => {
    earbud.style.background = colorPicker.value;
});

patternSelect.addEventListener("change", () => {
    if (patternSelect.value === "dots") {
        earbud.style.backgroundImage =
            "radial-gradient(white 10%, transparent 11%)";
        earbud.style.backgroundSize = "10px 10px";
    } else if (patternSelect.value === "lines") {
        earbud.style.backgroundImage =
            "repeating-linear-gradient(45deg, white, white 5px, transparent 5px, transparent 10px)";
    } else {
        earbud.style.backgroundImage = "none";
    }
});

sizeSlider.addEventListener("input", () => {
    const size = sizeSlider.value;
    earbud.style.transform = `scale(${size / 100})`;
});
