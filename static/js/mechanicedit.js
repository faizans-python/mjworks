$(document).ready(function() {
var csrftoken = getCookie('csrftoken');

       $("#mechaniceditform").submit(function(event){
            event.preventDefault();
            $.ajax({
                 type:"POST",
                 url:"",
                 data: $("#mechaniceditform").serialize(),
        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
                 success: function(data){
                    alert("Saved Successfully")
                    window.location.href = "/mechanic/view/"
                 },
                 error: function(){
                    alert("Something went wrong plz try again")
                    window.location.href = "/home/"
                 }
            });
            return false; //<---- move it here
       });
});
