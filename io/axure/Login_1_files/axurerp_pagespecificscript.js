for(var i = 0; i < 28; i++) { var scriptId = 'u' + i; window[scriptId] = document.getElementById(scriptId); }

$axure.eventManager.pageLoad(
function (e) {

if (true) {

SetWidgetRichText('u14', '<p style="text-align:left;"><span style="font-family:Arial;font-size:13px;font-weight:normal;font-style:normal;text-decoration:none;color:#000099;">' + (GetGlobalVariableValue('Username')) + '</span></p>');

}

});
document.getElementById('u21_img').tabIndex = 0;

u21.style.cursor = 'pointer';
$axure.eventManager.click('u21', function(e) {

if ((GetWidgetText('u19')) == ('')) {

	SetPanelState('u25', 'pd1u25','none','',500,'none','',500);

SetGlobalVariableValue('Username', '');

}
else
if (((GetWidgetText('u19')) == ('Ala')) && ((GetWidgetText('u20')) == ('12345'))) {

SetGlobalVariableValue('Username', GetWidgetText('u19'));

	self.location.href=$axure.globalVariableProvider.getLinkUrl('Home.html');

}
else
if (true) {

	SetPanelState('u25', 'pd0u25','none','',500,'none','',500);

SetGlobalVariableValue('Username', '');

}
});
gv_vAlignTable['u22'] = 'center';gv_vAlignTable['u24'] = 'center';gv_vAlignTable['u26'] = 'top';gv_vAlignTable['u27'] = 'top';gv_vAlignTable['u1'] = 'center';gv_vAlignTable['u2'] = 'top';gv_vAlignTable['u4'] = 'center';gv_vAlignTable['u7'] = 'center';document.getElementById('u8_img').tabIndex = 0;
HookHover('u8', false);

u8.style.cursor = 'pointer';
$axure.eventManager.click('u8', function(e) {

if (true) {

	self.location.href=$axure.globalVariableProvider.getLinkUrl('Home.html');

}
});
gv_vAlignTable['u9'] = 'center';document.getElementById('u10_img').tabIndex = 0;
HookHover('u10', false);

u10.style.cursor = 'pointer';
$axure.eventManager.click('u10', function(e) {

if (true) {

    self.location.href="resources/reload.html#" + encodeURI($axure.globalVariableProvider.getLinkUrl($axure.pageData.url));

}
});
gv_vAlignTable['u11'] = 'center';document.getElementById('u12_img').tabIndex = 0;
HookHover('u12', false);

u12.style.cursor = 'pointer';
$axure.eventManager.click('u12', function(e) {

if (true) {

	self.location.href=$axure.globalVariableProvider.getLinkUrl('Register_1.html');

}
});
gv_vAlignTable['u13'] = 'center';gv_vAlignTable['u14'] = 'top';gv_vAlignTable['u15'] = 'top';gv_vAlignTable['u17'] = 'top';gv_vAlignTable['u18'] = 'top';