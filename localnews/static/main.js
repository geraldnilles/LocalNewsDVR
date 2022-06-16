
function bind_show(){
    var buttons = document.querySelectorAll("button.show");
	for (var i = 0; i < buttons.length; i++){
        var b = buttons[i];
        b.onclick = function(e){
            // Remove the on-click for now so that we cant add more buttons
            var value = e.target.closest("button").innerText;
            // var count = document.querySelector("input.episodeCount").value;
            send_request("play/"+value+"/"+get_device_name());
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

function get_device_name(){
    /* Returns the name of the chromecast device which is currently selected
     * by the DOM elements
     */
    return document.querySelector("button.device.active").innerText;
}

function bind_toggle(){
    var buttons = document.querySelectorAll("button.device");
    // By default, activate the first device in the list
    buttons.forEach(function(b){
    	
    	if ( b.innerText == "Living Room TV" ){
		b.classList.add("active");
	}

        b.onclick = function(e){
            buttons.forEach(function(a){
                a.classList.remove("active"); 
            });
            e.target.classList.add("active");
        }
    });
}


function bind_buttons(){
    bind_show();
    bind_toggle();
}

bind_buttons();

