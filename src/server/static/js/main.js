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
  const stopMovement = function() {
    data = {'direction': 'stop'}
    postData('/move', data)
    .then((x) => console.log(x))
  }



  const danceButton = document.querySelector('#dance')
  danceButton.addEventListener('click', (e) => {
    postData('/dance')
    .then((x) => console.log(x))
  })

  const forwardButton = document.querySelector('#forward')
  forwardButton.addEventListener('mousedown', (e) => {
    data = {'direction': 'forward'}
    postData('/move', data)
    .then((x) => console.log(x))
  })

  forwardButton.addEventListener('mouseup', (e) => {
    stopMovement()
  })

  const reverseButton = document.querySelector('#reverse')
  reverseButton.addEventListener('mousedown', (e) => {
    data = {'direction': 'reverse'}
    postData('/move', data)
    .then((x) => console.log(x))
  })

  reverseButton.addEventListener('mouseup', (e) => {
    stopMovement()
  })

  const leftButton = document.querySelector('#left')
  leftButton.addEventListener('mousedown', (e) => {
    data = {'direction': 'left'}
    postData('/move', data)
    .then((x) => console.log(x))
  })

  leftButton.addEventListener('mouseup', (e) => {
    stopMovement()
  })

  const rightButton = document.querySelector('#right')
  rightButton.addEventListener('mousedown', (e) => {
    data = {'direction': 'right'}
    postData('/move', data)
    .then((x) => console.log(x))
  })

  rightButton.addEventListener('mouseup', (e) => {
    stopMovement()
  })

  const stopButton = document.querySelector('#stop')
  stopButton.addEventListener('click', (e) => {
    stopMovement()
  })
}


document.addEventListener('DOMContentLoaded', appStart);