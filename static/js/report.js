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
             	$("#reportresult").html(data);
                $("#generate-invoice").show();
                $.toast({
                    heading: 'Success',
                    text: 'Report sucessfully generated !!!'+,
                    icon: 'error',
                    hideAfter: 4000,
                    position: 'bottom-right'
                })
             },
             error: function(){
                $.toast({
                    heading: 'Error',
                    text: 'Something went wrong!!! Please try again',
                    icon: 'error',
                    hideAfter: 4000,
                    position: 'bottom-right'
                })
             }
        });
    });

    $("#generate-invoice").click(function(event) {
        $("#report-form").submit();
    });
});
