for(var i = 0; i < 36; i++) { var scriptId = 'u' + i; window[scriptId] = document.getElementById(scriptId); }

$axure.eventManager.pageLoad(
function (e) {

if (true) {

	SetPanelVisibility('u34','toggle','none',500);

	SetPanelVisibility('u30','toggle','none',500);

}

if (true) {

SetWidgetRichText('u14', '<p style="text-align:left;"><span style="font-family:Arial;font-size:13px;font-weight:normal;font-style:normal;text-decoration:none;color:#000099;">' + (GetGlobalVariableValue('Username')) + '</span></p>');

}

});

$axure.eventManager.focus('u20', function(e) {

if (true) {

	SetPanelVisibility('u30','','none',500);

	SetPanelState('u30', 'pd0u30','swing','right',500,'fade','',500);

}
});

$axure.eventManager.blur('u20', function(e) {

if (true) {

	SetPanelVisibility('u30','toggle','fade',500);

}
});

$axure.eventManager.focus('u21', function(e) {

if (true) {

	SetPanelVisibility('u30','','none',500);

	SetPanelState('u30', 'pd1u30','none','',500,'none','',500);

}
});

$axure.eventManager.blur('u21', function(e) {

if (true) {

	SetPanelState('u30', 'pd2u30','none','',500,'none','',500);

	SetPanelVisibility('u30','toggle','none',500);

}
});
gv_vAlignTable['u25'] = 'top';gv_vAlignTable['u26'] = 'top';gv_vAlignTable['u27'] = 'top';gv_vAlignTable['u28'] = 'top';gv_vAlignTable['u29'] = 'top';gv_vAlignTable['u31'] = 'top';gv_vAlignTable['u32'] = 'top';gv_vAlignTable['u33'] = 'top';gv_vAlignTable['u35'] = 'top';gv_vAlignTable['u1'] = 'center';gv_vAlignTable['u2'] = 'top';gv_vAlignTable['u4'] = 'center';gv_vAlignTable['u7'] = 'center';document.getElementById('u8_img').tabIndex = 0;
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

	self.location.href=$axure.globalVariableProvider.getLinkUrl('Login_1.html');

}
});
gv_vAlignTable['u11'] = 'center';document.getElementById('u12_img').tabIndex = 0;
HookHover('u12', false);

u12.style.cursor = 'pointer';
$axure.eventManager.click('u12', function(e) {

if (true) {

    self.location.href="resources/reload.html#" + encodeURI($axure.globalVariableProvider.getLinkUrl($axure.pageData.url));

}
});
gv_vAlignTable['u13'] = 'center';gv_vAlignTable['u14'] = 'top';gv_vAlignTable['u15'] = 'top';gv_vAlignTable['u18'] = 'center';
u19.style.cursor = 'pointer';
$axure.eventManager.click('u19', function(e) {

if (((GetWidgetValueLength('u20')) != ('0')) && (((GetWidgetValueLength('u22')) != ('0')) && (((GetWidgetValueLength('u23')) > Number('8')) && (((GetWidgetText('u21')) > Number('2')) && ((IsValueNumeric(GetWidgetText('u21'))) && (((GetWidgetText('u21')) < Number('150')) && ((GetSelectedOption('u24')) != (' ')))))))) {

	self.location.href=$axure.globalVariableProvider.getLinkUrl('Login_1.html');

}
else
if (((GetWidgetValueLength('u20')) == ('0')) || (((GetWidgetValueLength('u22')) == ('0')) || (((GetWidgetValueLength('u23')) == ('0')) || (((GetSelectedOption('u24')) == (' ')) || ((IsValueNotNumeric(GetWidgetText('u21'))) || (((GetWidgetText('u21')) > Number('150')) || ((GetWidgetText('u21')) < Number('2')))))))) {

	SetPanelVisibility('u34','toggle','none',500);

}
});
