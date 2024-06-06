const btnAdd = document.getElementById("add_item");

const ulElement = document.querySelector("ul");

btnAdd.addEventListener("click", () => {
  let newItem = document.createElement("li");
  newItem.textContent = "Item";
  ulElement.append(newItem);
});
