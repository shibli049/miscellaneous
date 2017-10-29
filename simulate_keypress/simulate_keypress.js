function simulateKeyPress(targetChar, targetHtmlElement){
    tkeyCode = targetChar.charCodeAt(0);
    $(targetHtmlElement).trigger({type: 'keypress', which: tkeyCode, keyCode: tkeyCode});
}