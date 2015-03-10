$(document).ready(function(){
    
    $("#geoLinkFullText").hide();
    $("#sloanFullText").hide();

    $("#geoLinkIntro").click(function(){
        $("#geoLinkIntroText").hide();
        $("#geoLinkFullText").show();
    });

    $("#geoLinkFull").click(function(){
        $("#geoLinkIntroText").show();
        $("#geoLinkFullText").hide();
    });

    $("#sloanIntro").click(function(){
        $("#sloanIntroText").hide();
        $("#sloanFullText").show();
    });

    $("#sloanFull").click(function(){
        $("#sloanIntroText").show();
        $("#sloanFullText").hide();
    });

});