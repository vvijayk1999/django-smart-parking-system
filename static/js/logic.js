checkslots_btn = document.getElementById('checkslots_btn');
slotsContainer = document.getElementById("slotresult");
book_btn = document.getElementById('book_btn');
update_slot_cards = document.getElementById('update-slot-cards');
slotCards = document.getElementsByClassName('slots-info');
var token = '{{csrf_token}}';

function toggleSlotInfo() {
  var x = document.getElementById("update-slot-cards");
  if (x.style.display === "none") {
    x.style.display = "block";
    updateSlotCardsOnce();
  } else {
    x.style.display = "none";
  }
}
function toggleMap() {
  var x = document.getElementById("map");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

function updateSlotCardsOnce(){
  var _place = document.getElementById("select_places").value;
  $.ajax({
    type:"GET",
    headers: { "X-CSRFToken": token },
    url: 'http://'+window.location.hostname+':'+location.port+'/slot-info',
    data: {
      place : _place
    },
    success: function (response) {
      document.getElementById('update-slot-cards').innerHTML = response;
    },
    error: function(request, error){
      document.getElementById('update-slot-cards').innerHTML = '<div class="slots-info"><h4>Error updating the slot information, Please check your Internet connection.</h4></div>';
    }
  });
}

function updateSlotCards(){
  var _place = document.getElementById("select_places").value;
  $.ajax({
    type:"GET",
    headers: { "X-CSRFToken": token },
    url: 'http://'+window.location.hostname+':'+location.port+'/slot-info',
    data: {
      place : _place
    },
    success: function (response) {
      document.getElementById('update-slot-cards').innerHTML = response;
    },
    complete: function(data){
      setTimeout(updateSlotCards,5000);
     },
    error: function(request, error){
      document.getElementById('update-slot-cards').innerHTML = '<div class="slots-info"><h4>Error updating the slot information, Please check your Internet connection.</h4></div>';
    }
  });
}

$(document).ready(function(){
  setTimeout(updateSlotCards,5000);
 });

book_btn.disabled = true;
book_btn.style.background = '#999999';

checkslots_btn.disabled = false;
checkslots_btn.style.background = '#4272d7';

checkslots_btn.addEventListener("click",function(){
    const _date = document.getElementById("date_input").value;
    const _time = document.getElementById("time_input").value;
    const _place = document.getElementById("select_places").value;
    const _duration = document.getElementById("duration")
    var token = '{{csrf_token}}';
    $.ajax({
        type:"GET",
        headers: { "X-CSRFToken": token },
        url: 'http://'+window.location.hostname+':'+location.port+'/request/',
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