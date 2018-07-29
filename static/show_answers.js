answerButton = document.querySelector('button#viewAnswers');
answerGrid = document.querySelector('div.answers');


answerButton.addEventListener('click', function() {
  answerGrid.style.display = 'grid';
});