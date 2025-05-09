fetch('http://127.0.0.1:8000/')
  .then(response => response.json())
  .then(data => {
      console.log(data);
      document.getElementById('tasks-list').innerHTML = JSON.stringify(data);
  })
  .catch(error => console.error('Error:', error));
