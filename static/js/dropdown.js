const dropdownBtn = document.getElementById('dropdown-btn');
const dropdownContainer = document.querySelector('.dropdown-container');

dropdownBtn.addEventListener('click', () => {
  dropdownContainer.classList.toggle('show');
});
