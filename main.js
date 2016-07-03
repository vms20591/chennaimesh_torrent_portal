function init(){
    var input_text=document.querySelector("div.search-group input.input-search");
    var search_icon=document.querySelector("div.search-group a");
    
    //Register event handlers to highlight the search box on load
    input_text.onfocus=function(event){
        event.target.style.boxShadow='0px 0px 5px #8BB726';
        search_icon.style.boxShadow='0px 0px 5px #8BB726';
    }
    
    //Register event handlers to remove highlight on search box
    input_text.onblur=function(event){
        event.target.style.boxShadow='';
        search_icon.style.boxShadow='';
    }
        
    //Register event handlers to create a click effect    
    search_icon.onclick=function(event){
        event.preventDefault();
        
        event.target.style.backgroundColor="#ACC844";
        
        setTimeout(click_handler.bind(event),100);
    };
    
    //Focus search box
    input_text.focus();
    
    return true;
}

function click_handler(){
    this.target.style.backgroundColor="";
}
