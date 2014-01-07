for(var i = 0; i < 14; i++) { var scriptId = 'u' + i; window[scriptId] = document.getElementById(scriptId); }

$axure.eventManager.pageLoad(
function (e) {

});

u10.style.cursor = 'pointer';
if (bIE) u10.attachEvent("onclick", ClickLinkToReferencePageu10);
else u10.addEventListener("click", ClickLinkToReferencePageu10, true);
function ClickLinkToReferencePageu10(e)
{
    self.location.href=$axure.globalVariableProvider.getLinkUrl('Login_1.html');
}

x = 0;
y = 56;
InsertAfterBegin(u10ann, "<img src='resources/images/newwindow.gif' id='u10PagePopup' style='cursor:pointer;position:absolute;z-index:500;left:" + x + ";top:" + y + "'>");

var u10PagePopup = document.getElementById('u10PagePopup');
if (bIE) u10PagePopup.attachEvent("onclick", u10PagePopupHandler);
else u10PagePopup.addEventListener("click", u10PagePopupHandler, true);

function u10PagePopupHandler(event)
{
    window.open($axure.globalVariableProvider.getLinkUrl('Login_1.html'));
}
gv_vAlignTable['u11'] = 'center';
u12.style.cursor = 'pointer';
if (bIE) u12.attachEvent("onclick", ClickLinkToReferencePageu12);
else u12.addEventListener("click", ClickLinkToReferencePageu12, true);
function ClickLinkToReferencePageu12(e)
{
    self.location.href=$axure.globalVariableProvider.getLinkUrl('Register_1.html');
}

x = 0;
y = 56;
InsertAfterBegin(u12ann, "<img src='resources/images/newwindow.gif' id='u12PagePopup' style='cursor:pointer;position:absolute;z-index:500;left:" + x + ";top:" + y + "'>");

var u12PagePopup = document.getElementById('u12PagePopup');
if (bIE) u12PagePopup.attachEvent("onclick", u12PagePopupHandler);
else u12PagePopup.addEventListener("click", u12PagePopupHandler, true);

function u12PagePopupHandler(event)
{
    window.open($axure.globalVariableProvider.getLinkUrl('Register_1.html'));
}
gv_vAlignTable['u13'] = 'center';gv_vAlignTable['u1'] = 'center';gv_vAlignTable['u3'] = 'center';gv_vAlignTable['u5'] = 'center';gv_vAlignTable['u7'] = 'center';
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