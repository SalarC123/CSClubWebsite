const hamburgerIcon = document.querySelector(".hamburger-icon")
const hamburgerDropdown = document.querySelector(".hamburger-dropdown")

function mobileMenuActivate() {
    hamburgerDropdown.style.transition = "all 0.5s ease"
    hamburgerDropdown.classList.toggle("active")
}