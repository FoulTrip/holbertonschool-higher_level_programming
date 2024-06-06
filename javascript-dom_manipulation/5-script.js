const changeText = document.querySelector("header");
const element = document.getElementById("update_header");

element.addEventListener("click", function () {
  changeText.textContent = "New Header!!!";
});
