$(document).ready(function() {
	var dateToday = new Date();
	var csrftoken = getCookie('csrftoken');

    $("#generate-report").click(function(event) {
      event.preventDefault();
      var customer_id = $('#customerdropdown').val();
      if ($('#pending').is(':checked')) {
        var pending = true
      }
      else{
        var pending = false
      }
    $.ajax({
         type:"POST",
         url:"",
         data: {
            "customer_id": customer_id,
            "pending": pending
         },

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
