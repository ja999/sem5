for(var i = 0; i < 10; i++) { var scriptId = 'u' + i; window[scriptId] = document.getElementById(scriptId); }

$axure.eventManager.pageLoad(
function (e) {

});
gv_vAlignTable['u1'] = 'center';gv_vAlignTable['u3'] = 'center';gv_vAlignTable['u5'] = 'center';
u6.style.cursor = 'pointer';
if (bIE) u6.attachEvent("onclick", ClickLinkToReferencePageu6);
else u6.addEventListener("click", ClickLinkToReferencePageu6, true);
function ClickLinkToReferencePageu6(e)
{
    self.location.href=$axure.globalVariableProvider.getLinkUrl('Login_1.html');
}

x = 0;
y = 56;
InsertAfterBegin(u6ann, "<img src='resources/images/newwindow.gif' id='u6PagePopup' style='cursor:pointer;position:absolute;z-index:500;left:" + x + ";top:" + y + "'>");

var u6PagePopup = document.getElementById('u6PagePopup');
if (bIE) u6PagePopup.attachEvent("onclick", u6PagePopupHandler);
else u6PagePopup.addEventListener("click", u6PagePopupHandler, true);

function u6PagePopupHandler(event)
{
    window.open($axure.globalVariableProvider.getLinkUrl('Login_1.html'));
}
gv_vAlignTable['u7'] = 'center';
u8.style.cursor = 'pointer';
if (bIE) u8.attachEvent("onclick", ClickLinkToReferencePageu8);
else u8.addEventListener("click", ClickLinkToReferencePageu8, true);
function ClickLinkToReferencePageu8(e)
{
    self.location.href=$axure.globalVariableProvider.getLinkUrl('Home.html');
}

x = 0;
y = 56;
InsertAfterBegin(u8ann, "<img src='resources/images/newwindow.gif' id='u8PagePopup' style='cursor:pointer;position:absolute;z-index:500;left:" + x + ";top:" + y + "'>");

var u8PagePopup = document.getElementById('u8PagePopup');
if (bIE) u8PagePopup.attachEvent("onclick", u8PagePopupHandler);
else u8PagePopup.addEventListener("click", u8PagePopupHandler, true);

function u8PagePopupHandler(event)
{
    window.open($axure.globalVariableProvider.getLinkUrl('Home.html'));
}
gv_vAlignTable['u9'] = 'center';