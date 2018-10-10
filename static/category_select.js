//let categorySelect = document.querySelector('select#id_category').value;
let problemType = document.querySelector('p.problem-type').textContent;
let problem = document.querySelector('p.problem').textContent;
let problemSelector = document.querySelector('select#id_problem');
problemSelector.value = problem;

console.log(problemSelector);
console.log(problem);