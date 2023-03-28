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

  // Send a POST request to the server with the user's input
  setTimeout(() => {
    fetch('/chatbot_web')
      .then(response => response.json())
      .then(data => {
        const botMessage = data;
        const botMessageElement = document.createElement('div');
        botMessageElement.classList.add('chatbot-message', 'bot-message');
        botMessageElement.innerHTML = `
          <p>${botMessage}</p>
        `;
        chatbotBody.appendChild(botMessageElement);
        chatbotContainer.scrollTop = chatbotContainer.scrollHeight;
      })
      .catch(error => {
        console.error('Request failed', error);
      });
  }, 1000);
});



// chatbotBtn.addEventListener('click', () => {
//   const userMessage = chatbotInput.value;
//   chatbotInput.value = '';

//   const userMessageElement = document.createElement('div');
//   userMessageElement.classList.add('chatbot-message', 'user-message');
//   userMessageElement.innerHTML = `
//     <p>${userMessage}</p>
//   `;

//   chatbotBody.appendChild(userMessageElement);

//   // Send a reply after a 1-second delay
//   setTimeout(() => {
//     fetch('/chatbot')
//       .then(response => response.text())
//       .then(data => {
//           botMessage=data;
//     })
//     // .catch(error => {
//     //     console.error('Request failed', error);
//     //   });
//     // Send a GET request to the server


//     const botMessageElement = document.createElement('div');
//     botMessageElement.classList.add('chatbot-message', 'bot-message');
//     botMessageElement.innerHTML = `
//       <p>${botMessage}</p>
//     `;

//     chatbotBody.appendChild(botMessageElement);

//     // Scroll to bottom of chat
//     chatbotContainer.scrollTop = chatbotContainer.scrollHeight;
//   }, 1000);
// });
