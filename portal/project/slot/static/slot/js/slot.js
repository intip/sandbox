$(function () {
    var html =
        '<div class="placeholder">' +
        '   <a title="Placeholder" class="fancybox"' +
        '      data-fancybox-type="iframe">⚙</a>' +
        '   <a title="Placeholder" class="fancybox"' +
        '   href="/slot/portlet/choices/" data-fancybox-type="iframe">☭</a>' +
        '</div>';
    var $buttons = $(html);
    $buttons.appendTo(document.body);
    var params = {
        afterClose: function () {

        }
    };
    $buttons.find("a").fancybox(params);
});
