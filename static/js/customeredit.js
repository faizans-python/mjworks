$(document).ready(function() {
var csrftoken = getCookie('csrftoken');

       $("#customereditform").submit(function(event){
            event.preventDefault();
            $.ajax({
                 type:"POST",
                 url:"",
                 data: $("#customereditform").serialize(),
        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
                 success: function(data){
                    alert("Saved Successfully")
                    window.location.href = "/customer/view/"
                 },
                 error: function(){
                    alert("Something went wrong plz try again")
                    window.location.href = "/home/"
                 }
            });
            return false; //<---- move it here
       });
});
