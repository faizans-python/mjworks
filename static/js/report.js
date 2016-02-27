$(document).ready(function() {
	var dateToday = new Date();
	var csrftoken = getCookie('csrftoken');
    $("#till-date").datepicker({
        maxDate: dateToday
    });
    $("#from-date").datepicker();

    $("#generate-report").click(function(event) {
      event.preventDefault();
        
    $.ajax({
         type:"POST",
         url:"",
         data: $("#report-form").serialize(),

        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
         success: function(data){
         	$("#reportresult").html(data)
         },
         error: function(){
            alert("Something went wrong plz try again")
            window.location.href = "/home/"
         }
    });
    });
});
