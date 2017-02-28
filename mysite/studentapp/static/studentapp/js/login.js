function keyUp(){
        var mainContent = document.getElementById('main-content');
        mainContent.addEventListener('keyup',function(e){
        keyLogin(e);
        });
    }
 function keyLogin(e){
    var password = document.getElementById('password');
    if (e.keyCode==13)  //回车键的键值为13
    {
        switch(e.target.id){
        case 'username':
        password.focus();
        break
        case'password':
        // sumitLogin();
        break
    }
}
}
keyUp();