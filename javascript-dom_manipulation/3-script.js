const btnToggle = document.getElementById("toggle_header");
const header = document.querySelector("header");

btnToggle.addEventListener("click", () => {
  if (header.classList.contains("red")) {
    header.classList.remove("red");
    header.classList.add("green");
  } else if (header.classList.contains("green")) {
    header.classList.remove("green");
    header.classList.add("red");
  }
});
