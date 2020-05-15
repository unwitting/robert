async function postData(url = '', data = {}) {
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  });
  return response.json();
}

const appStart = function() {
  const danceButton = document.querySelector('#dance-button');
  danceButton.addEventListener('click', (e) => {
    postData('/dance')
      .then(console.log('posting'))
  })
}


document.addEventListener('DOMContentLoaded', appStart);