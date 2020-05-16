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
  const danceButton = document.querySelector('#dance')
  danceButton.addEventListener('click', (e) => {
    postData('/dance')
    .then((x) => console.log(x))
  })

  const forwardButton = document.querySelector('#forward')
  forwardButton.addEventListener('click', (e) => {
    data = {'direction': 'forward'}
    postData('/move', data)
    .then((x) => console.log(x))
  })

  const reverseButton = document.querySelector('#reverse')
  reverseButton.addEventListener('click', (e) => {
    data = {'direction': 'reverse'}
    postData('/move', data)
    .then((x) => console.log(x))
  })

  const leftButton = document.querySelector('#left')
  leftButton.addEventListener('click', (e) => {
    data = {'direction': 'left'}
    postData('/move', data)
    .then((x) => console.log(x))
  })

  const rightButton = document.querySelector('#right')
  rightButton.addEventListener('click', (e) => {
    data = {'direction': 'right'}
    postData('/move', data)
    .then((x) => console.log(x))
  })
}


document.addEventListener('DOMContentLoaded', appStart);