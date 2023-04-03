// const userinputdisplay = document.querySelector('sent_msg');
// const chatbotbtn = document.querySelector('msg_send_btn');
// const userinputtext = document.querySelector('write_msg');

// chatbotbtn.addEventListener('click',()=>{
//     const usertext={{user_input}};
//     userinputtext.value = '';
//     // const userMessageElement = document.createElement('div');
//     // userMessageElement.classList.add('chatbot-message', 'user-message');
//     userinputdisplay.innerHTML = `
//         <p>${usertext}</p>
//     `;

//     // chatbotBody.appendChild(userMessageElement);

// });

const form = document.querySelector('form');

form.addEventListener('submit', function(event) {
  event.preventDefault();
  
  const userInput = document.querySelector('.write_msg').value;
  
  const messageDiv = document.createElement('div');
  messageDiv.classList.add('outgoing_msg');
  messageDiv.innerHTML = `
    <div class="sent_msg">
      <p>${userInput}</p>
      <span class="time_date">${new Date().toLocaleTimeString()} | ${new Date().toLocaleDateString()}</span>
    </div>
  `;
  
  const outgoingMsgDiv = document.querySelector('.msg_history');
  outgoingMsgDiv.appendChild(messageDiv);
  
  document.querySelector('.write_msg').value = '';
});
