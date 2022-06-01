
function bind_show(){
    var buttons = document.querySelectorAll("button.show");
	for (var i = 0; i < buttons.length; i++){
        var b = buttons[i];
        b.onclick = function(e){
            // Remove the on-click for now so that we cant add more buttons
            var value = e.target.closest("button").innerText;
            var count = document.querySelector("input.episodeCount").value;
            send_request("show/"+value+"/"+count);
        }
    }
}


function send_request(url){
    var request = new XMLHttpRequest();
    request.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            // Conver the database to JSON and render
            ;
        }
    };
    request.open("GET", url);
    request.send();
    
}


function bind_buttons(){
    bind_show();
}

bind_buttons();

