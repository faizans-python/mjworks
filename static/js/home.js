$(document).ready(function() {
var csrftoken = getCookie('csrftoken');

       $("#mechanicform").click(function(event){
            $.ajax({
                 type:"POST",
                 url:"/mechanic/add/",
                 data: {
                        'username': $('#username').val(),
                        'password': $('#password').val() // from form
                        },
        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
                 success: function(data){
                 },
                 error: function(){
                    alert("Something Went wrong plz try again")
                    window.location.href = "/home/"
                 }
            });
            return false; //<---- move it here
       });
});

