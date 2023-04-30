const dropdownBtn = document.getElementById('dropdown-btn');
const dropdownContainer = document.querySelector('.dropdown-container');
const display = document.getElementById("selectedCountry");

dropdownBtn.addEventListener('click', () => {
  dropdownContainer.classList.toggle('show');
});


function selectCountry(country) {
  localStorage.setItem("selectedCountry", country);
  document.getElementById("selectedCountry").textContent = country;
}


window.addEventListener('click', (event) => {
  if (!event.target.matches('.dropdown-container') && !event.target.matches('.dropdown-container *') && !event.target.matches('#dropdown-btn') && !event.target.matches('#dropdown-btn *')) {
    dropdownContainer.classList.remove('show');
  }
});