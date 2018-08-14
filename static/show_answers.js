let answerButton = document.querySelector('button#viewAnswers');
let answerGrid = document.querySelector('div.answers');


answerButton.addEventListener('click', function() {
  answerGrid.style.display = 'grid';
});