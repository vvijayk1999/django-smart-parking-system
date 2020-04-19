const timer = document.querySelector('.timepicker');
M.Timepicker.init(timer,{
    showClearBtn: true
});

$(document).ready(function(){
    $('.datepicker').datepicker();
});