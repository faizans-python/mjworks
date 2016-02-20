$(document).ready(function() {
    var csrftoken = getCookie('csrftoken');

    $("#customerform").submit(function(event){
        event.preventDefault();
        $.ajax({
             type:"POST",
             url:"/customer/create/",
             data: $("#customerform").serialize(),
    beforeSend: function(xhr) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
    },
             success: function(data){
                $("#customerform").trigger('reset');
                alert(data + " added successfully")
             },
             error: function(){
                alert("Something went wrong plz try again")
                window.location.href = "/home/"
             }
        });
        return false; //<---- move it here
   });
});
