$(document).ready(function() {
	var dateToday = new Date();
	var csrftoken = getCookie('csrftoken');

  function customerreportform(url) {
      var customer_id = $('#customerdropdown').val();
      if ($('#pending').is(':checked')) {
        var pending = true
      }
      else{
        var pending = false
      }
      $.ajax({
           type:"POST",
           url:url,
           data: {
              "customer_id": customer_id,
              "pending": pending
           },

          beforeSend: function(xhr) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          },
           success: function(data){
            $("#reportresult").html(data);
            $("#generate-invoice").show();
           },
           error: function(){
              alert("Something went wrong plz try again")
              window.location.href = "/home/"
           }
      });
    }

    $("#generate-report").click(function(event) {
      event.preventDefault();
      var url = ""
      customerreportform(url);
    });

    $("#generate-invoice").click(function(event) {
        console.log("clicked")
        event.preventDefault();
        var url = "/service/customer/report/generate/"
        customerreportform(url);
    });
});
