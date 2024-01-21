function login_user() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    
    $.ajax({
        url: '/login_response', 
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({  'username': username,
                                'password': password }),
        success: function(response) {
            console.log(response);
            if (response.result == "success") {
                window.location.href = "/dashboard";
            }
            else {
                alert("Login Failed");
            }
        },
        error: function(error) {
            console.log(error);
        }
    });
}