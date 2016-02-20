$(document).ready(function() {
var csrftoken = getCookie('csrftoken');

       $("#login").submit(function(event){
            $.ajax({
                 type:"POST",
                 url:"/login/",
                 data: {
                        'username': $('#username').val(),
                        'password': $('#password').val() // from form
                        },
        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
                 success: function(data){
                     if (data == "Success"){
                        window.location.href = "/home/"
                     } 
                 }
            });
            return false; //<---- move it here
       });
});
