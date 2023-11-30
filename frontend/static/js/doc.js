function showCode(elementId) {
    var codeContainer = document.getElementById(elementId);
    if (codeContainer.style.display === "none") {
        codeContainer.style.display = "block";
    } else {
        codeContainer.style.display = "none";
    }
}