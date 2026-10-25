
document.getElementById("year").textContent = new Date().getFullYear();

const themeButton = document.getElementById("theme-toggle");
themeButton.addEventListener("click", () => {
  document.body.classList.toggle("dark");
});

const menuButton = document.getElementById("menu-toggle");
const navLinks = document.getElementById("nav-links");

menuButton.addEventListener("click", () => {
  navLinks.classList.toggle("show");
});
