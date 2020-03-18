checkslots_btn = document.getElementById('checkslots_btn');
slotsContainer = document.getElementById("slotresult");
book_btn = document.getElementById('book_btn');

book_btn.disabled = true;
book_btn.style.background = '#999999';

checkslots_btn.disabled = false;
checkslots_btn.style.background = '#4272d7';

checkslots_btn.addEventListener("click",function(){
    const _date = document.getElementById("date_input").value;
    const _time = document.getElementById("time_input").value;
    const _place = document.getElementById("select_places").value;
    var token = '{{csrf_token}}';
    $.ajax({
        type:"GET",
        headers: { "X-CSRFToken": token },
        url: 'http://'+window.location.hostname+':8000/request/',
        data: {
            date : _date,
            time : _time,
            place : _place
        },
        success: function (response) {
          if(response == 'True'){

            book_btn.disabled = false;
            book_btn.style.background = '#4272d7';

            checkslots_btn.disabled = true;
            checkslots_btn.style.background = '#999999';
          }
          else{
            book_btn.disabled = true;
            book_btn.style.background = '#999999';

            checkslots_btn.disabled = false;
            checkslots_btn.style.background = '#4272d7';  
          }
            
          renderHTML(response);
        }
      });
});

function renderHTML(data){
    slotsContainer.insertAdjacentHTML('beforeend','<h4>'+data+' </h4>');
}

function changed(){
  checkslots_btn.disabled = false;
  checkslots_btn.style.background = '#4272d7';  
}