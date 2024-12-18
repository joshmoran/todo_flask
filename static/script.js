let dateNtime = document.getElementsByClassName( 'dateAndTime');

for ( let a = 0; a < dateNtime.length; a++ ) { 
  window.addEventListener( 'load', () => {
    setInterval( time_printer, 1000, a, dateNtime[a].innerHTML)
  });
}

function time_printer( number, string ) {
  var timeNow = new Date();
  let taskTime = new Date(string);

  let nowEpoch = Math.floor( timeNow / 1000 );
  let taskEpoch = Math.floor( taskTime / 1000 );

  let between = Math.abs( taskEpoch - nowEpoch );

  // Working from epoch    
  let year = Math.floor( between / 31536000 );
  between -= year * 31536000;

  let month = Math.floor(between / 2628000 );
  between -= month * 2628000;
  
  let days = Math.floor(between / 86400  );
  between -= days * 86400;

  let hours = Math.floor(between / 3600 );
  between -= hours * 3600;

  let minutes = Math.floor(between / 60 );
  between -= minutes * 60;

  let seconds = Math.floor(between % 60);

  parent = dateNtime[number].parentNode.parentNode.parentNode;
  if ( days < 1 ) {
    parent.style.border = '5px solid red';
    new_string = `${days} days, ${hours} hours, ${minutes} minutes, ${seconds} seconds`;
  } else {
    parent.style.border = 'none';
  new_string = `${year} years, ${month} months, ${days} days`;
  }

  dateNtime[number].innerHTML = new_string
}
