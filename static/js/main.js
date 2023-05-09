function toggleNav() {
  var navbar = document.getElementsByClassName("navbar")[0];
  if (navbar.className === "navbar") {
    navbar.className += " responsive";
  } else {
    navbar.className = "navbar";
  }

  window.addEventListener('click', function(event) {
    if (!navbar.contains(event.target)) {
      navbar.classList.remove('responsive');
    }
  });
}