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

document.getElementById('jojinse-link').addEventListener('click', function(event) {
    window.location.href = 'jojin/jo.html';
});

function handleUserMessage() {
    const userInput = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");
  
    if (!userInput.value.trim()) return;
  
    // Append user's message
    const userMessage = document.createElement("div");
    userMessage.classList.add("chat-message", "user");
    userMessage.innerHTML = `<div class="message user">${userInput.value}</div>`;
    chatBox.appendChild(userMessage);
  
    // Scroll to bottom
    chatBox.scrollTop = chatBox.scrollHeight;
  
    const userText = userInput.value.trim();
    userInput.value = "";
  
    // If specific question is asked, respond
    if (userText === "육개장사발면과 같이 먹을수있는 꿀조합이 있을까?") {
      setTimeout(() => {
        appendBotMessage(
          "이런 조합은 어떠세요? 육개장 사발면 + 참치마요삼각김밥",
          true
        );
      }, 2000);
    }
  }
  
  function appendBotMessage(text, includeImages = false) {
    const chatBox = document.getElementById("chat-box");
  
    const botMessage = document.createElement("div");
    botMessage.classList.add("chat-message", "bot");
    botMessage.innerHTML = `<div class="message bot">${text}</div>`;
    chatBox.appendChild(botMessage);
  
    if (includeImages) {
      const imageContainer = document.createElement("div");
      imageContainer.classList.add("image-container");
  
      // Add example images
      const img1 = document.createElement("img");
      img1.src = "https://via.placeholder.com/80";
      img1.alt = "육개장 사발면";
      imageContainer.appendChild(img1);
  
      const img2 = document.createElement("img");
      img2.src = "https://via.placeholder.com/80";
      img2.alt = "참치마요삼각김밥";
      imageContainer.appendChild(img2);
  
      botMessage.appendChild(imageContainer);
    }
  
    // Scroll to bottom
    chatBox.scrollTop = chatBox.scrollHeight;
  }