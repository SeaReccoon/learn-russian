function check() {
    // Максимальные и текущие баллы
    let maxPoints = 0
    let points = 0

    // Получаем все вопросы
    let questions = document.querySelectorAll(".question")
    for (let question of questions) {
        // Добовляем дополнительный класс, чтобы отключить стили наводки для вопросов
        question.classList.add("question_lock")

        // Получаем правильный и выбранный ответ
        let correctAnswer = question.querySelector(".answer[data-correct='True']")
        let selectedAnswer = question.querySelector(".answer:checked")
        
        // Получаем вес вопроса, то есть сколько за него дают баллов
        let weight = parseInt(question.getAttribute("data-weight"))
        maxPoints += weight

        // Подсвечиваем верный ответ
        correctAnswer.classList.add("option__input_correct")

        // Если ни один отвтет не выбран, то идем к следующему вопросу
        if (!selectedAnswer) continue

        // Совпадает ли выбранный и правильный ответ
        if (correctAnswer === selectedAnswer) {
            // Зачисляем баллы, если выбран правильный
            points += weight
        } else {
            // Подсвечиваем неправильный ответ 
            selectedAnswer.classList.add("option__input_wrong")
        }

        // Снимаем выделение с input
        selectedAnswer.checked = false
    }

    // Показываем результат
    document.querySelector(".btns").classList.add("btns_hide")
    document.querySelector(".result-test").classList.add("result-test_active")

    document.querySelector(".current-points").textContent = points
    document.querySelector(".max-points").textContent = maxPoints

    // Отключаем в input, чтобы нельзя было выбрать их заново
    let answers = document.querySelectorAll(".answer")
    answers.forEach(a => a.disabled = true)
}

// Привязываем проверку к кнопке
function init() {
    let btn = document.querySelector(".check-btn")
    btn.addEventListener("click", check)
}

init()
