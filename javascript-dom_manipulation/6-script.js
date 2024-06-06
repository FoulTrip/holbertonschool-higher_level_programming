async function fetchStarWarsName() {
  try {
    const response = await fetch(
      "https://swapi-api.hbtn.io/api/people/5/?format=json"
    );
    const data = await response.json();
    return data;
  } catch (error) {
    return error;
  }
}

function displayName(character) {
  const nameList = document.getElementById("character");

  const nameElement = document.createElement("div");
  nameElement.innerHTML = `
    <h2>${character.name}</h2>
    <hr>
    `;
  nameList.appendChild(nameElement);
}

async function main() {
  try {
    const character = await fetchStarWarsName();
    displayName(character);
  } catch (error) {
    console.error("Error fetching and displaying data:", error);
  }
}

main();
