async function fetchTranslation() {
  try {
    const response = await fetch(
      "https://hellosalut.stefanbohacek.dev/?lang=fr"
    );
    const data = await response.json();
    return data.hello;
  } catch (error) {
    return error;
  }
}

async function displayTranslation() {
  try {
    const phaseTransl = await fetchTranslation();
    const element = document.getElementById("hello");

    if (element) {
      element.textContent = phaseTransl;
    } else {
      return error;
    }
  } catch (error) {
    console.error(error);
  }
}

async function main() {
  await displayTranslation();
}

main();
