const chatbotContainer = document.querySelector('.chatbot-container');
const chatbotBody = document.querySelector('.chatbot-body');
const chatbotInput = document.querySelector('.chatbot-input input');
const chatbotBtn = document.querySelector('.chatbot-input button');

chatbotBtn.addEventListener('click', () => {
  const userMessage = chatbotInput.value;
  chatbotInput.value = '';

  const userMessageElement = document.createElement('div');
  userMessageElement.classList.add('chatbot-message', 'user-message');
  userMessageElement.innerHTML = `
    <p>${userMessage}</p>
  `;

  chatbotBody.appendChild(userMessageElement);

  // Send a reply after a 1-second delay
  setTimeout(() => {
    fetch('/get-response')
    .then(response => response.text())
    .then(data => {
        botMessage=data;
    })
    .catch(error => {
        console.error('Request failed', error);
      });
    // Send a GET request to the server


    const botMessageElement = document.createElement('div');
    botMessageElement.classList.add('chatbot-message', 'bot-message');
    botMessageElement.innerHTML = `
      <p>${botMessage}</p>
    `;

    chatbotBody.appendChild(botMessageElement);

    // Scroll to bottom of chat
    chatbotContainer.scrollTop = chatbotContainer.scrollHeight;
  }, 1000);
});
