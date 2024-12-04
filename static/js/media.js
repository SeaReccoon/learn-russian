// Настройка мобильной кнопки меню
function initMedia() {
    let btn = document.querySelector(".gamb-menu")
    let menu = document.querySelector(".top-menu")

    btn.addEventListener("click", () => menu.classList.toggle("top-menu_active"))
}

initMedia()
