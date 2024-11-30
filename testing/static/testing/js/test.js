function check() {
    let maxPoints = 0
    let points = 0

    let questions = document.querySelectorAll(".question")
    for (let question of questions) {
        question.classList.add("question_lock")

        let correctAnswer = question.querySelector(".answer[data-correct='True']")
        let selectedAnswer = question.querySelector(".answer:checked")
        
        let weight = parseInt(question.getAttribute("data-weight"))
        maxPoints += weight

        correctAnswer.classList.add("option__input_correct")

        if (!selectedAnswer) continue

        if (correctAnswer === selectedAnswer) {
            points += weight
        } else {
            selectedAnswer.classList.add("option__input_wrong")
        }

        selectedAnswer.checked = false
    }

    document.querySelector(".btns").classList.add("btns_hide")
    document.querySelector(".result-test").classList.add("result-test_active")

    document.querySelector(".current-points").textContent = points
    document.querySelector(".max-points").textContent = maxPoints

    let answers = document.querySelectorAll(".answer")
    answers.forEach(a => a.disabled = true)
}

function init() {
    let btn = document.querySelector(".check-btn")
    btn.addEventListener("click", check)
}

init()
