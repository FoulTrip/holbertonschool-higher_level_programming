async function fetchStarWarsFilms() {
  try {
    const response = await fetch(
      "https://swapi-api.hbtn.io/api/films/?format=json"
    );
    const data = await response.json();
    return data.results;
  } catch (error) {
    return error;
  }
}

function displayFilms(list_movies) {
  const nameList = document.getElementById("list_movies");

  list_movies.forEach((movie) => {
    const nameElement = document.createElement("li");
    nameElement.innerHTML = `
            ${movie.title}
            
        `;
    nameList.appendChild(nameElement);
  });
}

async function main() {
  try {
    const movies = await fetchStarWarsFilms();
    displayFilms(movies);
  } catch (error) {
    console.error(error);
  }
}

main();
