function createError(input) {
  const error = document.createElement("div");
  error.classList.add("error");
  input.parentNode.insertBefore(error, input.nextSibling);

  input.classList.add("error");
  input.style.border = '1px solid red';
}

function removeError(input) {
  input.classList.remove("error");
  const error = input.nextElementSibling;
  if (error && error.classList.contains("error")) {
    input.parentNode.removeChild(error);
    input.style.border = '';
  }
}

function validation(form) {
  const AllInput = form.querySelectorAll('input');
  let isFormValid = true;

  for (const input of AllInput) {
    if (input.value.trim() === "") {
      createError(input);
      isFormValid = false;
    } else {
      removeError(input);
    }
  }

  return isFormValid;
}

const form = document.querySelector("#add-form");

form.addEventListener("submit", function(event) {
  event.preventDefault();

  if (validation(form)) {
    
  }
});