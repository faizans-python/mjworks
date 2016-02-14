$(document).ready(function() {
var csrftoken = getCookie('csrftoken');
console.log("hellowwww")

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
                    console.log(location.host)
                     if (data == "Success"){
                        window.location.href = "/home/"
                        console.log(data)
                     } 
                 }
            });
            return false; //<---- move it here
       });
});
