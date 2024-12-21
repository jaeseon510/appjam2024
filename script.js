const slides = document.querySelectorAll('.slide');
let currentSlide = 0;

document.querySelectorAll('.next').forEach((button) => {
  button.addEventListener('click', () => {
    moveToNextSlide();
  });
});

document.querySelector('.finish').addEventListener('click', () => {
  alert('완료되었습니다!');
});

function moveToNextSlide() {
  slides[currentSlide].classList.remove('active');
  currentSlide++;
  if (currentSlide >= slides.length) currentSlide = slides.length - 1;
  updateSlidePosition();
}

function updateSlidePosition() {
  const container = document.querySelector('.container');
  container.style.transform = `translateX(-${currentSlide * 100}%)`;
}

function openDetails() {
    document.getElementById("main-container").classList.add("hidden");
    document.getElementById("details-container").classList.remove("hidden");
}
  
function goBack() {
    document.getElementById("details-container").classList.add("hidden");
    document.getElementById("main-container").classList.remove("hidden");
}  