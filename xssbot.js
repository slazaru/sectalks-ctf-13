var page = require('webpage').create();
var host = "app2:5002";
var url = "http://app2:5002/supers3cretgetmessagesthiswontbeinwordlists";
var timeout = 1000;

page.customHeaders = {
    "Referer": "sectalks{bl1nd-s1d3-best-side!!!!!}"
};

phantom.addCookie({
    'name': 'Flag',
    'value': 'sectalks{bl1nd-s1d3-best-side!!!!!}',
    'domain': host,
    'path': '/',
    'httponly': false
});

page.onNavigationRequested = function(url, type, willNavigate, main) {
    console.log("[URL] URL="+url);
};

page.settings.resourceTimeout = timeout;

page.onResourceTimeout = function(e) {
    setTimeout(function(){
        console.log("[INFO] Timeout")
        phantom.exit();
    }, 4);
};

page.open(url, function(status) {
    console.log("[INFO] rendered page");
    setTimeout(function(){
        console.log(page.content);
        phantom.exit();
    }, 4);
});

